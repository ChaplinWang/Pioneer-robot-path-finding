; Auto-generated. Do not edit!


(cl:in-package circleFilter-srv)


;//! \htmlinclude stateChange-request.msg.html

(cl:defclass <stateChange-request> (roslisp-msg-protocol:ros-message)
  ((state
    :reader state
    :initarg :state
    :type cl:fixnum
    :initform 0))
)

(cl:defclass stateChange-request (<stateChange-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <stateChange-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'stateChange-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name circleFilter-srv:<stateChange-request> is deprecated: use circleFilter-srv:stateChange-request instead.")))

(cl:ensure-generic-function 'state-val :lambda-list '(m))
(cl:defmethod state-val ((m <stateChange-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader circleFilter-srv:state-val is deprecated.  Use circleFilter-srv:state instead.")
  (state m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <stateChange-request>) ostream)
  "Serializes a message object of type '<stateChange-request>"
  (cl:let* ((signed (cl:slot-value msg 'state)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <stateChange-request>) istream)
  "Deserializes a message object of type '<stateChange-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<stateChange-request>)))
  "Returns string type for a service object of type '<stateChange-request>"
  "circleFilter/stateChangeRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'stateChange-request)))
  "Returns string type for a service object of type 'stateChange-request"
  "circleFilter/stateChangeRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<stateChange-request>)))
  "Returns md5sum for a message object of type '<stateChange-request>"
  "a9cd65d8935b4ee9054d79a1f68a4f05")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'stateChange-request)))
  "Returns md5sum for a message object of type 'stateChange-request"
  "a9cd65d8935b4ee9054d79a1f68a4f05")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<stateChange-request>)))
  "Returns full string definition for message of type '<stateChange-request>"
  (cl:format cl:nil "int8 state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'stateChange-request)))
  "Returns full string definition for message of type 'stateChange-request"
  (cl:format cl:nil "int8 state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <stateChange-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <stateChange-request>))
  "Converts a ROS message object to a list"
  (cl:list 'stateChange-request
    (cl:cons ':state (state msg))
))
;//! \htmlinclude stateChange-response.msg.html

(cl:defclass <stateChange-response> (roslisp-msg-protocol:ros-message)
  ((ok
    :reader ok
    :initarg :ok
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass stateChange-response (<stateChange-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <stateChange-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'stateChange-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name circleFilter-srv:<stateChange-response> is deprecated: use circleFilter-srv:stateChange-response instead.")))

(cl:ensure-generic-function 'ok-val :lambda-list '(m))
(cl:defmethod ok-val ((m <stateChange-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader circleFilter-srv:ok-val is deprecated.  Use circleFilter-srv:ok instead.")
  (ok m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <stateChange-response>) ostream)
  "Serializes a message object of type '<stateChange-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'ok) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <stateChange-response>) istream)
  "Deserializes a message object of type '<stateChange-response>"
    (cl:setf (cl:slot-value msg 'ok) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<stateChange-response>)))
  "Returns string type for a service object of type '<stateChange-response>"
  "circleFilter/stateChangeResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'stateChange-response)))
  "Returns string type for a service object of type 'stateChange-response"
  "circleFilter/stateChangeResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<stateChange-response>)))
  "Returns md5sum for a message object of type '<stateChange-response>"
  "a9cd65d8935b4ee9054d79a1f68a4f05")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'stateChange-response)))
  "Returns md5sum for a message object of type 'stateChange-response"
  "a9cd65d8935b4ee9054d79a1f68a4f05")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<stateChange-response>)))
  "Returns full string definition for message of type '<stateChange-response>"
  (cl:format cl:nil "bool ok~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'stateChange-response)))
  "Returns full string definition for message of type 'stateChange-response"
  (cl:format cl:nil "bool ok~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <stateChange-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <stateChange-response>))
  "Converts a ROS message object to a list"
  (cl:list 'stateChange-response
    (cl:cons ':ok (ok msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'stateChange)))
  'stateChange-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'stateChange)))
  'stateChange-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'stateChange)))
  "Returns string type for a service object of type '<stateChange>"
  "circleFilter/stateChange")
