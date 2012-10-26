
(cl:in-package :asdf)

(defsystem "circleFilter-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "coordinate" :depends-on ("_package_coordinate"))
    (:file "_package_coordinate" :depends-on ("_package"))
    (:file "moveNotify" :depends-on ("_package_moveNotify"))
    (:file "_package_moveNotify" :depends-on ("_package"))
  ))