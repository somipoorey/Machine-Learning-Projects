DATASET

The MNIST database of handwritten digits, available from this page, has a training set of 60,000 examples, and a test set of 10,000 examples. It is a subset of a larger set available from NIST. The digits have been size-normalized and centered in a fixed-size image.

Download Link: http://yann.lecun.com/exdb/mnist/

---------------------------------------
GIT PUSH & SOURCE CONTROL

echo "# model-latest" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/somipoorey/MNIST.git
git push -u origin main

Note: Git lfs can be setup using https://git-lfs.github.com/

-----------------------------------------
CREATING A DOCKER IMAGE

Set Current Working Directory To ....\model

>>docker ps

>>docker images

>>docker build -f Dockerfile .

>>docker images 
COPY <none> IMAGE ID

>>docker tag <IMAGE ID> <IMAGE_NAME:VERSION>

--------------------------------------------

RUNNING A DOCKER CONTAINER IN LOCAL MACHINE

>>docker run -d -p 5000:5000 --name MNIST <IMAGE_NAME:VERSION>

>> Launch Browser & Start getting inferences from the model

---------------------------------
REFER: https://www.freecodecamp.org/news/build-and-push-docker-images-to-aws-ecr/
---------------------------------

SETTING UP AWS CLI

Install CLI for Windows
>>C:\> msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi

Checking for the installation
>>aws --version

Login to AWS Console and add new permission under existing user in IAM policies and get secrets
>>add AmazonECS_FullAccess
>> Security credentials> Create access key > Download.csv

>>aws configure
AWS Access Key ID [None]: xxxxxxxxxxxxxxxxxxxxx
AWS Secret Access Key [None]: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Default region name [None]: us-east-1
Default output format [None]: json

-----------------------------------

Create a Repo in ECR

>>aws ecr create-repository --repository-name myrepo --region us-east-1

COPY URI from AWS Console
>>xxxxxxxx806.dkr.ecr.us-east-1.amazonaws.com/myrepo

-----------------------------------

PUSHING A DOCKER IMAGE FROM LOCAL TO AWS ECR

GetAuthorizationToken API
>>aws ecr get-login-password --region us-east-1

xxxxJwYXlsb2FkIjoiS3Y5WUZEN2hqcE90a......................................DIwxxxxfQ==

Now Lets Login into ECR
>> aws ecr --region <region> | docker login -u AWS -p <encrypted_token> <repo_uri>

>> aws ecr --region us-east-1 | docker login -u AWS -p xxxxJwYXlsb2FkIxxxxxxxUZEN2hqcE90a......................................DIwxxxxQ== xxxxxxxx806.dkr.ecr.us-east-1.amazonaws.com/myrepo

LOGIN SUCCEEDED!!

-----------------------------------------------

TAGGING A LOCAL DOCKER IMAGE

>>docker tag mnist:v1 xxxxxxxx806.dkr.ecr.us-east-1.amazonaws.com/myrepo

------------------------------------------------

FINAL STEP PUSHING THE DOCKER IMAGE TO ECR

>>docker push xxxxxxxx806.dkr.ecr.us-east-1.amazonaws.com/myrepo

------------------------------------------------

DEPLOY ECS CLUSTER USING FARGATE (WILL BE USING CUSTOM ECR IMAGE)
Concept : https://s3.amazonaws.com/ecs-console-prod-static-content-us-east-1/AWSECS_fargate.mp4

Refer https://acloudguru.com/blog/engineering/deploying-a-containerized-flask-application-with-aws-ecs-and-docker

>> Go to Amazon ECS from AWS Console >> Clusters >> Get Started

STEP-1 > Container Definition

>> Select Custom > Configure
Container Name: MNISTApplication
Image: 5xxxxxxx06.dkr.ecr.us-east-1.amazonaws.com/myrepo:latest (AWS ECR> Repo > IMAGE URI)
Memory Limits : Hard Limit > 1000
Port Mappings : 5000 /tcp

STEP-2 > Task Definition

>>Task definition name : first-run-task-definition
>>Network mode : awsvpc
>>Task execution role : Create new
>>Compatibilities : FARGATE
>>Task memory : 4GB (4096)
>>Task CPU : 2 vCPU (2048)

STEP-3 > Service

>>Service name : mnistApp-service
>>Number of desired tasks : 1
>>Security group : Automatically create new
>>Load balancer type : None


STEP-4 > Fargate Cluster

>>Cluster name : default
>>VPC ID : Automatically create new
>>Subnets : Automatically create new

Click CREATE to launch the automated resource creation wizard. The process may take upto 15 minutes.

--------------------------------------

> Once the resouces are ready, Return back to ECS Dashboard and Select the Default Cluster
> Click on the GenderApp-service that you created > Click on the running task
> Under Task / Newtork section Look for ENI Id. Click It.
> Now you will be re-directed to EC2 Console, where you need to look for IPv4 Public IP

Copy and paste this IP address in browser and you will be able to access you application and get predictions from your application.

Public IPv4 address
http://xx.xxx.xxx.xxx:5000/
