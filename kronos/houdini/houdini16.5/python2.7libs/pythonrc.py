import hou
import sys
import os
import platform



OS = platform.system()

ScriptsPath = "/houdini/houdini16.5/scripts/python/python27"
LibraryPath = "/libs/python27"


if OS == 'Linux':

   try:
       LinPath = os.getcwd()
       sys.path.append(LinPath + ScriptsPath)
       sys.path.append(LinPath + LibraryPath)


   except:
       pass

if OS == 'Windows':

   try:
       WinPath = os.getcwd()
       sys.path.append(WinPath + ScriptsPath)
       sys.path.append(WinPath + LibraryPath)


   except:
       pass
