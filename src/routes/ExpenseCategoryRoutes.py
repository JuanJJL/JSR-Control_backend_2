from fastapi import HTTPException, APIRouter, Depends
from ..database.ExpenseCategory_schema import ExpenseCategory, ExpenseCategory_create
from ..controllers import ExpenseCategoryController
from ..middlewares.auth_middeware import require_role

router_expense_categories = APIRouter(prefix="/expense_categories", tags=["expense_categories"])

@router_expense_categories.post("/create")
async def create_expense_category(data: ExpenseCategory_create, current_user: dict = Depends(require_role([3]))):
    if not data.category:
        raise HTTPException(status_code=400, detail="El nombre de la categoria es requerido")
        
    try:
        return await ExpenseCategoryController.create_expense_category(data.category)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router_expense_categories.get("/")
async def get_all_expense_categories():
    try:
        return await ExpenseCategoryController.get_expense_categories()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router_expense_categories.get("/{category_id}")
async def get_expense_category(category_id: int):
    try:
        return await ExpenseCategoryController.get_expense_category_by_id(category_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router_expense_categories.put("/update/{category_id}")
async def update_expense_category(category_id: int, data: ExpenseCategory_create, current_user: dict = Depends(require_role([3]))):
    try:
        return await ExpenseCategoryController.update_expense_category(category_id, data.category)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router_expense_categories.delete("/delete/{category_id}")
async def delete_expense_category(category_id: int, current_user: dict = Depends(require_role([3]))):
    try:
        return await ExpenseCategoryController.delete_expense_category(category_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
