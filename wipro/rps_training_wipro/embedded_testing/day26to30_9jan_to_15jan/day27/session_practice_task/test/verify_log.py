# Path to the log file
log_file = "log.txt"

with open(log_file, 'r') as log:
    content = log.read()

# Check for expected output
if "Expected Output" in content:
    print("Test Passed: Output matches expected.")
else:
    print("Test Failed: Output mismatch!")