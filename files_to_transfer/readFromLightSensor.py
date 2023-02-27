import smbus
import time

class color_sensor():
    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.address = 0x44
        self.bus.write_byte_data(self.address, 0x01, 0x05)

    def getAndUpdateColour(self):
        data = self.bus.read_i2c_block_data(self.address,0x09, 6)  
        green = int((data[1] * 256 + data[0])/256)
        red = int((data[3] * 256 + data[2])/256)
        blue = int((data[5] * 256 + data[4])/256)
        return (red,green,blue)
    

#testtsettest
# Get I2C bus


# ISL29125 address, 0x44(68)

# Select configuation-1register, 0x01(01)
# 0x0D(13) Operation: RGB, Range: 360 lux, Res: 16 Bits
#bus.write_byte_data(0x44, 0x01, 0x05)

#time.sleep(1)
'''
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
'''