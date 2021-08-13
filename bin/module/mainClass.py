import datetime
import time

# Import text color class.
from module import colorClass
Color = colorClass.ColorClass()

# Import conditional class.
from module import conditionalClass
Conditional = conditionalClass.ConditionalClass()

class MainClass:
    #def __init(selft):

    #------------------------------
    # Commit
    #------------------------------
    def fast_commit(self, input_message = ''):
        Color.set(' COMMIT ', 'green', 'white')

        if Conditional.stage_exists() == 0:
            Color.set('Nothing to stage.', 'yellow')

        # コミットメッセージ引数が無い場合は日付とステータスをメッセージとする
        # If there is no commit message argument, the date and status will be used as the message.
        if input_message == '':
            message = str(datetime.datetime.today()) + '\n' + Conditional.get_git_status()
        else:
            message = input_message

        # ローカルのブランチが存在しない初回pushとみられる場合はmasterにpushする
        # Push to master if it appears to be the first push where no local branch exists.
        if Conditional.branch_exists() == '':
            branch = 'main'
            Color.set('Initial commit.', 'yellow')
        else:
            branch = Conditional.branch_exists()

        Color.set('mesage', 'yellow')
        print (' ┗ ' + message)
        Color.set('branch', 'yellow')
        print (' ┗ ' + branch)

        read = input('Ready? [n/Y]')
        if read == 'no' or read == 'NO' or read == 'n' or read == 'N':
            return 0
        elif read == 'yes' or read == 'YES' or read == 'y' or read == 'Y':
            Conditional.do_git_add()
            Conditional.do_git_commit(message)
            Color.set('Commit done. ✔', 'green')
        else:
            Color.set('Process aborted.', 'red')
            return 0

    #------------------------------
    # Push
    #------------------------------
    def fast_push(self, input_message = ''):
        print(Conditional.get_git_status())
        # ステージングにファイルが存在するか
        if Conditional.get_git_status() == 0:
            Color.set('Nothing to stage.', 'yellow')
        else:
            Color.set('File exists to stage. Please commit!', 'yellow')
            self.fast_commit(input_message)

        # コミット済みファイルが存在するか
        if Conditional.commit_exists() == 0:
            Color.set('No files committed.', 'red')
            exit()

        Color.set(' PUSH ', 'green', 'white')

        # ローカルのブランチが存在しない初回pushとみられる場合はmasterにpushする
        if Conditional.branch_exists == 0:
            branch = 'main'
            Color.set('Initial commit', 'yellow')
        else:
            branch = Conditional.get_git_branch() 

        print('Push your commits.')
        Color.set('branch', 'yellow')
        print (' ┗ ' + branch)

        read = input('Ready? [n/Y]')
        if read == 'no' or read == 'NO' or read == 'n' or read == 'N':
            return 0
        elif read == 'yes' or read == 'YES' or read == 'y' or read == 'Y':
            print('yes')
            push = Conditional.do_git_push(branch)
            print(push)
            Color.set('Push done. ✔', 'green')
        else:
            Color.set('Process aborted.', 'red')
            return 0

    #------------------------------
    # Tags
    #------------------------------
    def fast_tag(self, new_tag = 0):
        Color.set(' TAG ', 'green', 'white')

        latest = Conditional.get_latest_tag()
        latest_list  = latest.split('.')
        latest_major = latest_list[0]
        latest_minor = latest_list[1]
        latest_patch = latest_list[2]
        patch_increment = int(latest_patch) + 1
        patch_ver       = latest_major + '.' + latest_minor + '.' + str(patch_increment)

        if new_tag == 0:
            Color.set('Latest tag is ' + latest, 'green')
            Color.set('Auto incremented version is ' + patch_ver, 'green')
            read = input('Ready? [n/Y]')
            if read == 'no' or read == 'NO' or read == 'n' or read == 'N':
                exit()
            elif read == 'yes' or read == 'YES' or read == 'y' or read == 'Y':
                Conditional.do_git_tag(patch_ver)
                Conditional.do_command('git push origin --tag')
            else:
                Color.set('Process aborted.', 'red')
                exit()
        else: # user add a tag
            Color.set('Latest tag is ' + latest, 'green')
            Color.set('New tag is ' + new_tag, 'green')
            read = input('Ready? [n/Y]')
            if read == 'no' or read == 'NO' or read == 'n' or read == 'N':
                exit()
            elif read == 'yes' or read == 'YES' or read == 'y' or read == 'Y':
                Conditional.do_git_tag(new_tag)
                Conditional.do_command('git push origin --tag')
            else:
                Color.set('Process aborted.', 'red')
                exit()

    #------------------------------
    # How to use
    #------------------------------
    def usage(self):
        Color.set(' HELP ', 'green', 'white')
        Color.set('gnow command :: Git commit for NOW', 'green')
        print("This is the 'gnow' command to do a quick git commit and git push.")
        print('')
        print("Options:")
        print("  -h, --help :Show helps.")
        print("  -v, -V, --version :Show version.")
        print("  -t, --tag [ARG] :Add tag. If no argument, current version will be automatically incremented.")

