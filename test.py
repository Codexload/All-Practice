import sys
def right():
    var = "Hello"
    vari = var.rjust(10, "*")
    print(vari)
def left():
    var1 = "Hello"
    vari1 = var1.ljust(10, "*")
    print(vari1)
for i in range(50):
    right()
    left()
sys.exit()