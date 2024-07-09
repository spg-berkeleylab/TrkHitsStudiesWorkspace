CMAKE_MINIMUM_REQUIRED(VERSION 3.15 FATAL_ERROR)

PROJECT(TrackPerfWorkspace)

#
# Find and add all packages
FILE(GLOB packages RELATIVE ${CMAKE_CURRENT_LIST_DIR} packages/*)
FOREACH(package ${packages})
  IF(IS_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/${package})
    MESSAGE("Add package ${package}")
    ADD_SUBDIRECTORY(${package})
  ENDIF()
ENDFOREACH()

# Data
# ADD_SUBDIRECTORY(data)
