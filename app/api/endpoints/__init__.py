from fastapi import APIRouter
from .hubspot import router as hubspot_router
from .clickup import router as clickup_router

router = APIRouter()
router.include_router(hubspot_router, prefix="/hubspot", tags=["HubSpot"])
router.include_router(clickup_router, prefix="/clickup", tags=["ClickUp"])
