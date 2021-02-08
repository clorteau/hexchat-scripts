#!/usr/bin/env python3

__module_name__ = 'Rainbow'
__module_version__ = '0.1'
__module_description__ = 'Send a colorful message'

import hexchat

def r(word, word_eol, userdata):
    text = word_eol[1]
    newtext = ''

    #cycle through mIRC colors (https://www.mirc.com/colors.html) 2 to 13 and apply to
    #characters one by one, prepended with ascii character 3, skipping space
    i = 2
    for c in text:
        if (c != ' '):
            c = chr(3) + str(i) + c
            i+=1
            if (i == 14): i = 2
        newtext = newtext + c

    hexchat.command('say ' + newtext)

print('Rainbox text script loaded')
hexchat.hook_command('r', r, help='usage: /r text - Sends [text] in multiple colors')