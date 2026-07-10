from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.database import engine, get_db, Base

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