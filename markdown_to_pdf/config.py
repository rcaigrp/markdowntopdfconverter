from pydantic import BaseModel, Field, ValidationError


class Config(BaseModel):
    output_path: str = Field(..., description="Path to output PDF file")
    font_size: int = Field(12, description="Font size for PDF")
    tesseract_path: str = Field(..., description="Path to Tesseract executable (optional)")

    class Config:
        schema_extra = {
            "example": {
                "output_path": "output.pdf",
                "font_size": 12,
                "tesseract_path": "/usr/bin/tesseract"
            }
        }

    @classmethod
    def load(cls, config_path: str):
        try:
            import json
            with open(config_path, 'r') as f:
                data = json.load(f)
            return cls(**data)
        except FileNotFoundError:
            raise ValidationError("Config file not found: " + config_path)
        except json.JSONDecodeError:
            raise ValidationError("Invalid JSON in config file")
        except ValidationError as e:
            raise ValidationError(f"Config validation error: {str(e)}")

    @classmethod
    def default(cls):
        return cls(
            output_path="output.pdf",
            font_size=12,
            tesseract_path=""  # empty = auto-detect
        )