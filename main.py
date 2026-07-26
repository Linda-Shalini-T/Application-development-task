from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from database import SessionLocal
from models import TaskItem, TaskStage

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")



# LOGIN


@app.get("/")
async def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )


@app.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    if username == "admin" and password == "admin123":
        return templates.TemplateResponse(
            request=request,
            name="dashboard.html",
            context={}
        )

    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={
            "error": "Invalid Username or Password"
        }
    )


@app.get("/dashboard")
async def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={}
    )

# TASK ITEM CRUD


@app.get("/task-items")
async def task_items(request: Request):

    db = SessionLocal()

    tasks = db.query(TaskItem).all()

    db.close()

    return templates.TemplateResponse(
        request=request,
        name="task_items.html",
        context={
            "tasks": tasks
        }
    )


@app.post("/add-task")
async def add_task(
    task_id: int = Form(...),
    lesson_id: int = Form(...),
    assigned_to: str = Form(...),
    start_date: str = Form(...),
    due_date: str = Form(...),
    status: str = Form(...)
):

    db = SessionLocal()

    task = TaskItem(
        task_item_id=task_id,
        lesson_id=lesson_id,
        assigned_to=assigned_to,
        start_date=start_date,
        due_date=due_date,
        status=status
    )

    db.add(task)
    db.commit()
    db.close()

    return RedirectResponse(
        "/task-items",
        status_code=303
    )


@app.post("/update-task")
async def update_task(
    task_id: int = Form(...),
    lesson_id: int = Form(...),
    assigned_to: str = Form(...),
    start_date: str = Form(...),
    due_date: str = Form(...),
    status: str = Form(...)
):

    db = SessionLocal()

    task = db.query(TaskItem).filter(
        TaskItem.task_item_id == task_id
    ).first()

    if task:
        task.lesson_id = lesson_id
        task.assigned_to = assigned_to
        task.start_date = start_date
        task.due_date = due_date
        task.status = status

        db.commit()

    db.close()

    return RedirectResponse(
        "/task-items",
        status_code=303
    )


@app.post("/delete-task")
async def delete_task(
    task_id: int = Form(...)
):

    db = SessionLocal()

    task = db.query(TaskItem).filter(
        TaskItem.task_item_id == task_id
    ).first()

    if task:
        db.delete(task)
        db.commit()

    db.close()

    return RedirectResponse(
        "/task-items",
        status_code=303
    )


@app.post("/search-task")
async def search_task(
    request: Request,
    task_id: int = Form(...)
):

    db = SessionLocal()

    result = db.query(TaskItem).filter(
        TaskItem.task_item_id == task_id
    ).first()

    tasks = db.query(TaskItem).all()

    db.close()

    return templates.TemplateResponse(
        request=request,
        name="task_items.html",
        context={
            "tasks": tasks,
            "search_result": result
        }
    )


# TASK STAGE CRUD


@app.get("/task-stage")
async def task_stage(request: Request):

    db = SessionLocal()

    stages = db.query(TaskStage).all()

    db.close()

    return templates.TemplateResponse(
        request=request,
        name="task_stage.html",
        context={
            "stages": stages
        }
    )


@app.post("/add-stage")
async def add_stage(
    stage_id: int = Form(...),
    task_id: int = Form(...),
    stage_name: str = Form(...),
    stage_status: str = Form(...),
    last_updated: str = Form(...),
    status: str = Form(...)
):

    db = SessionLocal()

    stage = TaskStage(
        stage_id=stage_id,
        task_item_id=task_id,
        stage_name=stage_name,
        stage_status=stage_status,
        last_updated_date=last_updated,
        status=status
    )

    db.add(stage)
    db.commit()
    db.close()

    return RedirectResponse(
        "/task-stage",
        status_code=303
    )
    db = SessionLocal()

    stage = TaskStage(
        stage_id=stage_id,
        task_item_id=task_id,
        stage_name=stage_name,
        stage_status=stage_status,
        last_updated_date=last_updated,
        status=status
)

    db.add(stage)
    db.commit()
    db.close()

    return RedirectResponse(
        "/task-stage",
        status_code=303
)


@app.post("/delete-stage")
async def delete_stage(
    stage_id: int = Form(...)
):

    db = SessionLocal()

    stage = db.query(TaskStage).filter(
        TaskStage.stage_id == stage_id
    ).first()

    if stage:
        db.delete(stage)
        db.commit()

    db.close()

    return RedirectResponse(
        "/task-stage",
        status_code=303
    )


@app.get("/report")
async def report(request: Request):

    db = SessionLocal()

    stages = db.query(TaskStage).all()

    report_data = []

    for stage in stages:

        task = db.query(TaskItem).filter(
            TaskItem.task_item_id == stage.task_item_id
        ).first()

        due_date = ""

        if task:
            due_date = task.due_date

        report_data.append({
            "stage_id": stage.stage_id,
            "task_id": stage.task_item_id,
            "due_date": due_date,
            "last_updated": stage.last_updated_date,
            "status": stage.status
        })

    db.close()

    return templates.TemplateResponse(
        request=request,
        name="report.html",
        context={
            "report_data": report_data
        }
    )