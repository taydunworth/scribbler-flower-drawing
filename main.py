from Myro import *
init("/dev/tty.IPRE6-365764-DevB")

count = ask("How many petals do you want on the flower?")

count = (int(count))

for x in range(count):
    forward(.5,1.8)
    turnBy(-45)
    motors(4,0,2)
    turnBy(-50)
    forward(.5,1.8)
    turnBy(86)
turnBy(10)
forward(.5,3)
motors(.7,0,.8)
forward(.5,1.5)
