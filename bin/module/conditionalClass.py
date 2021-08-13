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
        command = "git status -s 2>&1 > /dev/null | awk '{print $1}'"
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
        status  = self.do_command(command).replace('\n','')
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

    def get_latest_tag(self):
        command = 'git tag | sed s/v//g | sort -t . -n -k1,1 -k2,2 -k3,3 | tail -n1'
        tag     = self.do_command(command).replace('\n','')
        return tag

    def do_git_tag(self,tag = 0):
        command = 'git tag -a v' + tag + '-m v' + tag
        tag     = self.do_command(command)
        return tag

    def do_git_add(self):
        command = 'git add -A'
        result  = self.do_command(command)
        return result

    def do_git_commit(self, message = 0):
        command = 'git commit -m ' + message 
        result  = self.do_command(command)
        return result

    def do_git_push(self, branch = 0):
        command = 'git push origin ' + branch
        push    = self.do_command(command)
        return push



