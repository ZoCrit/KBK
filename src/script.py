import os
from text_color_preset import prRed, prGreen, prYellow, prCyan

kbk_config_file_path = '{}/Library/LaunchAgents/com.local.KeyRemapping.plist'.format(os.path.expanduser('~'))

set_classic_immediate = '''
        hidutil property --set '{"UserKeyMapping":[
      {
        "HIDKeyboardModifierMappingSrc": 0xC000000CF,
        "HIDKeyboardModifierMappingDst": 0xFF00000009
      },
      {
        "HIDKeyboardModifierMappingSrc": 0x10000009B,
        "HIDKeyboardModifierMappingDst": 0xFF00000008
      }
    ]}'
    '''
set_classic_persist_reboot = '''<?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
        <key>Label</key>
        <string>com.local.KeyRemapping</string>
        <key>ProgramArguments</key>
        <array>
            <string>/usr/bin/hidutil</string>
            <string>property</string>
            <string>--set</string>
            <string>{"UserKeyMapping":[
                {
                  "HIDKeyboardModifierMappingSrc": 0xC000000CF,
                  "HIDKeyboardModifierMappingDst": 0xFF00000009
                },
                {
                  "HIDKeyboardModifierMappingSrc": 0x10000009B,
                  "HIDKeyboardModifierMappingDst": 0xFF00000008
                }
            ]}</string>
        </array>
        <key>RunAtLoad</key>
        <true/>
    </dict>
    </plist>'''

def create_config():
  choice = input('\
  1) Classic (F5-F6)\n\
  2) Shifted (F3-F4)\n\
  Which one would you like? ') or '1'
  if choice == 1 or choice == '1' or choice.startswith('c') or choice.startswith('C'):
    os.system(set_classic_immediate)
    config = open(kbk_config_file_path, mode = 'w')
    config.write(set_classic_persist_reboot)
    config.close
  elif choice == 2 or choice == '2' or choice.startswith('s') or choice.startswith('S'):
    os.system('''
        hidutil property --set '{"UserKeyMapping":[
      {
        "HIDKeyboardModifierMappingSrc": 0xFF0100000010,
        "HIDKeyboardModifierMappingDst": 0xFF00000009
      },
      {
        "HIDKeyboardModifierMappingSrc": 0xC00000221,
        "HIDKeyboardModifierMappingDst": 0xFF00000008
      }
    ]}'
    ''')
    config = open(kbk_config_file_path, mode = 'w')
    config.write('''<?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
        <key>Label</key>
        <string>com.local.KeyRemapping</string>
        <key>ProgramArguments</key>
        <array>
            <string>/usr/bin/hidutil</string>
            <string>property</string>
            <string>--set</string>
            <string>{"UserKeyMapping":[
                {
                  "HIDKeyboardModifierMappingSrc": 0xFF0100000010,
                  "HIDKeyboardModifierMappingDst": 0xFF00000009
                },
                {
                  "HIDKeyboardModifierMappingSrc": 0xC00000221,
                  "HIDKeyboardModifierMappingDst": 0xFF00000008
                }
            ]}</string>
        </array>
        <key>RunAtLoad</key>
        <true/>
    </dict>
    </plist>''')
    config.close

def check_existing_config():
  if os.path.exists(kbk_config_file_path):
    ask_to_delete_config()
  else:
    create_config()

def ask_to_delete_config():
  choice = input('A KBK configuration already exists, do you want to delete it? [y/N]: \n') or 'N'
  if choice.startswith('y') or choice.startswith('Y'):
    os.remove(kbk_config_file_path)
    os.system("hidutil property --set '{\"UserKeyMapping\":[]}'")
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


main_menu()

# ------------------------------------------------------------------------------------

# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKCYAN = '\033[96m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'


# hidutil property --set '{"UserKeyMapping":[]}'
