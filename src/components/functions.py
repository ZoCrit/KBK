import os, sys, time
from components import layout, navigation
from presets import configs, styling

# ADD OR REMOVE CONFIG
def create_config():
  layout.print_configuration_menu()
  choice = input('\n\
  Make your choice! (Default: 1): ') or '1'
  if navigation.chose_1(choice):
    set_classic()
  elif navigation.chose_2(choice):
    set_mid()
  elif navigation.chose_3(choice):
    set_left()
  elif navigation.chose_4(choice):
    navigation.quit_program()

def delete_config():
  styling.prYellow(styling.divider)
  styling.prYellow('\n\
  Deleting...\n\
  ')
  time.sleep(1)
  os.remove(configs.kbk_config)
  os.system(configs.clear_immediate)
  os.system('clear')
  styling.prGreen('\n\
  Success!\n\
  The existing KBK configuration file has been deleted.')
  styling.prGreen(styling.divider)


# SET CONFIGS
def set_classic():
  config = open(configs.kbk_config, mode = 'w')
  config.write(configs.classic_persist)
  config.close
  styling.prYellow(styling.divider)
  styling.prYellow('\n\
  Creating config...\n\
  ')
  time.sleep(1)
  os.system(configs.classic_immediate)
  os.system('clear')
  styling.prGreen('\n\
  Success! CLASSIC configuration is now active. (F5-F6)')
  styling.prGreen(styling.divider)
  navigation.back_to_menu()

def set_mid():
  config = open(configs.kbk_config, mode = 'w')
  config.write(configs.mid_persist)
  config.close
  styling.prYellow(styling.divider)
  styling.prYellow('\n\
  Creating config...\n\
  ')
  time.sleep(1)
  os.system(configs.mid_immediate)
  os.system('clear')
  styling.prGreen('\n\
  Success! MID configuration is now active. (F4-F5)')
  styling.prGreen(styling.divider)
  navigation.back_to_menu()

def set_left():
  config = open(configs.kbk_config, mode = 'w')
  config.write(configs.left_persist)
  config.close
  styling.prYellow(styling.divider)
  styling.prYellow('\n\
  Creating config...\n\
  ')
  time.sleep(1)
  os.system(configs.left_immediate)
  os.system('clear')
  styling.prGreen('\n\
  Success! LEFT configuration is now active. (F3-F4)')
  styling.prGreen(styling.divider)
  navigation.back_to_menu()

# MAIN MENU
def main_menu():
  choice = input('\n\
  What do you want to do? (Default: 1): ') or '1'
  if navigation.chose_1(choice):
    if check_existing_configs() == True:
      ask_to_delete_config()
    elif check_existing_configs() == False:
      create_config()
  elif navigation.chose_4(choice):
    navigation.quit_program()
  else:
    styling.prRed('\
    Invalid input.')
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
  if navigation.chose_yes(choice) == True:
    delete_config()
    ask_new_config()
  elif navigation.chose_no(choice) == True:
    navigation.back_to_menu_fast()
  else:
    styling.prRed('\
    Invalid input.')

def ask_new_config():
  choice = input("\n\
  \033[96mDo you want to create a new configuration? [Y/n]: \033[00m") or 'Y'
  if navigation.chose_yes(choice) == True:
    create_config()
  elif navigation.chose_no(choice) == True:
    navigation.back_to_menu()
  else:
    styling.prRed('\
    Invalid input.')
    ask_new_config()