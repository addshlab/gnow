import datetime

# Import text color class.
from module import colorClass
Color = colorClass.ColorClass()

# Import conditional class.
from module import conditionalClass
Conditional = conditionalClass.ConditionalClass()

class MainClass:
  #def __init(selft):

  def fast_commit(self, input_message = ''):
    Color.set(' fast commit ', 'green', 'white')

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
      print('yes')
      status = Conditional.do_command("git add -A")
      print(status)
      commit = Conditional.do_command("git commit -m" + message)
      print(commit)
      Color.set('Commit done. ✔', 'green')
    else:
      Color.set('Process aborted.', 'red')
      return 0

# Commit
#func fast_commit {
#
#  has_repo
#
#  read input
#  if [ "${input}" = 'no' ] || [ "${input}" = 'NO' ] || [ "${input}" = 'n' ]; then
#    exit 0
#  elif [ "${input}" = 'yes' ] || [ "${input}" = 'YES' ] || [ "${input}" = 'y' ]; then
#    git add -A
#    git commit -m "${MESSAGE}"
#    green 'Commit done. ✔'
#  else
#    red 'Process aborted.'
#    exit 0
#  fi
#} # fast_commit end
#
#
#
#
#
