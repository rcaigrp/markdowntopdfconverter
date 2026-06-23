import os
import platform
import subprocess
from typing import Optional

def detect_tesseract() -> bool:
    """Detect if Tesseract is installed and accessible."""
    system = platform.system()
    try:
        if system == "Darwin":  # macOS
            result = subprocess.run([
                "brew", "list", "tesseract"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return "tesseract" in result.stdout
        elif system == "Linux":
            # Use 'which' to detect tesseract
            result = subprocess.run([
                "which", "tesseract"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return "tesseract" in result.stdout
        else:
            return False
    except Exception:
        return False

def install_tesseract() -> bool:
    """Install Tesseract using platform-specific package manager."""
    system = platform.system()
    try:
        if system == "Darwin":  # macOS
            subprocess.run([
                "brew", "install", "tesseract"], check=True)
            return True
        elif system == "Linux":
            subprocess.run([
                "sudo", "apt-get", "install", "-y", "tesseract-ocr"], check=True)
            return True
        else:
            print("Tesseract not supported on this platform.")
            return False
    except Exception as e:
        print(f"Failed to install Tesseract: {e}")
        return False

def ensure_tesseract_installed() -> bool:
    """Ensure Tesseract is installed and accessible."""
    if detect_tesseract():
        return True
    else:
        print("Tesseract not detected. Installing...")
        if install_tesseract():
            return True
        else:
            print("Failed to install Tesseract. Please install manually.")
            return False

def validate_config(config_dict: dict) -> dict:
    """Validate config using Pydantic."""
    from markdown_to_pdf.config import Config
    try:
        validated = Config.model_validate(config_dict)
        return validated
    except Exception as e:
        print(f"Config validation failed: {e}")
        raise e
