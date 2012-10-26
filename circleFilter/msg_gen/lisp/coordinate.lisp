; Auto-generated. Do not edit!


(cl:in-package circleFilter-msg)


;//! \htmlinclude coordinate.msg.html

(cl:defclass <coordinate> (roslisp-msg-protocol:ros-message)
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
   (theta
    :reader theta
    :initarg :theta
    :type cl:float
    :initform 0.0)
   (beaconcount
    :reader beaconcount
    :initarg :beaconcount
    :type cl:fixnum
    :initform 0))
)

(cl:defclass coordinate (<coordinate>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <coordinate>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'coordinate)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name circleFilter-msg:<coordinate> is deprecated: use circleFilter-msg:coordinate instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <coordinate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader circleFilter-msg:x-val is deprecated.  Use circleFilter-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <coordinate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader circleFilter-msg:y-val is deprecated.  Use circleFilter-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'theta-val :lambda-list '(m))
(cl:defmethod theta-val ((m <coordinate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader circleFilter-msg:theta-val is deprecated.  Use circleFilter-msg:theta instead.")
  (theta m))

(cl:ensure-generic-function 'beaconcount-val :lambda-list '(m))
(cl:defmethod beaconcount-val ((m <coordinate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader circleFilter-msg:beaconcount-val is deprecated.  Use circleFilter-msg:beaconcount instead.")
  (beaconcount m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <coordinate>) ostream)
  "Serializes a message object of type '<coordinate>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'theta))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'beaconcount)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <coordinate>) istream)
  "Deserializes a message object of type '<coordinate>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'theta) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'beaconcount) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<coordinate>)))
  "Returns string type for a message object of type '<coordinate>"
  "circleFilter/coordinate")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'coordinate)))
  "Returns string type for a message object of type 'coordinate"
  "circleFilter/coordinate")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<coordinate>)))
  "Returns md5sum for a message object of type '<coordinate>"
  "fa83e32d0048a022a60f823f2d5ea524")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'coordinate)))
  "Returns md5sum for a message object of type 'coordinate"
  "fa83e32d0048a022a60f823f2d5ea524")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<coordinate>)))
  "Returns full string definition for message of type '<coordinate>"
  (cl:format cl:nil "float64 x~%float64 y~%float64 theta~%int8 beaconcount~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'coordinate)))
  "Returns full string definition for message of type 'coordinate"
  (cl:format cl:nil "float64 x~%float64 y~%float64 theta~%int8 beaconcount~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <coordinate>))
  (cl:+ 0
     8
     8
     8
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <coordinate>))
  "Converts a ROS message object to a list"
  (cl:list 'coordinate
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':theta (theta msg))
    (cl:cons ':beaconcount (beaconcount msg))
))
