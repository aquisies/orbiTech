import hubspot
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from hubspot.crm.properties import ApiException
from app.database import create_api_call
from dotenv import load_dotenv
import os

router = APIRouter()

class ContactCreateRequest(BaseModel):
    email: str
    firstname: str
    lastname: str
    phone: str
    website: str

class ContactResponse(BaseModel):
    id: str
    email: str
    firstname: str
    lastname: str
    phone: str
    website: str

load_dotenv()

hubspot_access_token = os.getenv("HUBSPOT_ACCESS_TOKEN")

@router.post("/contacts")
async def create_hubspot_contact(contact: ContactCreateRequest):
    try:
        client = hubspot.Client.create(access_token=hubspot_access_token)

        contact_properties = {
            "email": contact.email,
            "firstname": contact.firstname,
            "lastname": contact.lastname,
            "phone": contact.phone,
            "website": contact.website,
        }
        created_contact = client.crm.contacts.basic_api.create(data=[contact_properties])

        params = f"Email: {contact.email}, First Name: {contact.firstname}, Last Name: {contact.lastname}, Phone: {contact.phone}, Website: {contact.website}"
        result = "Success"
        create_api_call(params=params, result=result)

        return JSONResponse(content=created_contact)

    except ApiException as e:
        params = f"Email: {contact.email}, First Name: {contact.firstname}, Last Name: {contact.lastname}, Phone: {contact.phone}, Website: {contact.website}"
        result = "Error"
        create_api_call(params=params, result=result)

        raise HTTPException(status_code=500, detail="Error al crear el contacto en HubSpot")

@router.get("/contacts")
async def get_hubspot_contacts():
    try:
        client = hubspot.Client.create(access_token=hubspot_access_token)

        contacts = client.crm.contacts.basic_api.get_page(limit=10, archived=False)

        # Mapea los datos de los contactos a objetos de respuesta
        contact_list = []
        for contact in contacts.results:
            contact_data = {
                "id": contact.id,
                "email": contact.properties.email,
                "firstname": contact.properties.firstname,
                "lastname": contact.properties.lastname,
                "phone": contact.properties.phone,
                "website": contact.properties.website,
            }
            contact_list.append(ContactResponse(**contact_data))

        return JSONResponse(content=contact_list)

    except ApiException as e:
        raise HTTPException(status_code=500, detail={e})
