import os
import subprocess
from typing import Optional

from markdown_to_pdf.config import MarkdownToPdfConfig


def has_tesseract() -> bool:
    """Auto-detect if Tesseract is installed."""
    try:
        result = subprocess.run([
            "tesseract",
            "--version",
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def validate_config(config_dict: dict) -> MarkdownToPdfConfig:
    """Validate config using Pydantic."""
    try:
        return MarkdownToPdfConfig(**config_dict)
    except ValidationError as e:
        raise ValueError(f"Invalid config: {e}")


def convert_markdown_to_pdf(input_path: str, output_path: str) -> None:
    """Convert Markdown to PDF using reportlab."""
    # Placeholder logic — actual implementation will follow
    pass
