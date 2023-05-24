from time import sleep
import sys
def fadeText(string,delay):
    x = len(string)
    i = 0
    output = ""
    for i in range(0,x):
        sys.stdout.write(string[i])
        sys.stdout.flush()
        sleep(delay)

## Usage: fadeText("string",delay)
