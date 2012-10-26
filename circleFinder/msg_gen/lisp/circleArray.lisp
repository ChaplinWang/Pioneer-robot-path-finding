; Auto-generated. Do not edit!


(cl:in-package circleFinder-msg)


;//! \htmlinclude circleArray.msg.html

(cl:defclass <circleArray> (roslisp-msg-protocol:ros-message)
  ((broadcastTime
    :reader broadcastTime
    :initarg :broadcastTime
    :type cl:real
    :initform 0)
   (duration
    :reader duration
    :initarg :duration
    :type cl:float
    :initform 0.0)
   (array
    :reader array
    :initarg :array
    :type (cl:vector circleFinder-msg:circleEntry)
   :initform (cl:make-array 0 :element-type 'circleFinder-msg:circleEntry :initial-element (cl:make-instance 'circleFinder-msg:circleEntry))))
)

(cl:defclass circleArray (<circleArray>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <circleArray>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'circleArray)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name circleFinder-msg:<circleArray> is deprecated: use circleFinder-msg:circleArray instead.")))

(cl:ensure-generic-function 'broadcastTime-val :lambda-list '(m))
(cl:defmethod broadcastTime-val ((m <circleArray>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader circleFinder-msg:broadcastTime-val is deprecated.  Use circleFinder-msg:broadcastTime instead.")
  (broadcastTime m))

(cl:ensure-generic-function 'duration-val :lambda-list '(m))
(cl:defmethod duration-val ((m <circleArray>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader circleFinder-msg:duration-val is deprecated.  Use circleFinder-msg:duration instead.")
  (duration m))

(cl:ensure-generic-function 'array-val :lambda-list '(m))
(cl:defmethod array-val ((m <circleArray>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader circleFinder-msg:array-val is deprecated.  Use circleFinder-msg:array instead.")
  (array m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <circleArray>) ostream)
  "Serializes a message object of type '<circleArray>"
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'broadcastTime)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'broadcastTime) (cl:floor (cl:slot-value msg 'broadcastTime)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'duration))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'array))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'array))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <circleArray>) istream)
  "Deserializes a message object of type '<circleArray>"
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'broadcastTime) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'duration) (roslisp-utils:decode-single-float-bits bits)))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'array) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'array)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'circleFinder-msg:circleEntry))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<circleArray>)))
  "Returns string type for a message object of type '<circleArray>"
  "circleFinder/circleArray")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'circleArray)))
  "Returns string type for a message object of type 'circleArray"
  "circleFinder/circleArray")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<circleArray>)))
  "Returns md5sum for a message object of type '<circleArray>"
  "00508b03c8630a4b200fe9395178279d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'circleArray)))
  "Returns md5sum for a message object of type 'circleArray"
  "00508b03c8630a4b200fe9395178279d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<circleArray>)))
  "Returns full string definition for message of type '<circleArray>"
  (cl:format cl:nil "time broadcastTime~%float32 duration~%circleEntry[] array~%~%================================================================================~%MSG: circleFinder/circleEntry~%float32 x~%float32 y~%float32 distance~%float32 theta~%float32 radius~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'circleArray)))
  "Returns full string definition for message of type 'circleArray"
  (cl:format cl:nil "time broadcastTime~%float32 duration~%circleEntry[] array~%~%================================================================================~%MSG: circleFinder/circleEntry~%float32 x~%float32 y~%float32 distance~%float32 theta~%float32 radius~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <circleArray>))
  (cl:+ 0
     8
     4
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'array) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <circleArray>))
  "Converts a ROS message object to a list"
  (cl:list 'circleArray
    (cl:cons ':broadcastTime (broadcastTime msg))
    (cl:cons ':duration (duration msg))
    (cl:cons ':array (array msg))
))
