import smbus
import time
#testtsettest
# Get I2C bus
bus = smbus.SMBus(1)

# ISL29125 address, 0x44(68)
address = 0x44
# Select configuation-1register, 0x01(01)
# 0x0D(13) Operation: RGB, Range: 360 lux, Res: 16 Bits
bus.write_byte_data(0x44, 0x01, 0x05)

time.sleep(1)

print("Reading colour values and displaying them in a new window\n")

def getAndUpdateColour():
    while True:
        data = bus.read_i2c_block_data(0x44,0x09, 6)  
        green = int((data[1] * 256 + data[0])/256)
        red = int((data[3] * 256 + data[2])/256)
        blue = int((data[5] * 256 + data[4])/256)
        print([red,green,blue])
        print("")
        time.sleep(2) 

getAndUpdateColour()