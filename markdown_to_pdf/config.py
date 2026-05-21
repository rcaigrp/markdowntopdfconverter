"""Configuration file handler for markdown to PDF converter."""
import json

def load_config(config_path):
    """Load configuration from JSON file.
    
    Args:
        config_path: Path to the config JSON file
        
    Returns:
        dict: Configuration dictionary with input/output paths
    """
    with open(config_path, 'r') as f:
        return json.load(f)
