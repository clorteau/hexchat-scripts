#!/usr/bin/env python3

__module_name__ = 'Rainbow'
__module_version__ = '0.2'
__module_description__ = 'Send a colorful message, or highlight a part of a message'

"""
Usage: Either type "/r some text" to send "some text" in colorful characters or
surround part of a message with "**" to only colorize that part
"""

import hexchat
import re

def colorize_text(text):
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
    newtext = newtext + chr(3) #stop colorizing
    return newtext

# colorize only what's between '**'
def colorize_part_of_text(text):
    delimiter = '**'

    if (delimiter in text):
        newtext = chr(3) #start by not colorizing in our client to see what others will see
        colorizing = False

        #split string by '**' delimiter, then walk through each part and alternate
        #colorizing and non-colorizing mode when encountering '**'
        parts = re.split('(\*\*)', text)
        for part in parts:
            if part == delimiter: colorizing = not colorizing
            #don't include that part since it's the delimiter
            else:
                if colorizing: newtext = newtext + colorize_text(part)
                else: newtext = newtext + part
        return newtext
    return text

def r(word, word_eol, userdata):
    newtext = colorize_text(word_eol[1])
    hexchat.command('say ' + newtext)

def keyPressed(word, word_eol, userdata):
    if not(word[0] == "65293"): #not "Enter"
        return
    msg = hexchat.get_info('inputbox')
    if msg is None:
        return
    msg = colorize_part_of_text(msg)
    hexchat.command("settext %s" % msg)

print('Rainbow text script loaded')
hexchat.hook_command('r', r, help='usage: /r text - Sends [text] in multiple colors')
hexchat.hook_print('Key Press', keyPressed)
