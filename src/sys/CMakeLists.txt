cmake_minimum_required(VERSION 3.10)
project(nitpick_nparse_sys C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

add_library(nitpick_nparse_sys SHARED libnparse.c)
