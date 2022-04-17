#!/bin/bash
cd ~/Library/LaunchAgents
touch com.local.KeyRemapping.plist
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
cat <<EOF > com.local.KeyRemapping.plist
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
EOF