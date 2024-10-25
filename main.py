from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from cryptography.fernet import Fernet
import hashlib
import base64

app = FastAPI()

# Helper function to derive encryption key from user-provided numeric key
def derive_key(user_key: str) -> Fernet:
    # Hash the user-provided key to create a consistent encryption key
    # This will allow the user to input a simple key, but it will still be secure
    hash_key = hashlib.sha256(user_key.encode()).digest()
    # Use the first 32 bytes for Fernet key and encode it in base64
    fernet_key = base64.urlsafe_b64encode(hash_key[:32])
    return Fernet(fernet_key)

class EncryptionRequest(BaseModel):
    plain_text: str = Field(..., description="Text to encrypt")
    key: str = Field(
        ..., 
        min_length=4, 
        max_length=10, 
        pattern=r"^\d+$", 
        description="Key should be a numeric string between 4 and 10 digits"
    )

class DecryptionRequest(BaseModel):
    encrypted_text: str = Field(..., description="Text to decrypt")
    key: str = Field(
        ..., 
        min_length=4, 
        max_length=10, 
        pattern=r"^\d+$", 
        description="Key should be a numeric string between 4 and 10 digits"
    )

@app.get("/")
def welcome():
    return {
        "message": "Welcome! Your API is running.",
        "instructions": {
            "encrypt": "To encrypt data, send a POST request to /encrypt with 'plain_text' and 'key'.",
            "decrypt": "To decrypt data, send a POST request to /decrypt with 'encrypted_text' and 'key'."
        }
    }

@app.post("/encrypt")
def encrypt_data(req: EncryptionRequest):
    try:
        fernet = derive_key(req.key)
        encrypted_text = fernet.encrypt(req.plain_text.encode())
        return {"encrypted_text": encrypted_text.decode()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Encryption failed: {str(e)}")

@app.post("/decrypt")
def decrypt_data(req: DecryptionRequest):
    try:
        fernet = derive_key(req.key)
        decrypted_text = fernet.decrypt(req.encrypted_text.encode()).decode()
        return {"decrypted_text": decrypted_text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Decryption failed: {str(e)}")

@app.get("/check")
def health_check():
    return {"status": "Server is running"}
