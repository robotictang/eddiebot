
(cl:in-package :asdf)

(defsystem "eddiebot_node-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "SetEddiebotMode" :depends-on ("_package_SetEddiebotMode"))
    (:file "_package_SetEddiebotMode" :depends-on ("_package"))
    (:file "SetDigitalOutputs" :depends-on ("_package_SetDigitalOutputs"))
    (:file "_package_SetDigitalOutputs" :depends-on ("_package"))
  ))