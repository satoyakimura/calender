from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from passlib.context import CryptContext
# from starlette.sessions import SessionMiddleware
from databases import Database

# from app.api.api import api_router
from app.core.config import settings

database = Database(settings.database_url)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI()
# app.include_router(api_router)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
# app.add_midleware(SessionMiddleware, secret_key="secret_key")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/signup", response_class=HTMLResponse)
async def sign_up(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.post("/signup_request", response_class=HTMLResponse)
async def signup_request(request: Request, username: str = Form(...), password: str = Form(...)):
    query = "SELECT * FROM users WHERE username = :username"
    result = await database.fetch_one(query=query, values={"username": username})
    # 同じusernameが存在する場合はエラーメッセージとともにレスポンスを返す
    if result:
        error_message = "このユーザー名は既に使われています。\n別のユーザー名を選んでください。"
        return templates.TemplateResponse("signin.html", {"request": request, "username": username, "error_message": error_message})
    hashed_password = pwd_context.hash(password)
    query = "INSERT INTO users(username, hashed_password) VALUES (:username, :hashed_password)"
    values = {"username": username, "hashed_password": hashed_password}

    await database.execute(query=query, values=values)

    return templates.TemplateResponse("register.html", {"request": request, "username": username})



@app.get("/signin", response_class=HTMLResponse)
async def log_in(request: Request):
    return templates.TemplateResponse("signin.html", {"request": request})

@app.post("/signin_request", response_class=HTMLResponse)
async def signin_request(request: Request, username: str = Form(...), password: str = Form(...)):
    query = "SELECT * FROM users WHERE username = :username"
    user = await database.fetch_one(query=query, values={"username": username, "password": password})
    if user and pwd_context.verify(password, user.hashed_password):
        request.session['user_id'] = str(user.id)
        return templates.TemplateResponse("signin_success.html", {"request": request, "username": username})
    else:
        error_message = "ユーザー名またはパスワードが間違っています。"
        return templates.TemplateResponse("signin.html", {"request": request, "error_message": error_message})


# @app.get("/signout")

