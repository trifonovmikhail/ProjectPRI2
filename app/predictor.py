from .model import ToxicityClassifier

classifier = ToxicityClassifier()

def get_toxicity_score(text: str) -> float:
    if not text.strip():  # если текст пустой
        raise ValueError("Текст не может быть пустым")
    return classifier.predict(text)