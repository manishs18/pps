# 1. Check the python version installed on your system through commandline. 



import sys

class CheckPythonVersion:
    def __init__(self):
        python_version = sys.version  
        print(f"Python version: {python_version}")

python_version = CheckPythonVersion()


# And by Command Line can find python version

# python --version
