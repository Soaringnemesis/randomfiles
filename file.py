import os
import itertools

def runprgm(pg, pin):
    try:
        string = "./prog1" + pin
        os.system(string)
        return True
    except KeyboardInterrupt:
        exit(0)
    except Exception as e:
        print(e)

alphabet = "0123456789"
prgm = prog1

for c in itertools.product(alphabet, repeat=4):
    pin = ''.join(c)
    pin = password.encode('utf-8')
    print("Trying: %s" % pin)
    