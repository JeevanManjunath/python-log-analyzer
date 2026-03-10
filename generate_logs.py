import random

# Function to generate random IP address
def generate_ip():
    return ".".join(str(random.randint(1,255)) for _ in range(4))

# Ask user for number of IPs
num_ips = int(input("Enter number of unique IP addresses: "))

# Generate IP list
ips = [generate_ip() for _ in range(num_ips)]

# Login status types
statuses = ["Login Failed", "Login Successful"]

# Ask user for number of logs
num_logs = int(input("Enter number of log entries to generate: "))

with open("server.log", "w") as file:
    for i in range(num_logs):

        ip = random.choice(ips)

        # Simulate attacker behaviour
        if random.random() < 0.7 and ip == ips[0]:
            status = "Login Failed"
        else:
            status = random.choice(statuses)

        file.write(f"{ip} - {status}\n")

print(f"\nGenerated {num_logs} log entries successfully.")