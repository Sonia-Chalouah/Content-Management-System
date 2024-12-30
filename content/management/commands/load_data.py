import os
import json
from django.core.management.base import BaseCommand
from content.models import WordPhrase

class Command(BaseCommand):
    help = 'Load initial data from JSON'

    def handle(self, *args, **kwargs):
        # Get the absolute path to the project root directory
        project_root = os.path.abspath(os.path.dirname(__file__) + "/../../../")  # Adjust path to project root
        json_path = os.path.join(project_root, 'data.json')  # Construct the full path to data.json

        # Debugging: Print the JSON path
        print(f"Looking for JSON file at: {json_path}")

        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for entry in data:
                    WordPhrase.objects.create(
                        word_phrase=entry.get("wordFirstLang"),
                        translation=entry.get("wordSecondLang"),
                        example_sentence=entry.get("sentenceFirstLang", "")
                    )
            self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))
