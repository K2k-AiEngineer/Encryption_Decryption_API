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
git clone <repository-url>
cd <repository-folder>

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install the required packages
pip install fastapi uvicorn cryptography
