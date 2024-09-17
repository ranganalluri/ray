import ray
from time import sleep

# Connect to the Ray cluster using Ray Client (default port is 10001)
# ray.init(address='ray://192.168.1.153:10001')
ray.init(address='localhost:6379')

@ray.remote(num_cpus=2)
def remote_task(x):
    sleep(1)
    return x * x

# Submit tasks to the remote cluster
results = ray.get([remote_task.remote(i) for i in range(100)])

print(results)
