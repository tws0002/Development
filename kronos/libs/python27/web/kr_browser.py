import webbrowser
import platform
import subprocess
import os

def PageforProjects(url):
    if platform.system() == 'Windows':
       chrome_Dir = os.path.isdir("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
       if chrome_Dir == 'True':
          webbrowser.get(chrome_Dir).open_new_tab(url)
