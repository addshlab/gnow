import subprocess
#------------------------------
# Confirm the existence of the Git repository.
#------------------------------

class ConditionalClass:
  #def __init__(self):

  def do_command(self,command):
    proc = subprocess.Popen(
      command,
      shell  = True,
      stdin  = subprocess.PIPE,
      stdout = subprocess.PIPE,
      stderr = subprocess.PIPE)
    stdout_data, stderr_data = proc.communicate()
    
    return stdout_data.decode()

  def repository_exists(self):
    command    = "git status -s 2>&1 > /dev/null | awk '{print $1}'"
    if self.do_command(command) == '':
      return 1
    else:
      return 0

  def stage_exists(self):
    command = "git status -s"
    if self.do_command(command) == '':
      return 0
    else:
      return 1

  def get_git_status(self):
    command = "git status -s"
    status  = self.do_command(command)
    return status

  def get_git_branch(self):
    command = "git rev-parse --abbrev-ref HEAD"
    branch  = self.do_command(command)
    return branch

  def branch_exists(self):
    command = "git branch"
    branch  = self.do_command(command)
    return branch

  def commit_exists(self):
    command = 'git log --pretty=format:"%H" origin/' + self.get_git_branch().rstrip('\r\n') + '..HEAD'
    commit  = self.do_command(command)
    return commit







