FILE(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "../src/eddiebot_node/msg"
  "../src/eddiebot_node/srv"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/eddiebot_node/msg/__init__.py"
  "../src/eddiebot_node/msg/_EddieSensorState.py"
  "../src/eddiebot_node/msg/_Drive.py"
  "../src/eddiebot_node/msg/_LaptopChargeStatus.py"
  "../src/eddiebot_node/msg/_BatteryState.py"
  "../src/eddiebot_node/msg/_Eddie.py"
  "../src/eddiebot_node/msg/_EddiebotSensorState.py"
  "../src/eddiebot_node/msg/_RawEddiebotSensorState.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
