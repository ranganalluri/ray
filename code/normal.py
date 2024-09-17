from collections import Counter
import socket
import time


class NodeActor:
    def __init__(self):
        self.ip_address = socket.gethostbyname(socket.gethostname())

    def get_ip(self):
        time.sleep(0.001)
        return self.ip_address

# Create multiple actor instances
num_actors = 10
actors = [NodeActor() for _ in range(num_actors)]

# Submit tasks to the actors
ip_addresses = [actor.get_ip() for actor in actors for _ in range(1000)]


# Process and print the results
print('Tasks executed')
for ip_address, num_tasks in Counter(ip_addresses).items():
    print('    {} tasks on {}'.format(num_tasks, ip_address))