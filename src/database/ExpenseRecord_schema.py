from pydantic import BaseModel
from typing import Optional

class ExpenseRecord_create(BaseModel):
    supervisor_id: int
    responsible_id: int
    category_id: int
    payment_method_id: int
    description: Optional[str] = None
    cost: int
    is_reviewed: Optional[int] = 0

class ExpenseRecord(BaseModel):
    id: int
    supervisor_id: int
    responsible_id: int
    category_id: int
    payment_method_id: int
    description: Optional[str]
    cost: int
    is_reviewed: int
    created_at: str
    updated_at: str
