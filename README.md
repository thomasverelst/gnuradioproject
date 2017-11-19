# GNU Radio Packetized transmissions

This repository contains my semester project of spring 2017, using GNU Radio 3.7.10.
A more flexible packet encoder and decoder block are implemented. 
The packet encoder encapsulates the incoming stream into packets, consisting of a preamble, header (containing packet length), 
payload and checksum. Soft-input error correction is also supported.

Also, better support for modulating the preamble with BPSK is be added,
since this is difficult with the current available blocks in the GNU Radio
framework. The synchronization can be modulated with BPSK, while a higher-
order modulation is used for other packet data to improve data throughput in
good channel conditions.

Some custom blocks were built, which can be useful for other cases. (see below)

# Custom blocks 
## Packet encoder and decoder
### Packet encoder features:
* Supports GNU Radio’s constellation objects in order to support a wide range of PSK and
QAM mappings. Optional support for differential encoding.
* Possibility to use distinct constellation types for preamble, header and payload.
* GNU Radio’s header formatter objects in order to support headers with custom
lengths and fields.
* The start of the payload data for a packet is indicated in the incoming byte stream
with a tag that has the payload length as tag value.
* Optional support for data whitening, as discussed in section 4.4 of the report0

### Packet decoder features:
* Decoding of packets that are encoded with the Extended Packet Encoder block
* Support for both hard and soft outputs, in order to support forward error correction
* Support for differential decoding, when hard-decision decoding is used

## Other blocks
### Tagged stream fix:
A tagged stream with more samples between tags than what the packet_len tag indicates
gives problems in GNU Radio’s tagged stream blocks, such as the Extended Tagged FEC
Decoder. These blocks expect that the packets are perfectly sequential, i.e. there are no
extra samples between packets. This new helper block ’truncates’ a tagged data stream. It only keeps the samples belonging to a packet, and removes the other
samples.

### Correlation Estimator
The correlation estimator blocks in GNU Radio 3.7.10 are not working, buggy or do not have enough functionality. This improved
Correlation Estimator implementation tries to solve most of these problems. See report for more details on the
problems of the blocks and the fixes made.

### Data whitening
Blocks that withen/dewhiten tagged streams





# Test systems and implementation examples
There are a lot of exampels (.grc) files on packetization, FEC, whitening and correlation estimation in this repo. 
See report for more detailed information

## Basic test examples (testing individual features)

### test_mapping:

tests mapping and constellation decoder for hard and soft decoding. Also demonstrates differential encoding/decoding.

### test_soft decoder:
tests soft constellation decoding

### test_fec:
tests FEC with soft and hard decoding

### test_tagged_stream_fix
tests the Tagged Stream Fixer block, which removes "unnecessary" padding samples in tagged streams, to make them compatible with tagged_stream blocks in GNU Radio

Tagged Stream Fix description: Fixes a stream where the packet length does not correspond to the number of samples.  For example, if we have a stream with a packet length tag with value 50, and between each tag there are 52 samples,
the block will remove the last 2 samples from the output stream to make a stream with packet length tag of 50 and 50 samples between each tag.


### test_time_phase_sync
The symbols are shaped with a root raised cosine filter. A channel model is added to simulate
a time offset, frequency offset, phase offset and noise in the signal. Time and phase
synchronization is added with the Polyphase Clock Sync block and Costas Loop. A BER
output is also provided to analyze the effects.

### test_whitener
illustrates the use of the Tagged Stream Whitener blocks

## Packet encoder/decoder test examples

### encdec_basic
Implementes a basic packet encoder/decoder using separate GNU Radio blocks (for debugging)

### encdec_basic_differential
Same as above but now with differential encoding/decoding

### encdec_custom
Implements Extended Packet Encoder/Extended Packet Decoder blocks

### encdec_custom_fec
Same as above but in combination with FEC encoding/decoding blocks



## Communication chain examples
### chain_cusomt
Communication chain using the Extended Packet Encoder/Decoder blocks

### chain_rx_debug 
Same as above but the packet decoder is made of individual blocks (for debugging purposes)

### chain_rx_debug_differential
Same as above but for differential decoding


