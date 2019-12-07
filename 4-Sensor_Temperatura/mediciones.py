import smbus
addr = 0x5a
i2c = smbus.SMBus(1)
for x in range(0,0x3F)+[0xf0,]:
        ret = i2c.read_word_data(addr, x)
        print("%s, %s, %s"%(x,ret,ret))