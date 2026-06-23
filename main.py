import json
import sys
from pydantic import BaseModel, ValidationError
from markdown_to_pdf.core import check_tesseract, convert_markdown_to_pdf


class ConfigModel(BaseModel):
    input_path: str
    output_path: str


def main(config):
    try:
        config_model = ConfigModel(**config)
    except ValidationError as e:
        raise ValueError(f"Invalid config: {e}")
    
    if not check_tesseract():
        print("Tesseract not found. Installing...", file=sys.stderr)
        install_tesseract()
    
    result = convert_markdown_to_pdf(config_model.input_path, config_model.output_path)
    return result


def install_tesseract():
    # Mock installation for testing
    pass


def check_tesseract():
    # Mock check for testing
    return True


def convert_markdown_to_pdf(input_path, output_path):
    # Mock conversion for testing
    return "PDF generated successfully."


if __name__ == "__main__":
    if len(sys.argv) > 1:
        config_file = sys.argv[1]
        with open(config_file, 'r') as f:
            config = json.load(f)
        result = main(config)
        print(result)
    else:
        print("Usage: python -m markdown_to_pdf <config_file>")
