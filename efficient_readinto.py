import time
import os
from array import array
from random import random

FILENAME = 'floats.bin'
if not os.path.exists(FILENAME):
    print('create file:', FILENAME)
    with open(FILENAME, 'wb') as f:
        floats = array('d', (random() for i in range(10 ** 7)))
        floats.tofile(f)
        print(floats[0])

# Snippet #1
with open(FILENAME, 'rb') as f:
    data = f.read()
    # data[0] = 97

# Snippet #2
with open(FILENAME, 'rb') as f:
    start = time.time()
    data = bytearray(f.read())
    data[0] = 97 # OK!
    print('#2:', time.time() - start)

with open(FILENAME, 'rb') as f:
    start = time.time()
    data = bytearray(os.path.getsize(FILENAME))
    f.readinto(data)
    print('#3:', time.time() - start)

# use memoryview to cast floats
mv_data = memoryview(data)
print('len:', len(mv_data))
floats = mv_data.cast('d')
print('len:', len(floats))
print(floats[0])