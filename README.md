# ☁️ Serverless Web Application using AWS

A fully serverless web application built using **Amazon S3, AWS Lambda, and Amazon API Gateway**. The application provides a simple web interface that collects user input and sends it to a Python-based Lambda function through an API Gateway endpoint.

## 🚀 Features

- 🌐 Static frontend hosted on Amazon S3
- ⚡ Serverless backend using AWS Lambda
- 🐍 Python-based Lambda function
- 🔗 API Gateway for HTTP communication
- 🔐 CORS-enabled API communication
- ☁️ No traditional server or EC2 instance required
- 📱 Simple and lightweight web interface

## 🧱 Architecture

The application follows a simple serverless architecture:

```text
User
  │
  ▼
HTML / JavaScript Frontend
  │
  │ HTTP Request
  ▼
Amazon API Gateway
  │
  ▼
AWS Lambda (Python)
  │
  ▼
Response
  │
  ▼
Frontend
```

The frontend is hosted on **Amazon S3** and communicates with the backend through **Amazon API Gateway**. API Gateway triggers the Python Lambda function, which processes the request and returns a response to the frontend.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| HTML | Frontend structure |
| JavaScript | Frontend interaction and API requests |
| Python | Backend Lambda function |
| AWS Lambda | Serverless backend processing |
| Amazon API Gateway | HTTP API endpoint |
| Amazon S3 | Static website hosting |

## 📂 Project Structure

```text
serverless-web-application-using-aws/
│
├── index.html
├── lambda_function.py
└── README.md
```

### `index.html`

Contains the frontend interface and JavaScript code used to collect user input and communicate with the API Gateway endpoint.

### `lambda_function.py`

Contains the Python AWS Lambda function responsible for processing the request and returning a response.

## ⚙️ AWS Configuration

### 1. Create an S3 Bucket

Create an Amazon S3 bucket and configure it for static website hosting.

Upload:

```text
index.html
```

to the bucket.

### 2. Create the Lambda Function

Create an AWS Lambda function using **Python**.

Upload or paste the contents of:

```text
lambda_function.py
```

into the Lambda function.

### 3. Create an API Gateway Endpoint

Create an API Gateway API and connect it to the Lambda function.

Configure an HTTP method such as:

```text
POST
```

and enable **CORS** so that the frontend can communicate with the API.

### 4. Update the Frontend

Update the API endpoint URL in `index.html`:

```javascript
const API_URL = "YOUR_API_GATEWAY_URL";
```

Replace `YOUR_API_GATEWAY_URL` with your deployed API Gateway endpoint.

### 5. Deploy and Test

After configuring the AWS services:

1. Deploy the Lambda function.
2. Deploy the API Gateway API.
3. Upload the frontend to S3.
4. Open the S3-hosted website.
5. Submit the form.
6. Verify that the request reaches Lambda and the response is displayed in the frontend.

## 🔄 How It Works

1. The user enters information in the web interface.
2. JavaScript collects the input.
3. The frontend sends an HTTP request to API Gateway.
4. API Gateway invokes the AWS Lambda function.
5. Lambda processes the request using Python.
6. Lambda returns a response.
7. The frontend displays the response to the user.

## 🔒 Security Notes

For production deployments:

- Avoid storing AWS credentials in frontend code.
- Use appropriate IAM permissions.
- Configure CORS to allow only trusted origins.
- Enable HTTPS for API communication.
- Validate and sanitize user input.
- Avoid exposing sensitive information in Lambda responses or logs.

## 💰 Serverless Benefits

This project demonstrates the benefits of a serverless architecture:

- No server management
- Automatic scaling
- Pay-per-use AWS services
- Reduced infrastructure overhead
- Easy integration between AWS services

## 🎯 Learning Objectives

This project demonstrates practical experience with:

- AWS Lambda
- Amazon API Gateway
- Amazon S3
- Serverless architecture
- REST API communication
- Python
- HTML and JavaScript
- CORS configuration
- Cloud-based application deployment

## 🔮 Future Improvements

Possible improvements include:

- Add a database using Amazon DynamoDB
- Add authentication using Amazon Cognito
- Add better input validation
- Improve the frontend user interface
- Add error handling and loading states
- Add automated testing
- Add CI/CD deployment using GitHub Actions
- Add monitoring and logging using Amazon CloudWatch

## 📄 License

This project is intended for educational and demonstration purposes.
