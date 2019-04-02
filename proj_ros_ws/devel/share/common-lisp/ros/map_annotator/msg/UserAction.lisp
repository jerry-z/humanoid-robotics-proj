; Auto-generated. Do not edit!


(cl:in-package map_annotator-msg)


;//! \htmlinclude UserAction.msg.html

(cl:defclass <UserAction> (roslisp-msg-protocol:ros-message)
  ((command
    :reader command
    :initarg :command
    :type cl:string
    :initform "")
   (name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (updated_name
    :reader updated_name
    :initarg :updated_name
    :type cl:string
    :initform ""))
)

(cl:defclass UserAction (<UserAction>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <UserAction>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'UserAction)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name map_annotator-msg:<UserAction> is deprecated: use map_annotator-msg:UserAction instead.")))

(cl:ensure-generic-function 'command-val :lambda-list '(m))
(cl:defmethod command-val ((m <UserAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader map_annotator-msg:command-val is deprecated.  Use map_annotator-msg:command instead.")
  (command m))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <UserAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader map_annotator-msg:name-val is deprecated.  Use map_annotator-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'updated_name-val :lambda-list '(m))
(cl:defmethod updated_name-val ((m <UserAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader map_annotator-msg:updated_name-val is deprecated.  Use map_annotator-msg:updated_name instead.")
  (updated_name m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<UserAction>)))
    "Constants for message type '<UserAction>"
  '((:CREATE . create)
    (:DELETE . delete)
    (:GOTO . goto)
    (:RENAME . rename))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'UserAction)))
    "Constants for message type 'UserAction"
  '((:CREATE . create)
    (:DELETE . delete)
    (:GOTO . goto)
    (:RENAME . rename))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <UserAction>) ostream)
  "Serializes a message object of type '<UserAction>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'command))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'command))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'updated_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'updated_name))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <UserAction>) istream)
  "Deserializes a message object of type '<UserAction>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'command) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'command) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'updated_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'updated_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<UserAction>)))
  "Returns string type for a message object of type '<UserAction>"
  "map_annotator/UserAction")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'UserAction)))
  "Returns string type for a message object of type 'UserAction"
  "map_annotator/UserAction")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<UserAction>)))
  "Returns md5sum for a message object of type '<UserAction>"
  "02b53ace3ff4f0b2c6988ccd36fc2910")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'UserAction)))
  "Returns md5sum for a message object of type 'UserAction"
  "02b53ace3ff4f0b2c6988ccd36fc2910")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<UserAction>)))
  "Returns full string definition for message of type '<UserAction>"
  (cl:format cl:nil "string CREATE=create~%string DELETE=delete~%string GOTO=goto~%string RENAME=rename~%string command~%string name # The name of the pose the command applies to~%string updated_name # If command is RENAME, this is the new name of the pose~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'UserAction)))
  "Returns full string definition for message of type 'UserAction"
  (cl:format cl:nil "string CREATE=create~%string DELETE=delete~%string GOTO=goto~%string RENAME=rename~%string command~%string name # The name of the pose the command applies to~%string updated_name # If command is RENAME, this is the new name of the pose~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <UserAction>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'command))
     4 (cl:length (cl:slot-value msg 'name))
     4 (cl:length (cl:slot-value msg 'updated_name))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <UserAction>))
  "Converts a ROS message object to a list"
  (cl:list 'UserAction
    (cl:cons ':command (command msg))
    (cl:cons ':name (name msg))
    (cl:cons ':updated_name (updated_name msg))
))
