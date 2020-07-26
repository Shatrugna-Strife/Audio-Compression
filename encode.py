import wave
import struct
import huff
import os


class encode_audio:
    
    def __init__(self,path):
        self.obj = wave.open(path)

        print(self.obj.getnchannels(), self.obj.getsampwidth(),self.obj.getframerate(), self.obj.getnframes(), self.obj.getparams())

        self.data = self.obj.readframes(self.obj.getnframes())

        if self.obj.getnchannels() == 1:
            self.has_2_channels = False
            
            print("Sound has only 1 channel.")

            self.amp_list_1 = []

            for i in range(0,len(self.data),2):
                self.amp_list_1.append(int.from_bytes(self.data[i:i+2],byteorder="little",signed=False))
        else:
            self.has_2_channels = True

            print("Sound has 2 channels for stereo, so 2 files will be created.")

            self.amp_list_1 = []

            self.amp_list_2 = []

            for i in range(0,len(self.data),4):
                self.amp_list_1.append(int.from_bytes(self.data[i:i+2],byteorder="little",signed=False))
                self.amp_list_2.append(int.from_bytes(self.data[i+2:i+4],byteorder="little",signed=False))

        self.obj.close()

        
    def diff_encoding(self):

        self.diff_list_1 = [self.amp_list_1[0]]

        for i in range(1,len(self.amp_list_1)):
            if self.amp_list_1[i]-self.amp_list_1[i-1] > 127 or self.amp_list_1[i]-self.amp_list_1[i-1] < -127:
                self.diff_list_1.append(self.amp_list_1[i])
            else:
                self.diff_list_1.append(self.amp_list_1[i]-self.amp_list_1[i-1])
        
        if self.has_2_channels:
            self.diff_list_2 = [self.amp_list_2[0]]

            for i in range(1,len(self.amp_list_2)):
                if self.amp_list_2[i]-self.amp_list_2[i-1] > 127 or self.amp_list_2[i]-self.amp_list_2[i-1] < -127:
                    self.diff_list_2.append(self.amp_list_2[i])
                else:
                    self.diff_list_2.append(self.amp_list_2[i]-self.amp_list_2[i-1])

    def write_intermediate_code(self,path):
        filename, file_extension = os.path.splitext(path)
        
        self.inter_path_name = filename

        self.inter_path_extension = file_extension

        self.encoded_bytes_1 = bytearray()

        for i in range(len(self.diff_list_1)):
            if self.diff_list_1[i] > 127 or self.diff_list_1[i]< -127:
                self.encoded_bytes_1+= bytearray(struct.pack('<H', self.diff_list_1[i]))
            else:
                self.encoded_bytes_1+= bytearray(struct.pack("b", self.diff_list_1[i]))
        
        self.encoded_bytes_1 = bytes(self.encoded_bytes_1)

        f = open(self.inter_path_name+ "_compressed" +"_1" + self.inter_path_extension, "wb")
        f.write(self.encoded_bytes_1)
        f.close()

        if self.has_2_channels:
            self.encoded_bytes_2 = bytearray()

            for i in range(len(self.diff_list_2)):
                if self.diff_list_2[i] > 127 or self.diff_list_2[i]< -127:
                    self.encoded_bytes_2+= bytearray(struct.pack('<H', self.diff_list_2[i]))
                else:
                    self.encoded_bytes_2+= bytearray(struct.pack("b", self.diff_list_2[i]))
            
            self.encoded_bytes_2 = bytes(self.encoded_bytes_2)

            f = open(self.inter_path_name+ "_compressed" +"_2" + self.inter_path_extension, "wb")
            f.write(self.encoded_bytes_2)
            f.close()

    def compression(self):
        encode_1 = huff.huff_man(self.inter_path_name+ "_compressed" + "_1" + self.inter_path_extension)

        encode_1.compress()

        if self.has_2_channels:
            encode_2 = huff.huff_man(self.inter_path_name+ "_compressed" +"_2" + self.inter_path_extension)
            encode_2.compress()

        print("Huffman Compression is done.")


if __name__ == "__main__":
    test = encode_audio("sample.wav")
    test.diff_encoding()
    test.write_intermediate_code("final.txt")
    test.compression()