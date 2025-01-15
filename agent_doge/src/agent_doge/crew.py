from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class AgentDoge():
	"""AgentDoge crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	# @agent
	# def researcher(self) -> Agent:
	# 	return Agent(
	# 		config=self.agents_config['researcher'],
	# 		verbose=True
	# 	)

	# @agent
	# def reporting_analyst(self) -> Agent:
	# 	return Agent(
	# 		config=self.agents_config['reporting_analyst'],
	# 		verbose=True
	# 	)

	@agent
	def business_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['business_analyst'],
			verbose=True
		)

	@agent
	def mock_user(self) -> Agent:
		return Agent(
			config=self.agents_config['mock_user'],
			verbose=True
		)
	
	@agent
	def software_engineer(self) -> Agent:
		return Agent(
			config=self.agents_config['software_engineer'],
			verbose=True
		)
	
	@agent
	def ai_engineer(self) -> Agent:
		return Agent(
			config=self.agents_config['ai_engineer'],
			verbose=True
		)
	
	@agent
	def data_engineer(self) -> Agent:
		return Agent(
			config=self.agents_config['data_engineer'],
			verbose=True
		)
	
	@agent
	def tech_lead(self) -> Agent:
		return Agent(
			config=self.agents_config['tech_lead'],
			verbose=True
		)
	
	@agent
	def financial_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['financial_analyst'],
			verbose=True
		)
	
	@agent
	def elon(self) -> Agent:
		return Agent(
			config=self.agents_config['elon'],
			verbose=True
		)
	
	@agent
	def vivek(self) -> Agent:
		return Agent(
			config=self.agents_config['vivek'],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	# @task
	# def research_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['research_task'],
	# 	)

	# @task
	# def reporting_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['reporting_task'],
	# 		output_file='report.md'
	# 	)

	@task
	def business_value_task(self) -> Task:
		return Task(
			config=self.tasks_config['business_value_task'],
		)

	@task
	def user_requirements_task(self) -> Task:
		return Task(
			config=self.tasks_config['user_requirements_task'],
		)
	
	@task
	def poc_development_task(self) -> Task:
		return Task(
			config=self.tasks_config['poc_development_task'],
		)
	
	@task
	def ai_workflow_task(self) -> Task:
		return Task(
			config=self.tasks_config['ai_workflow_task'],
		)
	
	@task
	def data_pipeline_task(self) -> Task:
		return Task(
			config=self.tasks_config['data_pipeline_task'],
		)
	
	@task
	def tech_review_task(self) -> Task:
		return Task(
			config=self.tasks_config['tech_review_task'],
		)
	
	@task
	def roi_metrics_task(self) -> Task:
		return Task(
			config=self.tasks_config['roi_metrics_task'],
		)
	
	@task
	def summary_task(self) -> Task:
		return Task(
			config=self.tasks_config['summary_task'],
			output_file='summary.md'
		)
	
	@crew
	def crew(self) -> Crew:
		"""Creates the AgentDoge crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
