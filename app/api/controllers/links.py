from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get("/")
async def redirect():
        return RedirectResponse("https://ai.gov.ae/uaecodes/")
