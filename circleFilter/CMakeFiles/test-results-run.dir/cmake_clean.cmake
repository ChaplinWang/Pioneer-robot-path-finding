FILE(REMOVE_RECURSE
  "src/circleFilter/msg"
  "src/circleFilter/srv"
  "msg_gen"
  "srv_gen"
  "msg_gen"
  "srv_gen"
  "CMakeFiles/test-results-run"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/test-results-run.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
