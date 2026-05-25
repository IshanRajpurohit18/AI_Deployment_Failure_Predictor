
import time
import random

print("Starting Monitoring Service...")

while True:
    cpu = random.randint(20, 95)
    memory = random.randint(30, 90)

    print(f"CPU Usage: {cpu}% | Memory Usage: {memory}%")

    if cpu > 85:
        print("WARNING: High CPU usage detected!")

    if memory > 80:
        print("WARNING: High memory usage detected!")

    time.sleep(5)
