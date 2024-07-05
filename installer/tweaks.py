import logger
from system_utils import install_package, copy_asset_tree, copy_asset

def install_tweaks(user_home):
  _install_waybar(user_home)
  _install_rofi(user_home)
  _install_gtk_theme(user_home)

def _install_waybar(user_home):
  logger.info('Installing Waybar...')
  install_package('waybar')
  copy_asset_tree('waybar', user_home + '/.config/waybar')
  logger.success('Waybar was installed\n')

def _install_rofi(user_home):
  logger.info('Installing Rofi...')
  install_package('rofi')
  copy_asset('rofi/config.rasi', user_home + '/.config/rofi/config.rasi')
  copy_asset_tree('rofi/theme', user_home + '/.local/share/rofi/themes/electro')
  logger.success('Rofi was installed\n')

def _install_gtk_theme(user_home):
  logger.info('Installing theme for GTK applications...')
  GTK_DIR = 'gtk'
  copy_asset_tree(GTK_DIR + '/themes', '/usr/share/themes')
  copy_asset(GTK_DIR + '/settings.ini', user_home + '/.config/gtk-3.0/settings.ini')
  logger.success('GTK theme was installed\n')