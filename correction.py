#!/usr/bin/env python3

__module_name__ = 'Correction'
__module_version__ = '0.1'
__module_description__ = 'Replace an expression with another in a past message'

import hexchat

messages = []

def s(word, word_eol, userdata):
    source = word[1]
    dest = word[2]

    #look for first message from user containing 'source' then replace 'source'
    #with 'dest' with highlight and say in channel
    for message in messages:
        if source in message:
            newmessage = 'Correction: ' + message.replace(source, '\002*' + dest +'*\017')
            hexchat.command('say ' + newmessage)
            break

def onMessage(word, word_eol, userdata):
    #keep last 10 messages we send
    messages.insert(0, word[1])
    if len(messages) > 10:
        del messages[-1]


print('In channel message correction script loaded')
hexchat.hook_print('Your Message', onMessage)
hexchat.hook_command('s', s, help='usage: /s <source> <dest> - replaces source with dest in last message containing source and resends it')