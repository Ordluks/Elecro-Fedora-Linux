import subprocess
import logger

def run_shell(command):
  proc = subprocess.Popen(command,
                          stderr=subprocess.PIPE, 
                          stdout=subprocess.PIPE,
                          shell=True,
                          universal_newlines=True)
  std_out, std_err = proc.communicate()
  return proc.returncode, std_out, std_err

def install_package(name):
  if run_shell(f'dnf list installed "{name}"')[0] == 0:
    logger.info(f'Package "{name}" already installed')
    return
  
  exit_code, _out, err = run_shell(f'dnf install {name} -y')
  if exit_code == 0:
    logger.success(f'Package "{name}" was installed')
  else:
    logger.error(f'Can not install "{name}":\n{err}')
    exit(1)

def install_packages_list(names):
  for name in names:
    install_package(name)