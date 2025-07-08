import pytest
from f1_codex import LevGuard

# Safe model deployment test
@LevGuard(harm_threshold=0.01)
def safe_model(data, simulated_harm=0.005):
    return "Model deployed"

# Unsafe model deployment test
@LevGuard(harm_threshold=0.01)
def unsafe_model(data, simulated_harm=0.02):
    return "Model deployed"

def test_safe_model_deploys():
    assert safe_model("example_data") == "Model deployed"

def test_unsafe_model_blocked():
    with pytest.raises(Exception, match="Harm threshold exceeded"):
        unsafe_model("example_data")
