import os
import subprocess

# path to the shell script
script_path = "start_script.sh"

# giving execute permissions
os.chmod(script_path, 0o755)

# run the shell script
subprocess.call(script_path, shell=True)