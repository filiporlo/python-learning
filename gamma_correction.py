# Gamma coefficient no generating the color if value is 0
gamma = {
    "all": 0,
    "red": 1.5,
    "green": 2.5,
    "blue": 2.5,
    "white": 1.2
}

max_in = 255
max_out = 255

#AVR or ARM
arch = "ARM"

#complete zero from second position with ones
one = 1


def gamma2file(gamma, max_in, max_out, file, ones):
    out = 0
    for i in range(0,max_in):
        if i > 0:
         file.write(",")
        if i % 15 == 0:
            file.write("\n")
        out = ((i / max_in) ** gamma) * max_out + 0.5
        out = int(out)
        if ones and not out and i:
            out = 1
        file.write("\t" + str(out))

f = open("gamma.h", "w")
f.truncate(0)
f.write("//--------------------------------------\n")
f.write("//GAMMA TABLE GENERATOR filiporlo.pl\n")
f.write("//--------------------------------------\n")



error = 0
for name, value in gamma.items():
    if value != 0:
        f.write("\n//GAMMA " + str(name) + " " + str(value) + "\n")

        if arch == "AVR":
            f.write("const uint8_t PROGMEM gamma_" + str(name) + "[] = {")
        elif arch == "ARM":
            f.write("const uint32_t gamma_" + str(name) + "[] = {")
        else:
            print("Not supported architecture!")
            error = 1
            break

        gamma2file(value, max_in, max_out, f, one)
        f.write(" };\n\n")

   
f.close()
if not error:
    print("Data save in " + f.name)