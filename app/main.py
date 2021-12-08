from fastapi import FastAPI, APIRouter
from routers import router as api_router
from starlette.middleware.cors import CORSMiddleware

router = APIRouter()
router.include_router(
    api_router,
    prefix='/api',
    tags=['api']
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
