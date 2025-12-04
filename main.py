from fastapi import FastAPI
from src.routes.UserRoutes import router_users
from src.routes.AuthRoutes import router
from src.routes.ProductRoutes import router_products
from src.routes.ClientsRoutes import router_clients
from src.routes.ProductCategoryRoutes import router_ProductsCategory



app = FastAPI()


app.include_router(router_users, tags=["users"])
app.include_router(router, tags=["auth"])
app.include_router(router_ProductsCategory, tags=["productsCategory"])
app.include_router(router_products, tags=["products"])
app.include_router(router_clients, tags=["clients"])
