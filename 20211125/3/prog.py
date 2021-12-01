import struct
import sys
fmt = "4sI4s4s4xHHI6xH4sI"

expect_size = struct.calcsize(fmt)

raw = sys.stdin.buffer.read(expect_size)
if len(raw) < expect_size:
    print('NO')
    quit()

(mrk_1, Size, mrk_2, mrk_3, Type, Channels, Rate, Bits, mrk_4, Data_size) = struct.unpack(fmt, raw)

if (mrk_1, mrk_2, mrk_3, mrk_4) != (b'RIFF', b'WAVE', b'fmt ', b'data'):
    print("NO")
else:
    print(f"{Size=}, {Type=}, {Channels=}, {Rate=}, {Bits=}, Data size={Data_size}")

