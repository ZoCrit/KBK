from presets import configs, styling
import os

active_config = 'Unable to detect any configuration.'

def create_config():
  choice = input('\n\
  ### CHOOSE YOUR CONFIGURATION ###\
  \n\
  1) Classic (F5-F6)\n\
  2) Mid (F4-F5)\n\
  3) Left (F3-F4)\n\
  \n\
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

def check_existing_configs():
  if os.path.exists(configs.kbk_config):
    return True
  else:
    return False

def ask_to_delete_config():
  choice = input('\n\
  A KBK configuration has been found, do you want to delete it? [y/N]: ') or 'N'
  if choice.startswith('y') or choice.startswith('Y'):
    delete_config()
    main_menu()
  else:
    main_menu()

def delete_config():
  os.remove(configs.kbk_config)
  os.system(configs.clear_immediate)
  print('The existing KBK configuration file has been deleted.')
  main_menu()


def set_classic():
  os.system(configs.classic_immediate)
  config = open(configs.kbk_config, mode = 'w')
  config.write(configs.classic_persist)
  config.close
  active_config = 'Classic (F5-F6)'
  styling.prGreen('\n\
  Success! CLASSIC configuration is now active. (F5-F6)')
  main_menu()

def set_mid():
  os.system(configs.mid_immediate)
  config = open(configs.kbk_config, mode = 'w')
  config.write(configs.mid_persist)
  config.close
  active_config = 'Mid (F4-F5)'
  styling.prGreen('\n\
  Success! MID configuration is now active. (F4-F5)')
  main_menu()

def set_left():
  os.system(configs.left_immediate)
  config = open(configs.kbk_config, mode = 'w')
  config.write(configs.left_persist)
  config.close
  active_config = 'Left (F3-F4)'
  styling.prGreen('\n\
  Success! CLASSIC configuration is now active. (F3-F4)')
  main_menu()

def main_menu():
  choice = input('\n\
  #### MAIN MENU ####\n\
  1) Create new configuration\n\
  2) Edit existing configuration\n\
  3) Delete existing configuration\n\
  4) Quit program\n\
  \n\
  What do you want to do? (1-4): ')
  if choice == 1 or choice.startswith('1') or choice.startswith('c') or choice.startswith ('C'):
    check_existing_config()
  elif choice == 2 or choice.startswith('2') or choice.startswith('e') or choice.startswith ('E'):
    print('Your current configuration is: {}'.format(active_config))
    choice = input('\n\
    Do you want to change it? [y/N]') or 'N'
    if choice.startswith('y') or choice.startswith('Y'):
      create_config()
    else:
      main_menu()
  elif choice == 3 or choice.startswith('3') or choice.startswith('d') or choice.startswith ('D'):
    if (check_existing_configs() == False):
      choice = input('\n\
      No existing configuration found. Do you want to go back to the main menu? [Y/n]')
      if choice.startswith('n') or choice.startswith('n'):
        choice = input('\n\
        Do you want to close the program? [Y/n]')
        if choice.startswith('n') or choice.startswith('N'):
          main_menu()
        else:
          os.system('clear')
          quit()
      else:
        main_menu()
    elif (check_existing_config() == True):
      ask_to_delete_config()
  elif choice == 4 or choice.startswith('4') or choice.startswith('q') or choice.startswith ('Q'):
    quit()
  else:
    styling.prRed('Invalid input.')



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
main_menu()

