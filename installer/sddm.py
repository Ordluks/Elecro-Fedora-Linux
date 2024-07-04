import logger
from system_utils import install_packages_list, run_shell, is_package_installed, copy_asset, copy_asset_tree

SDDM_ASSETS_DIR = 'sddm'

def install_sddm():
  logger.info('Installing SDDM...')

  install_packages_list([
    'sddm', 
    'qt6-qt5compat',
    'qt6-qtdeclarative',
    'qt6-qtquickcontrols2',
    'qt6-qtsvg'
    ])

  copy_asset_tree(f'{SDDM_ASSETS_DIR}/catppuccin-mocha', '/usr/share/sddm/themes/catppuccin-mocha')
  copy_asset(f'{SDDM_ASSETS_DIR}/theme.conf.user', '/etc/sddm.conf.d/theme.conf.user')
  logger.success('Installed SDDM theme')

  copy_asset('hyprland.desktop', '/usr/share/wayland-sessions/hyprland.desktop')
  logger.success('Added Hyprland session variant to SDDM')

  # login_managers = [
  #   'lightdm',
  #   'gdm',
  #   'lxdm',
  #   'lxdm-gtk3'
  # ]

  # for login_manager in login_managers:
  #   print(login_manager)
  #   if is_package_installed(login_managers):
  #     logger.info(f'Disabling "{login_manager}" login manager...')
  #     run_shell(
  #       f'sudo systemctl disable {login_manager}',
  #       on_fail=lambda err, _: logger.error(f'Unable to deactivate "{login_manager} service":\n{err}')
  #     )

  logger.info('Disabling GDM and enabling SDDM...')

  run_shell(
    'systemctl disable gdm',
    on_fail=lambda err, _: logger.error(f'Unable to deactivate "gdm" service:\n{err}')
  )

  def unable_to_activate(err, _):
    logger.error(f'Unable to activate "sddm" service:\n{err}')
  
  run_shell(
    'systemctl set-default graphical.target',
    on_success=lambda: run_shell('systemctl enable sddm', on_fail=unable_to_activate),
    on_fail=unable_to_activate
  )

  logger.success('SDDM was installed\n')
  