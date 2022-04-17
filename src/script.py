from presets import configs, styling
import os

active_config = 'Unable to detect any configuration.'

def create_config():
  styling.prCyan('\n\
  ### CHOOSE YOUR CONFIGURATION ###')
  choice = input('\
  1) Classic (F5-F6)\n\
  2) Mid (F4-F5)\n\
  3) Left (F3-F4)\n\
  \n\
  Which one would you like? (1-3): ') or '1'
  if choice == 1 or choice.startswith('1') or choice.startswith('c') or choice.startswith('C'):
    set_classic()
    active_config = 'Classic (F5-F6)'
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
  styling.prYellow('\n\
  An existing KBK configuration has been found.\n\
  It has to be deleted in order to create a new one.')
  choice = input('\n\
  Do you want to delete the existing configuration? [y/N]: ') or 'N'
  if choice.startswith('y') or choice.startswith('Y'):
    delete_config()
    main_menu()
  else:
    main_menu()

def delete_config():
  os.remove(configs.kbk_config)
  styling.prYellow('\n\
  Deleting...\n\
  ')
  os.system(configs.clear_immediate)
  styling.prGreen('\n\
  Success! The existing KBK configuration file has been deleted.\n\
  Going back to the main menu...')
  print_main_menu()
  main_menu()


def set_classic():
  config = open(configs.kbk_config, mode = 'w')
  config.write(configs.classic_persist)
  config.close
  print('\n\
  ##################################################')
  styling.prYellow('\n\
  Creating config...\n\
  ')
  os.system(configs.classic_immediate)
  active_config = 'Classic (F5-F6)'
  styling.prGreen('\n\
  Success! CLASSIC configuration is now active. (F5-F6)\n\
  Going back to the main menu...')
  print('\n\
  ##################################################')
  print_main_menu()
  main_menu()

def set_mid():
  os.system(configs.mid_immediate)
  config = open(configs.kbk_config, mode = 'w')
  config.write(configs.mid_persist)
  config.close
  active_config = 'Mid (F4-F5)'
  styling.prGreen('\n\
  Success! MID configuration is now active. (F4-F5)\n\
  Going back to the main menu...')
  print_main_menu()
  main_menu()

def set_left():
  os.system(configs.left_immediate)
  config = open(configs.kbk_config, mode = 'w')
  config.write(configs.left_persist)
  config.close
  active_config = 'Left (F3-F4)'
  styling.prGreen('\n\
  Success! CLASSIC configuration is now active. (F3-F4)\n\
  Going back to the main menu...')
  print_main_menu()
  main_menu()

def print_main_menu():
  styling.prCyan('\n\
  ### MAIN MENU ###')
  print('\
  1) Create new configuration\n\
  2) Edit existing configuration\n\
  3) Delete existing configuration\n\
  4) Quit program')

def main_menu():
  choice = input('\n\
  What do you want to do? (1-4): ')
  if choice == 1 or choice.startswith('1') or choice.startswith('c') or choice.startswith ('C'):
    check_existing_config()
  elif choice == 2 or choice.startswith('2') or choice.startswith('e') or choice.startswith ('E'):
    print(f'\n\
    Your current configuration is: {active_config}')
    choice = input('\
    Do you want to change it? [y/N]') or 'N'
    if choice.startswith('y') or choice.startswith('Y'):
      create_config()
    else:
      main_menu()
  elif choice == 3 or choice.startswith('3') or choice.startswith('d') or choice.startswith ('D'):
    print('\n\
  ##################################################')
    styling.prYellow('\n\
    Checking...')
    if (check_existing_configs() == False):
      styling.prRed('\n\
      No existing KBK configuration has been found.')
      choice = input('\n\
      Do you want to go back to the main menu? [Y/n]: ')
      if choice.startswith('n') or choice.startswith('n'):
        choice = input('\n\
        Do you want to close the program? [Y/n]: ')
        if choice.startswith('n') or choice.startswith('N'):
          main_menu()
        else:
          os.system('clear')
          quit()
      else:
        styling.prGreen('\n\
    Going back to the main menu...')
        print('\n\
  ##################################################')
        print_main_menu()
        main_menu()
    elif (check_existing_config() == True):
      ask_to_delete_config()
  elif choice == 4 or choice.startswith('4') or choice.startswith('q') or choice.startswith ('Q'):
    quit()
  else:
    styling.prRed('Invalid input.')
    main_menu()

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
print_main_menu()
main_menu()

