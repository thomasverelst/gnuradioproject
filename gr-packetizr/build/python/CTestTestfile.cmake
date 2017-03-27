# CMake generated Testfile for 
# Source directory: /home/thomas/gr/gr-packetizr/python
# Build directory: /home/thomas/gr/gr-packetizr/build/python
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(qa_packet_encoder "/bin/sh" "/home/thomas/gr/gr-packetizr/build/python/qa_packet_encoder_test.sh")
add_test(qa_packet_decoder "/bin/sh" "/home/thomas/gr/gr-packetizr/build/python/qa_packet_decoder_test.sh")
