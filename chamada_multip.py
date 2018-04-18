import box
import os 
from multiprocessing import Process
 
rows, columns = os.popen('stty size', 'r').read().split()

print ('1234567890' * int(round(float(columns)/10)))[:int(columns)]
for i in range(2,int(rows)):
    print(str(i) + '#' * (int(columns) - len(str(i))))

    
lst_ObjBox = []
lst_Process = []

lst_ObjBox.append(box.pyBox(30, 10, 40, 100, False, False))    
lst_ObjBox[0].create_box()

lst_ObjBox.append(box.pyBox(10, 70, 25, 120, True, False))
lst_ObjBox[1].create_box()

def multi_Box(int_Box):
    for i in range(501):
        lst_ObjBox[int_Box].box_print('Texto: ' + str(i) + ' - Process: ' + str(os.getpid()) + ' Lorem ipsum dolor sit amet, ad suas sale eam, falli suavitate corrumpit an sit. Latine viderer ex vis. Ex maiorum fuisset aliquando vix, in cum dicant gloriatur. Ei elit argumentum cum, quod blandit an eum.')

for index in range(2):
    obj_Process = Process(target=multi_Box, args=(index,))
    lst_Process.append(obj_Process)
    obj_Process.start()

# Exit the completed processes
for obj_Process in lst_Process:
    obj_Process.join()
    