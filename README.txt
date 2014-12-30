dvtext
======

Codec2 digital voice over text UI frames
This is an even uglier hack than dvopus, but it can actually be made to mostly work.

The encoder reads multiple codec2 frames and base64 encodes them into a single packet.

To test, start the TNCs in terminal mode and
make sure their on-air baud rates are set to 9600.
The transmitting TNC should be in CONVERS mode.

[raw input] | /path/to/c2enc 1300 - - | ./encoder.py /dev/ttyUSB0

./decoder.py < /dev/ttyUSB0 | /path/to/c2dec 1300 - - | [raw output]

Raw input and output are 8000Hz 16-bit 1-channel. This can be a file or pipelined from
another tool such as parec/pacat or arecord/aplay.

Initial tests done with a TH-D7 transmitting to a TH-D700 receiver.
Input was a file rather than real time recording.
The transmitter would burst a few frames, shut down, and start all over again.
I think the only reason I got stable audio was the massive amount of buffering
in the pipeline.
