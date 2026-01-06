from typing import List, Optional
from ..config.Conection import Conection
from ..database.SalesRecords_schema import SalesRecord, SalesRecordCreate
from ..controllers import ProductController, ClientController

async def create_sale(data: SalesRecordCreate) -> SalesRecord:
    """
    Crea una venta y descuenta el stock automáticamente
    """
    db = Conection()
    try:
        # 1. Verificar que el cliente existe
        client = await ClientController.get_client_by_id(data.id_client)
        if not client:
            raise Exception(f"Cliente con ID {data.id_client} no encontrado")
        
        # 2. Verificar que el producto existe y obtener precio/costo
        product = await ProductController.get_product_by_id(data.id_product)
        if not product:
            raise Exception(f"Producto con ID {data.id_product} no encontrado")
        
        # 3. Validar cantidad
        if data.quantity <= 0:
            raise Exception("La cantidad debe ser mayor a 0")
        
        # 4. Calcular valores
        unit_price = product.price
        total_amount = unit_price * data.quantity
        profit = (unit_price - product.cost) * data.quantity
        
        # 5. Descontar stock (se permite stock negativo)
        new_stock = product.stock - data.quantity
        
        # Actualizar stock del producto
        await db.execute(
            "UPDATE products SET stock = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
            [new_stock, data.id_product]
        )
        
        # 6. Insertar venta
        result = await db.execute(
            """
            INSERT INTO sales_records 
            (id_client, id_product, quantity, unit_price, total_amount, profit, id_payment_method)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            [data.id_client, data.id_product, data.quantity, unit_price, total_amount, profit, data.id_payment_method]
        )
        
        new_id = result.last_insert_rowid
        if new_id is None:
            raise Exception("No se pudo obtener el ID de la venta.")
        
        # 7. Obtener venta creada
        result = await db.execute(
            """
            SELECT id, id_client, id_product, quantity, unit_price, total_amount, 
                   profit, id_payment_method, created_at, updated_at 
            FROM sales_records WHERE id = ?
            """,
            [new_id]
        )
        
        sale_dict = dict(zip(result.columns, result.rows[0]))
        return SalesRecord(**sale_dict)
    
    finally:
        await db.close()


async def get_all_sales() -> List[SalesRecord]:
    """
    Obtener todas las ventas
    """
    db = Conection()
    try:
        result = await db.execute(
            """
            SELECT id, id_client, id_product, quantity, unit_price, total_amount,
                   profit, id_payment_method, created_at, updated_at
            FROM sales_records
            ORDER BY created_at DESC
            """
        )
        
        return [
            SalesRecord(**dict(zip(result.columns, row)))
            for row in result.rows
        ]
    
    finally:
        await db.close()


async def get_sale_by_id(sale_id: int) -> Optional[SalesRecord]:
    """
    Obtener una venta por su ID
    """
    db = Conection()
    try:
        result = await db.execute(
            """
            SELECT id, id_client, id_product, quantity, unit_price, total_amount,
                   profit, id_payment_method, created_at, updated_at
            FROM sales_records WHERE id = ?
            """,
            [sale_id]
        )
        
        if not result.rows:
            return None
        
        sale_dict = dict(zip(result.columns, result.rows[0]))
        return SalesRecord(**sale_dict)
    
    finally:
        await db.close()


async def delete_sale(sale_id: int) -> bool:
    """
    Eliminar una venta
    NOTA: No restaura el stock automáticamente
    """
    db = Conection()
    try:
        result = await db.execute(
            "DELETE FROM sales_records WHERE id = ?",
            [sale_id]
        )
        return result.rows_affected > 0
    
    finally:
        await db.close()


async def get_sales_by_client(client_id: int) -> List[SalesRecord]:
    """
    Obtener todas las ventas de un cliente específico
    """
    db = Conection()
    try:
        result = await db.execute(
            """
            SELECT id, id_client, id_product, quantity, unit_price, total_amount,
                   profit, id_payment_method, created_at, updated_at
            FROM sales_records 
            WHERE id_client = ?
            ORDER BY created_at DESC
            """,
            [client_id]
        )
        
        return [
            SalesRecord(**dict(zip(result.columns, row)))
            for row in result.rows
        ]
    
    finally:
        await db.close()


async def get_sales_by_product(product_id: int) -> List[SalesRecord]:
    """
    Obtener todas las ventas de un producto específico
    """
    db = Conection()
    try:
        result = await db.execute(
            """
            SELECT id, id_client, id_product, quantity, unit_price, total_amount,
                   profit, id_payment_method, created_at, updated_at
            FROM sales_records 
            WHERE id_product = ?
            ORDER BY created_at DESC
            """,
            [product_id]
        )
        
        return [
            SalesRecord(**dict(zip(result.columns, row)))
            for row in result.rows
        ]
    
    finally:
        await db.close()