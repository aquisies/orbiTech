from sqlalchemy.orm import Session
from .models import Contact, CallRecord, APICall
from datetime import datetime
from .connection import get_db

def create_contact(contact_data: dict):
    with get_db() as db:
        contact = Contact(**contact_data)
        db.add(contact)
        db.commit()
        db.refresh(contact)
        return contact

def create_call_record(call_data: dict):
    with get_db() as db:
        call_record = CallRecord(**call_data)
        db.add(call_record)
        db.commit()
        db.refresh(call_record)
        return call_record

def create_api_call(params: str, result: str):
    with get_db() as db:
        api_call = APICall(datetime=datetime.now(), params=params, result=result)
        db.add(api_call)
        db.commit()
        db.refresh(api_call)
        return api_call

def get_contact_by_email(email: str):
    with get_db() as db:
        contact = db.query(Contact).filter(Contact.email == email).first()
        return contact

def contact_exists(email: str):
    with get_db() as db:
        contact = db.query(Contact).filter(Contact.email == email).first()
        return contact is not None
