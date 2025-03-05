import subprocess
import os

# Get the current directory where the script is running
scripts_directory = os.path.dirname(os.path.abspath(__file__))

# Define the directory where JSON files will be stored
json_directory = os.path.join(scripts_directory, "JSON")
os.makedirs(json_directory, exist_ok=True)

# List all Python scripts in the directory (excluding this runner script)
scripts = [f for f in os.listdir(scripts_directory) if f.endswith(".py") and f != "runner.py"]

# Run all scripts and create a separate JSON file for each
for script in scripts:
    script_path = os.path.join(scripts_directory, script)
    json_output_path = os.path.join(json_directory, f"{script.replace('.py', '.json')}")

    print(f"Running {script}...")

    try:
        # Run the script and pass the JSON output path as an argument
        subprocess.run(["python", script_path, json_output_path], check=True)
        print(f"{script} completed successfully and saved to {json_output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script}: {e}")
