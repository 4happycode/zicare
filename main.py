from sqlalchemy.sql.expression import asc, desc
import uvicorn
from fastapi import FastAPI, HTTPException, Query
import os
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from models import User as ModelUser, Patient as ModelPatient
from schema import User as SchemaUser, Patient as SchemaPatient, PatientUpdate as SchemaPatientUpdate
from dotenv import load_dotenv
from datetime import datetime
from typing import Optional
from helpers import SortBy, SortType

# Load env
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI(
    title="Zicare Backend Test",
    description="This is a very fancy project, with auto docs for the API and everything. <br /> Created by Wari Nur Raharjo. <br /><br /> Powered by swagger",
    version="1.0.0"
)
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


# Create
@app.post("/patient/", response_model=SchemaPatient)
def patient_add(patient: SchemaPatient):
    check_ktp = db.session.query(ModelPatient).filter_by(ktp=patient.ktp).first()
    if check_ktp:
        raise HTTPException(status_code=404, detail="KTP already exists") # make response if found
        
    db_patient = ModelPatient(
        ktp=patient.ktp,
        full_name=patient.full_name,
        first_name=patient.first_name,
        last_name=patient.last_name,
        address=patient.address
    )
    db.session.add(db_patient)
    db.session.commit()     # insert execute

    return db_patient


# Read
@app.get("/patient/")
def patient_list(patient_id: Optional[int]=None, active: bool=None, offset: int=0, limit: int=10, sort_type: SortType=SortType.asc, sort_by: SortBy=SortBy.id):
    patient = db.session.query(ModelPatient).filter()

    # Additional filter
    if patient_id: patient = patient.filter_by(id=patient_id)
    if active is not None : patient = patient.filter_by(is_active=active)

    # Dynamic sorting
    db_pattient = patient.order_by(eval(sort_type.name)(sort_by))    # read execute
    
    count = db_pattient.count()
    data = db_pattient.limit(limit).offset(offset).all()
    response = {"data": data, "offset": offset, "limit": limit, "total":count}

    return response


# Update
# @app.put("/patient_detail/{patient_id}", tags=['Update Patient'])
@app.put("/patient_detail/{patient_id}")
def patient_update(patient_id: int, patient: SchemaPatientUpdate):
    db_patient = db.session.query(ModelPatient).filter(ModelPatient.id==patient_id)
    
    if not db_patient.first():      # Validate exist data
        raise HTTPException(status_code=404, detail="Patient not found") # make response if not found
    
    # Update data will be save to database
    save_to_db = db_patient.first().default_values()
    save_to_db.update( (k,v) for k,v in patient.__dict__.items() if v is not None ) # Data update from payload
    save_to_db.update( {'modified_date': datetime.now()} )

    # Check existing ktp
    check_ktp = db.session.query(ModelPatient).filter_by(ktp=save_to_db.get('ktp')).first()
    if check_ktp:
        if check_ktp.id != patient_id:
            raise HTTPException(status_code=404, detail="KTP already exists") # make response if not found
    
    db_patient.update(save_to_db)
    db.session.commit()     # update execute

    return db_patient.first()


# Delete
@app.delete("/patient_detail/{patient_id}")
def patient_delete(patient_id: int):
    patient = db.session.query(ModelPatient).filter(ModelPatient.id==patient_id).first()
    
    if not patient:                 # Validate exist data
        raise HTTPException(status_code=404, detail="Patient not found") # make response if not found

    db.session.delete(patient)
    db.session.commit()     # delete execute
    msg = 'deleted success'

    return {'message': msg}



# Run main.py in port 8000
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
