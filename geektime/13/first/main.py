from utils import get_sum
from class_utils import *
print(get_sum(1,3))

encoder = Encoder()
decoder = Decoder()

print(encoder.encode('abcde'))

print(encoder.encode('edcba'))