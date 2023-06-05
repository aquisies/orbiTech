from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
from hubspot.contacts import Contacts
from clickup.client import Client
from app.database import create_api_call, get_contact_by_email
import os

router = APIRouter()

@router.post("/sync")
async def sync_contacts(background_tasks: BackgroundTasks):
    try:
        hubspot_access_token = os.environ.get("HUBSPOT_ACCESS_TOKEN")
        hubspot_client = Contacts(access_token=hubspot_access_token)
        hubspot_contacts = hubspot_client.contacts.get_all_contacts()

        clickup_api_token = os.environ.get("CLICKUP_API_TOKEN")
        clickup_client = Client(api_token=clickup_api_token)
        for contact in hubspot_contacts:
            email = contact.get("email")
            if email:
                existing_contact = get_contact_by_email(email)
                if not existing_contact or not existing_contact.estado_clickup:
                    task_data = {
                        "name": contact.get("firstname", "") + " " + contact.get("lastname", ""),
                        "description": f"Email: {email}\nPhone: {contact.get('phone', '')}\nWebsite: {contact.get('website', '')}",
                        "status": "open"
                    }
                    clickup_task = clickup_client.tasks.create_task(task_data)
                    contact["properties"]["estado_clickup"] = True
                    update_contact_properties(contact)

        return JSONResponse(content={"message": "Sincronización completada."})

    except Exception as e:
        params = "No se pudieron sincronizar los contactos"
        result = "Error"
        create_api_call(params=params, result=result)

        raise HTTPException(status_code=500, detail="Error al sincronizar los contactos con ClickUp")
