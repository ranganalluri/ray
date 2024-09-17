# Ray Cluster with Docker Compose and Job Submission

This guide shows how to set up a Ray cluster using Docker Compose and submit a Ray job.

## Prerequisites

- Docker and Docker Compose are installed.
- Python and Ray are installed to submit jobs.

## 1. Starting the Ray Cluster

Use Docker Compose to spin up a Ray cluster locally. The `docker-compose.yml` should be configured properly with the Ray head and worker nodes.

To start the cluster, run the following command:

```bash
docker-compose up
```

To submit a job run the following command
```PowerShell
ray job submit --address http://localhost:8265 -- python data.py
```
To submit a job with the local working directory the following command

```PowerShell
ray job submit --address http://localhost:8265 --working-dir .   -- python test.py 
