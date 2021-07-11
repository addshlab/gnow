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

    if input_message == '':
      message = str(datetime.datetime.today()) + '\n' + Conditional.get_git_status()
      print(message)

# Commit
#func fast_commit {
#
#  has_repo
#
#  # コミットメッセージ引数が無い場合は日付とステータスをメッセージとする
#  # If there is no commit message argument, the date and status will be used as the message.
#  if [ -z "${1}" ]; then
#    MESSAGE="${DATE} ${GIT_STATUS}"
#  else
#    MESSAGE="${1}"
#  fi
#
#  # ローカルのブランチが存在しない初回pushとみられる場合はmasterにpushする
#  # Push to master if it appears to be the first push where no local branch exists.
#  if [ -z "${BRANCH_EXIST}" ]; then
#    BRANCH=master
#    yellow 'Initial Commit'
#  fi
#
#  yellow 'message'
#  echo ' ┗ '${MESSAGE}
#  yellow 'branch'
#  echo ' ┗ '${BRANCH}
#  echo "Ready? [n/Y]:"
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
