# Important notes
- **_This is only intended to be used on M1/M1 Pro/M1 Max MacBooks_**, on which the Keyboard Brightness function key shortcuts have been removed and native macOS System Preferences do not allow you to remap them. It has not been tested with Intel MacBooks.
- Using KBK will overwrite the default shortcut of the Function Keys you map it to. (reversible)
- If you have already manually created your own _hidutil_ custom bindings, using KBK will delete them (**you will receive a warning message** and be asked for confirmation). If you still want to use this, refer to the [Manual Configuration](#manual-configuration) section.
- Python3 is required to run KBK. **(included by default from macOS Monterey 12.3 onwards)**
- No installation is required.
## What is KBK?
**Keyboard Brightness Key** is a tiny CLI utility that allows you to remap the Keyboard Brightness Up and Keyboard Brightness Down back to the function row keys, as was the case with pre-M1 MacBooks.

KBK makes use of **_hidutil_** which was released alongside the **_IOHIDEventSystemClient API_** in macOS 10.12 (Sierra). You can find more details in [Apple's Technical Note TN2450](https://developer.apple.com/library/archive/technotes/tn2450/_index.html#//apple_ref/doc/uid/DTS40017618-CH1-KEY_TABLE_USAGES).

You will be offered three mapping choices:
- **Classic**: This maps the keys to **F5 and F6**, the same position they were in on previous MacBooks. This configuration will overwrite the Dictation(F5) and Focus Mode(F6) shortcuts.
- **Left**: This maps the keys to **F3 and F4**, next to the Screen Brightness shortcuts. This configuration will overwrite the Launchpad(F3) and Spotlight(F4) shortcuts.
- **Mid**: This maps the keys to **F4 and F5**, a middle ground between the previous choices. This configuration will overwrite the Spotlight(F4) and Dictation(F5) shortcuts.

Other configurations have not been added (but will be in the future) as the remaining function keys consist of the Screen Brightness, Media Control and Volume shortcuts, which are much more frequently used. If you want to overwrite those, you can refer to the [Manual Configuration](#manual-configuration) section in the meantime.

## Why KBK?
- A small QOL need: Unfortunately, the option to remap these keys is still missing from the native System Preferences and I found having to click multiple times through the UI each time I wanted to change the keyboard's brightness quite cumbersome.
- Minuscule program: If you're only interested in mapping these specific keys, you might dislike installing larger general purpose apps.
- _Needed an excuse to learn a little about Pythons syntax..._

## How to use
### Method 1 - CLI (Recommended)
1. `$ git clone https://github.com/ZoCrit/KBK.git` (or manually download and extract the ZIP file)
2. `$ cd YOUR_DOWNLOAD_PATH/KBK/src`
3. `$ python3 kbk.py`
4. Start KBK (press Enter, or type 1 and Enter). You'll either be asked to:
    - Create a new configuration
    - Delete your existing one (if any is detected)
      - [Screenshots](#screenshots)
### Method 2 - Bash script
1. `$ git clone https://github.com/ZoCrit/KBK.git` (or manually download and extract the ZIP file)
2. `$ cd YOUR_DOWNLOAD_PATH/KBK/src`
3. `$ sh kbk_bash_YOURCONFIGCHOICE.sh` **or** `$ bash kbk_bash_YOURCONFIGCHOICE.sh`
  - If you can't open it, use `$ chmod +x kbk_bash_YOURCONFIGCHOICE.sh` then repeat step 3
  

## Manual Configuration
**Adding configuration**
1. Navigate to `/Library/LaunchAgents` (if the LaunchAgents folder doesn't exist, create it)
2. Create a file called `com.local.KeyRemapping.plist`
3. Open it with the text editor of your choice
4. Paste the text that corresponds to your configuration of choice ([Presets (plist)](#presets-plist))
5. Open the terminal
6. Use the command that corresponds to your fongiruation of choice ([Presets (terminal)](#presets-terminal))

**Removing configuration**
1. Navigate to `/Library/LaunchAgents`
2. Delete `com.local.KeyRemapping.plist` 
3. Open the terminal and run `$ hidutil property --set '{"UserKeyMapping":[]}'`

### Presets (plist)
**Classic configuration** 
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
    </plist>
**Mid configuration**
From the Classic configuration, change:
- `0xC000000CF` to `0xC00000221`
- `0x10000009B` to `0xC000000CF`

**Left configuration**
From the Classic configuration, change:
- `0xC000000CF` to `0xFF0100000010`
- `0x10000009B` to `0xC00000221`
    
### Presets (terminal)
**Classic configuration** 
```hidutil property --set '{"UserKeyMapping":[
      {
        "HIDKeyboardModifierMappingSrc": 0xC000000CF,
        "HIDKeyboardModifierMappingDst": 0xFF00000009
      },
      {
        "HIDKeyboardModifierMappingSrc": 0x10000009B,
        "HIDKeyboardModifierMappingDst": 0xFF00000008
      }
    ]}'
 ```
    
**Mid configuration**
From the Classic configuration, change:
- `0xC000000CF` to `0xC00000221`
- `0x10000009B` to `0xC000000CF`

**Left configuration**
From the Classic configuration, change:
- `0xC000000CF` to `0xFF0100000010`
- `0x10000009B` to `0xC00000221`
## Screenshots
<img src="https://github.com/ZoCrit/KBK/blob/main/src/extras/screenshots/main.png?raw=true" style=" width:30% "><img src="https://github.com/ZoCrit/KBK/blob/main/src/extras/screenshots/config_menu.png?raw=true" style=" width:30% "><img src="https://github.com/ZoCrit/KBK/blob/main/src/extras/screenshots/config_success.png?raw=true" style=" width:30% "><img src="https://github.com/ZoCrit/KBK/blob/main/src/extras/screenshots/delete_dialogue.png?raw=true" style=" width:30% ">

