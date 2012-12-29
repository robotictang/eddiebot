FILE(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "../src/eddiebot_node/msg"
  "../src/eddiebot_node/srv"
  "CMakeFiles/ROSBUILD_genmsg_cpp"
  "../msg_gen/cpp/include/eddiebot_node/EddieSensorState.h"
  "../msg_gen/cpp/include/eddiebot_node/Drive.h"
  "../msg_gen/cpp/include/eddiebot_node/LaptopChargeStatus.h"
  "../msg_gen/cpp/include/eddiebot_node/BatteryState.h"
  "../msg_gen/cpp/include/eddiebot_node/Eddie.h"
  "../msg_gen/cpp/include/eddiebot_node/EddiebotSensorState.h"
  "../msg_gen/cpp/include/eddiebot_node/RawEddiebotSensorState.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
