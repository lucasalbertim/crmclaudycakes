# Claudycakes CRM Backend

## Como rodar

1. Configure o arquivo `.env` baseado no `.env.example`.
2. Crie o ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Execute as migrações:
   ```bash
   alembic upgrade head
   ```
4. Inicie o servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

## Principais variáveis de ambiente
- `DATABASE_URL`: conexão com PostgreSQL
- `SMTP_*`: dados para envio de e-mail
- `ZAPI_*`: dados para envio de WhatsApp

## Documentação automática
Acesse `/docs` para visualizar e testar todos os endpoints via Swagger.

## Estrutura modular
- Rotas: `app/routers/`
- Modelos: `app/models/`
- Schemas: `app/schemas/`
- Serviços: `app/services/`

## Observações
- Habilite o CORS para integração com o frontend.
- Todos os endpoints possuem validação e tratamento de erros.
- Para produção, configure variáveis de ambiente seguras.
