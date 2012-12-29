
(cl:in-package :asdf)

(defsystem "eddiebot_node-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "EddieSensorState" :depends-on ("_package_EddieSensorState"))
    (:file "_package_EddieSensorState" :depends-on ("_package"))
    (:file "Drive" :depends-on ("_package_Drive"))
    (:file "_package_Drive" :depends-on ("_package"))
    (:file "LaptopChargeStatus" :depends-on ("_package_LaptopChargeStatus"))
    (:file "_package_LaptopChargeStatus" :depends-on ("_package"))
    (:file "BatteryState" :depends-on ("_package_BatteryState"))
    (:file "_package_BatteryState" :depends-on ("_package"))
    (:file "Eddie" :depends-on ("_package_Eddie"))
    (:file "_package_Eddie" :depends-on ("_package"))
    (:file "EddiebotSensorState" :depends-on ("_package_EddiebotSensorState"))
    (:file "_package_EddiebotSensorState" :depends-on ("_package"))
    (:file "RawEddiebotSensorState" :depends-on ("_package_RawEddiebotSensorState"))
    (:file "_package_RawEddiebotSensorState" :depends-on ("_package"))
  ))