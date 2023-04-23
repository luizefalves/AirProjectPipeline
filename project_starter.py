import os
import subprocess
import webbrowser

# path to the shell script
script_path = "/home/lalves/teste1/start_script.sh"

# giving execute permissions
os.chmod(script_path, 0o755)

# run the shell script
subprocess.call(script_path, shell=True)

url = 'http://localhost:8081'
webbrowser.open(url)