import sys, logger
from getpass import getuser
from nvidia import install_nvidia_driver

def read_nth_arg(n):
  try:
    return sys.argv[n]
  except IndexError:
    return None
  
def get_user_home_arg():
  result = read_nth_arg(1)
  if result is None:
    logger.error('Not found user home argument')
    exit(1)

  return result

def main():
  if getuser() != 'root':
    logger.error('This script was started without superuser\'s permission')
    exit(1)

  user_home = get_user_home_arg()

  install_nvidia_driver()
  input('Press enter')

main()