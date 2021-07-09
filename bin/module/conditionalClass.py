import subprocess
#------------------------------
# Confirm the existence of the Git repository.
#------------------------------

class ConditionalClass:
  #def __init__(self):

  def repository_exists(self):
    command    = "git status -s 2>&1 > /dev/null | awk '{print $1}'"
    proc = subprocess.Popen(
      command,
      shell  = True,
      stdin  = subprocess.PIPE,
      stdout = subprocess.PIPE,
      stderr = subprocess.PIPE)
    stdout_data, stderr_data = proc.communicate()
    
    if stdout_data.decode() == '':
      print('ok')
      return 1
    else:
      print('ng')
      return 0
