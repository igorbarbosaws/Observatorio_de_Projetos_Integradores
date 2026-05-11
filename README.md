# Observatório de Projetos Integradores

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)
![Faculdade](https://img.shields.io/badge/SENAC-ADS-orange)

Plataforma web para centralizar a submissão, avaliação e consulta dos Projetos Integradores do curso de Análise e Desenvolvimento de Sistemas (ADS) do SENAC.

---

## Descrição

O sistema resolve a descentralização no envio de Projetos Integradores. A dependência de e-mails e plataformas genéricas causa perda de documentos, dificuldade no controle de versões e alto tempo gasto na organização manual. O Observatório PI centraliza todo esse fluxo em um ambiente seguro e organizado.

## Funcionalidades

- **Alunos** — submetem e acompanham seus projetos
- **Professores** — avaliam projetos e registram notas
- **Coordenação** — acompanha o processo e extrai relatórios
- **Empresas** — visualizam projetos e perfis de alunos (banco de talentos)

## Tecnologias

| Camada | Tecnologia |
|---|---|
| Backend | Python 3.13 + FastAPI |
| Banco de dados | SQLite + SQLAlchemy 2.x |
| Frontend | Jinja2 + Bootstrap 5 |
| Autenticação | JWT (python-jose) + bcrypt |

## Como executar

### Pré-requisitos

- Python 3.11 ou superior
- Git

### 1. Clone o repositório

```bash
git clone https://github.com/EdsonAguiar888/Observatorio_de_Projetos_Integradores.git
cd Observatorio_de_Projetos_Integradores
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r observatorio_pi/requirements.txt
```

### 4. Execute o projeto

```bash
python run.py
```

O script cria o banco de dados, aplica migrações e sobe o servidor automaticamente.  
Acesse em: **http://127.0.0.1:8000**

> **Windows:** você também pode dar duplo clique em `iniciar.bat`.

### Credenciais iniciais

| Campo | Valor |
|---|---|
| E-mail | `admin@observatorio.pi` |
| Senha | `admin1234` |

> Altere a senha após o primeiro login.

## Variáveis de ambiente (opcional)

| Variável | Descrição | Padrão |
|---|---|---|
| `SECRET_KEY` | Chave secreta para assinar os tokens JWT | `observatorio_secret_key_dev_only` |

Em produção, defina `SECRET_KEY` com um valor longo e aleatório.

## Estrutura do projeto

```
Observatorio_de_Projetos_Integradores/
├── run.py                        # Ponto de entrada
├── iniciar.bat                   # Atalho Windows
├── observatorio_pi/
│   ├── requirements.txt
│   └── app/
│       ├── main.py               # Rotas da interface web
│       ├── database.py           # Configuração do banco
│       ├── core/
│       │   ├── config.py         # Configurações gerais
│       │   └── security.py       # JWT e bcrypt
│       ├── models/               # Modelos SQLAlchemy
│       ├── routers/              # Routers da API REST
│       ├── schemas/              # Schemas Pydantic
│       └── templates/            # Templates HTML (Jinja2)
```

## Equipe

- Edson Aguiar
- Evencio Neto
- Estevão Enoque
- Igor Barbosa
- Paulo Coutinho
