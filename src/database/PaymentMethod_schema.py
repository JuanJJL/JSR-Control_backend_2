from pydantic import BaseModel
from typing import Optional

class PaymentMethod_create(BaseModel):
    method_name: str

class PaymentMethod(BaseModel):
    id: int
    payment_method: str
    created_at: str
    updated_at: str
