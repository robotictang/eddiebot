FILE(REMOVE_RECURSE
  "CMakeFiles/ROSBUILD_gencfg_cpp"
  "../cfg/cpp/pointcloud_to_laserscan/CloudScanConfig.h"
  "../docs/CloudScanConfig.dox"
  "../docs/CloudScanConfig-usage.dox"
  "../src/pointcloud_to_laserscan/cfg/CloudScanConfig.py"
  "../docs/CloudScanConfig.wikidoc"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gencfg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
