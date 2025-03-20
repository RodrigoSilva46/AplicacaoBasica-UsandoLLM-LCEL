# README - Projeto de Tradução com LangChain e Groq

## Índice

1. [Introdução](#introducao)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Pré-requisitos](#pre-requisitos)
4. [Instalação](#instalacao)
5. [Explicação do Código](#explicacao-do-codigo)
   - [Importação de Bibliotecas](#importacao-de-bibliotecas)
   - [Carregamento de Variáveis de Ambiente](#carregamento-de-variaveis-de-ambiente)
   - [Criação do Modelo Groq](#criacao-do-modelo-groq)
   - [Criação do Prompt](#criacao-do-prompt)
   - [Parser de Saída](#parser-de-saida)
   - [Criação da Chain](#criacao-da-chain)
   - [Execução da Chain](#execucao-da-chain)
6. [Glossário](#glossario)
7. [Contribuição](#contribuicao)
8. [Licença](#licenca)

---

## 1. Introdução&#x20;

Este projeto tem como objetivo demonstrar o uso da biblioteca LangChain para processamento de linguagem natural utilizando o modelo **Gemma2-9b-It** através da API do **Groq**. O sistema permite traduzir frases de um idioma para outro de forma dinâmica.

---

## 2. Tecnologias Utilizadas&#x20;

- Python 3.10+
- LangChain
- LangChain Groq
- dotenv

---

## 3. Pré-requisitos&#x20;

Antes de rodar o projeto, você precisa ter instalado:

- Python 3.10 ou superior
- Um editor de código (VS Code, PyCharm, etc.)
- Uma conta na Groq e uma chave de API válida

---

## 4. Instalação&#x20;

Para rodar este projeto, siga os passos abaixo:

### Clonar o repositório

### Criar um ambiente virtual (opcional, mas recomendado)

### Instalar as dependências

---

## 5. Explicação do Código&#x20;

### Importação de Bibliotecas&#x20;

Estas bibliotecas são essenciais para criar um modelo de IA interativo:

- `langchain_core.messages`: Lida com mensagens do usuário e do sistema.
- `langchain_core.prompts`: Permite criar templates de prompts.
- `langchain_core.output_parsers`: Formata a saída do modelo.
- `langchain_groq`: Conecta-se ao modelo **Gemma2-9b-It**.
- `dotenv`: Gerencia variáveis de ambiente.
- `os`: Permite acessar variáveis de ambiente.

### Carregamento de Variáveis de Ambiente&#x20;

Aqui carregamos a chave de API do Groq a partir de um arquivo `.env`.

### Criação do Modelo Groq&#x20;

Criamos uma instância do modelo **Gemma2-9b-It**, que será utilizado para gerar respostas baseadas no prompt fornecido.

### Criação do Prompt&#x20;

O template define a estrutura do prompt que será enviado ao modelo.

### Parser de Saída&#x20;

O parser garante que a saída do modelo seja formatada corretamente.

### Criação da Chain&#x20;

Uma **Chain** é uma sequência de operações que incluem o prompt, o modelo de IA e o parser.

### Execução da Chain&#x20;

Este comando executa a Chain e imprime a tradução para o francês da frase **"E aí, beleza?"**.

---

## 6. Glossário&#x20;

- **LLM (Large Language Model)**: Modelo de IA treinado para entender e gerar texto.
- **Prompt**: Entrada fornecida ao modelo para gerar uma resposta.
- **Chain**: Sequência de passos que processam os dados antes de exibi-los.
- **Parser**: Componente que organiza e melhora a saída do modelo.

---

## 7. Contribuição&#x20;

Se quiser contribuir com este projeto:

1. Faça um **fork** do repositório.
2. Crie uma **branch** para sua funcionalidade (`git checkout -b minha-feature`).
3. Faça o commit das suas mudanças (`git commit -m 'Minha nova feature'`).
4. Envie para o repositório (`git push origin minha-feature`).
5. Abra um **Pull Request**.

---

## 8. Licença&#x20;

Este projeto é licenciado sob a **MIT License**. Para mais informações, consulte o arquivo LICENSE.

---

Feito Por Rodrigo Viana Carneiro da Silva

