import os
from dotenv import load_dotenv
from langchain_chroma.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline


load_dotenv()
DB_DIR = os.getenv('DB_DIR')

prompt_template = """
    Responda a pergunta do ususário:
    {question_text}

    com base nessas informações abaixo:
    {knowledge}
"""

def ask_something():
    question_text = str(input("Escreva a pergunta: "))

    # Carregar banco de dados
    embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory=DB_DIR, embedding_function=embeddings_model)

    responses = db.similarity_search_with_relevance_scores(question_text, k=3)
    if len(responses) == 0 or responses[0][1] < 0.7:
        print("Nenhuma informação relevante foi encontrado na base.")
        return
    
    knowledge = "; ".join([response.page_content for response in responses])
    prompt = ChatPromptTemplate.from_template(prompt_template)
    prompt = prompt.invoke(
        {
            "question_text": question_text,
            "knowledge": knowledge
        })

    llm_base = HuggingFacePipeline.from_model_id(
        model_id="all-MiniLM-L6-v2", # Exemplo de modelo
        task="text-generation",
        pipeline_kwargs={"max_new_tokens": 512, "temperature": 0.7},
    )
    chat_model = ChatHuggingFace(llm=llm_base)
    end_response = chat_model.invoke(prompt)
    print(end_response)


if __name__ == "__main__":
    ask_something()
