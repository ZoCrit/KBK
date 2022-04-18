from presets import styling
from components import functions
import time, os

# MENU CHOICES
def chose_1(choice):
  if choice == 1 or choice.startswith('1') or choice.startswith('c') or choice.startswith ('C'):
    return True
def chose_2(choice):
  if choice == 2 or choice.startswith('2') or choice.startswith('e') or choice.startswith ('E'):
    return True 
def chose_3(choice):
  if choice == 3 or choice.startswith('3') or choice.startswith('d') or choice.startswith ('D'):
    return True
def chose_4(choice):
  if choice == 4 or choice.startswith('4') or choice.startswith('q') or choice.startswith ('Q'):
    return True
def chose_yes(choice):
  if choice.startswith('y') or choice.startswith('Y'):
    return True
  else:
    return False
def chose_no(choice):
  if choice.startswith('n') or choice.startswith('N'):
    return True
  else:
    return False
    
def quit_program():
  styling.prYellow('\
  Exiting...\n\
  ')
  time.sleep(0.5)
  os.system('clear')
  styling.prCyan(styling.logo_exit)
  quit()

def back_to_menu():
  styling.prGreen('\n\
  Going back to main menu in 3..')
  time.sleep(3)
  functions.start()

def back_to_menu_fast():
  styling.prGreen('\n\
  Going back to main menu...')
  time.sleep(0.5)
  functions.start()
