#IMPORTAÇÃO DE BIBLIOTECAS
from langchain_core.messages import HumanMessage, SystemMessage # MENSAGENS DO USUÁRIO E DO SISTEMA
from langchain_core.prompts import ChatPromptTemplate # PROMPT TEMPLATE
from langchain_core.output_parsers import StrOutputParser # PARSER DE SAÍDA
from langchain_groq import ChatGroq # MODELO DE LLM
from dotenv import load_dotenv, find_dotenv # CARREGAMENTO DE VARIÁVEIS DE AMBIENTE
import os # BIBLIOTECA DE SISTEMA

#CARREGAMENTO DE VARIÁVEIS DE AMBIENTE
load_dotenv(find_dotenv()) # CARREGAR VARIÁVEIS DE AMBIENTE
groq_api_key = os.getenv("GROQ_API_KEY") # CHAVE DE API DO GROQ

#CRIAR O MODELO GROQ
llm = ChatGroq(
    model = "Gemma2-9b-It", # MODELO DE LLM UTILIZADO
    groq_api_key = groq_api_key, # CHAVE DE API DO GROQ
)

#CRIAR O PROMPT ** ESTUDAR SOBRE PROMPT ENGINEERING (FEW-SHOT, ZERO-SHOT, ONE-SHOT, CHAIN OF THOUGHTS)
#messages = [
 #   SystemMessage(content="Translate the following sentence from English to French"),
  #  HumanMessage(content="Hello, how are you?")
#]

#PARSER DE SAÍDA: ISSO É NECESSARIO PARA QUE O SISTEMA ENTENDA A SAÍDA DO MODELO (MELHORIA DA SAÍDA)
parser = StrOutputParser() # PARSER DE SAÍDA

#Prompt Template: Usando LCEL - Chain the Components
generic_template = "Traduza a seguinte frase {language}" # TEMPLATE GENÉRICO

prompt = ChatPromptTemplate.from_messages( # CRIAR O PROMPT
    [
        ('system', generic_template), # MENSAGEM DO SISTEMA
        ('user', "{text}") # MENSAGEM DO USUÁRIO
    ]
)

#O QUE É UMA CHAIN?
#Uma cadeia é uma sequência de mensagens que são enviadas e recebidas entre o usuário e o sistema.
#O sistema envia uma mensagem, o usuário responde, o sistema responde, o usuário responde, e assim por diante.

chain = prompt | llm | parser # CRIAR A CHAIN

#EXECUTAR A CHAIN
print(chain.invoke({'language': 'French', 'text': 'E ai beleza?'})) 