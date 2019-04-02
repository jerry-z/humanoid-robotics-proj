;; Auto-generated. Do not edit!


(when (boundp 'perception_msgs::ObjectFeatures)
  (if (not (find-package "PERCEPTION_MSGS"))
    (make-package "PERCEPTION_MSGS"))
  (shadow 'ObjectFeatures (find-package "PERCEPTION_MSGS")))
(unless (find-package "PERCEPTION_MSGS::OBJECTFEATURES")
  (make-package "PERCEPTION_MSGS::OBJECTFEATURES"))

(in-package "ROS")
;;//! \htmlinclude ObjectFeatures.msg.html


(defclass perception_msgs::ObjectFeatures
  :super ros::object
  :slots (_object_name _names _values ))

(defmethod perception_msgs::ObjectFeatures
  (:init
   (&key
    ((:object_name __object_name) "")
    ((:names __names) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:values __values) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _object_name (string __object_name))
   (setq _names __names)
   (setq _values __values)
   self)
  (:object_name
   (&optional __object_name)
   (if __object_name (setq _object_name __object_name)) _object_name)
  (:names
   (&optional __names)
   (if __names (setq _names __names)) _names)
  (:values
   (&optional __values)
   (if __values (setq _values __values)) _values)
  (:serialization-length
   ()
   (+
    ;; string _object_name
    4 (length _object_name)
    ;; string[] _names
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _names)) 4
    ;; float64[] _values
    (* 8    (length _values)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _object_name
       (write-long (length _object_name) s) (princ _object_name s)
     ;; string[] _names
     (write-long (length _names) s)
     (dolist (elem _names)
       (write-long (length elem) s) (princ elem s)
       )
     ;; float64[] _values
     (write-long (length _values) s)
     (dotimes (i (length _values))
       (sys::poke (elt _values i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _object_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _object_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string[] _names
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _names (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _names i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; float64[] _values
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _values (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _values i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(setf (get perception_msgs::ObjectFeatures :md5sum-) "fe6a1b3ba02e62219365f96560d5f759")
(setf (get perception_msgs::ObjectFeatures :datatype-) "perception_msgs/ObjectFeatures")
(setf (get perception_msgs::ObjectFeatures :definition-)
      "string object_name
string[] names
float64[] values

")



(provide :perception_msgs/ObjectFeatures "fe6a1b3ba02e62219365f96560d5f759")


