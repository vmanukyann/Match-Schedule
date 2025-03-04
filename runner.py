import subprocess
import os

# Define the directory where the Python scripts are located (no more Blue and Red folders)
scripts_directory = "C:/Users/nsluser/Desktop/Match-Schedule"

# Define the directory where JSON files will be stored
json_directory = "C:/Users/nsluser/Desktop/Match-Schedule/JSON"
os.makedirs(json_directory, exist_ok=True)

# List all the scripts (Blue and Red combined, since no more folders)
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

# Run all scripts and create a separate JSON file for each
for script in scripts:
    script_path = os.path.join(scripts_directory, script)
    
    if os.path.exists(script_path):
        print(f"Running {script}...")
        json_output_path = os.path.join(json_directory, f"{script.replace('.py', '.json')}")
        
        try:
            # Run the script and pass the JSON output path
            subprocess.run(["python", script_path, json_output_path], check=True)
            print(f"{script} completed successfully and saved to {json_output_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error running {script}: {e}")
    else:
        print(f"Error: {script_path} not found!")
