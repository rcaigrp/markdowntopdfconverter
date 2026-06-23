import unittest
from unittest.mock import patch, MagicMock
import sys
import os

from markdown_to_pdf.utils import install_tesseract


class TestTesseractInstallation(unittest.TestCase):
    """
    Test Tesseract auto-installation with mocked subprocess.
    """

    def test_install_tesseract_windows(self):
        """
        Test installation on Windows via pip.
        """
        with patch('subprocess.run') as mock_run:
            # Mock subprocess.run to return success
            mock_run.side_effect = [
                MagicMock(returncode=0),  # pip install succeeds
            ]
            
            # Mock sys.modules to simulate module import
            original_import = __import__
            def mock_import(name, *args, **kwargs):
                if name == 'pytesseract':
                    return MagicMock()
                return original_import(name, *args, **kwargs)
            
            # Replace __import__ with mock
            sys.modules = {}
            sys.path = []
            
            with patch('__builtins__.__import__', side_effect=mock_import):
                install_tesseract()
                
                # Verify that pytesseract can be imported
                try:
                    import pytesseract
                    self.assertTrue(True, "pytesseract imported successfully")
                except Exception as e:
                    self.fail(f"Failed to import pytesseract: {e}")

    def test_install_tesseract_fallback(self):
        """
        Test fallback to pip on unsupported OS.
        """
        with patch('platform.system', return_value="Windows"),
             patch('subprocess.run') as mock_run:
            mock_run.side_effect = [MagicMock(returncode=0)]
            
            # Mock the actual behavior
            import sys
            original_import = sys.modules.get
            sys.modules = {}
            
            # Mock import
            def mock_import(name, *args, **kwargs):
                if name == 'pytesseract':
                    return MagicMock()
                return original_import(name, *args, **kwargs)
            
            # Test installation
            with patch('__builtins__.__import__', side_effect=mock_import):
                install_tesseract()

if __name__ == '__main__':
    unittest.main()