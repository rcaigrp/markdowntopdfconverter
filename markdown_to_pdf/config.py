from pydantic import BaseModel, Field, validator


class MarkdownToPDFConfig(BaseModel):
    input_path: str = Field(..., description="Path to the input Markdown file.")
    output_path: str = Field(..., description="Path to the output PDF file.")
    tesseract_path: str = Field("tesseract", description="Path to the Tesseract executable. Auto-detected on Linux/macOS.")

    @validator('tesseract_path')
    def validate_tesseract_path(cls, v):
        if not v:
            raise ValueError('Tesseract path must be provided.')
        return v