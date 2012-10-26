
(cl:in-package :asdf)

(defsystem "circleFilter-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "stateChange" :depends-on ("_package_stateChange"))
    (:file "_package_stateChange" :depends-on ("_package"))
  ))