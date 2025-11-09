# AI Teacher Bot

Este projeto é um bot de WhatsApp integrado com a API da OpenAI, projetado para ajudar usuários a aprender e praticar inglês de forma interativa.

## Funcionalidades

O bot é um tutor de inglês pessoal que pode:

*   **Tradução e Explicação:**
    *   Traduzir mensagens do inglês para o português.
    *   Explicar o significado e o contexto de frases em inglês.
    *   Fornecer 3 exemplos de uso real para cada expressão.

*   **Tradução Reversa:**
    *   Traduzir expressões do português para o inglês.
    *   Explicar o uso correto da tradução.
    *   Mostrar 3 exemplos práticos em diferentes contextos.

*   **Teste de Fixação:**
    *   Quando solicitado pelo usuário (`teste de fixacao`), o bot inicia um teste com 10 perguntas.
    *   As perguntas são baseadas no histórico da conversa.
    *   O bot avalia cada resposta e fornece feedback.
    *   Ao final do teste, apresenta um diagnóstico sobre o desempenho do usuário, destacando pontos fortes e áreas para melhoria.

## Tecnologias Utilizadas

*   **Backend:** Python, FastAPI
*   **Inteligência Artificial:** OpenAI API (gpt-4o-mini)
*   **Mensageria:** Evolution API (para integração com WhatsApp)
*   **Banco de Dados:** PostgreSQL
*   **Cache:** Redis
*   **Containerização:** Docker e Docker Compose

## Como Executar o Projeto

Siga as instruções abaixo para configurar e executar o projeto em sua máquina local.

### Pré-requisitos

Antes de começar, certifique-se de ter instalado:

*   [Python 3.9+](https://www.python.org/downloads/)
*   [Docker](https://docs.docker.com/get-docker/)
*   [Docker Compose](https://docs.docker.com/compose/install/)

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/ai-teacher.git
    cd ai-teacher
    ```

2.  **Crie o arquivo de ambiente:**
    Crie uma cópia do arquivo `.env.example` e renomeie para `.env`.
    ```bash
    cp .env.example .env
    ```
    Abra o arquivo `.env` e preencha as variáveis de ambiente necessárias:
    *   `EVOLUTION_INSTANCE_NAME`: Nome da sua instância na Evolution API.
    *   `AUTHENTICATION_API_KEY`: Sua chave de API da Evolution API.
    *   `PHONE_NUMBER`: O número de telefone que o bot utilizará.
    *   `OPENAI_API_KEY`: Sua chave de API da OpenAI.

3.  **Instale as dependências Python:**
    É recomendado criar um ambiente virtual.
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

### Executando a Aplicação

1.  **Inicie os serviços com Docker Compose:**
    Este comando irá iniciar os contêineres para a Evolution API, PostgreSQL e Redis.
    ```bash
    docker-compose up -d
    ```

2.  **Inicie a aplicação FastAPI:**
    ```bash
    uvicorn app:app --host 0.0.0.0 --port 8000 --reload
    ```

A aplicação estará disponível em `http://localhost:8000`. Configure o webhook na sua instância da Evolution API para `http://seu-ip-publico:8000/webhook`.