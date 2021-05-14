import ebx_printbox
from multiprocessing import Process
from time import sleep
import os

lst_ObjBox = []
lst_Process = []

# Box(Line:30, Column: 10 to Line: 40, Column: 100 - No Border, Clear Screen)
lst_ObjBox.append(ebx_printbox.pyBox(30, 10, 40, 100, False, True))
lst_ObjBox[0].create_box()

# Box(Line:10, Column: 70 to  Line: 25, Column: 120 - With Border, No Clear Screen)
lst_ObjBox.append(ebx_printbox.pyBox(10, 70, 25, 120, True, False))
lst_ObjBox[1].create_box()


def multi_Box(int_Box):
    for i in range(501):
        lst_ObjBox[int_Box].box_print('Texto: ' + str(i) + ' - Process: ' + str(
            os.getpid()) + ' Lorem ipsum dolor sit amet, ad suas sale eam, falli suavitate corrumpit an sit. Latine '
                           'viderer ex vis. Ex maiorum fuisset aliquando vix, in cum dicant gloriatur. Ei elit '
                           'argumentum cum, quod blandit an eum.')
        sleep(1)  # Time in seconds.


for index in range(2):
    obj_Process = Process(target=multi_Box, args=(index,))
    lst_Process.append(obj_Process)
    obj_Process.start()

# Exit the completed processes
for obj_Process in lst_Process:
    obj_Process.join()
