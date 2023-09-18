# lcd_display_raspberry

Do you have a Raspberry PI? 
Do you have a I2C 20x4 display bought for a couple of bucks? 
Do you have a short wave receiver and a 1$ USB sound dongle? 

Tune your short wave receiver on 10.100 MHz USB, and receive the weather forecast on the display! 

## connection schema 

    \|/  SWR antenna
     |       +------------------+   audio    +---------------+   +--------------+      RTTY                  +------------------+
     +-------| SDR/SWR receiver |----------->| USB soundcard |-->| raspberry PI |-->soundmodem -->read.py -->| I2C 20x4 display |
             +------------------+ out    mic +---------------+   +--------------+   (software)    (software) +------------------+


## requirements

1. raspberry PI, raspbian, I2c modules on
2. I2c display
3. python + smbus
4. minimodem (sudo apt install minimodem)

## memory map of the display 

20x4
|||||||||||||||||||||
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|80|81|82|83|84|85|86|87|88|89|8A|8B|8C|8D|8E|8F|90|91|92|93|
|C0|C1|C2|C3|C4|C5|C6|C7|C8|C9|CA|CB|CC|CD|CE|CF|D0|D1|D2|D3|
|94|95|96|97|98|99|9A|9B|9C|9D|9E|9F|A0|A1|A2|A3|A4|A5|A6|A7|
|D4|D5|D6|D7|D8|D9|DA|DB|DC|DD|DE|DF|E0|E1|E2|E3|E4|E5|E6|E7|

