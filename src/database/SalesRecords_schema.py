from pydantic import BaseModel
from typing import Optional

# Modelo de entrada para crear una venta (POST)
class SalesRecordCreate(BaseModel):
    id_client: int
    id_product: int
    quantity: int
    id_payment_method: int

# Modelo de lectura (salida) (GET)
class SalesRecord(BaseModel):
    id: int
    id_client: int
    id_product: int
    quantity: int
    unit_price: int          # Precio del producto al momento de la venta
    total_amount: int        # quantity * unit_price
    profit: int              # (unit_price - cost) * quantity
    id_payment_method: int
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True

# Modelo para actualizar (opcional, si lo necesitas después)
class SalesRecordUpdate(BaseModel):
    quantity: Optional[int] = None
    id_payment_method: Optional[int] = None