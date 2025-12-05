from fastapi import HTTPException, APIRouter
from ..controllers import PaymentMethodController

router_payment_methods = APIRouter(prefix="/payment_methods", tags=["payment_methods"])

@router_payment_methods.get("/")
async def get_all_payment_methods():
    try:
        return await PaymentMethodController.get_payment_methods()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router_payment_methods.get("/{method_id}")
async def get_payment_method(method_id: int):
    try:
        return await PaymentMethodController.get_payment_method_by_id(method_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
