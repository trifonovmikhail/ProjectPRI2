from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

MODEL_NAME = "s-nlp/russian_toxicity_classifier"

class ToxicityClassifier:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

    def predict(self, text: str) -> float:
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
            probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        return probs[0][1].item()