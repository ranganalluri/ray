from collections import Counter
import socket
import time
import ray

ray.init(address='auto')

print('''This cluster consists of
    {} nodes in total
    {} CPU resources in total
'''.format(len(ray.nodes()), ray.cluster_resources()['CPU']))

@ray.remote
class NodeActor:
    def __init__(self):
        self.ip_address = socket.gethostbyname(socket.gethostname())

    def get_ip(self):
        time.sleep(0.001)
        return self.ip_address

# Create multiple actor instances
num_actors = 10
actors = [NodeActor.remote() for _ in range(num_actors)]

# Submit tasks to the actors
object_ids = [actor.get_ip.remote() for actor in actors for _ in range(1000)]
ip_addresses = ray.get(object_ids)

# Process and print the results
print('Tasks executed')
for ip_address, num_tasks in Counter(ip_addresses).items():
    print('    {} tasks on {}'.format(num_tasks, ip_address))