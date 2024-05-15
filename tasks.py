from crewai import Task
from textwrap import dedent

class LegalTasks():
  def fact_checker(self, agent):
    return Task(description=dedent(f"""
        Briefly summarize the facts of the case.  Facts are the 
        “who, when, what, where, and why” of the case.  Describe
        the history of the dispute, including the events that led 
        to the lawsuit, the legal claims and defenses of each party, 
        and what happened in the trial court.  Do not merely copy the 
        facts verbatim; not every detail is important.  Instead, 
        include only the relevant facts.  To decide which facts are relevant, 
        ask yourself whether a particular fact was important to the 
        court’s decision.  If the answer is yes, include that fact in your brief.  
        Also check whether the court’s decision may have been 
        different if a particular fact was omitted or changed.  
        If so, then it is important.  Also look for facts that 
        are repeated at least once in the court’s opinion since these tend to be
        legally relevant. 
      """),
                expected_output="Summary of the facts",
      agent=agent
    )
    
  def issues_checker(self, agent): 
    return Task(description=dedent(f"""
        The issue is a statement of the question of law that the court must
        answer in order to decide which party should win.  A case may involve 
        more than one issue.  Sometimes the court will directly state the issue
        in the opinion.  If so, then quote the court’s statement of the
        issue in the brief.  In most cases, however, you will need to write your 
        own statement of the issue.  The issue should be expressed in the form 
        of a question that can be answered “yes” or “no”.  To ensure that your 
        issue statements are written in the form of a question, begin them with
        “whether,” “did,” “can,” “does,” “is,” etc. 
      """),
                expected_output="Summary of the issues",
      agent=agent
    )

  def holdings_checker(self, agent):
    return Task(description=dedent(f""" 
        The holding is the answer to the issue.  If there are multiple issues, 
        then state a holding for each issue.  The holding succinctly
        states the court’s ultimate conclusion, but does not fully explain the conclusion.
        Write the holding as a single sentence that begins with “yes” or “no,” followed
        by the word “because.”  Doing this will ensure that you directly answer the 
        issue and provide a brief reason for the court’s conclusion.         
      """),
                expected_output="Summary of the holdings generated",
      agent=agent
    )

  def rationale(self, agent):
    return Task(description=dedent(f"""
        The court must justify its holding by providing reasons for answering 
        the issue in the way that it did. The rationale is a summary of the 
        reasons that explain how the court reached its decision. The goal for 
        this part of your brief is to understand how the court used the rules 
        of law to resolve the dispute. The court will state the applicable rules 
        of law, and they can be found in readings from your textbook as well.  
        You should summarize how the court applied the rules to the facts to reach its
        conclusions
      """),
                expected_output="Summary of the rationale generated",
      agent=agent
    )

