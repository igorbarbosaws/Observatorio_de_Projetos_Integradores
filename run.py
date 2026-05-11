"""
Ponto de entrada unico do Observatorio PI.

Formas de executar:
    .venv\\Scripts\\python.exe run.py
    iniciar.bat  (duplo clique no Windows)
"""
import sys
import os
import subprocess


def main():
    ROOT = os.path.dirname(os.path.abspath(__file__))

    # ── Garante que esta rodando dentro do .venv ──────────────────────────────
    VENV_PYTHON = os.path.join(ROOT, ".venv", "Scripts", "python.exe")

    if os.path.exists(VENV_PYTHON) and os.path.abspath(sys.executable) != os.path.abspath(VENV_PYTHON):
        print(f"Relancando com o venv: {VENV_PYTHON}")
        result = subprocess.run([VENV_PYTHON, __file__] + sys.argv[1:])
        sys.exit(result.returncode)

    # ── A partir daqui estamos no .venv ──────────────────────────────────────
    APP_DIR = os.path.join(ROOT, "observatorio_pi")

    # Muda o diretorio de trabalho e adiciona ao path
    os.chdir(APP_DIR)
    sys.path.insert(0, APP_DIR)

    # ── 1. Banco e tabelas ────────────────────────────────────────────────────
    from sqlalchemy import text
    from app.database import engine, Base
    from app.models.user import User      # noqa: F401
    from app.models.project import Project  # noqa: F401

    Base.metadata.create_all(bind=engine)

    # ── 2. Migracao: coluna 'ativo' para bancos antigos ───────────────────────
    with engine.connect() as conn:
        cols = [row[1] for row in conn.execute(text("PRAGMA table_info(users)"))]
        if "ativo" not in cols:
            conn.execute(text("ALTER TABLE users ADD COLUMN ativo BOOLEAN NOT NULL DEFAULT 1"))
            conn.commit()
            print("Coluna 'ativo' adicionada ao banco.")

    # ── 3. Usuario admin padrao ───────────────────────────────────────────────
    from app.database import SessionLocal
    from app.core.security import hash_senha

    db = SessionLocal()
    try:
        if db.query(User).count() == 0:
            admin = User(
                nome="Administrador",
                email="admin@observatorio.pi",
                senha_hash=hash_senha("admin1234"),
                tipo="ADMIN",
                ativo=True,
            )
            db.add(admin)
            db.commit()
            print("Admin criado: admin@observatorio.pi / admin1234")
            print("ATENCAO: Altere a senha apos o primeiro login!")
    finally:
        db.close()

    # ── 4. Servidor ───────────────────────────────────────────────────────────
    import uvicorn

    print("")
    print("Servidor iniciando em: http://127.0.0.1:8000")
    print("Pressione CTRL+C para parar.")
    print("")

    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        reload_dirs=[APP_DIR],
    )


if __name__ == "__main__":
    main()
