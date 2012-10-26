
(cl:in-package :asdf)

(defsystem "circleFinder-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "circleEntry" :depends-on ("_package_circleEntry"))
    (:file "_package_circleEntry" :depends-on ("_package"))
    (:file "coordinate" :depends-on ("_package_coordinate"))
    (:file "_package_coordinate" :depends-on ("_package"))
    (:file "circleArray" :depends-on ("_package_circleArray"))
    (:file "_package_circleArray" :depends-on ("_package"))
  ))