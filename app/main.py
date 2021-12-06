from fastapi import FastAPI, APIRouter
from routers.trend import router as trend_router
from starlette.middleware.cors import CORSMiddleware

router = APIRouter()
router.include_router(
    trend_router,
    prefix='/trends',
    tags=['trends']
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

app.include_router(router)
