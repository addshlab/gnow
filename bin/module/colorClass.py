class ColorClass:
  def __init__(self):
    self.colors = {
      'red'    : '\033[31m',
      'green'  : '\033[32m',
      'yellow' : '\033[33m'
    }
    self.end    = '\033[0m'

  def set(self, color, text):
    colorCode = self.colors.get(color, '\033[30m')
    output    = colorCode + text + self.end
    print(output)

