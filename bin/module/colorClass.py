class ColorClass:
  def __init__(self):
    self.colors = {
      'red'    : '\033[31',
      'green'  : '\033[32',
      'yellow' : '\033[33',
    }

    self.backgrounds = {
      'white' : ';47',
    }

    self.end    = '\033[0m'

  def set(self, text, color, background = ''):
    colorCode = self.colors.get(color, '\033[30m')
    bgCode    = self.backgrounds.get(background, '')
    output    = colorCode + bgCode + 'm' + text + self.end
    print(output)

