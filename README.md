🧠 Digital Twin Chatbox

Serverless AI-Powered Digital Twin Deployed on AWS

A production-ready conversational AI Digital Twin built with FastAPI, OpenAI, AWS Lambda, API Gateway, S3, and CloudFront.

This project transforms a locally running AI assistant into a fully deployed, serverless cloud application capable of persistent conversations, personalized context injection, and global HTTPS delivery.

🚀 Live Architecture Overview
User Browser
    ↓ HTTPS
CloudFront (CDN + TLS)
    ↓
S3 Static Website (Next.js Frontend)
    ↓ HTTPS API Calls
API Gateway (HTTP API)
    ↓
AWS Lambda (FastAPI Backend)
    ↓
    ├── OpenAI API (LLM responses)
    └── S3 Memory Bucket (Conversation storage)

📌 Features
🧠 Personalized AI Digital Twin

Injects structured personal data (facts.json)

Uses professional summary and communication style

Parses LinkedIn profile PDF for extended context

Strict anti-hallucination and anti-jailbreak rules

Maintains professional tone suitable for employers or clients

☁ Serverless Backend (AWS Lambda)

FastAPI application wrapped using Mangum

Stateless compute with persistent S3 storage

Auto-scaling and pay-per-use

💾 Persistent Memory

Each session stored as JSON in S3

Conversation history loaded dynamically

Survives Lambda restarts

🌍 Global Delivery

Frontend hosted on S3 static website

Distributed via CloudFront CDN

HTTPS enforced

🔐 Secure and Production-Ready

CORS restricted to CloudFront origin

IAM roles for least-privilege access

CloudWatch logging for monitoring

Docker-based Lambda packaging for runtime compatibility

🛠 Tech Stack
Backend

FastAPI

OpenAI API

Mangum (Lambda adapter)

Boto3 (S3 integration)

Pydantic

Python 3.12

Frontend

Next.js (Static Export Mode)

TypeScript

Cloud Infrastructure

AWS Lambda

API Gateway (HTTP API)

S3 (Memory + Static Hosting)

CloudFront

IAM

CloudWatch

📂 Project Structure
Digital-twin-chatbox/
│
├── backend/
│   ├── data/
│   │   ├── facts.json
│   │   ├── summary.txt
│   │   ├── style.txt
│   │   └── linkedin.pdf
│   │
│   ├── server.py
│   ├── context.py
│   ├── resources.py
│   ├── lambda_handler.py
│   ├── deploy.py
│   └── requirements.txt
│
├── frontend/
│   └── (Next.js app)
│
└── .env

🧠 How the Digital Twin Works
1️⃣ Context Injection

At runtime, the backend constructs a dynamic system prompt using:

Personal identity data (facts.json)

Professional summary (summary.txt)

Communication tone (style.txt)

Extracted LinkedIn profile text

Current timestamp

This creates a structured AI persona that:

Represents the individual faithfully

Refuses to hallucinate

Resists jailbreak attempts

Maintains professionalism

💬 Memory Design

Each conversation:

Generates or uses a session_id

Loads conversation history from S3

Sends last 10 messages + system prompt to OpenAI

Saves updated conversation back to S3

Storage format:

session-id.json


Example:

[
  {
    "role": "user",
    "content": "Tell me about your DevOps experience",
    "timestamp": "2026-01-25T12:30:00"
  }
]


This allows:

Stateless Lambda execution

Horizontal scaling

Persistent memory across sessions

🖥 Local Development
1️⃣ Backend Setup
cd backend
uv add -r requirements.txt
uv run uvicorn server:app --reload


Backend runs at:

http://localhost:8000

2️⃣ Frontend Setup
cd frontend
npm install
npm run dev


Frontend runs at:

http://localhost:3000

☁ AWS Deployment
🔹 Step 1: Package Lambda

Docker is required to ensure Lambda runtime compatibility.

cd backend
uv run deploy.py


This generates:

lambda-deployment.zip

🔹 Step 2: Deploy Lambda

Runtime: Python 3.12

Architecture: x86_64

Handler:

lambda_handler.handler

Required Environment Variables
OPENAI_API_KEY=your_key
USE_S3=true
S3_BUCKET=your-memory-bucket
CORS_ORIGINS=https://your-cloudfront-domain.cloudfront.net


Timeout: 30 seconds

🔹 Step 3: API Gateway

Routes configured:

Method	Path
ANY	/{proxy+}
GET	/
GET	/health
POST	/chat
OPTIONS	/{proxy+}

CORS enabled for:

https://your-cloudfront-domain.cloudfront.net

🔹 Step 4: S3 Buckets
Memory Bucket

Private

Stores conversation JSON files

Frontend Bucket

Static website hosting enabled

Public read access via bucket policy

🔹 Step 5: CloudFront

Origin:

S3 static website endpoint (HTTP only)


Viewer protocol policy:

Redirect HTTP to HTTPS


Default root object:

index.html

🔎 Monitoring & Debugging
CloudWatch Logs
/aws/lambda/twin-api

Common Issues
Problem	Solution
CORS error	Verify exact CloudFront URL in CORS_ORIGINS
500 error	Check CloudWatch logs
No memory persistence	Confirm USE_S3=true and bucket name correct
Slow responses	Increase Lambda timeout
💰 Cost Estimate

For moderate usage:

Lambda: Mostly free tier

API Gateway: Mostly free tier

S3: ~$0.02/GB

CloudFront: Free for first 1TB

Expected:

< $5/month


OpenAI usage costs not included.

🔐 Security Considerations

CORS restricted to CloudFront

Lambda role limited to required permissions

No secrets committed to Git

Environment variables stored in Lambda configuration

HTTPS enforced via CloudFront

📈 Production Improvements (Future Enhancements)

Replace S3 memory with DynamoDB

Add AWS WAF

Use ACM custom domain

Store secrets in AWS Secrets Manager

Implement rate limiting

Add CI/CD pipeline (GitHub Actions → Lambda deploy)

Add logging + metrics dashboards

🎯 What This Project Demonstrates

Serverless architecture design

AWS cloud deployment

DevOps packaging strategies

Production-grade prompt engineering

Persistent AI memory systems

Secure frontend/backend separation

CDN configuration with HTTPS

👤 Author

Patrick Mbaza
Cloud & DevOps Engineer
AI-Augmented Infrastructure Builder