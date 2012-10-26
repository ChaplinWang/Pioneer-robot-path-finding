FILE(REMOVE_RECURSE
  "../src/circleFinder/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_cpp"
  "../msg_gen/cpp/include/circleFinder/circleEntry.h"
  "../msg_gen/cpp/include/circleFinder/coordinate.h"
  "../msg_gen/cpp/include/circleFinder/circleArray.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
