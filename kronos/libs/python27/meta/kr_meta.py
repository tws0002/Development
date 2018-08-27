import os
import hou

def currentuser():
  """
  En...
  This func is return EnvUsername
  Sample***
  User = currentuser()
  """
  try:
      cu_user =  os.environ.get("USERNAME")
      return cu_user

  except NameError:
      pass


def currentpath():
  """
  En...
  This func is return Setting default path
  Sample***
  getpath = currentpath()
  """
  try:
      cu_path = os.getcwd()
      return cu_path

  except NameError:
      pass



