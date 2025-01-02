from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

import os

openai_api_key = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4'

@CrewBase
class StoryCreator():
	"""StoryCreator crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

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

	@agent
	def translator(self) -> Agent:
		return Agent(
			config=self.agents_config['translator'],
			allow_delegation=False,
			verbose=True
		)


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

	@task
	def story_translation_task(self) -> Task:
		return Task(
			config=self.tasks_config['story_translation_task'],
			output_file='translated_story.md'
		)



	@crew
	def crew(self) -> Crew:
		"""Creates the StoryGenerator crew"""

		return Crew(
			agents=[
				self.character_generator(),
				self.plot_heading_generator(),
				self.story_generator(),
				self.formatter(),
				self.translator(),
			],  
			tasks=[
				self.character_generation_task(),
				self.plot_heading_generation_task(),
				self.story_generation_task(),
				self.story_formatting_task(),
				self.story_translation_task()
			],  
			process=Process.sequential,  
			verbose=True,
		)

