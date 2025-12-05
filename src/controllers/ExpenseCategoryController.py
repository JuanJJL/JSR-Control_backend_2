from ..config.Conection import Conection
from ..database.ExpenseCategory_schema import ExpenseCategory

async def create_expense_category(category: str):
    db = Conection()
    try:
        result = await db.execute(
            "INSERT INTO expense_categories (category) VALUES (?)",
            [category]
        )
        
        if result.rows_affected == 0:
            return None
            
        return {"message": "Categoria de expensa creada exitosamente", "category": category}
    except Exception as e:
        return {"message": f"{e}"}
    finally:
        db.close()

async def get_expense_categories() -> list[ExpenseCategory]:
    db = Conection()
    try:
        result = await db.execute("SELECT * FROM expense_categories")
        
        categories_list = [ExpenseCategory(**dict(zip(result.columns, row))) for row in result.rows]
        return categories_list
    except Exception as e:
        return {"message": f"{e}"}
    finally:
        db.close()

async def get_expense_category_by_id(category_id: int) -> ExpenseCategory:
    db = Conection()
    try:
        result = await db.execute(
            "SELECT * FROM expense_categories WHERE id = ?",
            [category_id]
        )
        
        if not result.rows:
            return None
            
        category_dict = dict(zip(result.columns, result.rows[0]))
        return ExpenseCategory(**category_dict)
    except Exception as e:
        return {"message": f"{e}"}
    finally:
        db.close()

async def update_expense_category(category_id: int, category: str) -> bool:
    db = Conection()
    try:
        result = await db.execute(
            "UPDATE expense_categories SET category = ? WHERE id = ?",
            [category, category_id]
        )
        return True
    except Exception as e:
        return {"message": f"{e}"}
    finally:
        db.close()

async def delete_expense_category(category_id: int):
    db = Conection()
    try:
        result = await db.execute(
            "DELETE FROM expense_categories WHERE id = ?",
            [category_id]
        )
        return True
    except Exception as e:
        return {"message": f"{e}"}
    finally:
        db.close()
