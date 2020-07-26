import wave,struct
obj = wave.open("sample.wav")
print(obj.getnchannels(), obj.getsampwidth(),obj.getframerate(), obj.getnframes(), obj.getparams())
print(1306624/44100)
data = obj.readframes(obj.getnframes())
amp_list = []
for i in data:
    amp_list.append(int(i))
print([x for x in data[:10]])
print(amp_list[:10])
obj.close()



sampleRate = 44100.0 # hertz
duration = 1.0 # seconds
frequency = 440.0 # hertz
obj = wave.open('sample1.wav','w')
obj.setnchannels(1) # mono
obj.setsampwidth(2)
obj.setframerate(sampleRate)
for i in range(0 ,len(amp_list),4):
   value = amp_list[i]
   data = struct.pack('B', value)
   obj.writeframesraw( data )
   value = amp_list[i+1] 
   data = struct.pack('B', value)
   obj.writeframesraw( data )
obj.close()


obj = wave.open("sample1.wav")
data = obj.readframes(obj.getnframes())
print([x for x in data[:10]])
