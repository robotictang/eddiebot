#!/usr/bin/python

# The BSD License
# Copyright (c) 2010, Willow Garage Inc.
# Copyright (c) 2012 Tang Tiong Yew 
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# Modified for use in ROS by Tang Tiong Yew. API names have been modified
# for consistency ROS Python coding guidelines.

from __future__ import with_statement

"""iRobot Roomba Serial control Interface (SCI) and Turtlebot Open Interface (OI).

turtlebot.py is a fork of PyRobot.

PyRobot was originally based on openinterface.py, developed by iRobot
Corporation. Many of the docstrings from openinterface.py, particularly those
which describe the specification, are also used here. Also, docstrings may
contain specification text copied directly from the Roomba SCI Spec Manual and
the Turtlebot Open Interface specification.

Since SCI is a subset of OI, PyRobot first defines the Roomba's functionality
in the Roomba class and then extends that with the Turtlebot's additional
functionality in the Turtlebot class. In addition, since OI is built on SCI the
SerialCommandInterface class is also used for OI.

"""
__author__ = "tang.tiong.yew@gmail.com (Tang Tiong Yew)"

import logging
import math
import serial
import struct
import time
import threading
import traceback
import rospy

import binascii


EDDIE_OPCODES = dict(
    start =  '', #128,
    baud =  '', #129,
    control =  '', #130,
    safe =  '', #131,
    full =  '', #132,
    power =  '', #133,
    spot =  '', #134,
    clean =  '', #135,
    max =  '', #136,
    drive =  'GO', #137,
#    drive =  'GO', #137,
    motors =  'SV', #138,
    leds =  '', #139,
    song =  '', #140,
    play =  '', #141,
    sensors =  '', #142,
    force_seeking_dock =  '', #143,

    
    soft_reset =  '', #7,  # Where is this documented?
    low_side_drivers =  '', #138,
    play_song =  '', #141,
    pwm_low_side_drivers =  '', #144,
    direct_drive =  'GO', #145,
  #  direct_drive =  'GO', #145,
    digital_outputs =  '', #147,
    stream =  '', #148,
    query_list =  '', #149,
    pause_resume_stream =  '', #150,
    send_ir =  '', #151,
    script =  '', #152,
    play_script =  '', #153,
    show_script =  '', #154,
    wait_time =  '', #155,
    wait_distance =  '', #156,
    wait_angle =  '', #157,
    wait_event =  '', #158,
    )

REMOTE_OPCODES = {
    # Remote control.
    129: 'left',
    130: 'forward',
    131: 'right',
    132: 'spot',
    133: 'max',
    134: 'small',
    135: 'medium',
    136: 'large',
    136: 'clean',
    137: 'pause',
    138: 'power',
    139: 'arc-left',
    140: 'arc-right',
    141: 'drive-stop',
    # Scheduling remote.
    142: 'send-all',
    143: 'seek-dock',
    # Home base.
    240: 'reserved',
    242: 'force-field',
    244: 'green-buoy',
    246: 'green-buoy-and-force-field',
    248: 'red-buoy',
    250: 'red-buoy-and-force-field',
    252: 'red-buoy-and-green-buoy',
    254: 'red-buoy-and-green-buoy-and-force-field',
    255: 'none',
    }

BAUD_RATES = (  # In bits per second.
    300,
    600,
    1200,
    2400,
    4800,
    9600,
    14400,
    19200,
    28800,
    38400,
    57600,  # Default.
    115200)

CHARGING_STATES = (
    'not-charging',
    'charging-recovery',
    'charging',
    'trickle-charging',
    'waiting',
    'charging-error')

OI_MODES = (
    'off',
    'passive',
    'safe',
    'full')

# Various state flag masks
WHEEL_DROP_CASTER = 0x10
WHEEL_DROP_LEFT = 0x08
WHEEL_DROP_RIGHT = 0x04
BUMP_LEFT = 0x02
BUMP_RIGHT = 0x01

OVERCURRENTS_DRIVE_LEFT = 0x10
OVERCURRENTS_DRIVE_RIGHT = 0x08
OVERCURRENTS_MAIN_BRUSH = 0x04
OVERCURRENTS_VACUUM = 0x02
OVERCURRENTS_SIDE_BRUSH = 0x01

BUTTON_POWER = 0x08
BUTTON_SPOT = 0x04
BUTTON_CLEAN = 0x02
BUTTON_MAX = 0x01

