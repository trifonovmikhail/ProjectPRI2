import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.predictor import get_toxicity_score

def test_toxicity_prediction():
    score = get_toxicity_score("Ты ужасный человек!")
    assert isinstance(score, float)
    assert 0.0 <= score <= 1.0

def test_empty_text():
    with pytest.raises(Exception):
        get_toxicity_score("")