/* Auto-generated by genmsg_cpp for file /home/paralax2/fuerte_workspace/sandbox/eddiebot/eddiebot_node/msg/EddiebotSensorState.msg */
#ifndef EDDIEBOT_NODE_MESSAGE_EDDIEBOTSENSORSTATE_H
#define EDDIEBOT_NODE_MESSAGE_EDDIEBOTSENSORSTATE_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "std_msgs/Header.h"

namespace eddiebot_node
{
template <class ContainerAllocator>
struct EddiebotSensorState_ {
  typedef EddiebotSensorState_<ContainerAllocator> Type;

  EddiebotSensorState_()
  : header()
  , bumps_wheeldrops(0)
  , wall(false)
  , cliff_left(false)
  , cliff_front_left(false)
  , cliff_front_right(false)
  , cliff_right(false)
  , virtual_wall(false)
  , motor_overcurrents(0)
  , dirt_detector_left(0)
  , dirt_detector_right(0)
  , remote_opcode(0)
  , buttons(0)
  , distance(0.0)
  , angle(0.0)
  , charging_state(0)
  , voltage(0)
  , current(0)
  , temperature(0)
  , charge(0)
  , capacity(0)
  , wall_signal(0)
  , cliff_left_signal(0)
  , cliff_front_left_signal(0)
  , cliff_front_right_signal(0)
  , cliff_right_signal(0)
  , user_digital_outputs(0)
  , user_digital_inputs(0)
  , user_analog_input(0)
  , charging_sources_available(0)
  , oi_mode(0)
  , song_number(0)
  , song_playing(false)
  , number_of_stream_packets(0)
  , requested_velocity(0)
  , requested_radius(0)
  , requested_right_velocity(0)
  , requested_left_velocity(0)
  {
  }

  EddiebotSensorState_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , bumps_wheeldrops(0)
  , wall(false)
  , cliff_left(false)
  , cliff_front_left(false)
  , cliff_front_right(false)
  , cliff_right(false)
  , virtual_wall(false)
  , motor_overcurrents(0)
  , dirt_detector_left(0)
  , dirt_detector_right(0)
  , remote_opcode(0)
  , buttons(0)
  , distance(0.0)
  , angle(0.0)
  , charging_state(0)
  , voltage(0)
  , current(0)
  , temperature(0)
  , charge(0)
  , capacity(0)
  , wall_signal(0)
  , cliff_left_signal(0)
  , cliff_front_left_signal(0)
  , cliff_front_right_signal(0)
  , cliff_right_signal(0)
  , user_digital_outputs(0)
  , user_digital_inputs(0)
  , user_analog_input(0)
  , charging_sources_available(0)
  , oi_mode(0)
  , song_number(0)
  , song_playing(false)
  , number_of_stream_packets(0)
  , requested_velocity(0)
  , requested_radius(0)
  , requested_right_velocity(0)
  , requested_left_velocity(0)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef uint8_t _bumps_wheeldrops_type;
  uint8_t bumps_wheeldrops;

  typedef uint8_t _wall_type;
  uint8_t wall;

  typedef uint8_t _cliff_left_type;
  uint8_t cliff_left;

  typedef uint8_t _cliff_front_left_type;
  uint8_t cliff_front_left;

  typedef uint8_t _cliff_front_right_type;
  uint8_t cliff_front_right;

  typedef uint8_t _cliff_right_type;
  uint8_t cliff_right;

  typedef uint8_t _virtual_wall_type;
  uint8_t virtual_wall;

  typedef uint8_t _motor_overcurrents_type;
  uint8_t motor_overcurrents;

  typedef uint8_t _dirt_detector_left_type;
  uint8_t dirt_detector_left;

  typedef uint8_t _dirt_detector_right_type;
  uint8_t dirt_detector_right;

  typedef uint8_t _remote_opcode_type;
  uint8_t remote_opcode;

  typedef uint8_t _buttons_type;
  uint8_t buttons;

  typedef double _distance_type;
  double distance;

  typedef double _angle_type;
  double angle;

  typedef uint8_t _charging_state_type;
  uint8_t charging_state;

  typedef uint16_t _voltage_type;
  uint16_t voltage;

  typedef int16_t _current_type;
  int16_t current;

  typedef int8_t _temperature_type;
  int8_t temperature;

  typedef uint16_t _charge_type;
  uint16_t charge;

  typedef uint16_t _capacity_type;
  uint16_t capacity;

  typedef uint16_t _wall_signal_type;
  uint16_t wall_signal;

