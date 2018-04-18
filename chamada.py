from time import sleep
import box
import os 
print "\033c"

obj_Box1 = box.pyBox(16, 1, 52, 120, False, False)        
obj_Box1.create_box()

for i in range(501):
    obj_Box1.box_print('Texto: ' + str(i) + ' Lorem ipsum dolor sit amet, ad suas sale eam, falli suavitate corrumpit an sit. Latine viderer ex vis. Ex maiorum fuisset aliquando vix, in cum dicant gloriatur. Ei elit argumentum cum, quod blandit an eum.')
    sleep(1) # Time in seconds.


import box
from text_color import text_color
from time import sleep
print "\033c"    

obj_Box1 = box.pyBox(16, 1, 20, 120, False, False)        
obj_Box1.create_box()

num_IP = dict()
num_IP['DC'] = 'dc-1'
num_IP['IP'] = '192.168.1.1'

for i in range(501):
    obj_Box1.box_print('[' + text_color.fg_Bright_Red + 'BACKUPING ' + text_color.text_reset + '] JVM on %s  -  %s \r' % ('192.168.1.' + str(i), num_IP['IP']),True)
    sleep(1) # Time in seconds.
    obj_Box1.box_print('[' + text_color.fg_Bright_Red + 'CHANGING  ' + text_color.text_reset + '] JVM on %s  -  %s \r' % ('192.168.1.' + str(i), num_IP['IP']),False)
    sleep(1) # Time in seconds.
    obj_Box1.box_print('[' + text_color.fg_Bright_Red + 'APPLYING  ' + text_color.text_reset + '] JVM on %s  -  %s \r' % ('192.168.1.' + str(i), num_IP['IP']),False)
    sleep(1) # Time in seconds.
    obj_Box1.box_print('[' + text_color.fg_Bright_Green + 'RESTARTING' + text_color.text_reset + '] JVM on %s  -  %s \r' % ('192.168.1.' + str(i), num_IP['IP']),False)
    sleep(1) # Time in seconds.
     