SENSOR_GROUP_PACKET_LENGTHS = {
    0: 26,
    1: 10,
    2: 6,
    3: 10,
    4: 14,
    5: 12,
    6: 52,
    100: 80 }

# drive constants.
RADIUS_TURN_IN_PLACE_CW = -2000 # TODO: Radius is unknown without create robot.
RADIUS_TURN_IN_PLACE_CCW = 2000
RADIUS_STRAIGHT = 32768
RADIUS_MAX = 2000

VELOCITY_MAX = 127  # positions per second
VELOCITY_SLOW = int(VELOCITY_MAX * 0.10)
VELOCITY_FAST = int(VELOCITY_MAX * 0.66)

PWM_RATIO_FORWARD_MAX = 127
PWM_RATIO_BACKWARD_MAX = -127

MAX_WHEEL_SPEED = 70
WHEEL_SEPARATION = 260  # mm

SERIAL_TIMEOUT = 2  # Number of seconds to wait for reads. 2 is generous.
START_DELAY = 5  # Time it takes the Roomba/Turtlebot to boot.

BAUDRATE = 115200

assert struct.calcsize('H') == 2, 'Expecting 2-byte shorts.'

class DriverError(Exception):
  pass

class SerialCommandInterface(object):

  """A higher-level wrapper around PySerial specifically designed for use with
  Parallax Eddie Propeller Board.

  """

  def __init__(self, tty, baudrate):
    self.ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=BAUDRATE,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=SERIAL_TIMEOUT
    )

    self.ser.open()
#    self.wake()
    self.opcodes = {}

    #TODO: kwc all locking code should be outside of the driver. Instead,
    #could place a lock object in Roomba and let people "with" it
    self.lock = threading.RLock()

  def wake(self):
    """wake up robot."""
    print "wake"
#    self.ser.setRTS(0)
#    time.sleep(0.1)
#    self.ser.setRTS(1)
#    time.sleep(0.75)  # Technically it should wake after 500ms.
#    for i in range(3):
#        self.ser.setRTS(0)
#        time.sleep(0.25)
#        self.ser.setRTS(1)
#        time.sleep(0.25) 

  def add_opcodes(self, opcodes):
    """Add available opcodes to the SCI."""
    self.opcodes.update(opcodes)

  def send(self, bytes):
    """send a string of bytes to the robot."""
    with self.lock:
      self.ser.write(bytes)

  #TODO: kwc the locking should be done at a higher level
  def read(self, num_bytes):
    """Read a string of 'num_bytes' bytes from the robot."""
#    logging.debug('Attempting to read %d bytes from SCI port.' % num_bytes)
#    with self.lock:
    data = self.ser.read(num_bytes)
#    logging.debug('Read %d bytes from SCI port.' % len(data))
#    if not data:
#      raise DriverError('Error reading from SCI port. No data.')
#    if len(data) != num_bytes:
#      raise DriverError('Error reading from SCI port. Wrong data length.')
    return data

  def flush_input(self):
    """Flush input buffer, discarding all its contents."""
    logging.debug('Flushing serial input buffer.')
    self.ser.flushInput()
    
  def inWaiting(self):
    """ InWaiting Called """
    logging.debug('Called inWaiting')
    self.ser.inWaiting()

  def __getattr__(self, name):
    """Eddiebots methods for opcodes on the fly.

    Each opcode method sends the opcode optionally followed by a string of
    parameter.

    """
    #TODO: kwc do static initialization instead
    if name in self.opcodes:
      def send_opcode(input_string):
        logging.debug('sending opcode %s.' % name)
        self.send(self.opcodes[name] + ' ' + input_string)
      return send_opcode
    raise AttributeError

  def getSer(self):
    return self.ser
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Eddiebot():

  """Represents a Eddiebot robot."""

  def __init__(self):
    """
    @param sensor_class: Sensor class to use for fetching and decoding sensor data.
    """
    logging.basicConfig(filename='eddiebot_driver.log', level=logging.INFO)
    self.tty = None
    self.sci = None
    self.safe = True
    self.start()
    
  def start(self, tty='/dev/ttyUSB0', baudrate=115200):
    self.tty = tty
    self.sci = SerialCommandInterface(tty, baudrate)
    self.sci.add_opcodes(EDDIE_OPCODES)
      
  def control(self):
    """Start the robot's SCI interface and place it in safe or full mode."""
    logging.info('sending control opcodes.')
