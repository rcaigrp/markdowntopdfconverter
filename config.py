from pydantic import BaseModel, Field


class Config(BaseModel):
    input_path: str = Field(..., description="Path to the input Markdown file.")
    output_path: str = Field(..., description="Path to the output PDF file.")

    class Config:
        arbitrary_types_allowed = True
