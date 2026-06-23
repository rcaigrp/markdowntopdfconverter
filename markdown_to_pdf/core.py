import json
import os
import subprocess
import sys
from typing import Optional

from pydantic import BaseModel, ValidationError


class ConfigSchema(BaseModel):
    input_path: str
    output_path: str


def validate_config(config_file_path: str) -> ConfigSchema:
    """
    Validate config file using Pydantic.
    """
    try:
        with open(config_file_path, 'r') as f:
            config_data = json.load(f)
        # Validate using the model
        config = ConfigSchema(**config_data)
        return config
    except FileNotFoundError:
        raise ValueError("Config file not found.")
    except ValidationError as e:
        raise ValueError(f"Config validation failed: {e}")


def detect_tesseract() -> Optional[str]:
    """
    Detect Tesseract installation and return path or None if not found.
    """
    try:
        result = subprocess.run(['tesseract', '--version'], capture_output=True, text=True, check=True)
        return 'tesseract'
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def install_tesseract(platform: str) -> None:
    """
    Install Tesseract based on platform.
    """
    if platform == 'linux':
        print("Tesseract not found. Installing via apt...")
        try:
            subprocess.run(['apt-get', 'update'], check=True)
            subprocess.run(['apt-get', 'install', '-y', 'tesseract-ocr'], check=True)
        except subprocess.CalledProcessError:
            raise RuntimeError("Failed to install Tesseract on Linux.")
    elif platform == 'darwin':
        print("Tesseract not found. Installing via Homebrew...")
        try:
            subprocess.run(['brew', 'install', 'tesseract'], check=True)
        except subprocess.CalledProcessError:
            raise RuntimeError("Failed to install Tesseract on macOS.")
    else:
        print("Tesseract not found. Please install manually.")


def check_tesseract_and_install(platform: str) -> str:
    """
    Check for Tesseract and install if missing.
    """
    tesseract_path = detect_tesseract()
    if tesseract_path is None:
        install_tesseract(platform)
        tesseract_path = detect_tesseract()
        if tesseract_path is None:
            raise ValueError("Failed to detect Tesseract after installation.")
    return tesseract_path