from pydantic import BaseModel, ValidationError

class ConfigSchema(BaseModel):
    input_path: str
    output_path: str

    class Config:
        extra = "ignore"  # Allow extra fields if needed


def validate_config(config_dict: dict) -> ConfigSchema:
    """Validate config dictionary against schema."""
    try:
        return ConfigSchema(**config_dict)
    except ValidationError as e:
        raise ValueError(f"Config validation failed: {e}")