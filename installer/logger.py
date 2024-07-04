import os.path, sys
from datetime import datetime

LOGS_DIR = 'logs'

if not os.path.exists(LOGS_DIR):
  os.mkdir(LOGS_DIR)

_default_stdout = sys.stdout
_file = open(os.path.join('logs', str(datetime.now()) + '.log'), 'w')

class Logger:
  def write(self, text):
    _default_stdout.write(text)
    _file.write(text)
  
  def flush(self):
    _default_stdout.flush()
    _file.write('\n')
    _file.flush()

sys.stdout = Logger()

def info(message):
  print(f'(Info) {message}')

def success(message):
  print(f'(Success) {message}')

def error(message):
  print(f'(Error) {message}')

def echo(message):
  _default_stdout.write(message)

def log(message):
  _file.write(message)