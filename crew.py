from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

import os

openai_api_key = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4'


# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class StoryCreator():
	"""StoryCreator crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def character_generator(self) -> Agent:
		return Agent(
			config=self.agents_config['character_generator'],
			allow_delegation=False,
			verbose=True
		)

	@agent
	def plot_heading_generator(self) -> Agent:
		return Agent(
			config=self.agents_config['plot_heading_generator'],
			allow_delegation=False,
			verbose=True
		)

	@agent
	def story_generator(self) -> Agent:
		return Agent(
			config=self.agents_config['story_generator'],
			allow_delegation=False,
			verbose=True
		)

	@agent
	def formatter(self) -> Agent:
		return Agent(
			config=self.agents_config['formatter'],
			allow_delegation=False,
			verbose=True
		)


	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def character_generation_task(self) -> Task:
		return Task(
			config=self.tasks_config['character_generation_task'],
		)

	@task
	def plot_heading_generation_task(self) -> Task:
		return Task(
			config=self.tasks_config['plot_heading_generation_task'],
		)

	@task
	def story_generation_task(self) -> Task:
		return Task(
			config=self.tasks_config['story_generation_task'],
			output_file='story_draft.md'
		)

	@task
	def story_formatting_task(self) -> Task:
		return Task(
			config=self.tasks_config['story_formatting_task'],
			output_file='final_story.md'
		)


	@crew
	def crew(self) -> Crew:
		"""Creates the StoryGenerator crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=[
				self.character_generator(),
				self.plot_heading_generator(),
				self.story_generator(),
				self.formatter(),
			],  # Automatically created by the @agent decorator
			tasks=[
				self.character_generation_task(),
				self.plot_heading_generation_task(),
				self.story_generation_task(),
				self.story_formatting_task(),
			],  # Automatically created by the @task decorator
			process=Process.sequential,  # Executes tasks in a step-by-step sequence
			verbose=True,
			# process=Process.hierarchical, # Use this for more complex task hierarchies
		)

