from machine import Pin, I2C
from ssd1306

i2c = I2C(1, sda=Pin(26), scl=Pin(27))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.text('Ignatius ' , 0, 0)
display.text('' , 0, 16)
display.text('' , 0, 32)
display.text('' , 0, 0)
          
          
display.show()