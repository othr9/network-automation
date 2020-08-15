import getpass
import telnetlib

HOST = "192.168.1.20"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
for i in range(2,7):
        tn.write(b"vlan " + str(i).encode('ascii') + b"\n")
        tn.write(b"name VLAN " + str(i).encode('ascii') + b"\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
