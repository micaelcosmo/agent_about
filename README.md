```markdown
# Agent About 🤖

Este projeto é um agente de inteligência artificial especializado em processamento de documentos (RAG - Retrieval-Augmented Generation). Ele utiliza uma arquitetura moderna para ler arquivos PDF, transformá-los em vetores e permitir consultas inteligentes baseadas no conteúdo desses documentos.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **LangChain**: Framework para orquestração da lógica de LLM e dados.
- **ChromaDB**: Banco de dados vetorial para armazenamento e busca de alta performance.
- **HuggingFace (Embeddings)**: Utilização do modelo `all-MiniLM-L6-v2` para processamento local de linguagem natural.
- **Python-dotenv**: Gerenciamento de variáveis de ambiente.

## 🚀 Funcionalidades

- **Carga de Documentos**: Leitura automatizada de múltiplos PDFs em um diretório configurável.
- **Processamento de Texto**: Divisão inteligente de documentos em chunks (`RecursiveCharacterTextSplitter`) para otimizar o contexto da IA.
- **Vetorização**: Geração de embeddings e persistência automática em banco vetorial local.
- **Busca Semântica**: Preparado para responder perguntas baseadas estritamente nos dados carregados.

## 📋 Pré-requisitos

- Python 3.10 ou superior
- Pip (gerenciador de pacotes)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone [https://github.com/micaelcosmo/agent_about.git](https://github.com/micaelcosmo/agent_about.git)
cd agent_about

```

2. Crie um ambiente virtual e ative-o:

```bash
python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

```

3. Instale as dependências:

```bash
pip install -r requirements.txt

```

4. Configure as variáveis de ambiente:
Crie um arquivo `.env` na raiz do projeto com as seguintes chaves:

```env
BASE_DIR="caminho/para/seus/pdfs"
DB_DIR="caminho/para/salvar/o/banco"
HF_TOKEN="seu_token_huggingface_opcional"

```

## 📖 Como Usar

Para inicializar o banco de dados vetorial com seus documentos:

```bash
python main.py

```

O script irá processar os PDFs do seu `BASE_DIR`, criar os embeddings e salvar o banco pronto para consulta no `DB_DIR`.

## 📂 Estrutura do Projeto

* `main.py`: Script principal contendo o fluxo de ETL (Extract, Transform, Load) dos documentos.
* `schema.py`: Definições de estruturas de dados e contratos do sistema.
* `requirements.txt`: Lista de dependências do projeto.
* `.env`: Configurações sensíveis e caminhos de diretório (não versionado).

## ✒️ Autor

**Micael Cosmo** - [GitHub](https://github.com/micaelcosmo)
