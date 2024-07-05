import logger
from system_utils import install_packages_list, copy_asset_tree

def install_hyprland(user_home):
  logger.info('Installing Hyprland...')

  install_packages_list(['hyprland', 'hyprpaper'])
  copy_asset_tree('hypr', user_home + '/.config/hypr')

  logger.success('Hyprland was installed\n')
