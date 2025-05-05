
# 📌 TaskManagerAPI

API RESTful desenvolvida em Python com Flask para gerenciamento de tarefas pessoais. Cada usuário pode criar, listar, editar e excluir suas próprias tarefas de forma segura e organizada. O sistema utiliza autenticação JWT, criptografia de senhas e conexão com banco de dados PostgreSQL.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.12.3**
- **Flask** — Criação da API RESTful
- **SQLAlchemy** — ORM para integração com o banco de dados
- **psycopg2** — Driver PostgreSQL
- **bcrypt** — Criptografia segura de senhas
- **PyJWT** — Geração e validação de tokens JWT
- **python-dotenv** — Leitura de variáveis de ambiente via `.env`
- **pandas** — Manipulação de dados nas queries SQL

---

## 📂 Como Rodar o Projeto

### ✅ Pré-requisitos

- Python 3.12 ou superior
- PostgreSQL instalado e rodando
- Variáveis de ambiente no arquivo `.env`:
  
```env
JWT_KEY=chave_secreta
POSTGRE_URI_DEV=postgresql://usuario:senha@localhost:5432/seubanco
POSTGRE_URI_PRD=...
```

### 📥 Instalação

```bash
# Clone o repositório
git clone https://github.com/Vitorugz/personal_tasks_api.git

# Acesse o diretório
cd personal_tasks_api

# Crie e ative um ambiente virtual (opcional)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python run.py
```

### 🗄️ Estrutura das Tabelas (PostgreSQL)

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  full_name VARCHAR(170) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  password VARCHAR(128) NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  active BOOLEAN DEFAULT TRUE
);

CREATE TABLE task (
  id SERIAL PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  description VARCHAR(255) NOT NULL,
  status INT DEFAULT 0,
  user_task INT NOT NULL,
  FOREIGN KEY (user_task) REFERENCES users(id) ON DELETE CASCADE
);
```

---

## 🔐 Autenticação

Esta API utiliza **JWT (JSON Web Token)** para autenticação.

- Faça login com e-mail e senha via `/login` e receba um token.
- Envie esse token no **header** `Authorization` com o prefixo `Bearer` em todas as requisições protegidas:

```http
Authorization: Bearer seu_token_aqui
```

---

## 📡 Endpoints Disponíveis

### 🔸 **[POST]** `/register`
Cria um novo usuário.

#### Request
```json
{
  "full_name": "Vitor de Lima",
  "email": "vitor@email.com",
  "password": "senha123"
}
```
#### Response
```json
{
  "Message": "user created successfully"
}
```

---

### 🔸 **[POST]** `/login`
Faz login do usuário e retorna um JWT.

#### Request
```json
{
  "email": "vitor@email.com",
  "password": "senha123"
}
```

#### Response
```json
{
  "token": "jwt_gerado"
}
```

---

### 🔸 **[POST]** `/task/create`  
Cria uma nova tarefa. (Autenticação obrigatória)

#### Headers
```http
Authorization: Bearer seu_token
```

#### Request
```json
{
  "title": "Estudar Flask",
  "description": "Focar nos decorators e blueprints"
}
```

---

### 🔸 **[GET]** `/task/getAllTasks`  
Retorna todas as tarefas do usuário autenticado.

#### Headers
```http
Authorization: Bearer seu_token
```

---

### 🔸 **[DELETE]** `/task/delete?task_id=<id>`  
Deleta uma tarefa específica do usuário autenticado.

#### Headers
```http
Authorization: Bearer seu_token
```

---

### 🔸 **[PUT]** `/task/update?task_id=<id>`  
Atualiza uma tarefa específica.

#### Headers
```http
Authorization: Bearer seu_token
```

#### Request
```json
{
  "title": "Novo título",
  "description": "Nova descrição",
  "status": 1
}
```

---

## 📈 Possíveis Evoluções Futuras

- Sistema de categorias ou tags
- Filtros por status de tarefas
- Painel web com frontend em React ou Angular
- Notificações por e-mail
- Deploy da API em ambiente de produção (Render, Railway, etc.)

---

## 👨‍💻 Autor

Desenvolvido por **Vitor** — Desenvolvedor Back-end Python Jr.  
📫 [linkedin.com/in/vitordelimacosta](https://www.linkedin.com/in/vitordelimacosta)  

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
