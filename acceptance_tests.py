import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

from markdown_to_pdf.config import Config


class TestConfigValidation(unittest.TestCase):
    def test_valid_config(self):
        config = Config(
            input_path="input.md",
            output_path="output.pdf"
        )
        self.assertIsInstance(config, Config)

    def test_invalid_config_missing_input(self):
        with self.assertRaises(TypeError):
            Config(output_path="output.pdf")

    def test_invalid_config_missing_output(self):
        with self.assertRaises(TypeError):
            Config(input_path="input.md")

    def test_invalid_config_wrong_type(self):
        with self.assertRaises(TypeError):
            Config(input_path=123, output_path="output.pdf")

    def test_invalid_config_invalid_path(self):
        with self.assertRaises(ValueError):
            Config(input_path="invalid_path", output_path="output.pdf")

    def test_invalid_config_invalid_output(self):
        with self.assertRaises(ValueError):
            Config(input_path="input.md", output_path=123)


class TestConversion(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp()
        self.input_file = os.path.join(self.tmp_dir, "input.md")
        self.output_file = os.path.join(self.tmp_dir, "output.pdf")
        with open(self.input_file, "w") as f:
            f.write("# Hello World\n\nThis is a test.")

    def tearDown(self):
        subprocess.run(["rm", "-rf", self.tmp_dir])

    def test_conversion_success(self):
        # Use the CLI to convert
        result = subprocess.run([
            "python", "-m", "markdown_to_pdf" 
        ], cwd=self.tmp_dir, capture_output=True, text=True)

        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists(self.output_file))


if __name__ == '__main__':
    unittest.main()
