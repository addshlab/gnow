class ColorClass:
  def __init__(self):
    self.colors = {
      'gray'   : '\033[30',
      'red'    : '\033[31',
      'green'  : '\033[32',
      'yellow' : '\033[33',
      'blue'   : '\033[34',
      'purple' : '\033[35',
      'lime'   : '\033[36',
      'white'  : '\033[37',
    }

    self.backgrounds = {
        'gray'   : ';40',
        'red'    : ';41',
        'green'  : ';42',
        'yellow' : ';43',
        'blue'   : ';44',
        'purple' : ';45',
        'lime'   : ';46',
        'white'  : ';47',
    }

    self.end    = '\033[0m'

  def set(self, text, color, background = ''):
    colorCode = self.colors.get(color, '\033[30m')
    bgCode    = self.backgrounds.get(background, '')
    output    = colorCode + bgCode + 'm' + text + self.end
    print(output)

