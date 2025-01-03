
from transformers import pipeline

class Translator:
    def __init__(self, model_name="Helsinki-NLP/opus-mt-en-de"):
        # Initialize the translation pipeline
        self.pipe = pipeline("translation", model=model_name)

    def translate(self, text):
        # Use the pipeline to translate the input text
        result = self.pipe(text)
        return result[0]['translation_text']
