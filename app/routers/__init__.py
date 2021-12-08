from fastapi import APIRouter
from routers.trend import router as trend_router


router = APIRouter()
router.include_router(trend_router, prefix="/trends", tags=["trends"])
