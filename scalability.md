<h2>Reviewing the current architecture</h2>
<h3>Current Architecture Diagram</h3>

![alt text](https://github.com/Prachit99/PackTravel/blob/ashish_dev/images/previous_architecture.jpg)

Shortcomings of current arhitecture:
- Not Scalable
- Not Performant
- Security Vulnerability (runs on HTTP insetad of HTTPS)
- Painful Server Maintainance

<h2>Proposed architecture</h2>
<h3>Proposed Architecture Diagram</h3>

![alt text](https://github.com/Prachit99/PackTravel/blob/ashish_dev/images/proposed_architecture.png)

Steps to implement this proposed architecture:
1. Containerize the current appllication using Docker. We will write a GitHub workflow to dockerize the app after every push and then upload it to AWS Elastic Container Registry and then run it in Elastic Containers.
2. Add an Application Load Balancer (ALB) to enable horizontal scaling and health checks. Now the requests can be distributed between several instances and unhealthy instances can be detected and replaced. The ALB also supports port forwarding so we won’t need intermediate proxies like nginx as the requests can be directly forwarded to the application on port 8000.
3. Elastic Container Service(ECS) allows running docker containers in the cloud. We will use it to run our Django app instances. ECS supports two ways of running containers: running the containers inside a server (EC2 VM or on-premise) or running containers in serverless mode using Fargate. We will use Fargate to avoid managing servers.
4. A database is stateful by nature because it stores data that has to be persistent. So it can’t run as a stateless container in ECS/Fargate. But we don’t want to manage a server or VM for the database. So we will use serversless MongoDB.

Advantages of the proposed architecture:
- Automatically Scalable - Elastic Container Service can be configured to scale automatically.
- Highly Performant - can handle multiple concurrent users due to load balancer and containers
- Secure - Application Load Balancer supports HTTPS and SSL/TLS certificates that can be added using the AWS Certificates Manager.
- Easy Maintainance - We will use serverless mode in ECS and serverless MongoDB, both are easy to maintain and manage. 
