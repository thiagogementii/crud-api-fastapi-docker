# CRUD API com FastAPI e Docker

Projeto simples de API REST com operações CRUD utilizando:

- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose

---

## 📁 Configuração de ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
POSTGRES_USER=app_user
POSTGRES_PASSWORD=testando123
POSTGRES_DB=app_db

PGADMIN_DEFAULT_EMAIL=emailteste@gmail.com
PGADMIN_DEFAULT_PASSWORD=testando123
```

---

## 🚀 Como rodar

### 1. Subir banco de dados e pgAdmin

```bash
docker-compose up -d
```

---

### 2. Build da aplicação

```bash
docker build -t crud-api .
```

---

### 3. Rodar a aplicação

```bash
docker run -p 8000:8000 crud-api
```

---

## 🌐 Acessos

- API (Swagger):
  - http://localhost:8000/docs

- pgAdmin:
  - http://localhost:16543

---

## 🛠️ Observações

- O banco PostgreSQL roda em container separado via Docker Compose
- A aplicação FastAPI roda em outro container
- As credenciais são configuradas via arquivo `.env`
- O host do banco dentro da aplicação deve ser: `postgres` (nome do serviço no Docker)

---

## 📌 Próximos passos

- Integrar FastAPI ao PostgreSQL
- Adicionar camada de services e repositories
- Criar Dockerfile otimizado
- Adicionar testes automatizados