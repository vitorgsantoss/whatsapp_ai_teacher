# AI Teacher Bot

Este projeto é um bot de WhatsApp integrado com a API da OpenAI, projetado para ajudar usuários a aprender e praticar inglês de forma interativa.

## Funcionalidades

O bot é um tutor de inglês pessoal que fornece:

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

*   [Python 3.11+](https://www.python.org/downloads/)
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


### Executando a Aplicação

1.  **Inicie os serviços com Docker Compose:**
    Este comando irá iniciar os contêineres para a Evolution API, PostgreSQL e Redis.
    ```bash
    docker compose up --build
    ```
2. **Crie a instancia do Evolution-API:**
    *   Acesse: [Evolution API](http://localhost:8080/manager/)

    *   Crie a instancia do Evolution utilizando Baileys como Channel e informando o seu número de telefone.
    *   Conecte no seu WhatsApp através do QRCode.

3. **Configure o webhook:**
    *   Acesse as configurações da instância clicando na engrenagem presente no painel.
    *   Acesse events/webhook no painel lateral.
    *   Ative o webhook.
    *   Altere a URL do webhook para http://bot:8000/webhook/.
    *   Ative MESSAGE_UPSERT e salve as configurações.

O agente estará disponível no seu WhatsApp, basta enviar uma mensagem para o seu próprio número.