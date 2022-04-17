# print('''
#  █████   ████ ███████████  █████   ████
# ░░███   ███░ ░░███░░░░░███░░███   ███░ 
#  ░███  ███    ░███    ░███ ░███  ███   
#  ░███████     ░██████████  ░███████    
#  ░███░░███    ░███░░░░░███ ░███░░███   
#  ░███ ░░███   ░███    ░███ ░███ ░░███  
#  █████ ░░████ ███████████  █████ ░░████
# ░░░░░   ░░░░ ░░░░░░░░░░░  ░░░░░   ░░░░ 
#                                       ''')

import os

home = os.path.expanduser('~')
kbk_config_file_path = f'{home}/Library/LaunchAgents/com.local.KeyRemapping.plist'
# os.chdir(f'{home}/Library/LaunchAgents')

# def create_config():
#   print('Make a choice from F1 to F12.')
#   brightness_decrease_choice = input('What would you like your DECREASE brightness key to be? [Default: F3]') or 'F3'
#   brightness_increase_choice = input('What would you like your DECREASE brightness key to be? [Default: F4]') or 'F4'
#   # os.chdir(f'{home}/Library/LaunchAgents')

# create_config()

config = open(kbk_config_file_path, mode = 'w')
config.write('''
<?xml version="1.0" encoding="UTF-8"?>
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
</plist>
''')
config.close

# def check_existing_config():
#   if os.path.exists(kbk_config_file_path):
#     ask_to_delete_config()
#   else:
#     default_decrease =
#     create_config()
#     print('Moving on')

# def ask_to_delete_config():
#   choice = input('A KBK configuration already exists, do you want to delete it? [y/N]: \n') or 'N'
#   if choice.startswith('y') or choice.startswith('Y') or len(choice) == 0:
#     os.remove(kbk_config_file_path)
#     print('The existing KBK configuration file has been deleted.')
#   else:
#     print('Exiting program')

# check_existing_config()

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

# print(bcolors.WARNING + """
# n publishing and graphic design, 
# Lorem ipsum is a placeholder text 
# commonly used to demonstrate the visual 
# form of a document or a typeface without 
# relying on meaningful content.
# """ + bcolors.ENDC)

