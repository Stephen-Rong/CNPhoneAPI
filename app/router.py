from fastapi import APIRouter, Query, HTTPException

from app.phone_service import lookup_phone, is_valid_phone

router = APIRouter(prefix="/api", tags=["Phone Lookup"])


@router.get("/phone")
async def query_phone(
    phone: str = Query(..., description="手机号码，如 13800138000")
):
    if not phone or not is_valid_phone(phone):
        raise HTTPException(status_code=400, detail="Invalid phone number")

    result = await lookup_phone(phone)
    
    if not result:
        raise HTTPException(status_code=404, detail="Phone number not found")
    
    return result


@router.get("/health")
async def health_check():
    return {"status": "ok"}
