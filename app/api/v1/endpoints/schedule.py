from fastapi import FastAPI
from fastapi.responses import HTMLResponse
schedule_router = FastAPI()

@schedule_router.get("/schedule", response_class=HTMLResponse)
async def schedule(request: Request):
    return templates.TemplateResponse()