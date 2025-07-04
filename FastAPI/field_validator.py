from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight : float
    married : bool
    allergies : List[str]
    contact_details : Dict[str,str]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domain = ['hdfc.com','icici.com']
        #abc@gmail.com
        domain_name = value.split("@")[-1]
        
        if domain_name not in valid_domain:
            raise ValueError("Not a valid domain")
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.email)
    print(patient.allergies)
    print(patient.married)
    print("inserted")
    
def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    
    print("updated")
    
patient_info = {"name":"Gaurav", 
                "age": 22, 
                "weight":75.2, 
                "email":"gaurav@hdfc.com",
                "married":False,
                "allergies":["dust","pollen"], 
                "contact_details":{"phone":"12344"}}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)

