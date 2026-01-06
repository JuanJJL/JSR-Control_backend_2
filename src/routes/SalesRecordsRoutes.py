from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from ..database.SalesRecords_schema import SalesRecord, SalesRecordCreate
from ..controllers import SalesRecordsController
from ..middlewares.auth_middeware import verify_token

router_sales = APIRouter(prefix="/sales", tags=["sales"])

# ========== RUTAS PROTEGIDAS ==========

@router_sales.post("/create", response_model=SalesRecord, status_code=status.HTTP_201_CREATED)
async def create_sale_route(data: SalesRecordCreate, current_user: dict = Depends(verify_token)):
   
    try:
        return await SalesRecordsController.create_sale(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router_sales.get("/", response_model=List[SalesRecord])
async def get_all_sales_route(current_user: dict = Depends(verify_token)):

    try:
        return await SalesRecordsController.get_all_sales()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router_sales.get("/{sale_id}", response_model=SalesRecord)
async def get_sale_by_id_route(sale_id: int, current_user: dict = Depends(verify_token)):

    sale = await SalesRecordsController.get_sale_by_id(sale_id)
    if not sale:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return sale


@router_sales.delete("/delete/{sale_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_sale_route(sale_id: int, current_user: dict = Depends(verify_token)):

    deleted = await SalesRecordsController.delete_sale(sale_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return


@router_sales.get("/client/{client_id}", response_model=List[SalesRecord])
async def get_sales_by_client_route(client_id: int, current_user: dict = Depends(verify_token)):

    try:
        return await SalesRecordsController.get_sales_by_client(client_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router_sales.get("/product/{product_id}", response_model=List[SalesRecord])
async def get_sales_by_product_route(product_id: int, current_user: dict = Depends(verify_token)):

    try:
        return await SalesRecordsController.get_sales_by_product(product_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))