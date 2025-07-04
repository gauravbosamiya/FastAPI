from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name : Annotated[str, Field(max_length=50, title="Name of the patient", 
                                description="name of the patient less than 50 char",
                                examples=["Gaurav"])]
    email : EmailStr
    linkedin_url : AnyUrl
    age : int = Field(gt=0, le=120)
    weight : Annotated[float, Field(gt=0, strict=True)]
    married : Annotated[bool, Field(default=None, description="Is the patient married or not")]
    allergies : Annotated[Optional[List[str]],  Field(max_length=5, default=None)]
    contact_details : Dict[str,str]
    
    
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
                "email":"gaurav@gmail.com",
                "linkedin_url":"http://linkedin.com/1322",
                # "married":False,
                # "allergies":["dust","pollen"], 
                "contact_details":{"phone":"12344"}}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)

