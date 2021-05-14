# example1.py
import ebx_printbox
from time import sleep

print("\033c")

# Box(Line:16, Column: 1 to Line: 52, Column: 120 - No Border, No Clear Screen)
obj_Box1 = ebx_printbox.pyBox(16, 1, 52, 120, False, False)
obj_Box1.create_box()

for i in range(501):
    obj_Box1.box_print('Texto: ' + str(
        i) + ' Lorem ipsum dolor sit amet, ad suas sale eam, falli suavitate corrumpit an sit. Latine viderer ex vis. '
             'Ex maiorum fuisset aliquando vix, in cum dicant gloriatur. Ei elit argumentum cum, quod blandit an eum.')
    sleep(1)  # Time in seconds.

# example2.py
import ebx_printbox
from time import sleep


class text_color:
    fg_Black = "\033[0;30m"
    fg_Red = "\033[0;31m"
    fg_Green = "\033[0;32m"
    fg_Yellow = "\033[0;33m"
    fg_Blue = "\033[0;34m"
    fg_Magenta = "\033[0;35m"
    fg_Cyan = "\033[0;36m"
    fg_White = "\033[0;37m"
    fg_Bright_Black = "\033[0;90m"
    fg_Bright_Red = "\033[0;91m"
    fg_Bright_Green = "\033[0;92m"
    fg_Bright_Yellow = "\033[0;93m"
    fg_Bright_Blue = "\033[0;94m"
    fg_Bright_Magenta = "\033[0;95m"
    fg_Bright_Cyan = "\033[0;96m"
    fg_Bright_White = "\033[0;97m"
    text_reverse = "\033[;7m"
    text_underline = "\033[1;4m"
    text_reset_underline = "\033[1;24m"
    text_reset = "\033[0;0m"
    bg_Black = "\033[1;40m"
    bg_Red = "\033[1;41m"
    bg_Green = "\033[1;42m"
    bg_Yellow = "\033[1;43m"
    bg_Blue = "\033[1;44m"
    bg_Magenta = "\033[1;45m"
    bg_Cyan = "\033[1;46m"
    bg_White = "\033[1;47m"
    bg_Bright_Black = "\033[1;100m"
    bg_Bright_Red = "\033[1;101m"
    bg_Bright_Green = "\033[1;102m"
    bg_Bright_Yellow = "\033[1;103m"
    bg_Bright_Blue = "\033[1;104m"
    bg_Bright_Magenta = "\033[1;105m"
    bg_Bright_Cyan = "\033[1;106m"
    bg_Bright_White = "\033[1;107m"


obj_Box1 = ebx_printbox.pyBox(16, 1, 20, 120, False, True)
obj_Box1.create_box()

num_IP = dict()
num_IP['DC'] = 'dc-1'
num_IP['IP'] = '192.168.1.1'

for i in range(501):
    obj_Box1.box_print(
        '[' + text_color.fg_Bright_Red + 'BACKUPING ' + text_color.text_reset + '] JVM on %s  -  %s \r' % (
            '192.168.1.' + str(i), num_IP['IP']), True)
    sleep(1)  # Time in seconds.
    obj_Box1.box_print(
        '[' + text_color.fg_Bright_Red + 'CHANGING  ' + text_color.text_reset + '] JVM on %s  -  %s \r' % (
            '192.168.1.' + str(i), num_IP['IP']), False)
    sleep(1)  # Time in seconds.
    obj_Box1.box_print(
        '[' + text_color.fg_Bright_Red + 'APPLYING  ' + text_color.text_reset + '] JVM on %s  -  %s \r' % (
            '192.168.1.' + str(i), num_IP['IP']), False)
    sleep(1)  # Time in seconds.
    obj_Box1.box_print(
        '[' + text_color.fg_Green + 'RESTARTING' + text_color.text_reset + '] JVM on %s  -  %s \r' % (
            '192.168.1.' + str(i), num_IP['IP']), False)
    sleep(1)  # Time in seconds.