#    self.passive() Not implemented in Eddie
#    if self.safe:
#      self.sci.safe()
#    else:
#      self.sci.full()
#    time.sleep(0.5)

  def power_low_side_drivers(self, drivers):
    """Enable or disable power to low side drivers.

    'drivers' should be a list of booleans indicating which low side drivers
    should be powered.

    """
    assert len(drivers) == 3, 'Expecting 3 low side driver power settings.'
    byte = 0
    for driver, power in enumerate(drivers):
      byte += (2 ** driver) * int(power)
    # self.sci.low_side_drivers(byte) Not implemented in Eddie

  def set_digital_outputs(self, value):
    """Enable or disable digital outputs."""
    # self.sci.digital_outputs(value) Not implemented in Eddie

  def soft_reset(self):
    """Do a soft reset of the Turtlebot."""
    logging.info('sending soft reset.')
#    self.sci.soft_reset()
#    time.sleep(START_DELAY)
#    self.passive()
    
    
    #------------------- Roomba methods -----------------------------
  def change_baud_rate(self, baud_rate):
    """Sets the baud rate in bits per second (bps) at which SCI commands and
    data are sent according to the baud code sent in the data byte.

    The default baud rate at power up is 57600 bps. (See Serial Port Settings,
    above.) Once the baud rate is changed, it will persist until Roomba is
    power cycled by removing the battery (or until the battery voltage falls
    below the minimum requir''' ed for processor operation). You must wait 100ms
    after sending this command before sending additional commands at the new
    baud rate. The SCI must be in passive, safe, or full mode to accept this
    command. This command puts the SCI in passive mode.

    """
    if baud_rate not in BAUD_RATES:
      raise DriverError('Invalid baud rate specified.')
    self.sci.baud(baud_rate)
    self.sci = SerialCommandInterface(self.tty, baud_rate)

  def passive(self):
    """Put the robot in passive mode."""
    # self.sci.start() Not implemented in Eddie
    print "passive"
#    time.sleep(0.5)

  def direct_drive(self, velocity_left, velocity_right):
#    print("direct_drive(self, velocity_left, velocity_right)")
#    print("velocity_left: " + str(int(velocity_left)))
#    print("velocity_right: " + str(int(velocity_right)))
    # Mask integers to 2 bytes.
    vl = int(velocity_left) & 0xffff
    vr = int(velocity_right) & 0xffff
    
    parameters = binascii.hexlify(struct.pack('>2H', vr, vl))
    
    parameters_output = ''
    
    for i in range(len(parameters)):
             parameters_output += parameters[i]
             if(i == 3):
                 parameters_output += ' '
        
    self.sci.direct_drive(parameters_output + chr(13))
    
  def drive(self, velocity, radius):
    logging.debug("drive(self, velocity, radius)")
    """controls Roomba's drive wheels.

    NOTE(damonkohler): The following specification applies to both the Roomba
    and the Turtlebot.

    The Roomba takes four data bytes, interpreted as two 16-bit signed values
    using two's complement. The first two bytes specify the average velocity
    of the drive wheels in millimeters per second (mm/s), with the high byte
    being sent first. The next two bytes specify the radius in millimeters at
    which Roomba will turn. The longer radii make Roomba drive straighter,
    while the shorter radii make Roomba turn more. The radius is measured from
    the center of the turning circle to the center of Roomba.

    A drive command with a positive velocity and a positive radius makes
    Roomba drive forward while turning toward the left. A negative radius
    makes Roomba turn toward the right. Special cases for the radius make
    Roomba turn in place or drive straight, as specified below. A negative
    velocity makes Roomba drive backward.

    Also see drive_straight and turn_in_place convenience methods.

    """
    # Mask integers to 2 bytes.
    velocity = int(velocity)# & 0xffff TODO:removed the marks to avoid problem
    radius = int(radius)# & 0xffff
    
    # Convert to direct_drive parameter
    velocity_left = ((2000.0 + radius) / 2000.0) * velocity
    velocity_right = ((2000.0 - radius) / 2000.0) * velocity
    
    # STRAIGHT radius set to velocity to drive straight line FW and BW
    if(RADIUS_STRAIGHT == radius):
        velocity_left = velocity
        velocity_right = velocity
    
    self.direct_drive(velocity_left, velocity_right)
    
  def command_joints(self, pan_degree, tilt_degree):
    pan_degree = int(pan_degree)
    tilt_degree = int(tilt_degree)
    parameters = binascii.hexlify(struct.pack('>H', pan_degree))
    self.sci.motors(' 4 ' + parameters + chr(13)) # Pan Servo
    
    #parameters = binascii.hexlify(struct.pack('>H', tilt_degree))
    #self.sci.motors(' 5 ' + parameters + chr(13)) # Pan Servo

  def stop(self):
    """Set velocity and radius to 0 to stop movement."""
    self.direct_drive(0, 0)

  def slow_stop(self, velocity):
    """Slowly reduce the velocity to 0 to stop movement."""
    velocities = xrange(velocity, VELOCITY_SLOW, -8)
    if velocity < 0:
      velocities = xrange(velocity, -VELOCITY_SLOW, 8)
    for v in velocities:
      self.drive(v, RADIUS_STRAIGHT)
      time.sleep(1)
    self.stop()

