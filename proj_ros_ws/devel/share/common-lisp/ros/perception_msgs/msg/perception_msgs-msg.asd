
(cl:in-package :asdf)

(defsystem "perception_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ObjectFeatures" :depends-on ("_package_ObjectFeatures"))
    (:file "_package_ObjectFeatures" :depends-on ("_package"))
  ))