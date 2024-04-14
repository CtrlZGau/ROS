; Auto-generated. Do not edit!


(cl:in-package mobile_manipulator_body-srv)


;//! \htmlinclude velocity-request.msg.html

(cl:defclass <velocity-request> (roslisp-msg-protocol:ros-message)
  ((sec_int
    :reader sec_int
    :initarg :sec_int
    :type cl:integer
    :initform 0))
)

(cl:defclass velocity-request (<velocity-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <velocity-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'velocity-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mobile_manipulator_body-srv:<velocity-request> is deprecated: use mobile_manipulator_body-srv:velocity-request instead.")))

(cl:ensure-generic-function 'sec_int-val :lambda-list '(m))
(cl:defmethod sec_int-val ((m <velocity-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mobile_manipulator_body-srv:sec_int-val is deprecated.  Use mobile_manipulator_body-srv:sec_int instead.")
  (sec_int m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <velocity-request>) ostream)
  "Serializes a message object of type '<velocity-request>"
  (cl:let* ((signed (cl:slot-value msg 'sec_int)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <velocity-request>) istream)
  "Deserializes a message object of type '<velocity-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'sec_int) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<velocity-request>)))
  "Returns string type for a service object of type '<velocity-request>"
  "mobile_manipulator_body/velocityRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'velocity-request)))
  "Returns string type for a service object of type 'velocity-request"
  "mobile_manipulator_body/velocityRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<velocity-request>)))
  "Returns md5sum for a message object of type '<velocity-request>"
  "4a43c3133b1d7fcbde17a0d788417bc1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'velocity-request)))
  "Returns md5sum for a message object of type 'velocity-request"
  "4a43c3133b1d7fcbde17a0d788417bc1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<velocity-request>)))
  "Returns full string definition for message of type '<velocity-request>"
  (cl:format cl:nil "int32 sec_int~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'velocity-request)))
  "Returns full string definition for message of type 'velocity-request"
  (cl:format cl:nil "int32 sec_int~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <velocity-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <velocity-request>))
  "Converts a ROS message object to a list"
  (cl:list 'velocity-request
    (cl:cons ':sec_int (sec_int msg))
))
;//! \htmlinclude velocity-response.msg.html

(cl:defclass <velocity-response> (roslisp-msg-protocol:ros-message)
  ((msg
    :reader msg
    :initarg :msg
    :type cl:string
    :initform ""))
)

(cl:defclass velocity-response (<velocity-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <velocity-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'velocity-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mobile_manipulator_body-srv:<velocity-response> is deprecated: use mobile_manipulator_body-srv:velocity-response instead.")))

(cl:ensure-generic-function 'msg-val :lambda-list '(m))
(cl:defmethod msg-val ((m <velocity-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mobile_manipulator_body-srv:msg-val is deprecated.  Use mobile_manipulator_body-srv:msg instead.")
  (msg m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <velocity-response>) ostream)
  "Serializes a message object of type '<velocity-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'msg))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'msg))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <velocity-response>) istream)
  "Deserializes a message object of type '<velocity-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'msg) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'msg) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<velocity-response>)))
  "Returns string type for a service object of type '<velocity-response>"
  "mobile_manipulator_body/velocityResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'velocity-response)))
  "Returns string type for a service object of type 'velocity-response"
  "mobile_manipulator_body/velocityResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<velocity-response>)))
  "Returns md5sum for a message object of type '<velocity-response>"
  "4a43c3133b1d7fcbde17a0d788417bc1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'velocity-response)))
  "Returns md5sum for a message object of type 'velocity-response"
  "4a43c3133b1d7fcbde17a0d788417bc1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<velocity-response>)))
  "Returns full string definition for message of type '<velocity-response>"
  (cl:format cl:nil "string msg~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'velocity-response)))
  "Returns full string definition for message of type 'velocity-response"
  (cl:format cl:nil "string msg~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <velocity-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'msg))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <velocity-response>))
  "Converts a ROS message object to a list"
  (cl:list 'velocity-response
    (cl:cons ':msg (msg msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'velocity)))
  'velocity-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'velocity)))
  'velocity-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'velocity)))
  "Returns string type for a service object of type '<velocity>"
  "mobile_manipulator_body/velocity")