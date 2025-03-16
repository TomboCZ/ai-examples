import sys
import os

# This setup ensures that we can import modules from ai_core and utils directories
# regardless of where the script is run from. It solves issues with relative imports
# and allows for consistent module imports across the project.

def setup_paths():
    # Get absolute path to project root directory
    project_root = os.path.abspath(os.path.dirname(__file__))

    # Add ai_core and utils folders to Python's import path
    for folder in ["ai_core", "utils"]:
        path = os.path.join(project_root, folder)
        if path not in sys.path:
            sys.path.insert(0, path)

# Run setup when this file is imported
setup_paths()
