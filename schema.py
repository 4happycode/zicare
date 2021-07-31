from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    first_name: str
    last_name: str
    age: int

    class Config:
        orm_mode = True

class Patient(BaseModel):
    id: Optional[int] = None
    ktp: int
    full_name: str
    first_name: str
    last_name: str
    address: str

    class Config:
        orm_mode = True
        schema_extra = {"example": {
                            "ktp": 1234567890,
                            "full_name": "lufi taro",
                            "first_name": "lufy",
                            "last_name": "taro",
                            "address": "jl. laughtale"
                        }}


class PatientUpdate(BaseModel):
    ktp: Optional[int] = None
    full_name: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    address: Optional[str] = None

    created_date: Optional[datetime] = None
    modified_date: Optional[datetime] = None
    is_active: Optional[bool] = None

    class Config:
        orm_mode = True
        schema_extra = {"example": {
                            "ktp": 1234567890,
                            "full_name": "lufi taro",
                            "first_name": "lufy",
                            "last_name": "taro",
                            "address": "jl. laughtale",
                            "is_active": False
                        }}
