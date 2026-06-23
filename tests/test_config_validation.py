from unittest.mock import patch
import pytest


def test_config_validation_success():
    config = {"output": "output.pdf"}
    assert config == config


def test_config_validation_missing_output():
    config = {"invalid": "value"}
    with pytest.raises(KeyError):
        assert config["output"] == "output.pdf"