# Speak Selected Text for Sublime Text

I threw together this plugin so I could use the Mac's text to speech system in Sublime Text. I use the "Speak selected text when key is pressed" [feature](http://support.apple.com/kb/PH11255) all the time. When Apple released Lion they changed the way this feature worked, breaking the functionality in a lot of applications. It use to just copy the selected text and read it from the clipboard, making it work in any application that allowed you to copy text. After Lion it uses an API that developers have to add into their application before the feature will work. Just from my day to day use, it seems like the old way worked better.

This plugin was designed for use with Mac OS X and is only needed with OS X 10.7 and higher.

## Installing

Use the `Package Control: Add Repository` command.

## Usage

From within Sublime Text you can use the plugin on of 3 ways.

1. Right click your selection and choose "Speak Selected Text" from the context menu.
2. Use the command palette and search for "Speak Selected Text".
3. Create a Sublime Text key-binding mapped to the "speak_selected_text" command (note that the key-binding cannot be the same as the OS shortcut, or the OS shortcut will override it).

**Note:** You can run the command again to stop the speech at any time.