  typedef uint16_t _cliff_left_signal_type;
  uint16_t cliff_left_signal;

  typedef uint16_t _cliff_front_left_signal_type;
  uint16_t cliff_front_left_signal;

  typedef uint16_t _cliff_front_right_signal_type;
  uint16_t cliff_front_right_signal;

  typedef uint16_t _cliff_right_signal_type;
  uint16_t cliff_right_signal;

  typedef uint8_t _user_digital_outputs_type;
  uint8_t user_digital_outputs;

  typedef uint8_t _user_digital_inputs_type;
  uint8_t user_digital_inputs;

  typedef uint16_t _user_analog_input_type;
  uint16_t user_analog_input;

  typedef uint8_t _charging_sources_available_type;
  uint8_t charging_sources_available;

  typedef uint8_t _oi_mode_type;
  uint8_t oi_mode;

  typedef uint8_t _song_number_type;
  uint8_t song_number;

  typedef uint8_t _song_playing_type;
  uint8_t song_playing;

  typedef uint8_t _number_of_stream_packets_type;
  uint8_t number_of_stream_packets;

  typedef int32_t _requested_velocity_type;
  int32_t requested_velocity;

  typedef int32_t _requested_radius_type;
  int32_t requested_radius;

  typedef int32_t _requested_right_velocity_type;
  int32_t requested_right_velocity;

  typedef int32_t _requested_left_velocity_type;
  int32_t requested_left_velocity;

  enum { OI_MODE_OFF = 0 };
  enum { OI_MODE_PASSIVE = 1 };
  enum { OI_MODE_SAFE = 2 };
  enum { OI_MODE_FULL = 3 };
  enum { REMOTE_LEFT = 129 };
  enum { REMOTE_FORWARD = 130 };
  enum { REMOTE_RIGHT = 131 };
  enum { REMOTE_SPOT = 132 };
  enum { REMOTE_MAX = 133 };
  enum { REMOTE_SMALL = 134 };
  enum { REMOTE_MEDIUM = 135 };
  enum { REMOTE_LARGE = 136 };
  enum { REMOTE_CLEAN = 136 };
  enum { REMOTE_PAUSE = 137 };
  enum { REMOTE_POWER = 138 };
  enum { REMOTE_ARC_LEFT = 139 };
  enum { REMOTE_ARC_RIGHT = 140 };
  enum { REMOTE_DRIVE_STOP = 141 };
  enum { REMOTE_SEND_ALL = 142 };
  enum { REMOTE_SEEK_DOCK = 143 };
  enum { REMOTE_RESERVED = 240 };
  enum { REMOTE_FORCE_FIELD = 242 };
  enum { REMOTE_GREEN_BUOY = 244 };
  enum { REMOTE_GREEN_BUOY_AND_FORCE_FIELD = 246 };
  enum { REMOTE_RED_BUOY = 248 };
  enum { REMOTE_RED_BUOY_AND_FORCE_FIELD = 250 };
  enum { REMOTE_RED_BUOY_AND_GREEN_BUOY = 252 };
  enum { REMOTE_RED_BUOY_AND_GREEN_BUOY_AND_FORCE_FIELD = 254 };
  enum { REMOTE_NONE = 255 };
  enum { CHARGING_NOT_CHARGING = 0 };
  enum { CHARGING_CHARGING_RECOVERY = 1 };
  enum { CHARGING_CHARGING = 2 };
  enum { CHARGING_TRICKLE_CHARGING = 3 };
  enum { CHARGING_WAITING = 4 };
  enum { CHARGING_CHARGING_ERROR = 5 };

  typedef boost::shared_ptr< ::eddiebot_node::EddiebotSensorState_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::eddiebot_node::EddiebotSensorState_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct EddiebotSensorState
typedef  ::eddiebot_node::EddiebotSensorState_<std::allocator<void> > EddiebotSensorState;

typedef boost::shared_ptr< ::eddiebot_node::EddiebotSensorState> EddiebotSensorStatePtr;
typedef boost::shared_ptr< ::eddiebot_node::EddiebotSensorState const> EddiebotSensorStateConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::eddiebot_node::EddiebotSensorState_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::eddiebot_node::EddiebotSensorState_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace eddiebot_node

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::eddiebot_node::EddiebotSensorState_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::eddiebot_node::EddiebotSensorState_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::eddiebot_node::EddiebotSensorState_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d8f8ec7fa031fc9cc88e8319cd08a785";
  }

