import subprocess
import os

# Define the base directory where the scripts are located
script_directory = "C:/Users/nsluser/Desktop/Match-Schedule"

# Define the directory where JSON files will be stored
json_directory = os.path.join(script_directory, "JSON")

# Ensure the JSON directory exists
os.makedirs(json_directory, exist_ok=True)

# List of script filenames (corrected with BlueSub.py and RedSub.py)
scripts = [
    "BlueOne.py",
    "BlueTwo.py",
    "BlueThree.py",
    "BlueSub.py",
    "RedOne.py",
    "RedTwo.py",
    "RedThree.py",
    "RedSub.py"
]

# Run each script with the correct full path
for script in scripts:
    script_path = os.path.join(script_directory, script)
    
    if os.path.exists(script_path):
        print(f"Running {script}...")
        try:
            subprocess.run(["python", script_path, json_directory], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running {script}: {e}")
    else:
        print(f"Error: {script_path} not found!")
