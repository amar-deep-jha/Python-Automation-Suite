# System monitor script
import psutil, time

print("Monitoring system performance... (Ctrl+C to stop)")
while True:
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    print(f"CPU: {cpu}% | Memory: {mem}%")
    time.sleep(3)
