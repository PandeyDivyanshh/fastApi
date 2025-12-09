from fastapi import FastAPI
from pydantic import BaseModel

# FastAPI app
app = FastAPI()

# -------------------- #
# Pydantic Schemamyvev
# -------------------- #
class Patient(BaseModel):   # yaha ideal schema define kar rahe hain
    name: str
    age: int

# -------------------- #
# API Endpoint
# -------------------- #
@app.post("/patient")
def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted")

    return {
        "status": "success",
        "message": "Patient inserted successfully",
        "data": patient
    }
