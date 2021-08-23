import subprocess

# Import text color class.
from module import colorClass
Color = colorClass.ColorClass()

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
            return False
        else:
            return True

    def get_git_status(self):
        command = "git status -s"
        status  = self.do_command(command)
        if not status:
            return ''
        else:
            return status

    def is_change(self, area=''):
        workingtree = ''
        index       = ''
        if self.get_git_status() == False:
            return False
        status = self.get_git_status().split('\n')
        for item in status:
            if item:
                index       = index + item.rsplit(' ')[0]
                workingtree = workingtree + item.rsplit(' ')[1]

        if area == 'index':
            if index:
                return True
            else:
                return False
        elif area == 'workingtree':
            if workingtree:
                return True
            else:
                return False
        else:
            return False

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
        if not commit:
            return False
        else:
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

    def do_git_commit(self, message = ''):
        message = message.replace('\n','')
        command = "git commit -m '" + message + "'"
        result  = self.do_command(command)
        return result

    def do_git_push(self, branch = 'main'):
        command = 'git push origin ' + branch
        push    = self.do_command(command)
        return push

    def status(self, status = ''):
        index_i       = 0
        workingtree_i = 0
        status = self.get_git_status()
        status_dict = {
            'M  ':'i.Updated ',
            'A  ':'i.Added ',
            'D  ':'i.Deleted ',
            'R  ':'i.Renamed ',
            'C  ':'i.Copied ',
            ' M ':'w.Updated ',
            ' A ':'w.Added ',
            ' D ':'w.Deleted ',
            ' R ':'w.Renamed ',
            ' C ':'w.Copied ',
            '?? ':'o.Untracked ',
            '!! ':'o.Ignored '
        }
        for word, read in status_dict.items():
            status = status.replace(word, read)
        status_list = status.split('\n')
        del status_list[-1]
        # Border between status display.
        if not status_list:
            max_file_name = 1
        else:
            max_file_name = len(max((x for x in status_list), key=len))
        if max_file_name <= 14:
            border = '-' * 15
        else:
            border = '-' * (max_file_name + 2)

        print(border)
        Color.set(' Index ', 'white', 'green')
        it = iter(status_list)
        for item in status_list:
            if item.startswith('i.'):
                print(' - ' + item.strip('i.'))
                index_i += 1
        if index_i == 0:
            print(' - No files.')

        Color.set(' Working tree ', 'white', 'red')
        for item in status_list:
            if item.startswith('w.') or item.startswith('o.'):
                if item.startswith('w.'):
                    print(' - ' + item.strip('w.'))
                    workingtree_i += 1
                if item.startswith('o.'):
                    print(' - ', end='')
                    Color.set(item.strip('o.'), 'red')
                    workingtree_i += 1
        if workingtree_i == 0:
            print(' - No files.')
        print(border)

    def format_status(self, status = ''):
        format_dict = {
            'M  ':'Updated ',
            'A  ':'Added ',
            'D  ':'Deleted ',
            'R  ':'Renamed ',
            'C  ':'Copied '
        }
        for word, read in format_dict.items():
            status = status.replace(word, read)
        return status.replace('\n', ', ').strip(', ')
