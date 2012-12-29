; Auto-generated. Do not edit!


(cl:in-package eddiebot_node-msg)


;//! \htmlinclude Eddie.msg.html

(cl:defclass <Eddie> (roslisp-msg-protocol:ros-message)
  ((linear
    :reader linear
    :initarg :linear
    :type cl:float
    :initform 0.0)
   (angular
    :reader angular
    :initarg :angular
    :type cl:float
    :initform 0.0))
)

(cl:defclass Eddie (<Eddie>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Eddie>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Eddie)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name eddiebot_node-msg:<Eddie> is deprecated: use eddiebot_node-msg:Eddie instead.")))

(cl:ensure-generic-function 'linear-val :lambda-list '(m))
(cl:defmethod linear-val ((m <Eddie>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader eddiebot_node-msg:linear-val is deprecated.  Use eddiebot_node-msg:linear instead.")
  (linear m))

(cl:ensure-generic-function 'angular-val :lambda-list '(m))
(cl:defmethod angular-val ((m <Eddie>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader eddiebot_node-msg:angular-val is deprecated.  Use eddiebot_node-msg:angular instead.")
  (angular m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Eddie>) ostream)
  "Serializes a message object of type '<Eddie>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'linear))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'angular))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Eddie>) istream)
  "Deserializes a message object of type '<Eddie>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'linear) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angular) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Eddie>)))
  "Returns string type for a message object of type '<Eddie>"
  "eddiebot_node/Eddie")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Eddie)))
  "Returns string type for a message object of type 'Eddie"
  "eddiebot_node/Eddie")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Eddie>)))
  "Returns md5sum for a message object of type '<Eddie>"
  "9d5c2dcd348ac8f76ce2a4307bd63a13")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Eddie)))
  "Returns md5sum for a message object of type 'Eddie"
  "9d5c2dcd348ac8f76ce2a4307bd63a13")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Eddie>)))
  "Returns full string definition for message of type '<Eddie>"
  (cl:format cl:nil "float32 linear~%float32 angular~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Eddie)))
  "Returns full string definition for message of type 'Eddie"
  (cl:format cl:nil "float32 linear~%float32 angular~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Eddie>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Eddie>))
  "Converts a ROS message object to a list"
  (cl:list 'Eddie
    (cl:cons ':linear (linear msg))
    (cl:cons ':angular (angular msg))
))
