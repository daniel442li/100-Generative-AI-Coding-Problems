import questionary
import os
from junior_dev import run_test
custom_style_fancy = questionary.Style([
    ('qmark', 'fg:#e770ff bold'),       # token in front of the question
    ('question', 'bold'),               # question text
    ('answer', 'fg:#e770ff bold'),      # submitted answer text behind the question
    ('pointer', 'fg:#e770ff bold'),     # pointer used in select and checkbox prompts
    ('highlighted', 'fg:#e770ff bold'), # pointed-at choice in select and checkbox prompts
    ('selected', 'fg:#e770ff'),         # style for a selected item of a checkbox
    ('separator', 'fg:#e770ff'),        # separator in lists
    ('instruction', ''),                # user instructions for select, rawselect, checkbox
    ('text', ''),                       # plain text
    ('disabled', 'fg:#e770ff italic')   # disabled choices for select and checkbox prompts
])  

def get_json_filenames(path):
    json_filenames = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.json'):
                json_filenames.append(file)  # Append only the file name
    return json_filenames

json_filenames = get_json_filenames('tests')

menu = questionary.select(
            "Select Test Suite", style = custom_style_fancy,
            choices=json_filenames).ask()

questionary.print("Running LLM Testing Suite :-)", style = "bold italic fg:darkred")

run_test(menu)