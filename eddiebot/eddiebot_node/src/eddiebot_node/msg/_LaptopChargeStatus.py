"""autogenerated by genpy from eddiebot_node/LaptopChargeStatus.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class LaptopChargeStatus(genpy.Message):
  _md5sum = "201bffbb268bdae8f8389acae4ae6db2"
  _type = "eddiebot_node/LaptopChargeStatus"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """uint8 DISCHARGING = 0
uint8 CHARGING    = 1
uint8 CHARGED     = 2

Header  header
float32 voltage          # Voltage in Volts
float32 rate             # Negative when discharging (A)
float32 charge           # Current charge in Ah
float32 capacity         # Capacity in Ah (last full capacity)
float32 design_capacity  # Capacity in Ah (design capacity)
int32   percentage       # Charge percentage
uint8   charge_state     # Enum 
bool    present          # Should be an error if battery is not present
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

"""
  # Pseudo-constants
  DISCHARGING = 0
  CHARGING = 1
  CHARGED = 2

  __slots__ = ['header','voltage','rate','charge','capacity','design_capacity','percentage','charge_state','present']
  _slot_types = ['std_msgs/Header','float32','float32','float32','float32','float32','int32','uint8','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,voltage,rate,charge,capacity,design_capacity,percentage,charge_state,present

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LaptopChargeStatus, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.voltage is None:
        self.voltage = 0.
      if self.rate is None:
        self.rate = 0.
      if self.charge is None:
        self.charge = 0.
      if self.capacity is None:
        self.capacity = 0.
      if self.design_capacity is None:
        self.design_capacity = 0.
      if self.percentage is None:
        self.percentage = 0
      if self.charge_state is None:
        self.charge_state = 0
      if self.present is None:
        self.present = False
    else:
      self.header = std_msgs.msg.Header()
      self.voltage = 0.
      self.rate = 0.
      self.charge = 0.
      self.capacity = 0.
      self.design_capacity = 0.
      self.percentage = 0
      self.charge_state = 0
      self.present = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_5fi2B.pack(_x.voltage, _x.rate, _x.charge, _x.capacity, _x.design_capacity, _x.percentage, _x.charge_state, _x.present))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 26
      (_x.voltage, _x.rate, _x.charge, _x.capacity, _x.design_capacity, _x.percentage, _x.charge_state, _x.present,) = _struct_5fi2B.unpack(str[start:end])
      self.present = bool(self.present)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_5fi2B.pack(_x.voltage, _x.rate, _x.charge, _x.capacity, _x.design_capacity, _x.percentage, _x.charge_state, _x.present))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 26
      (_x.voltage, _x.rate, _x.charge, _x.capacity, _x.design_capacity, _x.percentage, _x.charge_state, _x.present,) = _struct_5fi2B.unpack(str[start:end])
      self.present = bool(self.present)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_5fi2B = struct.Struct("<5fi2B")
