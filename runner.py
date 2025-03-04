import subprocess
import os

# Define the base directories for Blue and Red scripts
blue_directory = "C:/Users/nsluser/Desktop/Match-Schedule/Blue"
red_directory = "C:/Users/nsluser/Desktop/Match-Schedule/Red"

# Define the directory where JSON files will be stored
json_directory = "C:/Users/nsluser/Desktop/Match-Schedule/JSON"
os.makedirs(json_directory, exist_ok=True)

# Blue script list
blue_scripts = [
    "BlueOne.py",
    "BlueTwo.py",
    "BlueThree.py",
    "BlueSub.py"
]

# Red script list
red_scripts = [
    "RedOne.py",
    "RedTwo.py",
    "RedThree.py",
    "RedSub.py"
]

# Run Blue scripts
for script in blue_scripts:
    script_path = os.path.join(blue_directory, script)
    
    if os.path.exists(script_path):
        print(f"Running {script} from Blue folder...")
        try:
            subprocess.run(["python", script_path, json_directory], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running {script} from Blue folder: {e}")
    else:
        print(f"Error: {script_path} not found in Blue folder!")

# Run Red scripts
for script in red_scripts:
    script_path = os.path.join(red_directory, script)
    
    if os.path.exists(script_path):
        print(f"Running {script} from Red folder...")
        try:
            subprocess.run(["python", script_path, json_directory], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running {script} from Red folder: {e}")
    else:
        print(f"Error: {script_path} not found in Red folder!")