#  def drive_straight(self, velocity):
#    """drive in a straight line."""
#    self.gospd(velocity)
    
  def drive_straight(self, velocity):
    self.drive(velocity, RADIUS_STRAIGHT)

  def turn_in_place(self, velocity, direction):
    """Turn in place either clockwise or counter-clockwise."""
#    valid_directions = {'cw': RADIUS_TURN_IN_PLACE_CW,
#                        'ccw': RADIUS_TURN_IN_PLACE_CCW}
#    self.drive(velocity, valid_directions[direction])
    velocity = int(velocity)
    if(direction ==  'cw'):
        self.direct_drive(-velocity, velocity)
    if(direction ==  'ccw'):
        self.direct_drive(velocity, -velocity)
    

  def dock(self):
    """Start looking for the dock and then dock."""
    # NOTE(damonkohler): We should be able to call dock from any mode, however
    # it only seems to work from passive.
    #self.sci.start()  Not implemented in Eddie
#    time.sleep(0.01)
    # self.sci.force_seeking_dock() Not implemented in Eddie
    print "dock"
    
  def sensors(self):
    """This is a sensor command to emulate SCI sensor sending"""
    # =========== Ping ============
    
    ping_left_f = 0
    ping_right_f = 0
    ping_left_r = 0
    ping_right_r = 0
    
    ping_left_f_str = ''
    ping_right_f_str = ''
    ping_left_r_str = ''
    ping_right_r_str = ''
    
    self.sci.getSer().write('PING' + chr(13))
    out = ''
    # let's wait one second before reading output (let's give device time to answer)
    time.sleep(0.07)
    i = 0;
    while self.sci.getSer().inWaiting() > 0:
        out += self.sci.getSer().read(1)
        if(i == 0 or i == 1 or i == 2):
            ping_right_f_str += out[i]
        if(i == 4 or i == 5 or i == 6):
            ping_left_f_str += out[i]
        if(i == 8 or i == 9 or i == 10):
            ping_right_r_str += out[i]
        if(i == 12 or i == 13 or i == 14):
            ping_left_r_str += out[i]
        i+=1
    
    try:
        ping_left_f = int(ping_left_f_str,16)
        ping_right_f = int(ping_right_f_str,16)
        ping_left_r = int(ping_left_r_str,16)
        ping_right_r = int(ping_right_r_str,16)
    except Exception as ex:
        print ex
        
#    print "ping_left: " + str(ping_left)
#    print "ping_right: " + str(ping_right)
    
    ### =========  ADC =============
        
    adc_left_f_str = ''
    adc_right_f_str = ''
    adc_center_f_str = ''
    adc_left_r_str = ''
    adc_right_r_str = ''
    adc_center_r_str = ''
    
    
    adc_battery_str = ''
    self.sci.getSer().write('ADC' + chr(13))
    out = ''
    # let's wait one second before reading output (let's give device time to answer)
    time.sleep(0.07)
    
    i = 0;
    while self.sci.getSer().inWaiting() > 0:
        out += self.sci.getSer().read(1)
        if(i == 0 or i == 1 or i == 2):
            adc_right_f_str += out[i]
        if(i == 4 or i == 5 or i == 6):
            adc_center_f_str += out[i]
        if(i == 8 or i == 9 or i == 10):
            adc_left_f_str += out[i]
        if(i == 12 or i == 13 or i == 14):
            adc_right_r_str += out[i]
        if(i == 16 or i == 17 or i == 18):
            adc_center_r_str += out[i]
        if(i == 20 or i == 21 or i == 22):
            adc_left_r_str += out[i]
            
        if(i == 28 or i == 29 or i == 30):
            adc_battery_str += out[i]
        i+=1
    
    try:
        adc_left_f = int(adc_left_f_str,16)
        adc_right_f = int(adc_right_f_str,16)
        adc_center_f = int(adc_center_f_str,16)
        
        adc_left_r = int(adc_left_r_str,16)
        adc_right_r = int(adc_right_r_str,16)
        adc_center_r = int(adc_center_r_str,16)
        adc_battery = int(adc_battery_str,16)
    except Exception as ex:
        print ex
    
