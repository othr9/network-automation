import getpass
import telnetlib

user = input("Enter your remote account: ")
password = getpass.getpass()

f = open("myswitches")

for lien in f:
	print("Configuring Switch " + (line))
	HOST = line
	tn = telnetlib.Telnet(HOST)


	tn.read_until(b"Username: ")
	tn.write(user.encode('ascii') + b"\n")
	if password:
    	 tn.read_until(b"Password: ")
    	 tn.write(password.encode('ascii') + b"\n")




	tn.write(b"enable\n")
	tn.write(b"cisco\n")
	tn.write(b"conf t\n")
	

	for i in range(2,5):
        	tn.write(b"vlan " + str(i).encode('ascii') + b"\n")
        	tn.write(b"name VLAN_Loop " + str(i).encode('ascii') + b"\n")
	tn.write(b"end\n")
	tn.write(b"exit\n")

	print(tn.read_all().decode('ascii'))
