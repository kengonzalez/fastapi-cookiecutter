from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .users.controller import router as userrouter
from .books.controller import router as booksrouter
from .userbooks.controller import router as userbooksrouter

app = FastAPI()

origins = ["http://localhost:6000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

routers = [userrouter, booksrouter, userbooksrouter]

for route in routers:
    app.include_router(route)
