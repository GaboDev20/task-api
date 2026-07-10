from sqlalchemy.orm import Session
from app import models, schemas

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()

def create_task(db: Session, task: schemas.TaskCreate):
    nueva_tarea = models.Task(title = task.title, description = task.description)
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea

def update_task(db: Session, task_id: int, task: schemas.TaskUpdate):
    tarea_existente = get_task(db, task_id)

    if tarea_existente is None:
        return None
    tarea_existente.title = task.title
    tarea_existente.description = task.description
    db.commit()
    db.refresh(tarea_existente)
    return tarea_existente

def delete_task(db: Session, task_id: int):
    tarea_existente = get_task(db, task_id)
    if tarea_existente is None:
        return None
    db.delete(tarea_existente)
    db.commit()
    return tarea_existente
