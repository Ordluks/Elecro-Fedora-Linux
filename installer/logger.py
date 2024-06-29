import os.path, sys
from datetime import datetime

class Logger:
  def __init__(self):
    self._terminal = sys.stdout
    self._file = open(os.path.join('logs', str(datetime.now()) + '.log'), 'w')

  def write(self, text):
    self._terminal.write(text)
    self._file.write(text)

  def flush(self):
    self._terminal.flush()
    self._file.flush()

sys.stdout = Logger()

def info(message):
  print(f'(Info) {message}')

def success(message):
  print(f'(Success) {message}')

def error(message):
  print(f'(Error) {message}')

