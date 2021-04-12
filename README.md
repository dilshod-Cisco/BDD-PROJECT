# Installation of packages
# create virtual environment using terminal type this command:-->  python -m venv .venv

>>> python3 -m venv .projvenv/
>>> pip install -r requirements.txt

# Note: if any problems with environment you can remove (rm -r .projvenv), then repeat the process to recreate.

## Project structure


- pip install pytest, pytest-bdd, selenium
  BDD project structure:
  -pip list
  -test - package
  - base - package (directory needs to have __init__.py emty file)
    - test - package
    -page - package
      - feature - package
      - step_definitions - package
      
    - utilities  - package
  - configfiles - packages
  - screenshots
  - reports 
    
- 
  - pip uninstall packagename
    
  -pip install behave ('u can use cmd) 
  - adding first time cucumberTool for GherkinLanguage on pycharm python
  - first CTRL+ALT+S go to Plugin
  - Market Place search cucumber and Install and Apply. You Welcome ^_* 
- Execution script: python -m pytest -v -s