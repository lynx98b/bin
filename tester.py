from netmiko import ConnectHandler

checkpoint = {
    "device_type": "checkpoint_gaia",
    "host": "192.168.2.66",
    "username": "admin",
    "password": "1234Alger++"
}

connection = ConnectHandler(**checkpoint)


which_prompt = connection.find_prompt() # Find prompt method
print(which_prompt) # Print the prompt
output = connection.send_command('scp file.txt remote_username@10.10.0.2:/remote/directory/newfilename.txt')


print(output)

print('Closing Connection')
connection.disconnect()