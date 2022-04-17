# from config_presets import kbk_config, classic_immediate, classic_persist, mid_immediate, mid_persist, left_immediate, left_persist, clear_immediate
# from styling_presets import prRed, prGreen, prYellow, prCyan
from presets import config_presets, styling_presets
import os

def create_config():
  choice = input('\
  1) Classic (F5-F6)\n\
  2) Mid (F4-F5)\n\
  3) Left (F3-F4)\n\
  Which one would you like? ') or '1'
  if choice == 1 or choice == '1' or choice.startswith('c') or choice.startswith('C'):
    os.system(classic_immediate)
    config = open(kbk_config, mode = 'w')
    config.write(classic_persist)
    config.close
  elif choice == 2 or choice == '2' or choice.startswith('m') or choice.startswith('M'):
    os.system(mid_immediate)
    config = open(kbk_config, mode = 'w')
    config.write(mid_persist)
    config.close
  elif choice == 3 or choice == '3' or choice.startswith('l') or choice.startswith('L'):
    os.system(left_immediate)
    config = open(kbk_config, mode = 'w')
    config.write(left_persist)
    config.close

def check_existing_config():
  if os.path.exists(kbk_config):
    ask_to_delete_config()
  else:
    create_config()

def ask_to_delete_config():
  choice = input('A KBK configuration already exists, do you want to delete it? [y/N]: \n') or 'N'
  if choice.startswith('y') or choice.startswith('Y'):
    os.remove(kbk_config)
    os.system(clear_immediate)
    print('The existing KBK configuration file has been deleted.')
  else:
    print('Exiting program')

check_existing_config()

def main_menu():
  os.system('clear')
  prCyan('''
    █████   ████ ███████████  █████   ████
   ░░███   ███░ ░░███░░░░░███░░███   ███░ 
    ░███  ███    ░███    ░███ ░███  ███   
    ░███████     ░██████████  ░███████    
    ░███░░███    ░███░░░░░███ ░███░░███   
    ░███ ░░███   ░███    ░███ ░███ ░░███  
    █████ ░░████ ███████████  █████ ░░████
   ░░░░░   ░░░░ ░░░░░░░░░░░  ░░░░░   ░░░░\n''')
  print('\
  Welcome,\n')
  print('\
  Keyboard Brightness Key is a tiny utility program that allows you ')

# main_menu()

