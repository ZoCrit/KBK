from presets import configs, styling
import os

def create_config():
  choice = input('\
  1) Classic (F5-F6)\n\
  2) Mid (F4-F5)\n\
  3) Left (F3-F4)\n\
  Which one would you like? ') or '1'
  if choice == 1 or choice.startswith('1') or choice.startswith('c') or choice.startswith('C'):
    set_classic()
  elif choice == 2 or choice.startswith('2') or choice.startswith('m') or choice.startswith('M'):
    set_mid()
  elif choice == 3 or choice.startswith('3') or choice.startswith('l') or choice.startswith('L'):
    set_left()

def check_existing_config():
  if os.path.exists(configs.kbk_config):
    ask_to_delete_config()
  else:
    create_config()

def ask_to_delete_config():
  choice = input('A KBK configuration file already exists, do you want to delete it? [y/N]: ') or 'N'
  if choice.startswith('y') or choice.startswith('Y'):
    delete_config()
  else:
    main_menu()

def delete_config():
  os.remove(configs.kbk_config)
  os.system(configs.clear_immediate)
  print('The existing KBK configuration file has been deleted.')

def set_classic():
  os.system(configs.classic_immediate)
  config = open(configs.kbk_config, mode = 'w')
  config.write(configs.classic_persist)
  config.close

def set_mid():
  os.system(configs.mid_immediate)
  config = open(configs.kbk_config, mode = 'w')
  config.write(configs.mid_persist)
  config.close

def set_left():
  os.system(configs.left_immediate)
  config = open(configs.kbk_config, mode = 'w')
  config.write(configs.left_persist)
  config.close


# check_existing_config()

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
  choice = input('\
  #### MAIN MENU ####\n\
  1) Create new configuration\n\
  2) Edit existing configuration\n\
  3) Delete existing configuration\n\
  4) Quit program\n\
  What do you want to do? (1-4): ')
  if choice == 1 or choice.startswith('1') or choice.startswith('c') or choice.startswith ('C'):
    check_existing_config()
  elif choice == 2 or choice.startswith('2') or choice.startswith('e') or choice.startswith ('E'):
    print('unfinished')



main_menu()

