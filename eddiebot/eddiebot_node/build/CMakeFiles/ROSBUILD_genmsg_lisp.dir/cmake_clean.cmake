FILE(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "../src/eddiebot_node/msg"
  "../src/eddiebot_node/srv"
  "CMakeFiles/ROSBUILD_genmsg_lisp"
  "../msg_gen/lisp/EddieSensorState.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_EddieSensorState.lisp"
  "../msg_gen/lisp/Drive.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_Drive.lisp"
  "../msg_gen/lisp/LaptopChargeStatus.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_LaptopChargeStatus.lisp"
  "../msg_gen/lisp/BatteryState.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_BatteryState.lisp"
  "../msg_gen/lisp/Eddie.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_Eddie.lisp"
  "../msg_gen/lisp/EddiebotSensorState.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_EddiebotSensorState.lisp"
  "../msg_gen/lisp/RawEddiebotSensorState.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_RawEddiebotSensorState.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
