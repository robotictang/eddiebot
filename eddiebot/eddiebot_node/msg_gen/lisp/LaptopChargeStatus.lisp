; Auto-generated. Do not edit!


(cl:in-package eddiebot_node-msg)


;//! \htmlinclude LaptopChargeStatus.msg.html

(cl:defclass <LaptopChargeStatus> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (voltage
    :reader voltage
    :initarg :voltage
    :type cl:float
    :initform 0.0)
   (rate
    :reader rate
    :initarg :rate
    :type cl:float
    :initform 0.0)
   (charge
    :reader charge
    :initarg :charge
    :type cl:float
    :initform 0.0)
   (capacity
    :reader capacity
    :initarg :capacity
    :type cl:float
    :initform 0.0)
   (design_capacity
    :reader design_capacity
    :initarg :design_capacity
    :type cl:float
    :initform 0.0)
   (percentage
    :reader percentage
    :initarg :percentage
    :type cl:integer
    :initform 0)
   (charge_state
    :reader charge_state
    :initarg :charge_state
    :type cl:fixnum
    :initform 0)
   (present
    :reader present
    :initarg :present
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass LaptopChargeStatus (<LaptopChargeStatus>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LaptopChargeStatus>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LaptopChargeStatus)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name eddiebot_node-msg:<LaptopChargeStatus> is deprecated: use eddiebot_node-msg:LaptopChargeStatus instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <LaptopChargeStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader eddiebot_node-msg:header-val is deprecated.  Use eddiebot_node-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'voltage-val :lambda-list '(m))
(cl:defmethod voltage-val ((m <LaptopChargeStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader eddiebot_node-msg:voltage-val is deprecated.  Use eddiebot_node-msg:voltage instead.")
  (voltage m))

(cl:ensure-generic-function 'rate-val :lambda-list '(m))
(cl:defmethod rate-val ((m <LaptopChargeStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader eddiebot_node-msg:rate-val is deprecated.  Use eddiebot_node-msg:rate instead.")
  (rate m))

(cl:ensure-generic-function 'charge-val :lambda-list '(m))
(cl:defmethod charge-val ((m <LaptopChargeStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader eddiebot_node-msg:charge-val is deprecated.  Use eddiebot_node-msg:charge instead.")
  (charge m))

(cl:ensure-generic-function 'capacity-val :lambda-list '(m))
(cl:defmethod capacity-val ((m <LaptopChargeStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader eddiebot_node-msg:capacity-val is deprecated.  Use eddiebot_node-msg:capacity instead.")
  (capacity m))

(cl:ensure-generic-function 'design_capacity-val :lambda-list '(m))
(cl:defmethod design_capacity-val ((m <LaptopChargeStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader eddiebot_node-msg:design_capacity-val is deprecated.  Use eddiebot_node-msg:design_capacity instead.")
  (design_capacity m))

(cl:ensure-generic-function 'percentage-val :lambda-list '(m))
(cl:defmethod percentage-val ((m <LaptopChargeStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader eddiebot_node-msg:percentage-val is deprecated.  Use eddiebot_node-msg:percentage instead.")
  (percentage m))

(cl:ensure-generic-function 'charge_state-val :lambda-list '(m))
(cl:defmethod charge_state-val ((m <LaptopChargeStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader eddiebot_node-msg:charge_state-val is deprecated.  Use eddiebot_node-msg:charge_state instead.")
  (charge_state m))

(cl:ensure-generic-function 'present-val :lambda-list '(m))
(cl:defmethod present-val ((m <LaptopChargeStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader eddiebot_node-msg:present-val is deprecated.  Use eddiebot_node-msg:present instead.")
  (present m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<LaptopChargeStatus>)))
    "Constants for message type '<LaptopChargeStatus>"
  '((:DISCHARGING . 0)
    (:CHARGING . 1)
    (:CHARGED . 2))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'LaptopChargeStatus)))
    "Constants for message type 'LaptopChargeStatus"
  '((:DISCHARGING . 0)
    (:CHARGING . 1)
    (:CHARGED . 2))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LaptopChargeStatus>) ostream)
  "Serializes a message object of type '<LaptopChargeStatus>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'voltage))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'rate))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'charge))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'capacity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'design_capacity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'percentage)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'charge_state)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'present) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LaptopChargeStatus>) istream)
  "Deserializes a message object of type '<LaptopChargeStatus>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'voltage) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'rate) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'charge) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'capacity) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'design_capacity) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'percentage) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'charge_state)) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'present) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LaptopChargeStatus>)))
  "Returns string type for a message object of type '<LaptopChargeStatus>"
  "eddiebot_node/LaptopChargeStatus")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LaptopChargeStatus)))
  "Returns string type for a message object of type 'LaptopChargeStatus"
  "eddiebot_node/LaptopChargeStatus")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LaptopChargeStatus>)))
  "Returns md5sum for a message object of type '<LaptopChargeStatus>"
  "201bffbb268bdae8f8389acae4ae6db2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LaptopChargeStatus)))
  "Returns md5sum for a message object of type 'LaptopChargeStatus"
  "201bffbb268bdae8f8389acae4ae6db2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LaptopChargeStatus>)))
  "Returns full string definition for message of type '<LaptopChargeStatus>"
  (cl:format cl:nil "uint8 DISCHARGING = 0~%uint8 CHARGING    = 1~%uint8 CHARGED     = 2~%~%Header  header~%float32 voltage          # Voltage in Volts~%float32 rate             # Negative when discharging (A)~%float32 charge           # Current charge in Ah~%float32 capacity         # Capacity in Ah (last full capacity)~%float32 design_capacity  # Capacity in Ah (design capacity)~%int32   percentage       # Charge percentage~%uint8   charge_state     # Enum ~%bool    present          # Should be an error if battery is not present~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LaptopChargeStatus)))
  "Returns full string definition for message of type 'LaptopChargeStatus"
  (cl:format cl:nil "uint8 DISCHARGING = 0~%uint8 CHARGING    = 1~%uint8 CHARGED     = 2~%~%Header  header~%float32 voltage          # Voltage in Volts~%float32 rate             # Negative when discharging (A)~%float32 charge           # Current charge in Ah~%float32 capacity         # Capacity in Ah (last full capacity)~%float32 design_capacity  # Capacity in Ah (design capacity)~%int32   percentage       # Charge percentage~%uint8   charge_state     # Enum ~%bool    present          # Should be an error if battery is not present~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LaptopChargeStatus>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
     4
     4
     4
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LaptopChargeStatus>))
  "Converts a ROS message object to a list"
  (cl:list 'LaptopChargeStatus
    (cl:cons ':header (header msg))
    (cl:cons ':voltage (voltage msg))
    (cl:cons ':rate (rate msg))
    (cl:cons ':charge (charge msg))
    (cl:cons ':capacity (capacity msg))
    (cl:cons ':design_capacity (design_capacity msg))
    (cl:cons ':percentage (percentage msg))
    (cl:cons ':charge_state (charge_state msg))
    (cl:cons ':present (present msg))
))
