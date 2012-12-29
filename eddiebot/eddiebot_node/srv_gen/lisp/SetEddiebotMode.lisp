; Auto-generated. Do not edit!


(cl:in-package eddiebot_node-srv)


;//! \htmlinclude SetEddiebotMode-request.msg.html

(cl:defclass <SetEddiebotMode-request> (roslisp-msg-protocol:ros-message)
  ((mode
    :reader mode
    :initarg :mode
    :type cl:fixnum
    :initform 0))
)

(cl:defclass SetEddiebotMode-request (<SetEddiebotMode-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetEddiebotMode-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetEddiebotMode-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name eddiebot_node-srv:<SetEddiebotMode-request> is deprecated: use eddiebot_node-srv:SetEddiebotMode-request instead.")))

(cl:ensure-generic-function 'mode-val :lambda-list '(m))
(cl:defmethod mode-val ((m <SetEddiebotMode-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader eddiebot_node-srv:mode-val is deprecated.  Use eddiebot_node-srv:mode instead.")
  (mode m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetEddiebotMode-request>) ostream)
  "Serializes a message object of type '<SetEddiebotMode-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'mode)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetEddiebotMode-request>) istream)
  "Deserializes a message object of type '<SetEddiebotMode-request>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'mode)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetEddiebotMode-request>)))
  "Returns string type for a service object of type '<SetEddiebotMode-request>"
  "eddiebot_node/SetEddiebotModeRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetEddiebotMode-request)))
  "Returns string type for a service object of type 'SetEddiebotMode-request"
  "eddiebot_node/SetEddiebotModeRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetEddiebotMode-request>)))
  "Returns md5sum for a message object of type '<SetEddiebotMode-request>"
  "652c4fe00e931153f82f8af90f1da441")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetEddiebotMode-request)))
  "Returns md5sum for a message object of type 'SetEddiebotMode-request"
  "652c4fe00e931153f82f8af90f1da441")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetEddiebotMode-request>)))
  "Returns full string definition for message of type '<SetEddiebotMode-request>"
  (cl:format cl:nil "uint8 mode~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetEddiebotMode-request)))
  "Returns full string definition for message of type 'SetEddiebotMode-request"
  (cl:format cl:nil "uint8 mode~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetEddiebotMode-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetEddiebotMode-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SetEddiebotMode-request
    (cl:cons ':mode (mode msg))
))
;//! \htmlinclude SetEddiebotMode-response.msg.html

(cl:defclass <SetEddiebotMode-response> (roslisp-msg-protocol:ros-message)
  ((valid_mode
    :reader valid_mode
    :initarg :valid_mode
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass SetEddiebotMode-response (<SetEddiebotMode-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetEddiebotMode-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetEddiebotMode-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name eddiebot_node-srv:<SetEddiebotMode-response> is deprecated: use eddiebot_node-srv:SetEddiebotMode-response instead.")))

(cl:ensure-generic-function 'valid_mode-val :lambda-list '(m))
(cl:defmethod valid_mode-val ((m <SetEddiebotMode-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader eddiebot_node-srv:valid_mode-val is deprecated.  Use eddiebot_node-srv:valid_mode instead.")
  (valid_mode m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetEddiebotMode-response>) ostream)
  "Serializes a message object of type '<SetEddiebotMode-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'valid_mode) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetEddiebotMode-response>) istream)
  "Deserializes a message object of type '<SetEddiebotMode-response>"
    (cl:setf (cl:slot-value msg 'valid_mode) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetEddiebotMode-response>)))
  "Returns string type for a service object of type '<SetEddiebotMode-response>"
  "eddiebot_node/SetEddiebotModeResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetEddiebotMode-response)))
  "Returns string type for a service object of type 'SetEddiebotMode-response"
  "eddiebot_node/SetEddiebotModeResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetEddiebotMode-response>)))
  "Returns md5sum for a message object of type '<SetEddiebotMode-response>"
  "652c4fe00e931153f82f8af90f1da441")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetEddiebotMode-response)))
  "Returns md5sum for a message object of type 'SetEddiebotMode-response"
  "652c4fe00e931153f82f8af90f1da441")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetEddiebotMode-response>)))
  "Returns full string definition for message of type '<SetEddiebotMode-response>"
  (cl:format cl:nil "bool valid_mode~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetEddiebotMode-response)))
  "Returns full string definition for message of type 'SetEddiebotMode-response"
  (cl:format cl:nil "bool valid_mode~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetEddiebotMode-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetEddiebotMode-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SetEddiebotMode-response
    (cl:cons ':valid_mode (valid_mode msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SetEddiebotMode)))
  'SetEddiebotMode-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SetEddiebotMode)))
  'SetEddiebotMode-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetEddiebotMode)))
  "Returns string type for a service object of type '<SetEddiebotMode>"
  "eddiebot_node/SetEddiebotMode")