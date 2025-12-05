from fastapi import HTTPException, APIRouter
from ..database.ExpenseRecord_schema import ExpenseRecord, ExpenseRecord_create
from ..controllers import ExpenseRecordController

router_expense_records = APIRouter(prefix="/expense_records", tags=["expense_records"])

@router_expense_records.post("/create")
async def create_expense_record(data: ExpenseRecord_create):
    if data.cost < 0:
        raise HTTPException(status_code=400, detail="El costo no puede ser negativo")
        
    try:
        return await ExpenseRecordController.create_expense_record(
            data.supervisor_id,
            data.responsible_id,
            data.category_id,
            data.payment_method_id,
            data.description,
            data.cost,
            data.is_reviewed
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router_expense_records.get("/")
async def get_all_expense_records():
    try:
        return await ExpenseRecordController.get_expense_records()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router_expense_records.get("/{record_id}")
async def get_expense_record(record_id: int):
    try:
        return await ExpenseRecordController.get_expense_record_by_id(record_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router_expense_records.put("/update/{record_id}")
async def update_expense_record(record_id: int, data: ExpenseRecord_create):
    try:
        return await ExpenseRecordController.update_expense_record(
            record_id,
            data.supervisor_id,
            data.responsible_id,
            data.category_id,
            data.payment_method_id,
            data.description,
            data.cost,
            data.is_reviewed
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router_expense_records.delete("/delete/{record_id}")
async def delete_expense_record(record_id: int):
    try:
        return await ExpenseRecordController.delete_expense_record(record_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
