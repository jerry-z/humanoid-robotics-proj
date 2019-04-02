
(cl:in-package :asdf)

(defsystem "map_annotator-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "PoseNames" :depends-on ("_package_PoseNames"))
    (:file "_package_PoseNames" :depends-on ("_package"))
    (:file "UserAction" :depends-on ("_package_UserAction"))
    (:file "_package_UserAction" :depends-on ("_package"))
  ))