sampleRate = 44100.0 # hertz
duration = 1.0 # seconds
frequency = 440.0 # hertz
obj = wave.open('sample2.wav','w')
obj.setnchannels(1) # mono
obj.setsampwidth(2)
obj.setframerate(sampleRate)
for i in range(0 ,len(amp_list)):
   data = struct.pack('<H', amp_list[i])
   obj.writeframesraw( data )
obj.close()