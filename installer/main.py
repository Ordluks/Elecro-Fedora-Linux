import sys, os, logger
from getpass import getuser
from nvidia import install_nvidia_driver
from sddm import install_sddm
from hyprland import install_hyprland

def read_nth_arg(n):
  try:
    return sys.argv[n + 1]
  except IndexError:
    return None
  
def get_user_home_arg():
  result = read_nth_arg(0)
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
    install_hyprland(user_home)
  except OSError:
    logger.echo('\n\nIt seams something went wrong during installation. You can found logs in ./logs')
    input()
    exit(1)
  else:
    input('Reboot required. Press enter to reboot.')
    os.system('systemctl reboot')

main()