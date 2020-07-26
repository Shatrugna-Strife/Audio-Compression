import wave
import struct
import heapq
import os
import huff
from functools import total_ordering

obj = wave.open("sample.wav")
print(obj.getnchannels(), obj.getsampwidth(),obj.getframerate(), obj.getnframes(), obj.getparams())
data = obj.readframes(obj.getnframes())
print(len(data))
amp_list = []
for i in range(0,len(data),2):
    # amp_list.append(struct.unpack('>BB', data[i:i+2]))
    amp_list.append(int.from_bytes(data[i:i+2],byteorder="little",signed=False))
print([x for x in data[:10]])
print(amp_list[:10])
obj.close()

f = open("test.txt", "wb")
f.write(data)
f.close()

encode = huff.HuffmanCoding("test.txt")
encode.compress()
# encode.decompress("test.bin")

# f = open("test_decompressed.txt", "rb")
# data = f.read()
# f.close()
