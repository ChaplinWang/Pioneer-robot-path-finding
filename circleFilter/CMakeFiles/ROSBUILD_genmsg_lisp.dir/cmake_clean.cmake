FILE(REMOVE_RECURSE
  "src/circleFilter/msg"
  "src/circleFilter/srv"
  "msg_gen"
  "srv_gen"
  "msg_gen"
  "srv_gen"
  "CMakeFiles/ROSBUILD_genmsg_lisp"
  "msg_gen/lisp/coordinate.lisp"
  "msg_gen/lisp/_package.lisp"
  "msg_gen/lisp/_package_coordinate.lisp"
  "msg_gen/lisp/moveNotify.lisp"
  "msg_gen/lisp/_package.lisp"
  "msg_gen/lisp/_package_moveNotify.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
