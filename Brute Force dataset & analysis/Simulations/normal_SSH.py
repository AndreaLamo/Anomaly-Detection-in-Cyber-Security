import paramiko
import random
import time

hostname = "xxx.xxx.xxx.xx" # your server host
port = 22  


users = [
    {"username": "root", "password": "ciao"},
    {"username": "user", "password": "ciaoo"}
]

# Normal commands that uses SHH
commands = ["ls -l", "df -h", "whoami", "cat /etc/os-release", "uptime", "echo 'Testing normal SSH traffic'",]

def simulate_user_traffic(user):
    #Simulate SSH traffic for a single user.
    try:
        print(f"[INFO] Connecting as {user['username']}...")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=hostname, port=port, username=user["username"], password=user["password"])

        # Execute random commands
        for _ in range(random.randint(1, 5)):  # Random number of commands per session
            command = random.choice(commands)
            print(f"[INFO] Executing command: {command}")
            stdin, stdout, stderr = client.exec_command(command)
            print(stdout.read().decode())  # Print command output
            time.sleep(random.randint(1, 3))  # Random delay between commands

        client.close()
        print(f"[INFO] Session for {user['username']} ended.")
    except Exception as e:
        print(f"[ERROR] Failed for {user['username']}: {e}")

# Simulation of traffic
def simulate_traffic():
    while True:
        user = random.choice(users)  
        simulate_user_traffic(user)
        time.sleep(random.randint(5, 15))  

# Actual run
if __name__ == "__main__":
    try:
        simulate_traffic()
    except KeyboardInterrupt:
        print("[INFO] Simulation stopped.")
