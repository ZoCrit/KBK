# Important notes
- **_This is only intended to be used on M1/M1 Pro/M1 Max MacBooks_**, on which the Keyboard Brightness function key shortcuts have been removed and native macOS System Preferences do not allow you to remap them. It has not been tested with Intel MacBooks.
- Using KBK will overwrite the default shortcut of the Function Keys you map it to. (reversible)
- If you have already manually created your own _hidutil_ custom bindings, using KBK will delete them (**you will receive a warning message** and be asked for confirmation), refer to the Manual Installation section if this is the case.
- Python3 is required to run KBK. **(included by default from macOS Monterey 12.3 onwards)**

## What is KBK?
Keyboard Brightness Key is a tiny CLI utility that allows you to remap the Keyboard Brightness Up and Keyboard Brightness Down back to the function row keys, as was the case with pre-M1 MacBooks.

KBK makes use of **_hidutil_** which was released alongside the **_IOHIDEventSystemClient API_** in macOS 10.12 (Sierra). You can find more details in [Apple's Technical Note TN2450](https://developer.apple.com/library/archive/technotes/tn2450/_index.html#//apple_ref/doc/uid/DTS40017618-CH1-KEY_TABLE_USAGES).

You will be offered three mapping choices:
- **Classic**: This maps the keys to **F5 and F6**, the same position they were in on previous MacBooks. This configuration will overwrite the Dictation(F5) and Focus Mode(F6) shortcuts.
- **Left**: This maps the keys to **F3 and F4**, next to the Screen Brightness shortcuts. This configuration will overwrite the Launchpad(F3) and Spotlight(F4) shortcuts.
- **Mid**: This maps the keys to **F4 and F5**, a middle ground between the previous choices. This configuration will overwrite the Spotlight(F4) and Dictation(F5) shortcuts.

Other configurations have not been added (but will be in the future) as the remaining function keys consit of the Screen Brightness, Media Control and Volume shortcuts, which are much more frequently used. If you want to overwrite those, you can refer to the Manual Installation section in the meantime.

## Why KBK?
- A small QOL need: Unfortunately, the option to remap these keys is still missing from the native System Preferences and I found having to click multiple times through the UI each time I wanted to change the keyboard's brightness quite cumbersome.
- Minuscule program: If you're only interested in mapping these specific keys, you might dislike installing larger general purpose apps.
