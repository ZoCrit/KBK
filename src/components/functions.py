import os
import sys
import time
from components import layout, navigation
from presets import configs, styling

# ADD OR REMOVE CONFIG
def create_config():
  layout.print_configuration_menu()
  choice = input('\n\
  Make your choice! (1-4): ') or '1'
  if navigation.chose_1(choice):
    set_classic()
  elif navigation.chose_2(choice):
    set_mid()
  elif navigation.chose_3(choice):
    set_left()
  elif navigation.chose_4(choice):
    navigation.quit_program()

def delete_config():
  os.remove(configs.kbk_config)
  styling.prYellow('\n\
  Deleting...\n\
  ')
  os.system(configs.clear_immediate)
  time.sleep(1.5)
  styling.prGreen('\n\
  Success!')
  styling.prGreen('\
  The existing KBK configuration file has been deleted.')
  styling.prGreen('\
  Going back to the main menu in...')
  time.sleep(1)
  styling.prGreen('\
  3...')
  time.sleep(1)
  styling.prGreen('\
  2...')
  time.sleep(1)
  styling.prGreen('\
  1...')
  time.sleep(1)
  start()


# SET CONFIGS
def set_classic():
  config = open(configs.kbk_config, mode = 'w')
  config.write(configs.classic_persist)
  config.close
  styling.prYellow(styling.divider)
  styling.prYellow('\n\
  Creating config...\n\
  ')
  os.system(configs.classic_immediate)
  styling.prGreen('\n\
  Success! CLASSIC configuration is now active. (F5-F6)\n\
  Going back to the main menu...')
  styling.prGreen(styling.divider)
  layout.print_main_menu()
  main_menu()

def set_mid():
  config = open(configs.kbk_config, mode = 'w')
  config.write(configs.mid_persist)
  config.close
  styling.prYellow(styling.divider)
  styling.prYellow('\n\
  Creating config...\n\
  ')
  os.system(configs.mid_immediate)
  styling.prGreen('\n\
  Success! MID configuration is now active. (F4-F5)\n\
  Going back to the main menu...')
  styling.prGreen(styling.divider)
  layout.print_main_menu()
  main_menu()

def set_left():
  config = open(configs.kbk_config, mode = 'w')
  config.write(configs.left_persist)
  config.close
  styling.prYellow(styling.divider)
  styling.prYellow('\n\
  Creating config...\n\
  ')
  os.system(configs.left_immediate)
  styling.prGreen('\n\
  Success! LEFT configuration is now active. (F3-F4)\n\
  Going back to the main menu...')
  styling.prGreen(styling.divider)
  layout.print_main_menu()
  main_menu()

# MAIN MENU
def main_menu():
  choice = input('\n\
  What do you want to do? (1-4): ')
  if navigation.chose_1(choice):
    if check_existing_configs() == True:
      ask_to_delete_config()
    elif check_existing_configs() == False:
      create_config()
  elif navigation.chose_2(choice):
    print('\n\
    Your current configuration is: ')
    choice = input('\
    Do you want to change it? [y/N]: ') or 'N'
    if choice.startswith('y') or choice.startswith('Y'):
      create_config()
    else:
      main_menu()
  elif navigation.chose_3(choice):
    print(styling.divider)
    styling.prYellow('\n\
    Checking...')
    if (check_existing_configs() == False):
      styling.prRed('\n\
      No existing KBK configuration has been found.')
      choice = input('\n\
      Do you want to go back to the main menu? [Y/n (quit)]: ')
      if choice.startswith('n') or choice.startswith('n'):
        navigation.quit_program()
      else:
        styling.prGreen('\n\
    Going back to the main menu...')
        print(styling.divider)
        layout.print_main_menu()
        main_menu()
    elif (check_existing_configs() == True):
      ask_to_delete_config()
  elif navigation.chose_4(choice):
    navigation.quit_program()
  else:
    styling.prRed('Invalid input.')
    main_menu()

def start():
  os.system('clear')
  styling.prCyan(styling.logo)
  layout.print_main_menu()
  main_menu()
# CHECKS AND ASKS
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