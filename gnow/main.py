import datetime
import time

from .color import ColorClass
from .check import CheckClass
Color = ColorClass()
Check = CheckClass()

class MainClass:
    #def __init(selft):

    #------------------------------
    # Add
    #------------------------------
    def fast_add(self):
        Color.set(' ADD ', 'green', 'white')
        try:
            read = input('Add a file to the index? [n/Y]')
            if read == 'no' or read == 'NO' or read == 'n' or read == 'N':
                exit()
            elif read == 'yes' or read == 'YES' or read == 'y' or read == 'Y':
                Check.do_git_add()
                Color.set('Staging done. ✔', 'green')
            else:
                Check.do_git_add()
                Color.set('Staging done. ✔', 'green')
        except (KeyboardInterrupt) as e:
            print()
            exit()

    #------------------------------
    # Commit
    #------------------------------
    def fast_commit(self, input_message = ''):
        Color.set(' COMMIT ', 'green', 'white')

        if Check.is_change('workingtree') == True:
            self.fast_add()

        # コミットメッセージ引数が無い場合は日付とステータスをメッセージとする
        # If there is no commit message argument, the date and status will be used as the message.
        if input_message == '':
            now     = str(datetime.datetime.today())
            message = Check.format_status(Check.get_git_status())
        else:
            message = input_message

        # ローカルのブランチが存在しない初回pushとみられる場合はmasterにpushする
        # Push to master if it appears to be the first push where no local branch exists.
        if Check.branch_exists() == '':
            branch = 'main'
            Color.set('Initial commit.', 'yellow')
        else:
            branch = Check.branch_exists()

        Color.set('message', 'yellow')
        print (' ┗ ' + message)
        Color.set('branch', 'yellow')
        print (' ┗ ' + branch)

        try:
            read = input('Ready? [n/Y]')
            if read == 'no' or read == 'NO' or read == 'n' or read == 'N':
                exit()
            elif read == 'yes' or read == 'YES' or read == 'y' or read == 'Y':
                Check.do_git_commit(message)
                Color.set('Commit done. ✔', 'green')
            else:
                Check.do_git_commit(message)
                Color.set('Commit done. ✔', 'green')
        except (KeyboardInterrupt) as e:
            print()
            exit()

    #------------------------------
    # Push
    #------------------------------
    def fast_push(self, input_message = ''):
        Check.status()
        # Check any file exists in the working tree.
        if Check.is_change('workingtree') == True:
            self.fast_add()
        # Check any file exists in the index. 
        if Check.is_change('index') == True:
            self.fast_commit(input_message)

        # コミット済みファイルが存在するか
        # Check any file exists in the index. 
        if Check.commit_exists() == False:
            exit()

        Color.set(' PUSH ', 'green', 'white')

        # ローカルのブランチが存在しない初回pushとみられる場合はmasterにpushする
        if Check.branch_exists == 0:
            branch = 'main'
            Color.set('Initial commit', 'yellow')
        else:
            branch = Check.get_git_branch() 

        print('Push your commits.')
        Color.set('branch', 'yellow')
        print (' ┗ ' + branch)

        try:
            read = input('Ready? [n/Y]')
            if read == 'no' or read == 'NO' or read == 'n' or read == 'N':
                exit()
            elif read == 'yes' or read == 'YES' or read == 'y' or read == 'Y':
                push = Check.do_git_push(branch)
                Color.set('Push done. ✔', 'green')
            else:
                push = Check.do_git_push(branch)
                Color.set('Push done. ✔', 'green')
                exit()
        except (KeyboardInterrupt) as e:
            print()
            exit()

    #------------------------------
    # Tags
    #------------------------------
    def fast_tag(self, new_tag = 0):
        Color.set(' TAG ', 'green', 'white')

        latest = Check.get_latest_tag()
        latest_list  = latest.split('.')
        latest_major = latest_list[0]
        latest_minor = latest_list[1]
        latest_patch = latest_list[2]
        patch_increment = int(latest_patch) + 1
        patch_ver       = latest_major + '.' + latest_minor + '.' + str(patch_increment)

        if new_tag == 0:
            Color.set('Latest tag is ' + latest, 'green')
            Color.set('Auto incremented version is ' + patch_ver, 'green')
            try:
                read = input('Ready? [n/Y]')
                if read == 'no' or read == 'NO' or read == 'n' or read == 'N':
                    exit()
                elif read == 'yes' or read == 'YES' or read == 'y' or read == 'Y':
                    Check.do_git_tag(patch_ver)
                    Check.do_command('git push origin --tag')
                else:
                    Color.set('Process aborted.', 'red')
                    exit()
            except (KeyboardInterrupt) as e:
                print()
                exit()
        else: # user add a tag
            Color.set('Latest tag is ' + latest, 'green')
            Color.set('New tag is ' + new_tag, 'green')
            try:
                read = input('Ready? [n/Y]')
                if read == 'no' or read == 'NO' or read == 'n' or read == 'N':
                    exit()
                elif read == 'yes' or read == 'YES' or read == 'y' or read == 'Y':
                    Check.do_git_tag(new_tag)
                    Check.do_command('git push origin --tag')
                else:
                    Color.set('Process aborted.', 'red')
                    exit()
            except (KeyboardInterrupt) as e:
                print()
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
        print("  (no args): Run git add -> commit -> push")
        print("  -h, --help :Show helps.")
        print("  -v, -V, --version :Show version.")
        print("  -c, --commit [ARG] :Commit only.")
        print("  -t, --tag [ARG] :Add tag. If no argument, current version will be automatically incremented.")

