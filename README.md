# FastAPI Encryption and Decryption API

## Introduction

This API allows you to securely encrypt and decrypt text using a user-provided numeric key. Built with **FastAPI**, this application leverages the **cryptography** library to perform secure encryption and decryption using the **Fernet** symmetric encryption algorithm. 

The API supports two main operations: 
- **Encryption**: Convert plain text into encrypted text.
- **Decryption**: Convert encrypted text back into the original plain text.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **Pydantic**: For data validation and settings management using Python type annotations.
- **Cryptography**: Provides cryptographic recipes and primitives to Python developers.
- **Python 3.6+**: The programming language used to build the API.

## Features

- Encrypt and decrypt text securely.
- User-defined numeric key for encryption and decryption.
- Validation for input data ensuring the key is a numeric string between 4 and 10 digits.

## Installation

To run this API, ensure you have Python 3.6 or higher installed. You can create a virtual environment and install the required dependencies as follows:

```bash
# Clone the repository
git clone https://github.com/K2k-AiEngineer/Encryption_Decryption_API.git


# Install the required packages
pip install fastapi uvicorn cryptography

OR
pip install -r requirements.txt
```

## Running the API

Once the dependencies are installed, you can run the API using Uvicorn:

```bash
uvicorn main:app --reload

## API Endpoints
1. Welcome Endpoint
GET /
Returns a welcome message and instructions for using the API.

2. Encryption Endpoint
POST /encrypt

Request Body
```bash
{
  "plain_text": "Your text to encrypt",
  "key": "1234"  // Numeric key between 4 and 10 digits
}
Response
{
  "encrypted_text": "gAAAAABh... (encrypted text)"
}
```
![image](https://github.com/user-attachments/assets/511acea3-db92-46c1-b823-7cc00d07894f)
3. Decryption Endpoint
POST /decrypt

Request Body
```bash
{
  "encrypted_text": "gAAAAABh... (encrypted text)",
  "key": "1234"  // Numeric key used during encryption
}
Response
{
  "decrypted_text": "Your text to decrypt"
}
```
4. Health Check Endpoint
GET /health-check

```bash
Response
{
  "status": "Server is running"
}
```

```
