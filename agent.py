import psutil # System information
import requests # Sending data to api
import time # for scheduling
import platform # for system information
import socket # for network information
import subprocess # for executing commands

# Define the django api url
api_url = "http://127.0.0.1:8000/systeminfo/"   

# Creating a class for the agent
class SystemAgent:

    def __init__(self):
        self.system = platform.system() # OS name
        self.node = platform.node() # Network name
        self.machine = platform.machine() # Machine type
        self.ip_address = socket.gethostbyname(self.node) # IP address

    # RAM information
    def get_ram_info(self):
        return psutil.virtual_memory().total # Memory usage and total memory

    # Internet connection
    def internet_connection(self):
        try:
            requests.head("https://google.com/", timeout=5) # Use head method instead of get to save bandwidth and time
            return True
        except requests.ConnectionError:
            return False 

    # Get installed apps
    def get_installed_apps(self):
        if self.system == 'Windows': # if OS is Windows
            command = 'wmic product get name' # get installed apps
        elif self.system == 'Linux': # if OS is Linux
            command = 'apt list --installed' # get installed apps
        else:
            return None # not for other OS

        output = subprocess.check_output(command, shell=True) # executing command
        output = output.decode('utf-8') # decoding output
        output = output.split('\n', 1)[1] # split the output in new line and skip the first element which is not an app name
        installed_apps = [app.strip() for app in output.splitlines() if app.strip()] # stripping any whitespace from each app name and removing any empty strings
        
        return installed_apps

    # Get running processes
    def get_running_processes(self):
        processes = []
        for process in psutil.process_iter(['pid', 'name', 'username']): # iterating over all processes with specified attributes
            processes.append(process.info) # appending the process info dictionary to the list

        return processes
    

#Return data in JSON
def get_detail():
    agent = SystemAgent()  # Instance of the agent class    

    data = {
        "system": agent.system,  # system information
        "username": agent.node,
        "machine": agent.machine,
        "ip_address": agent.ip_address,
        "total_memory": round(agent.get_ram_info()/(1024 * 1024 * 1024),2) or 0,  # Memory in GB or 0 if None
        "internet_connected": agent.internet_connection(),  # Internet connected or not
        "installed_apps": len(agent.get_installed_apps()) or 0,  # Number of installed apps or 0 if None
        "running_processes": len(agent.get_running_processes()) or 0  # Number of running processes or 0 if None
    }

    return data

def send_system_info():
    data = get_detail()  # Get system information

    try:
        response = requests.post(api_url, json=data)
    except Exception as e:
        print(e)
        return
    print(response.status_code, response.text)


def run_agent():
    while True:  # Run an infinite loop
        send_system_info()  # Send the system information to django api
        time.sleep(20)  # Wait for 20 seconds

run_agent()  # Run the agent
