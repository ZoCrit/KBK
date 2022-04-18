import os
kbk_config = '{}/Library/LaunchAgents/com.local.KeyRemapping.plist'.format(os.path.expanduser('~'))
kbk_config_location = '{}/Library/LaunchAgents'.format(os.path.expanduser('~'))

# CLASSIC CONFIG (F5-F6)
classic_immediate = '''
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
classic_persist = '''<?xml version="1.0" encoding="UTF-8"?>
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

# MID CONFIG (F4-F5)
mid_immediate = '''
        hidutil property --set '{"UserKeyMapping":[
      {
        "HIDKeyboardModifierMappingSrc": 0xC00000221,
        "HIDKeyboardModifierMappingDst": 0xFF00000009
      },
      {
        "HIDKeyboardModifierMappingSrc": 0xC000000CF,
        "HIDKeyboardModifierMappingDst": 0xFF00000008
      }
    ]}'
    '''
mid_persist = '''<?xml version="1.0" encoding="UTF-8"?>
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
                  "HIDKeyboardModifierMappingSrc": 0xC00000221,
                  "HIDKeyboardModifierMappingDst": 0xFF00000009
                },
                {
                  "HIDKeyboardModifierMappingSrc": 0xC000000CF,
                  "HIDKeyboardModifierMappingDst": 0xFF00000008
                }
            ]}</string>
        </array>
        <key>RunAtLoad</key>
        <true/>
    </dict>
    </plist>'''

# LEFT CONFIG (F3-F4)
left_immediate = '''
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
    '''
left_persist = '''<?xml version="1.0" encoding="UTF-8"?>
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
    </plist>'''

# CLEAR CONFIG
clear_immediate = "hidutil property --set '{\"UserKeyMapping\":[]}'"
# clear_persist = 