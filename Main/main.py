import subprocess

'''
This is a script that runs the program of the AI Assistant.
It first specifies the name of the AI assistant, which is set to 'Eve' in this case. 
It also requires the OpenAI API key to be set.
It then runs the assistant by using the subprocess module's run method, 
which takes a list of arguments that specify the command to run. 
It runs the assistant_gpt Python module's Assistant class with the specified name and API_key as arguments.
The stderr=subprocess.DEVNULL argument is used to discard any error output from the command.
'''
#Name your AI Assistant
name = 'Eve'
#Input your OpenAI API Secret Key
API_key = "Your API Key"


# run Assistant and discard output
try:
    subprocess.run([f"python", "-c", f"from assistant_gpt import Assistant; Assistant('{name}', '{API_key}')"], stderr=subprocess.DEVNULL)
except:
    subprocess.run([f"python3", "-c", f"from assistant_gpt import Assistant; Assistant('{name}', '{API_key}')"], stderr=subprocess.DEVNULL)
