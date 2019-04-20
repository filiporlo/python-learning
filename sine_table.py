#phase shift in degrees
phi = 0

#amplitude min and max
#a_min = 0
a_max = 255

#number of steps
steps = 256

#architecture AVR or ARM
arch = "ARM"

import numpy as np

f = open("sine.h", "w")


def sine2file(phi, a_max, steps, file):
    out = 0
    for i in range(0,steps):
        if i > 0:
         file.write(",")
        if i % 15 == 0:
            file.write("\n")

        out = ((a_max/2) * (np.sin(np.radians(i * (360/steps) + phi)) + 1))+0.5
        out = int(out)
        file.write("\t" + str(out))

    f.write(" };\n\n")






f.truncate(0)
f.write("//--------------------------------------\n")
f.write("//SINE TABLE GENERATOR filiporlo.pl\n")
f.write("//--------------------------------------\n")

if arch == "AVR":
    f.write("const uint8_t PROGMEM sine[] = {")
    sine2file(phi, a_max, steps, f)
    f.close()

elif arch == "ARM":
    f.write("const uint32_t sine[] = {")
    sine2file(phi, a_max, steps, f)
    f.close()

else:
    print("Not supported architecture!")
    f.close()







