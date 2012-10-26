FILE(REMOVE_RECURSE
  "../src/circleFinder/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/circleFinder/msg/__init__.py"
  "../src/circleFinder/msg/_circleEntry.py"
  "../src/circleFinder/msg/_coordinate.py"
  "../src/circleFinder/msg/_circleArray.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
