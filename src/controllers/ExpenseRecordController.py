from ..config.Conection import Conection
from ..database.ExpenseRecord_schema import ExpenseRecord

async def create_expense_record(supervisor_id: int, responsible_id: int, category_id: int, payment_method_id: int, description: str, cost: int, is_reviewed: int):
    db = Conection()
    try:
        result = await db.execute(
            "INSERT INTO expense_records (supervisor_id, responsible_id, category_id, payment_method_id, description, cost, is_reviewed) VALUES (?, ?, ?, ?, ?, ?, ?)",
            [supervisor_id, responsible_id, category_id, payment_method_id, description, cost, is_reviewed]
        )
        
        if result.rows_affected == 0:
            return None
            
        return {"message": "Registro de expensa creado exitosamente"}
    except Exception as e:
        return {"message": f"{e}"}
    finally:
        db.close()

async def get_expense_records() -> list[ExpenseRecord]:
    db = Conection()
    try:
        result = await db.execute("SELECT * FROM expense_records")
        
        records_list = [ExpenseRecord(**dict(zip(result.columns, row))) for row in result.rows]
        return records_list
    except Exception as e:
        return {"message": f"{e}"}
    finally:
        db.close()

async def get_expense_record_by_id(record_id: int) -> ExpenseRecord:
    db = Conection()
    try:
        result = await db.execute(
            "SELECT * FROM expense_records WHERE id = ?",
            [record_id]
        )
        
        if not result.rows:
            return None
            
        record_dict = dict(zip(result.columns, result.rows[0]))
        return ExpenseRecord(**record_dict)
    except Exception as e:
        return {"message": f"{e}"}
    finally:
        db.close()

async def update_expense_record(record_id: int, supervisor_id: int, responsible_id: int, category_id: int, payment_method_id: int, description: str, cost: int, is_reviewed: int) -> bool:
    db = Conection()
    try:
        result = await db.execute(
            "UPDATE expense_records SET supervisor_id = ?, responsible_id = ?, category_id = ?, payment_method_id = ?, description = ?, cost = ?, is_reviewed = ? WHERE id = ?",
            [supervisor_id, responsible_id, category_id, payment_method_id, description, cost, is_reviewed, record_id]
        )
        return True
    except Exception as e:
        return {"message": f"{e}"}
    finally:
        db.close()

async def delete_expense_record(record_id: int):
    db = Conection()
    try:
        result = await db.execute(
            "DELETE FROM expense_records WHERE id = ?",
            [record_id]
        )
        return True
    except Exception as e:
        return {"message": f"{e}"}
    finally:
        db.close()
