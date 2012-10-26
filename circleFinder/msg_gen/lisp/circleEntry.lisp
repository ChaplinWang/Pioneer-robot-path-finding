; Auto-generated. Do not edit!


(cl:in-package circleFinder-msg)


;//! \htmlinclude circleEntry.msg.html

(cl:defclass <circleEntry> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0)
   (distance
    :reader distance
    :initarg :distance
    :type cl:float
    :initform 0.0)
   (theta
    :reader theta
    :initarg :theta
    :type cl:float
    :initform 0.0)
   (radius
    :reader radius
    :initarg :radius
    :type cl:float
    :initform 0.0))
)

(cl:defclass circleEntry (<circleEntry>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <circleEntry>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'circleEntry)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name circleFinder-msg:<circleEntry> is deprecated: use circleFinder-msg:circleEntry instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <circleEntry>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader circleFinder-msg:x-val is deprecated.  Use circleFinder-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <circleEntry>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader circleFinder-msg:y-val is deprecated.  Use circleFinder-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'distance-val :lambda-list '(m))
(cl:defmethod distance-val ((m <circleEntry>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader circleFinder-msg:distance-val is deprecated.  Use circleFinder-msg:distance instead.")
  (distance m))

(cl:ensure-generic-function 'theta-val :lambda-list '(m))
(cl:defmethod theta-val ((m <circleEntry>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader circleFinder-msg:theta-val is deprecated.  Use circleFinder-msg:theta instead.")
  (theta m))

(cl:ensure-generic-function 'radius-val :lambda-list '(m))
(cl:defmethod radius-val ((m <circleEntry>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader circleFinder-msg:radius-val is deprecated.  Use circleFinder-msg:radius instead.")
  (radius m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <circleEntry>) ostream)
  "Serializes a message object of type '<circleEntry>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'theta))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'radius))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <circleEntry>) istream)
  "Deserializes a message object of type '<circleEntry>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'distance) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'theta) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'radius) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<circleEntry>)))
  "Returns string type for a message object of type '<circleEntry>"
  "circleFinder/circleEntry")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'circleEntry)))
  "Returns string type for a message object of type 'circleEntry"
  "circleFinder/circleEntry")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<circleEntry>)))
  "Returns md5sum for a message object of type '<circleEntry>"
  "8f570732ed87e134eeda1a3829552b4e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'circleEntry)))
  "Returns md5sum for a message object of type 'circleEntry"
  "8f570732ed87e134eeda1a3829552b4e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<circleEntry>)))
  "Returns full string definition for message of type '<circleEntry>"
  (cl:format cl:nil "float32 x~%float32 y~%float32 distance~%float32 theta~%float32 radius~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'circleEntry)))
  "Returns full string definition for message of type 'circleEntry"
  (cl:format cl:nil "float32 x~%float32 y~%float32 distance~%float32 theta~%float32 radius~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <circleEntry>))
  (cl:+ 0
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <circleEntry>))
  "Converts a ROS message object to a list"
  (cl:list 'circleEntry
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':distance (distance msg))
    (cl:cons ':theta (theta msg))
    (cl:cons ':radius (radius msg))
))
