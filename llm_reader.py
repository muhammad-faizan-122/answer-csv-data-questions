from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from dotenv import load_dotenv
import os


load_dotenv()

class CSV_READER():
    def __init__(self, user_query) -> None:
        self.llm_response = self.run_csv_agent(user_query)

    def load_llm(self):        
        llm = ChatOpenAI(
            temperature=os.getenv("TEMPERATURE"),
            model=os.getenv("MODEL"),
            api_key=os.getenv('OPENAI_API_KEY')
            )
        return llm
        
    def run_csv_agent(self, user_query):
        llm =  self.load_llm()
        agent = create_csv_agent(
            llm,
            os.getenv("USER_CSV_DATA"),
            verbose=False,
            agent_type=AgentType.OPENAI_FUNCTIONS,
        )
        self.llm_response  = agent.run(user_query)
        return self.llm_response


        
