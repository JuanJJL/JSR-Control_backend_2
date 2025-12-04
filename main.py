from fastapi import FastAPI
from src.routes.UserRoutes import router_users
from src.routes.AuthRoutes import router
from src.routes.ProductRoutes import router_products
from src.routes.ClientsRoutes import router_clients
from src.routes.ProductCategoryRoutes import router_ProductsCategory
from src.routes.PaymentMethodRoutes import router_payment_methods
from src.routes.ExpenseCategoryRoutes import router_expense_categories
from src.routes.ExpenseRecordRoutes import router_expense_records

app = FastAPI()

app.include_router(router_users,tags=["users"])
app.include_router(router,tags=["auth"])
app.include_router(router_products,tags=["products"])
app.include_router(router_payment_methods,tags=["payment_methods"])
app.include_router(router_expense_categories,tags=["expense_categories"])
app.include_router(router_expense_records,tags=["expense_records"])