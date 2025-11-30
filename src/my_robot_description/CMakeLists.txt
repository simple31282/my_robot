cmake_minimum_required(VERSION 3.8)
project(my_robot_description)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)

# Install resource directories (URDFs, meshes, RViz configs, launch files)
install(
  DIRECTORY urdf meshes rviz launch
  DESTINATION share/${PROJECT_NAME}/
)
# (Optional) Install package.xml for clarity in workspace
install(FILES package.xml DESTINATION share/${PROJECT_NAME})

ament_package()