  static const char* value(const  ::eddiebot_node::EddiebotSensorState_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xd8f8ec7fa031fc9cULL;
  static const uint64_t static_value2 = 0xc88e8319cd08a785ULL;
};

template<class ContainerAllocator>
struct DataType< ::eddiebot_node::EddiebotSensorState_<ContainerAllocator> > {
  static const char* value() 
  {
    return "eddiebot_node/EddiebotSensorState";
  }

  static const char* value(const  ::eddiebot_node::EddiebotSensorState_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::eddiebot_node::EddiebotSensorState_<ContainerAllocator> > {
  static const char* value() 
  {
    return "uint8 OI_MODE_OFF = 0\n\
uint8 OI_MODE_PASSIVE = 1\n\
uint8 OI_MODE_SAFE = 2\n\
uint8 OI_MODE_FULL = 3\n\
\n\
uint8 REMOTE_LEFT = 129\n\
uint8 REMOTE_FORWARD = 130 \n\
uint8 REMOTE_RIGHT = 131 \n\
uint8 REMOTE_SPOT = 132 \n\
uint8 REMOTE_MAX = 133 \n\
uint8 REMOTE_SMALL = 134 \n\
uint8 REMOTE_MEDIUM = 135 \n\
uint8 REMOTE_LARGE = 136 \n\
uint8 REMOTE_CLEAN = 136 \n\
uint8 REMOTE_PAUSE = 137 \n\
uint8 REMOTE_POWER = 138 \n\
uint8 REMOTE_ARC_LEFT = 139 \n\
uint8 REMOTE_ARC_RIGHT = 140 \n\
uint8 REMOTE_DRIVE_STOP = 141 \n\
# Scheduling remote\n\
uint8 REMOTE_SEND_ALL = 142 \n\
uint8 REMOTE_SEEK_DOCK = 143 \n\
# Home base\n\
uint8 REMOTE_RESERVED = 240 \n\
uint8 REMOTE_FORCE_FIELD = 242 \n\
uint8 REMOTE_GREEN_BUOY = 244 \n\
uint8 REMOTE_GREEN_BUOY_AND_FORCE_FIELD = 246 \n\
uint8 REMOTE_RED_BUOY = 248 \n\
uint8 REMOTE_RED_BUOY_AND_FORCE_FIELD = 250 \n\
uint8 REMOTE_RED_BUOY_AND_GREEN_BUOY = 252 \n\
uint8 REMOTE_RED_BUOY_AND_GREEN_BUOY_AND_FORCE_FIELD = 254 \n\
uint8 REMOTE_NONE = 255\n\
\n\
uint8 CHARGING_NOT_CHARGING = 0\n\
uint8 CHARGING_CHARGING_RECOVERY = 1\n\
uint8 CHARGING_CHARGING = 2\n\
uint8 CHARGING_TRICKLE_CHARGING = 3\n\
uint8 CHARGING_WAITING = 4 \n\
uint8 CHARGING_CHARGING_ERROR = 5\n\
\n\
Header header\n\
\n\
uint8 bumps_wheeldrops\n\
bool wall\n\
bool cliff_left\n\
bool cliff_front_left\n\
bool cliff_front_right\n\
bool cliff_right\n\
bool virtual_wall\n\
uint8 motor_overcurrents\n\
uint8 dirt_detector_left  #roomba_only\n\
uint8 dirt_detector_right #roomba_only\n\
uint8 remote_opcode\n\
uint8 buttons\n\
float64 distance  # m\n\
float64 angle #radians\n\
uint8 charging_state\n\
uint16 voltage  # mV\n\
int16 current  # mA\n\
int8 temperature  # C\n\
uint16 charge  # mAh\n\
uint16 capacity  # mAh\n\
\n\
uint16 wall_signal\n\
uint16 cliff_left_signal\n\
uint16 cliff_front_left_signal\n\
uint16 cliff_front_right_signal\n\
uint16 cliff_right_signal\n\
uint8 user_digital_outputs\n\
uint8 user_digital_inputs\n\
uint16 user_analog_input\n\
uint8 charging_sources_available\n\
uint8 oi_mode\n\
uint8 song_number\n\
bool song_playing\n\
\n\
uint8 number_of_stream_packets\n\
int32 requested_velocity  # m/s\n\
int32 requested_radius  # m\n\
int32 requested_right_velocity  # m/s\n\
int32 requested_left_velocity  # m/s\n\
\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.secs: seconds (stamp_secs) since epoch\n\
# * stamp.nsecs: nanoseconds since stamp_secs\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
";
  }

  static const char* value(const  ::eddiebot_node::EddiebotSensorState_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::eddiebot_node::EddiebotSensorState_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::eddiebot_node::EddiebotSensorState_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::eddiebot_node::EddiebotSensorState_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.bumps_wheeldrops);
    stream.next(m.wall);
    stream.next(m.cliff_left);
    stream.next(m.cliff_front_left);
    stream.next(m.cliff_front_right);
    stream.next(m.cliff_right);
    stream.next(m.virtual_wall);
    stream.next(m.motor_overcurrents);
    stream.next(m.dirt_detector_left);
    stream.next(m.dirt_detector_right);
    stream.next(m.remote_opcode);
    stream.next(m.buttons);
    stream.next(m.distance);
    stream.next(m.angle);
    stream.next(m.charging_state);
    stream.next(m.voltage);
    stream.next(m.current);
    stream.next(m.temperature);
    stream.next(m.charge);
    stream.next(m.capacity);
    stream.next(m.wall_signal);
    stream.next(m.cliff_left_signal);
    stream.next(m.cliff_front_left_signal);
    stream.next(m.cliff_front_right_signal);
    stream.next(m.cliff_right_signal);
    stream.next(m.user_digital_outputs);
    stream.next(m.user_digital_inputs);
    stream.next(m.user_analog_input);
    stream.next(m.charging_sources_available);
    stream.next(m.oi_mode);
    stream.next(m.song_number);
    stream.next(m.song_playing);
    stream.next(m.number_of_stream_packets);
    stream.next(m.requested_velocity);
    stream.next(m.requested_radius);
    stream.next(m.requested_right_velocity);
    stream.next(m.requested_left_velocity);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct EddiebotSensorState_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::eddiebot_node::EddiebotSensorState_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::eddiebot_node::EddiebotSensorState_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "bumps_wheeldrops: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.bumps_wheeldrops);
    s << indent << "wall: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.wall);
    s << indent << "cliff_left: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.cliff_left);
    s << indent << "cliff_front_left: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.cliff_front_left);
    s << indent << "cliff_front_right: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.cliff_front_right);
    s << indent << "cliff_right: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.cliff_right);
    s << indent << "virtual_wall: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.virtual_wall);
    s << indent << "motor_overcurrents: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.motor_overcurrents);
    s << indent << "dirt_detector_left: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.dirt_detector_left);
    s << indent << "dirt_detector_right: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.dirt_detector_right);
    s << indent << "remote_opcode: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.remote_opcode);
    s << indent << "buttons: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.buttons);
    s << indent << "distance: ";
    Printer<double>::stream(s, indent + "  ", v.distance);
    s << indent << "angle: ";
    Printer<double>::stream(s, indent + "  ", v.angle);
    s << indent << "charging_state: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.charging_state);
    s << indent << "voltage: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.voltage);
    s << indent << "current: ";
    Printer<int16_t>::stream(s, indent + "  ", v.current);
    s << indent << "temperature: ";
    Printer<int8_t>::stream(s, indent + "  ", v.temperature);
    s << indent << "charge: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.charge);
    s << indent << "capacity: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.capacity);
    s << indent << "wall_signal: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.wall_signal);
    s << indent << "cliff_left_signal: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.cliff_left_signal);
    s << indent << "cliff_front_left_signal: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.cliff_front_left_signal);
    s << indent << "cliff_front_right_signal: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.cliff_front_right_signal);
    s << indent << "cliff_right_signal: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.cliff_right_signal);
    s << indent << "user_digital_outputs: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.user_digital_outputs);
    s << indent << "user_digital_inputs: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.user_digital_inputs);
    s << indent << "user_analog_input: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.user_analog_input);
    s << indent << "charging_sources_available: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.charging_sources_available);
    s << indent << "oi_mode: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.oi_mode);
    s << indent << "song_number: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.song_number);
    s << indent << "song_playing: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.song_playing);
    s << indent << "number_of_stream_packets: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.number_of_stream_packets);
    s << indent << "requested_velocity: ";
    Printer<int32_t>::stream(s, indent + "  ", v.requested_velocity);
    s << indent << "requested_radius: ";
    Printer<int32_t>::stream(s, indent + "  ", v.requested_radius);
    s << indent << "requested_right_velocity: ";
    Printer<int32_t>::stream(s, indent + "  ", v.requested_right_velocity);
    s << indent << "requested_left_velocity: ";
    Printer<int32_t>::stream(s, indent + "  ", v.requested_left_velocity);
  }
};


} // namespace message_operations
} // namespace ros

#endif // EDDIEBOT_NODE_MESSAGE_EDDIEBOTSENSORSTATE_H

