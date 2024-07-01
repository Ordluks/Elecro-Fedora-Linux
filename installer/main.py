import sys, logger
from getpass import getuser
from nvidia import install_nvidia_driver
from sddm import install_sddm

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

  try:
    install_nvidia_driver()
    install_sddm()
  except OSError:
    logger.echo('\n\n\nIt seams something went wrong during installation. You can found logs in ./logs')

  input('')

main()