;; Auto-generated. Do not edit!


(when (boundp 'map_annotator::PoseNames)
  (if (not (find-package "MAP_ANNOTATOR"))
    (make-package "MAP_ANNOTATOR"))
  (shadow 'PoseNames (find-package "MAP_ANNOTATOR")))
(unless (find-package "MAP_ANNOTATOR::POSENAMES")
  (make-package "MAP_ANNOTATOR::POSENAMES"))

(in-package "ROS")
;;//! \htmlinclude PoseNames.msg.html


(defclass map_annotator::PoseNames
  :super ros::object
  :slots (_names ))

(defmethod map_annotator::PoseNames
  (:init
   (&key
    ((:names __names) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _names __names)
   self)
  (:names
   (&optional __names)
   (if __names (setq _names __names)) _names)
  (:serialization-length
   ()
   (+
    ;; string[] _names
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _names)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string[] _names
     (write-long (length _names) s)
     (dolist (elem _names)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string[] _names
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _names (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _names i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(setf (get map_annotator::PoseNames :md5sum-) "dc7ae3609524b18034e49294a4ce670e")
(setf (get map_annotator::PoseNames :datatype-) "map_annotator/PoseNames")
(setf (get map_annotator::PoseNames :definition-)
      "string[] names

")



(provide :map_annotator/PoseNames "dc7ae3609524b18034e49294a4ce670e")


