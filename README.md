# chris_moreira_week4_project

# Project Week 4
This project tests multiple versions of python in Github. The main file retrieves the version of Python currently being used and the name of the operating system (OS) on which the script is running. 

# Use Cases 
1. Detecting environment details: The function might be useful in environments like CI/CD pipelines (e.g., GitHub Actions) where you need to detect and log the Python version and the operating system the script is running on.
2. Cross-platform compatibility: By obtaining this information, you can tailor behavior based on the operating system or Python version.

# Test 
test function designed to verify two things: the Python version and the operating system (OS) returned by main_function() are within expected values. 
Python Version Check: The test ensures that the Python version being used is one of the expected versions (3.7 to 3.11).
Operating System Check: The test checks whether the detected operating system (if available) is either "Windows" or "Linux". If no OS is detected (os_name is None), this part of the test is skipped. The test is designed to validate the Python version and operating system to ensure they match specific expected values. This is a basic unit test that checks the environment setup for compatibility.

# Passing Tests Screenshot
![image](https://github.com/user-attachments/assets/b4735c7d-b647-4efc-8d13-22578896aa59)
