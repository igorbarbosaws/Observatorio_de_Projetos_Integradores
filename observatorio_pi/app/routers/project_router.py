from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.project import Project
from app.schemas.project_schema import ProjectCreate, ProjectUpdate

router = APIRouter(prefix="/projects", tags=["Projetos"])


@router.get("/")
def listar_projetos(db: Session = Depends(get_db)):
    return db.query(Project).all()


@router.post("/", status_code=201)
def criar_projeto(projeto: ProjectCreate, db: Session = Depends(get_db)):
    novo = Project(titulo=projeto.titulo, descricao=projeto.descricao)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@router.put("/{project_id}")
def atualizar_projeto(project_id: int, projeto: ProjectUpdate, db: Session = Depends(get_db)):
    projeto_db = db.query(Project).filter(Project.id == project_id).first()
    if not projeto_db:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")

    if projeto.titulo is not None:
        projeto_db.titulo = projeto.titulo
    if projeto.descricao is not None:
        projeto_db.descricao = projeto.descricao

    projeto_db.versao += 1
    projeto_db.ultima_atualizacao = datetime.now(timezone.utc)

    db.commit()
    db.refresh(projeto_db)
    return projeto_db


@router.delete("/{project_id}", status_code=204)
def deletar_projeto(project_id: int, db: Session = Depends(get_db)):
    projeto_db = db.query(Project).filter(Project.id == project_id).first()
    if not projeto_db:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    db.delete(projeto_db)
    db.commit()
