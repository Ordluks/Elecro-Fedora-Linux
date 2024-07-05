import subprocess, os.path, logger
from shutil import copyfile, copytree

def run_shell_base(command):
  proc = subprocess.Popen(
    command,
    stderr=subprocess.PIPE, 
    stdout=subprocess.PIPE,
    shell=True,
    universal_newlines=True
  )
  std_out, std_err = proc.communicate()
  return proc.returncode, std_out, std_err

def run_shell(command: str, on_success=None, on_fail=None):
  exit_code, out, err = run_shell_base(command)
  logger.log(f'{out}\n{err}')
  if exit_code == 0:
    if on_success is not None:
      on_success()
  else:
    if on_fail is not None:
      on_fail(err, out)
    else:
      logger.error(f'Command "{command.split(' ')[0]}" failed:\n{out}\n\n{err}')

    raise OSError

def is_package_installed(name):
  return run_shell_base(f'dnf list installed "{name}"')[0] == 0

def install_package(name):
  if is_package_installed(name):
    logger.info(f'Package "{name}" already installed')
    return
  
  run_shell(
    f'dnf install {name} -y',
    on_success=lambda: logger.success(f'Package "{name}" was installed'),
    on_fail=lambda err, _: logger.error(f'Can not install "{name}":\n{err}')
  )

def install_packages_list(names):
  for name in names:
    install_package(name)

ASSETS_PATH = 'assets'

def copy_asset(asset: str, to: str):
  target_dir = '/'.join(to.split('/')[:-1])
  os.makedirs(target_dir, exist_ok=True)

  try:
    copyfile(os.path.join(ASSETS_PATH, asset), to)
  except OSError as error:
    logger.error(f'Can not copy file "{asset}":\n{error}')
    raise OSError

def copy_asset_tree(asset: str, to):
  os.makedirs(to, exist_ok=True)

  try:
    copytree(os.path.join(ASSETS_PATH, asset), to, dirs_exist_ok=True)
  except OSError as error:
    logger.error(f'Can not copy folder "{asset}":\n{error}')
    raise OSError
  