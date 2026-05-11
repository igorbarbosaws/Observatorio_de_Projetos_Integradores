# Observatório de Projetos Integradores

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![Linguagem](https://img.shields.io/badge/Python-3.x-blue)
![Faculdade](https://img.shields.io/badge/SENAC-ADS--2%C2%BA%20M%C3%B3dulo-orange)

Este repositório contém o desenvolvimento do **Observatório de Projetos Integradores**, uma plataforma web centralizada projetada para organizar a submissão, avaliação e consulta de projetos acadêmicos do curso de Análise e Desenvolvimento de Sistemas (ADS) do SENAC.

---

## 🇧🇷 Português

### 📝 Descrição do Sistema
O projeto surge como uma solução para a descentralização no envio de Projetos Integradores (PIs). Atualmente, a dependência de e-mails e plataformas genéricas causa perda de documentos, dificuldade no controle de versões e alto tempo gasto na organização manual por parte dos professores e coordenação. O sistema centraliza todo esse fluxo em um ambiente seguro e organizado.

### 🎯 Objetivos
* **Centralização:** Unificar a submissão e o armazenamento de todos os trabalhos em um único local.
* **Avaliação Integrada:** Permitir que professores avaliem os projetos diretamente na plataforma através de rubricas acadêmicas.
* **Gestão Estratégica:** Oferecer aos coordenadores uma visão gerencial do progresso das turmas.
* **Vitrine de Talentos:** Funcionar como um portfólio digital, permitindo que empresas parceiras visualizem projetos e identifiquem potenciais talentos para recrutamento.

### 🛠 Tecnologias Utilizadas
* **Backend:** Python com FastAPI (Performance e documentação Swagger automática).
* **Banco de Dados:** SQLite com SQLAlchemy ORM.
* **Frontend:** Jinja2 Templates e Bootstrap 5 para responsividade.
* **Segurança:** Autenticação JWT (JSON Web Token) e criptografia de senhas com bcrypt.
* **Versionamento:** Git e GitHub.

### 💼 Regras de Negócio
* **Níveis de Acesso (RBAC):** Perfis distintos para Aluno, Professor e Administrador (Coordenador).
* **Gestão de Usuários:** Cadastro restrito ao perfil de Administrador.
* **Privacidade:** Alunos acessam apenas seus próprios projetos; a edição/exclusão é bloqueada após a avaliação.
* **Fluxo de Avaliação:** Registros de notas baseados em rubricas com auditoria de data e professor responsável.
* **Visibilidade Externa:** Projetos são exibidos para empresas parceiras somente após aprovação docente.

### 👥 Equipe do Projeto
* Edson Aguiar
* Evencio Neto
* Estevão Enoque
* Igor Barbosa
* Paulo Coutinho

### 🚀 Como Executar o Projeto
1.  Clone este repositório:
    ```bash
    git clone [https://github.com/EdsonAguiar888/Observatorio_de_Projetos_Integradores.git](https://github.com/EdsonAguiar888/Observatorio_de_Projetos_Integradores.git)
    ```
2.  Navegue até o diretório do projeto:
    ```bash
    cd Observatorio_de_Projetos_Integradores
    ```
3.  Instale as dependências (se necessário) e execute o arquivo principal:
    ```bash
    python app.py
    ```

### 📄 Documentação
A documentação técnica detalhada, incluindo Análise de Requisitos, Diagramas ER e conformidade com a LGPD, está disponível na raiz deste repositório..

---

## 🇺🇸 English

### 📝 System Description
This project is a solution for the decentralization of Integrative Project (PI) submissions. Currently, relying on emails and generic platforms leads to document loss, version control issues, and significant time spent by teachers and coordinators on manual organization. The system centralizes this entire workflow in a secure and organized environment.

### 🎯 Objectives
* **Centralization:** Unify the submission and storage of all works in a single location.
* **Integrated Evaluation:** Enable teachers to evaluate projects directly on the platform using academic rubrics.
* **Strategic Management:** Provide coordinators with a managerial view of class progress.
* **Talent Showcase:** Act as a digital portfolio, allowing partner companies to view projects and identify potential talents for recruitment.

### 🛠 Technologies Used
* **Backend:** Python with FastAPI (Performance and automatic Swagger documentation).
* **Database:** SQLite with SQLAlchemy ORM.
* **Frontend:** Jinja2 Templates and Bootstrap 5 for responsiveness.
* **Security:** JWT (JSON Web Token) authentication and bcrypt password encryption.
* **Versioning:** Git and GitHub.

### 💼 Business Rules
* **Access Control (RBAC):** Distinct profiles for Student, Teacher, and Administrator (Coordinator).

* **User Management:** Registration is restricted to the Administrator profile.

* **Privacy:** Students access only their own projects; editing/deletion is blocked after evaluation.

* **Evaluation Workflow:** Grade records based on rubrics with date and responsible teacher auditing.

* **External Visibility:** Projects are displayed to partner companies only after teacher approval.

### 👥 Project Team
* Edson Aguiar
* Evencio Neto
* Estevão Enoque
* Igor Barbosa
* Paulo Coutinho

### 🚀 How to Run the Project
1.  Clone this repository:
    ```bash
    git clone [https://github.com/EdsonAguiar888/Observatorio_de_Projetos_Integradores.git](https://github.com/EdsonAguiar888/Observatorio_de_Projetos_Integradores.git)
    ```
2.  Navigate to the project directory:
    ```bash
    cd Observatorio_de_Projetos_Integradores
    ```
3.  Install dependencies (if necessary) and run the main file:
    ```bash
    python app.py
    ```

### 📄 Documentation
Full technical documentation, including Requirements Analysis, ER Diagrams, and LGPD compliance, is available in the root of this repository.
