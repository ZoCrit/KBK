from presets import styling

def print_configuration_menu():
  styling.prCyan('\n\
  ### CHOOSE YOUR CONFIGURATION ###')
  print('\
  1) Classic(F5-F6)\n\
  2) Mid (F4-F5)\n\
  3) Left (F3-F4)\n\
  4) Quit program')

def print_main_menu():
  styling.prCyan('\n\
  ### MAIN MENU ###')
  print('\
  1) Create or Edit configuration\n\
  2) Edit existing configuration\n\
  3) Delete existing configuration\n\
  4) Quit program')