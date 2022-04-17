from presets import configs, styling
import os

def create_config():
  choice = input('\
  1) Classic (F5-F6)\n\
  2) Mid (F4-F5)\n\
  3) Left (F3-F4)\n\
  Which one would you like? ') or '1'
  if choice == 1 or choice == '1' or choice.startswith('c') or choice.startswith('C'):
    os.system(configs.classic_immediate)
    config = open(configs.kbk_config, mode = 'w')
    config.write(configs.classic_persist)
    config.close
  elif choice == 2 or choice == '2' or choice.startswith('m') or choice.startswith('M'):
    os.system(configs.mid_immediate)
    config = open(configs.kbk_config, mode = 'w')
    config.write(configs.mid_persist)
    config.close
  elif choice == 3 or choice == '3' or choice.startswith('l') or choice.startswith('L'):
    os.system(configs.left_immediate)
    config = open(configs.kbk_config, mode = 'w')
    config.write(configs.left_persist)
    config.close

def check_existing_config():
  if os.path.exists(configs.kbk_config):
    ask_to_delete_config()
  else:
    create_config()

def ask_to_delete_config():
  choice = input('A KBK configuration already exists, do you want to delete it? [y/N]: \n') or 'N'
  if choice.startswith('y') or choice.startswith('Y'):
    os.remove(configs.kbk_config)
    os.system(configs.clear_immediate)
    print('The existing KBK configuration file has been deleted.')
  else:
    print('Exiting program')

check_existing_config()

def main_menu():
  os.system('clear')
  styling.prCyan('''
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

