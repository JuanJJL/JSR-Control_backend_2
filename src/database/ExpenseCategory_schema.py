from pydantic import BaseModel
from typing import Optional

class ExpenseCategory_create(BaseModel):
    category: str

class ExpenseCategory(BaseModel):
    id: int
    category: str
    created_at: str
    updated_at: str
