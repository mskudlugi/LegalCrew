from crewai import Crew
from crewai.process import Process
from agents import LegalAgents
from tasks import LegalTasks

from dotenv import load_dotenv
load_dotenv()

class LegalCrew:
  def __init__(self, file_path):
    self.file_path = file_path
    
  def run(self):
    agents = LegalAgents(file_path=self.file_path)
    tasks = LegalTasks()

    facts_agent = agents.fact_checker()
    issues_agent = agents.issue_handler()
    holdings_agent = agents.holding_provider()
    rationale_agent = agents.rationale_provider()

    fact_checking_task = tasks.fact_checker(facts_agent)
    issues_task = tasks.issues_checker(issues_agent)
    holdings_task = tasks.holdings_checker(holdings_agent)
    rationale_task = tasks.rationale(rationale_agent)

    crew = Crew(
      agents=[
        facts_agent,
        issues_agent,
        holdings_agent,
        rationale_agent
      ],
      tasks=[
        fact_checking_task,
        issues_task,
        holdings_task,
        rationale_task
      ],
      process=Process.sequential,
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("## Welcome to Legal Analysis Crew")
  print('-------------------------------')
  
  file_path = "Judgement_Triple_Talaq.txt"
  
  legal_crew = LegalCrew(file_path=file_path)
  result = legal_crew.run()
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)
