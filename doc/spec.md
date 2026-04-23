# 📄 Especificação do Projeto

## 📌 Objetivo

Este projeto tem como objetivo principal o **estudo prático de desenvolvimento backend** utilizando as seguintes tecnologias:

- FastAPI
- Docker
- Dockerfile
- Integração com banco de dados relacional

A proposta é construir uma aplicação simples, porém estruturada, que permita:

- Entender a organização de um projeto backend profissional
- Aplicar boas práticas de separação de responsabilidades
- Evoluir de um código simples para uma arquitetura mais robusta
- Preparar o ambiente para execução em containers com Docker

---

## 🎯 Motivação

O projeto foi criado com foco em aprendizado, visando:

- Compreender o funcionamento do FastAPI na prática
- Aprender a criar e gerenciar containers com Docker
- Entender como estruturar um backend de forma escalável
- Aprender a integrar a aplicação com PostgreSQL
- Evoluir um código simples para um padrão mais próximo do mercado

---

## 🏗️ Escopo Inicial

O sistema será uma API simples de gerenciamento de usuários, contendo operações básicas de CRUD:

- Criar usuário
- Listar usuários
- Atualizar usuário
- Deletar usuário

---

## 🧱 Entidade Principal

### User

Representa um usuário do sistema.

Campos:

- `id`: inteiro (chave primária)
- `name`: string
- `email`: string

---

## 🌐 Rotas da API

### ➕ Criar Usuário

**POST** `/users/`

Cria um novo usuário no sistema.

#### Request Body

```json
{
  "name": "string",
  "email": "string"
}
```

#### Response

```json
{
  "id": 1,
  "name": "string",
  "email": "string"
}
```

---

### 📄 Listar Usuários

**GET** `/users/`

Retorna a lista de todos os usuários cadastrados.

#### Response

```json
[
  {
    "id": 1,
    "name": "string",
    "email": "string"
  }
]
```

---

### ✏️ Atualizar Usuário

**PUT** `/users/{user_id}`

Atualiza os dados de um usuário existente.

#### Path Params

- `user_id`: ID do usuário

#### Request Body

```json
{
  "name": "string",
  "email": "string"
}
```

#### Response

```json
{
  "id": 1,
  "name": "string",
  "email": "string"
}
```

---

### ❌ Deletar Usuário

**DELETE** `/users/{user_id}`

Remove um usuário do sistema.

#### Path Params

- `user_id`: ID do usuário

#### Response

```json
{
  "message": "Usuário deletado"
}
```

---

## ⚙️ Tecnologias Utilizadas

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker

---

## 🚀 Evoluções Futuras

- Adicionar camada de services e repositories
- Implementar validação com Pydantic
- Adicionar testes automatizados
- Utilizar migrations com Alembic
- Configurar ambiente com Docker Compose
- Melhorar a organização da aplicação em camadas

---

## 📌 Observações

Este projeto é iterativo e será evoluído ao longo do tempo, com foco em aprendizado e aplicação de boas práticas de desenvolvimento backend.  
A aplicação será estruturada utilizando **PostgreSQL** como banco de dados principal, aproximando o projeto de um cenário real de mercado.