#    print "left: " + str(adc_left)
#    print "right: " + str(adc_right)
#    print "center: " + str(adc_center)
#    print "battery: " + str(adc_battery)
    PING_THRESHOLD = 0
    ADC_THRESHOLD = 800
    
    ping_left_bumps_f = False
    ping_right_bumps_f = False
    ping_left_bumps_r = False
    ping_right_bumps_r = False
    
    adc_left_bumps_f = False
    adc_right_bumps_f = False
    adc_center_bumps_f = False
    adc_left_bumps_r = False
    adc_right_bumps_r = False
    adc_center_bumps_r = False
    
#    if(ping_left_f < PING_THRESHOLD):
#        ping_left_bumps_f = True
#    if(ping_right_f < PING_THRESHOLD):
#        ping_right_bumps_f = True
#    if(ping_left_r < PING_THRESHOLD):
#        ping_left_bumps_r = True
#    if(ping_right_r < PING_THRESHOLD):
#        ping_right_bumps_r = True
    
    if(adc_left_f > ADC_THRESHOLD):
        adc_left_bumps_f = True
    if(adc_right_f > ADC_THRESHOLD + 100):
        adc_right_bumps_f = True
    if(adc_center_f > ADC_THRESHOLD + 100):
        adc_center_bumps_f = True
    if(adc_left_r > ADC_THRESHOLD + 300): # Plus 300 to avoid side sensing during narrow sliding through the obstacle
        adc_left_bumps_r = True
    if(adc_right_r > ADC_THRESHOLD + 300):
        adc_right_bumps_r = True
#    if(adc_center_r > ADC_THRESHOLD):
#        adc_center_bumps_r = True
        
#    print "Bumps!!!!!!!!!:"
#    print ping_left_bumps_f or ping_right_bumps_f or adc_left_bumps_f or adc_right_bumps_f or adc_center_bumps_f or ping_left_bumps_r or ping_right_bumps_r or adc_left_bumps_r or adc_right_bumps_r or adc_center_bumps_r 
#    
    return (ping_left_bumps_f or ping_right_bumps_f or adc_left_bumps_f or adc_right_bumps_f or adc_center_bumps_f or ping_left_bumps_r or ping_right_bumps_r or adc_left_bumps_r or adc_right_bumps_r or adc_center_bumps_r ,#1
            adc_center_bumps_f,#2 wall
            adc_left_bumps_r,#3 cliff_left
            adc_left_bumps_f,#4 cliff_front_left
            adc_right_bumps_f,#5 cliff_front_right
            adc_right_bumps_r,#6 cliff_right
            0,#7
            0,#8
            0,#9
            0,#10
            0,#11
            0,#12
            0,#13
            0,#14
            0,#15
            0,#16
            0,#17
            0,#18
            0,#19
            0,#20 adc_battery,
            0,#21
            0,#22
            0,#23
            0,#24
            0,#25
            0,#26
            0,#27
            0,#28
            0,#29
            0,#30
            0,#31
            0,#32
            0,#33
            0,#34
            0,#35
            0,#36
            0,#37
            0,#38
            0,#39 light_bumper
            0,#40 light_bump_left
            0,#41 light_bump_front_left
            0,#42 light_bump_center_left
            0,#43 light_bump_center_right
            0,#44 light_bump_front_right
            0,#45 light_bump_right
            0,#46
            0,#47
            0,#48
            0,#49
            0,#50
            0,#51
            0)#52
#   (ping_left, ping_right, adc_left, adc_right, adc_center, adc_battery)
        
        
    
    
    
    




