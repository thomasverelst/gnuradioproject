INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_PACKETIZR packetizr)

FIND_PATH(
    PACKETIZR_INCLUDE_DIRS
    NAMES packetizr/api.h
    HINTS $ENV{PACKETIZR_DIR}/include
        ${PC_PACKETIZR_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    PACKETIZR_LIBRARIES
    NAMES gnuradio-packetizr
    HINTS $ENV{PACKETIZR_DIR}/lib
        ${PC_PACKETIZR_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(PACKETIZR DEFAULT_MSG PACKETIZR_LIBRARIES PACKETIZR_INCLUDE_DIRS)
MARK_AS_ADVANCED(PACKETIZR_LIBRARIES PACKETIZR_INCLUDE_DIRS)

