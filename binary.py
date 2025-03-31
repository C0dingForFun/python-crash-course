# Working with binary files
# Install Hex Editor extension
# Right click and click 'open with'

# Imports
import random; # creates random numbers
import operator; # compares two lists

#  Create  random bytes
def randomBytes(size):
    bytes = []
    for x in range(size):
        bytes.append(random.randrange(0, 255))
    return bytes

# Displays the bytes
def displayBytes(bytes):
    print("-"*20)
    for index, item in enumerate(bytes, start=1):
        print(f'{index} = {item} ({hex(item)})')
    print("-"*20)

# Write bytes
def writeBytes(filename, bytes):
    with open(filename, 'wb') as file:
        for i in bytes:
            file.write(i.to_bytes(1, byteorder= 'big'))

#  Read bytes
def readBytes(filename):
    bytes = []
    with open(filename, 'rb') as file:
        while True:
            b = file.read(1)
            if not b:
                break
            bytes.append(int.from_bytes(b, byteorder= 'big'))
    return bytes
        
# See it in action 

# Create the random bytes
outBytes = randomBytes(12)
displayBytes(outBytes)

# Write bytes
filename = 'test.txt'
writeBytes(filename, outBytes)

# Read bytes
inBytes = readBytes(filename)
displayBytes(inBytes)
print(f'Math: {operator.eq(outBytes, inBytes)}')