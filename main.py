from fastapi import FastAPI
from src.routes.UserRoutes import router_users
from src.routes.AuthRoutes import router
from src.routes.ProductRoutes import router_products
from src.routes.PaymentMethodRoutes import router_payment_methods


app = FastAPI()

app.include_router(router_users,tags=["users"])
app.include_router(router,tags=["auth"])
app.include_router(router_products,tags=["products"])
app.include_router(router_payment_methods,tags=["payment_methods"])