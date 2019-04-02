;; Auto-generated. Do not edit!


(when (boundp 'map_annotator::UserAction)
  (if (not (find-package "MAP_ANNOTATOR"))
    (make-package "MAP_ANNOTATOR"))
  (shadow 'UserAction (find-package "MAP_ANNOTATOR")))
(unless (find-package "MAP_ANNOTATOR::USERACTION")
  (make-package "MAP_ANNOTATOR::USERACTION"))

(in-package "ROS")
;;//! \htmlinclude UserAction.msg.html


(intern "*CREATE*" (find-package "MAP_ANNOTATOR::USERACTION"))
(shadow '*CREATE* (find-package "MAP_ANNOTATOR::USERACTION"))
(defconstant map_annotator::UserAction::*CREATE* "create")
(intern "*DELETE*" (find-package "MAP_ANNOTATOR::USERACTION"))
(shadow '*DELETE* (find-package "MAP_ANNOTATOR::USERACTION"))
(defconstant map_annotator::UserAction::*DELETE* "delete")
(intern "*GOTO*" (find-package "MAP_ANNOTATOR::USERACTION"))
(shadow '*GOTO* (find-package "MAP_ANNOTATOR::USERACTION"))
(defconstant map_annotator::UserAction::*GOTO* "goto")
(intern "*RENAME*" (find-package "MAP_ANNOTATOR::USERACTION"))
(shadow '*RENAME* (find-package "MAP_ANNOTATOR::USERACTION"))
(defconstant map_annotator::UserAction::*RENAME* "rename")
(defclass map_annotator::UserAction
  :super ros::object
  :slots (_command _name _updated_name ))

(defmethod map_annotator::UserAction
  (:init
   (&key
    ((:command __command) "")
    ((:name __name) "")
    ((:updated_name __updated_name) "")
    )
   (send-super :init)
   (setq _command (string __command))
   (setq _name (string __name))
   (setq _updated_name (string __updated_name))
   self)
  (:command
   (&optional __command)
   (if __command (setq _command __command)) _command)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:updated_name
   (&optional __updated_name)
   (if __updated_name (setq _updated_name __updated_name)) _updated_name)
  (:serialization-length
   ()
   (+
    ;; string _command
    4 (length _command)
    ;; string _name
    4 (length _name)
    ;; string _updated_name
    4 (length _updated_name)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _command
       (write-long (length _command) s) (princ _command s)
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; string _updated_name
       (write-long (length _updated_name) s) (princ _updated_name s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _command
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _command (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _updated_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _updated_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get map_annotator::UserAction :md5sum-) "02b53ace3ff4f0b2c6988ccd36fc2910")
(setf (get map_annotator::UserAction :datatype-) "map_annotator/UserAction")
(setf (get map_annotator::UserAction :definition-)
      "string CREATE=create
string DELETE=delete
string GOTO=goto
string RENAME=rename
string command
string name # The name of the pose the command applies to
string updated_name # If command is RENAME, this is the new name of the pose

")



(provide :map_annotator/UserAction "02b53ace3ff4f0b2c6988ccd36fc2910")


