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

import time
import serial
import binascii
import struct
import logging
from eddiebot_driver import Eddiebot
#from PIDController import PIDController
from decimal import *

logging.basicConfig(filename='test_eddiebot_driver.log', level=logging.INFO)
# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.open()
ser.isOpen()

print 'Enter your commands below.\r\nInsert "exit" to leave the application.'

eddiebot = Eddiebot()

input=1
while 1 :
    # get keyboard input
    command = raw_input("command: ")
    
    if command == "": # Stop the Eddie robot
        # send the character to the device
        # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
        ser.write('STOP' + ' 0' + chr(13))
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1)

        if out != '':
            print "output: " + out
    
    if command == "GO" or command == "go":
        left = raw_input("left power: ")
        right = raw_input("right power: ")
    
        vl = int(left) & 0xffff
        vr = int(right) & 0xffff
    
        parameters = binascii.hexlify(struct.pack('>2H', vr, vl))
    
        parameters_output = ''
    
        for i in range(len(parameters)):
             if(i == 2 or i == 3 or i == 6 or i== 7):
                 parameters_output += parameters[i]
             if(i == 4):
                 parameters_output += ' '
                 
                     
        ser.write(command + ' ' + parameters_output + chr(13))
        
#    if command == "PID" or command == "pid":
#        
#        left = raw_input("left power: ")
#        right = raw_input("right power: ")
#    
#        vl = int(left) & 0xffff
#        vr = int(right) & 0xffff
#        
#        out = ''
#        if out != '':
#            print "output: " + out
#
#        parameters = binascii.hexlify(struct.pack('>2H', vr, vl))
#        
#        parameters_output = ''
#    
#        for i in range(len(parameters)):
#            if(i == 2 or i == 3 or i == 6 or i== 7):
#                parameters_output += parameters[i]
#            if(i == 4):
#                parameters_output += ' '
#        
#        ser.write('GO' + ' ' + parameters_output + chr(13))
#        
#        pid_left = PIDController()
#        pid_left.eddiebot_setting(2, 2, 0)
#        pid_left.set_target(int(left))
#        
#        pid_right = PIDController()
#        pid_left.eddiebot_setting(2, 2, 0)
#        pid_right.set_target(int(right))
#        
#        pid_left_output = 0
#        pid_right_output = 0
#        
#        time.sleep(2)
#        
#        while True:
#            ser.write('SPD' + chr(13))
#            out = ''
#            # let's wait one second before reading output (let's give device time to answer)
#            time.sleep(0.01)
#
#            if out != '':
#                print "output: " + out   
#            left_speed = ''
#            right_speed = ''
#            # let's wait one second before reading output (let's give device time to answer)
#            a = 0
#            while ser.inWaiting() > 0:
#                out += ser.read(1)
#                if(a == 1 or a == 2 or a == 3 or a == 4):
#                    left_speed += out[a]
#                if(a == 6 or a == 7 or a == 8 or a == 9):
#                    right_speed += out[a]
#                a += 1
#                
#            pid_left.update(int(left_speed, 16))
#            pid_left_output = pid_left.get_output()
#            pid_right.update(int(right_speed, 16))
#            pid_right_output = pid_right.get_output()
#            
#            vl = int(pid_left_output) & 0xffff
#            vr = int(pid_right_output) & 0xffff
#        
#            if out != '':
#                print "speed: " + out
#
#                parameters = binascii.hexlify(struct.pack('>2H', vr, vl))
#        
#                parameters_output = ''
#    
#            for i in range(len(parameters)):
#                if(i == 2 or i == 3 or i == 6 or i== 7):
#                    parameters_output += parameters[i]
#                if(i == 4):
#                    parameters_output += ' '
#            print 'GO' + ' ' + parameters_output + chr(13)
##            ser.write('GO' + ' ' + parameters_output + chr(13))
#            time.sleep(0.5)
#            
        
    if command == "GOSPD" or command == "gospd":
        left = raw_input("left positions per second: ")
        right = raw_input("right positions per second: ")
    
        vl = int(left) & 0xffff
        vr = int(right) & 0xffff
    
        parameters = binascii.hexlify(struct.pack('>2H', vr, vl))
    
        parameters_output = ''
    
        for i in range(len(parameters)):
             parameters_output += parameters[i]
             if(i == 3):
                 parameters_output += ' '
                 
        ser.write(command + ' ' + parameters_output + chr(13))
    
    if command == 'EXIT' or command == "exit":
        ser.close()
        exit()
    if command == 'VER' or command == "ver":
        # send the character to the device
        # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
        ser.write(command + chr(13))
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1)

        if out != '':
            print "output: " + out
    
        
    if command == "SPD" or command == "spd":
        ser.write('SPD' + chr(13))
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(0.01)
        while ser.inWaiting() > 0:
            out += ser.read(1)

        if out != '':
            print "output: " + out   
        
    if command == "ADC" or command == "adc":
        adc_left_f_str = ''
        adc_right_f_str = ''
        adc_center_f_str = ''
        adc_left_r_str = ''
        adc_right_r_str = ''
        adc_center_r_str = ''
        
        adc_battery_str = ''
        while True:
            ser.write('ADC' + chr(13))
            out = ''
            # let's wait one second before reading output (let's give device time to answer)
            time.sleep(0.2)
    
            i = 0;
            while ser.inWaiting() > 0:
                out += ser.read(1)
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
                print "output:" + out
                print "left front: " + str(int(adc_left_f_str,16))
                print "right front: " + str(int(adc_right_f_str,16))
                print "center front: " + str(int(adc_center_f_str,16))
                print "left rear: " + str(int(adc_left_r_str,16))
                print "right rear: " + str(int(adc_right_r_str,16))
                print "center rear: " + str(int(adc_center_r_str,16))
                
                print "battery: " + str(int(adc_battery_str,16))
            except Exception as ex:
                print ex
                
            adc_left_f_str = ''
            adc_right_f_str = ''
            adc_center_f_str = ''
            adc_left_r_str = ''
            adc_right_r_str = ''
            adc_center_r_str = ''
            
            adc_battery_str = ''
            
    if command == "PING" or command == "ping":
        ping_left_f_str = ''
        ping_right_f_str = ''
        ping_left_r_str = ''
        ping_right_r_str = ''
        while True:
            ser.write('PING' + chr(13))
            out = ''
            # let's wait one second before reading output (let's give device time to answer)
            time.sleep(0.07)
            i = 0;
            while ser.inWaiting() > 0:
                out += ser.read(1)
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
                print "left front: " + str(int(ping_left_f_str,16))
                print "right front: " + str(int(ping_right_f_str,16))
                print "left rear: " + str(int(ping_left_r_str,16))
                print "right rear: " + str(int(ping_right_r_str,16))
            except Exception as ex:
                print ex
                
            ping_left_f_str = ''
            ping_right_f_str = ''
            ping_left_r_str = ''
            ping_right_r_str = ''
            
            
    if command == "SV" or command == "sv":        
        pan = raw_input("pan degree: ")
        tilt = raw_input("tilt degree: ")
        eddiebot.command_joints(pan,tilt)
                
    if command == "DIST" or command == "dist":
        ser.write('DIST' + chr(13))
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(0.5)
        while ser.inWaiting() > 0:
            out += ser.read(1)

        if out != '':
            print "output: " + out  
            
    if command == "DIRECT_DRIVE" or command == "direct_drive":
        left = raw_input("left positions per second: ")
        right = raw_input("right positions per second: ")
    
        eddiebot.direct_drive(left, right)
        
    if command == "DRIVE" or command == "drive":
        velocity = raw_input("velocity: ")
        radius = raw_input("radius: ")
    
        eddiebot.drive(velocity, radius)
        
    if command == "CONTROL" or command == "control":
        eddiebot.control()
    
    if command == "SLOW_STOP" or command == "slow_stop":
        velocity = raw_input("velocity: ")
        eddiebot.slow_stop(int(velocity))
        
    if command == "STOP" or command == "stop":
        eddiebot.stop()
        
    if command == "DRIVE_STRAIGHT" or command == "drive_straight":
        velocity = raw_input("velocity: ")
        eddiebot.drive_straight(velocity)
        
    if command == "TURN_IN_PLACE" or command == "turn_in_place":
        velocity = raw_input("velocity: ")
        direction = raw_input("direction (E.g., cw, ccw): ")
        eddiebot.turn_in_place(velocity, direction)
        