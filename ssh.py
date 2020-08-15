from netmiko import ConnectHandler


iosv_l3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.21',
    'username': 'khalid',
    'password': 'cisco',
}

net_connect = ConnectHandler(**iosv_l3)

output = net_connect.send_command('sh run')
print (output)







config_commands = ['show vlan breif']
output = net_connect.send_config_set(config_commands)
print output





for n in range (2,21):
    print "Creating VLAN " + str(n)
    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print output 
