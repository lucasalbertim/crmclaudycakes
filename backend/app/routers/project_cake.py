from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.project_cake import ProjectCake
from app.schemas.project_cake import ProjectCakeCreate, ProjectCakeRead
from typing import List
import os

router = APIRouter(prefix="/project-cakes", tags=["ProjectCakes"])
UPLOAD_DIR = "uploads/cakes"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/", response_model=ProjectCakeRead)
def create_project_cake(project: ProjectCakeCreate, db: Session = Depends(get_db)):
    db_project = ProjectCake(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@router.get("/", response_model=List[ProjectCakeRead])
def list_project_cakes(db: Session = Depends(get_db)):
    return db.query(ProjectCake).all()

@router.post("/upload-photo/{project_id}", response_model=ProjectCakeRead)
def upload_project_photo(project_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    project = db.query(ProjectCake).filter(ProjectCake.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    with open(filepath, "wb") as buffer:
        buffer.write(file.file.read())
    project.photo = filepath
    db.commit()
    db.refresh(project)
    return project

@router.patch("/{project_id}/reference", response_model=ProjectCakeRead)
def mark_as_reference(project_id: int, db: Session = Depends(get_db)):
    project = db.query(ProjectCake).filter(ProjectCake.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    project.is_reference = True
    db.commit()
    db.refresh(project)
    return project
