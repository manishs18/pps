#!/bin/bash

# Step 1: Setup environment
echo "Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Step 2: Install required packages
echo "Installing required packages..."
pip install --upgrade pip > setup.log 2>&1
pip install selenium pytest pytest-html pytest-selenium > setup.log 2>&1

# Step 3: Run test cases and log results
echo "Running test cases on the website..."
pytest --html=report.html --self-contained-html > test_log.log 2>&1

# Step 4: Deactivate the virtual environment
deactivate

echo "Automation completed! Logs are in 'test_log.log', and the report is in 'report.html'."
