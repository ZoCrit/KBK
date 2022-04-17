from presets import styling

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
def quit_program():
  styling.prYellow('\n\
  Exiting program...\
  ')
  styling.prCyan(styling.logo)
  quit()

