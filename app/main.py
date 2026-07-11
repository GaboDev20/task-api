from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.database import engine, get_db, Base
from fastapi.security import OAuth2PasswordRequestForm
from app.security import verify_password, create_access_token

Base.metadata.create_all(bind=engine) #Crea las tablas si no existen

app = FastAPI()

@app.post("/tasks", response_model=schemas.TaskOut)
def create_Task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@app.get("/tasks", response_model = list[schemas.TaskOut])
def list_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@app.get("/tasks/{task_id}", response_model=schemas.TaskOut)
def view_task(task_id: int, db: Session = Depends(get_db)):
    tarea = crud.get_task(db, task_id)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@app.put("/tasks/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    tarea = crud.update_task(db, task_id, task)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@app.delete("/tasks/{task_id}",status_code=204)
def delete_task(task_id: int,db: Session = Depends(get_db)):
    tarea = crud.delete_task(db, task_id)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return None

@app.post("/register",response_model = schemas.UserOut)
def register(user: schemas.UserCreate, db:Session = Depends(get_db)):
    usuario_existente = crud.get_user_by_email(db,user.email)
    if usuario_existente is not None:
        raise HTTPException(status_code = 400, detail = "Este Email Ya Está Registrado" )
    return crud.create_user(db,user)
    
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
        usuario = crud.get_user_by_email(db, form_data.username)
        if usuario is None:
            raise HTTPException(status_code = 401, detail="Credenciales Incorrectas")
        if not verify_password(form_data.password, usuario.hashed_password):
            raise HTTPException(status_code=401, detail="Credenciales Incorrectas")
        
        access_token = create_access_token(data={"sub": usuario.email})
        return {"access_tokens": access_token, "token_type": "bearer"}