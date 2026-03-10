import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import defaultdict

log_file = "server.log"

fig, ax = plt.subplots()

def update(frame):

    failed_attempts = defaultdict(int)

    with open(log_file, "r") as file:
        for line in file:
            parts = line.split(" - ")
            ip = parts[0]
            status = parts[1].strip()

            if status == "Login Failed":
                failed_attempts[ip] += 1

    # Top 10 attackers
    top_attackers = sorted(failed_attempts.items(), key=lambda x: x[1], reverse=True)[:10]

    ips = [ip for ip, count in top_attackers]
    attempts = [count for ip, count in top_attackers]

    ax.clear()

    ax.barh(ips, attempts)

    ax.set_title("Top Attacking IPs (Real-Time)")
    ax.set_xlabel("Failed Login Attempts")
    ax.set_ylabel("IP Address")

    plt.tight_layout()

    # Automatically save graph
    plt.savefig("attack_graph.png")

    print("Graph updated and saved as attack_graph.png")

ani = FuncAnimation(fig, update, interval=3000)

plt.show()