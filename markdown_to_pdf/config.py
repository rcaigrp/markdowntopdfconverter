from pydantic import BaseModel, Field

class Config(BaseModel):
    input_path: str = Field(..., description="Path to the Markdown file.")
    output_path: str = Field(..., description="Path to the output PDF file.")