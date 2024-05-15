from crewai import Agent
from crewai_tools import FileReadTool
from langchain_community.llms import HuggingFaceHub

llm = HuggingFaceHub(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    huggingfacehub_api_token="",
    task="text-generation",
)

class LegalAgents():
  def __init__(self, file_path):
    self.file_path = file_path
    self.file_reader = FileReadTool(file_path=self.file_path.encode('utf-8'))
  
  def fact_checker(self):
    return Agent(
      role='The Best Fact Checker',
      goal="""Being the best at gather, interpret data and amaze
      your customer with it""",
      backstory="""The most seasoned legal fact checker with 
      lots of expertise in sifting through legal documents looking for facts
      that is working for a super important customer.""",
      llm=llm,
      verbose=True,
      tools=[self.file_reader]
    )

  def issue_handler(self):
    return Agent(
      role='Issue Handling Analyst',
      goal="""Report the issue mentioned in the legal document""",
      backstory="""Known as the BEST issues reporter, you're
      skilled in sifting through legal documents, reporting the issues mentioned in it.
      Now you're working on a super important customer""",
      llm=llm,
      verbose=True,
      tools=[self.file_reader]
  )

  def holding_provider(self):
    return Agent(
      role='Holding provider',
      goal="""Report the answer to the issue succinctly. """,
      backstory="""You're the most experienced holding provider
      and you combine various analytical insights to formulate
      the answer to the issue reported. You are now working for
      a super important customer you need to impress.""",
      llm=llm,
      verbose=True,
      tools=[self.file_reader]
    )
    
  def rationale_provider(self):
    return Agent(
      role='Rationale provider',
      goal="""Report the rationale behind the judgement based
      on the previous tasks.""",
      backstory="""You're the most experienced rationale provider
      and you combine various analytical insights to formulate
      and summarize the rationale of the judgement. You are now working for
      a super important customer you need to impress.""",
      llm=llm,
      verbose=True,
      tools=[self.file_reader]
    )