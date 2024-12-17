import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import config
from database import Base, engine

from service.User import user_router
from service.Record import record_router
from service.Commodity import commodity_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title='DATABASE')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router, prefix="/user")
app.include_router(record_router, prefix='/record')
app.include_router(commodity_router, prefix='/commodity')


@app.get("/")
async def root():
    return {
        "status": 0,
        "message": "OK",
        "version": "v1.0.0"
    }

if __name__ == "__main__":
    uvicorn.run(app, host=config.bind_host, port=config.bind_port)
