from pydantic import BaseModel, Field, ValidationError

class MarkdownToPdfConfig(BaseModel):
    input_path: str = Field(..., description="Path to input Markdown file")
    output_path: str = Field(..., description="Path to output PDF file")
    tesseract_path: str = Field("tesseract", description="Path to Tesseract executable (optional)")

    class Config:
        extra = "ignore"  # Allow extra fields in config
