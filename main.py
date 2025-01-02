#!/usr/bin/env python
import os
import sys
import warnings

sys.path.append("..")
from story_creator.crew import StoryCreator

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'genre': 'Fairy Tale story',
        'style': 'children bedtime story',
        'features': {
            'Hero': 'Innocent and golden heart prince',
            'Heroine': 'Smart and witty princess',
            'Villain': 'Not specific',
            'theme': 'royal affairs and love story',
            'tone': 'Sweet, loving and caring relationship and language should be simple as story for children'
        },
        'NumberOfCharacters': 'not specific',
        'language': 'English'
    }

    StoryCreator().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'genre': 'Fantasy',
        'features': {
            'hero_nature': 'sarcastic and witty',
            'relationships': 'complex family ties and a loyal companion',
            'tone': 'sarcastic'
        },
        'pages': 2
    }
    try:
        StoryCreator().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        StoryCreator().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        StoryCreator().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
