import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np
import os

os.remove("finalcompressed_1.txt")
#     if c in freq:
#         freq[c] += 1
#     else:
#         freq[c] = 1

# freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# if DEBUG:
#     print(' Char | Freq ')
#     for (key, c) in freq:
#         print(' %4r | %d' % (key, c))

# nodes = freq

# while len(nodes) > 1:
#     (key1, c1) = nodes[-1]
#     (key2, c2) = nodes[-2]
#     nodes = nodes[:-2]
#     node = NodeTree(key1, key2)
#     nodes.append((node, c1 + c2))

#     nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

# if DEBUG:
#     print('left: %s' % nodes[0][0].nodes()[0])
#     print('right: %s' % nodes[0][0].nodes()[1])

# huffmanCode = huffmanCodeTree(nodes[0][0])

# print(' Char | Huffman code ')
# print('----------------------')
# for (char, frequency) in freq:
#     print(' %-4r |%12s' % (char, huffmanCode[char]))
