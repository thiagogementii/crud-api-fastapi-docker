# 📦 Docker Compose - Ambiente de Desenvolvimento

Este arquivo `docker-compose.yml` define o ambiente de desenvolvimento da aplicação, utilizando containers para banco de dados e ferramenta de administração.

---

## 🧱 Serviços

### 🐘 PostgreSQL

Serviço responsável pelo banco de dados da aplicação.

- Utiliza a imagem oficial do PostgreSQL
- Expõe a porta padrão `5432` para acesso local
- Persiste os dados em volume local (evita perda de dados ao recriar o container)
- Faz parte de uma rede interna para comunicação com outros serviços

📌 **Importante:**  
As credenciais de acesso (usuário, senha, banco) são configuradas via variáveis de ambiente e **não devem ser versionadas no repositório**.

---

### 🛠️ pgAdmin

Interface web para gerenciamento do PostgreSQL.

- Permite visualizar tabelas, executar queries e administrar o banco
- Disponível via navegador
- Depende do serviço PostgreSQL para funcionamento
- Conectado à mesma rede interna

📌 **Importante:**  
As credenciais de acesso ao pgAdmin também são definidas via variáveis de ambiente.

---

## 🌐 Rede

### `postgres-compose-network`

- Tipo: `bridge`
- Responsável pela comunicação entre os containers
- Permite que o pgAdmin acesse o PostgreSQL usando o nome do serviço

---

## ▶️ Como executar

No diretório do projeto, execute:

```bash
docker-compose up
```

Para rodar em segundo plano:

```bash
docker-compose up -d
```

---

## ⏹️ Como parar

```bash
docker-compose down
```

---

## 🔌 Acessos

- **PostgreSQL**
  - Host: `localhost`
  - Porta: `5432`

- **pgAdmin**
  - URL: http://localhost:16543

---

## 💡 Boas práticas aplicadas

- Separação de serviços por responsabilidade
- Uso de rede interna para comunicação entre containers
- Persistência de dados com volumes
- Não exposição de credenciais no código

---

## 🚀 Possíveis melhorias

- Utilizar arquivo `.env` para variáveis de ambiente
- Definir versão fixa das imagens (evitar `latest`)
- Adicionar healthcheck para o banco
- Integrar com a aplicação FastAPI no mesmo `docker-compose`
- Adicionar serviço da API no futuro

---

## 📌 Observações

Este ambiente é voltado para **desenvolvimento local**.  
Para produção, serão necessárias configurações adicionais de segurança, backup e gerenciamento de credenciais.