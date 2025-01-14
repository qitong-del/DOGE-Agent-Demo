# DOGE-Agent-Demo

### Overivew
This is a test demo of a multiagent tool for searching for areas of
potential automation for DOGE.
** Note: Downgrade python to below 3.12.8 (<=3.12.1 works or >=3.10)

### Specifications
The tool follows the details listed below.
1. DOGE Agent receives input of a user query on a use case. "Can this use case be automated?" ex. "Can I replace data entry at the DMV?"
2. DOGE Agent first takes insight from ELON & VIVEK roles. Elon focuses on technical and future proofing, vivek focused on financial feasibility and healthcare. VIVEK and ELON create tasks for the following personas:

Business Analyst - identifies business value of automation (is it worth it)
Mock User - expresses what they want from the program/automation
Software Engineer - develops POC software/code
AI Engineer - develops AI workflows for software
Data Engineer - develops data pipelines for software and AI
Tech Lead - Identifies how to automate business problem with technology. reviews developed technology, identifies deficiencies and how to fix, delegates work to software + AI + Data engineers. Also identifies timeline to implement this into production. 
Financial Analyst - Reviews tech lead and business analyst's outputs, provides ROI metrics and others to justify pilot/MVP/Prod app
 
3. The personas all work together to identify the business value for a solution, and then if it makes sense to solve the issue with technology, then the Tech Lead directs AI, Data and Software Engineer to build prototype.
 
4. Once prototype is developed, financial analyst develops ROI metrics and then provides info to ELON and VIVEK. 
 
5. Vivek or Elon provide summary to user on the solution, what the code would do, the ROI, and what next steps look like, timeline to get it implemented.
