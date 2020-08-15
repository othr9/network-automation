import getpass
import telnetlib

HOST = "192.168.10.2"
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
tn.write(b"int e1/0\n")
tn.write(b"no sh\n")
tn.write(b"ip add 192.168.1.1 255.255.255.224\n")
tn.write(b"end\n")
tn.write(b"conf t\n")
tn.write(b"ip dhcp pool LAB-1\n")
tn.write(b"network 192.168.1.0 255.255.255.224\n")
tn.write(b"default-router 192.168.1.1\n")
tn.write(b"end\n")
tn.write(b"conf t\n")
tn.write(b"int e1/1\n")
tn.write(b"no sh\n")
tn.write(b"ip add 192.168.1.33 255.255.255.224\n")
tn.write(b"end\n")
tn.write(b"conf t\n")
tn.write(b"ip dhcp pool LAB-2\n")
tn.write(b"network 192.168.1.33 255.255.255.224\n")
tn.write(b"default-router 192.168.1.33\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
