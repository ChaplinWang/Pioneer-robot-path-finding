FILE(REMOVE_RECURSE
  "../src/circleFinder/msg"
  "../msg_gen"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_lisp"
  "../msg_gen/lisp/circleEntry.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_circleEntry.lisp"
  "../msg_gen/lisp/coordinate.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_coordinate.lisp"
  "../msg_gen/lisp/circleArray.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_circleArray.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
