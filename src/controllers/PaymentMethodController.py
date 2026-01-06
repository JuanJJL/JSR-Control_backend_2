from ..config.Conection import Conection
from ..database.PaymentMethod_schema import PaymentMethod

async def get_payment_methods() -> list[PaymentMethod]:
    db = Conection()
    try:
        result = await db.execute("SELECT * FROM payment_methods")
        
        payment_methods_list = [PaymentMethod(**dict(zip(result.columns, row))) for row in result.rows]
        return payment_methods_list
    except Exception as e:
        return {"message": f"{e}"}
    finally:
        db.close()

async def get_payment_method_by_id(method_id: int) -> PaymentMethod:
    db = Conection()
    try:
        result = await db.execute(
            "SELECT * FROM payment_methods WHERE id = ?",
            [method_id]
        )
        
        if not result.rows:
            return None
            
        payment_method_dict = dict(zip(result.columns, result.rows[0]))
        return PaymentMethod(**payment_method_dict)
    except Exception as e:
        return {"message": f"{e}"}
    finally:
        db.close()
