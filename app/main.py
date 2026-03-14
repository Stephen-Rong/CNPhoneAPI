from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.router import router

app = FastAPI(
    title="CNPhoneAPI",
    description="免费的中国手机号归属地查询API",
    version="1.0.2",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
async def root():
    return {
        "name": "CNPhoneAPI",
        "version": "1.0.2",
        "docs": "/docs",
        "endpoints": {
            "query": "/api/phone?phone=13800138000",
            "health": "/api/health",
        },
    }
