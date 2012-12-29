FILE(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "../src/eddiebot_node/msg"
  "../src/eddiebot_node/srv"
  "CMakeFiles/ROSBUILD_gencfg_cpp"
  "../cfg/cpp/eddiebot_node/EddieBotConfig.h"
  "../docs/EddieBotConfig.dox"
  "../docs/EddieBotConfig-usage.dox"
  "../src/eddiebot_node/cfg/EddieBotConfig.py"
  "../docs/EddieBotConfig.wikidoc"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gencfg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
