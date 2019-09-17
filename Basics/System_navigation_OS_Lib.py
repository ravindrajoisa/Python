import os
os.getcwd()     // will give the path of Python where it is installed.
                // Output: 'C:\\Users\\ravkrish\\AppData\\Local\\Programs\\Python\\Python37-32'
                
os.chdir('C:\\Users\\ravkrish\\Desktop')  // to change directory
os.getcwd()     // Output: 'C:\\Users\\ravkrish\\Desktop'
                

>>> os.chdir('C:\\Users\\ravkrish\\Desktop')
>>> os.getcwd()
'C:\\Users\\ravkrish\\Desktop'
>>> os.makedirs('Folder1')
>>> os.makedirs('C:\\Users\\ravkrish\\Desktop\\Folder1\\Folder2')
>>> os.path.abspath('C:\\Users\\ravkrish\\Desktop')
'C:\\Users\\ravkrish\\Desktop'
>>> os.path.abspath('Folder2')
'C:\\Users\\ravkrish\\Desktop\\Folder2'
>>> os.path.abspath('Folder1')
'C:\\Users\\ravkrish\\Desktop\\Folder1'
>>> file_path = "C:\\Users\\ravkrish\\Desktop\\file.txt"
>>> os.path.basename(file_path)
'file.txt'
>>> os.path.dirname(file_path)
'C:\\Users\\ravkrish\\Desktop'
>>> os.path.split(file_path)
('C:\\Users\\ravkrish\\Desktop', 'file.txt')
>>> directory, filename = os.path.split(file_path)
>>> print('File:' + filename + 'is in path' + directory)
File:file.txtis in pathC:\Users\ravkrish\Desktop
>>> print('File: ' + filename + ' is in path: ' + directory)
File: file.txt is in path: C:\Users\ravkrish\Desktop
>>> os.getcwd()
'C:\\Users\\ravkrish\\Desktop'
>>> os.system('di')
1
>>> os.system('dir')
0
>>> os.path.getsize(file_path)
0
>>> os.path.getsize(file_path)
14
>>> import subprocess
>>> subprocess.check_output
<function check_output at 0x0328F348>
>>> subprocess.check_output('dir', shell = True)

>>> os.path.isdir('C:\\Users\\ravkrish\\Desktop\\file.txt')
False
>>> os.path.isfile('C:\\Users\\ravkrish\\Desktop\\file.txt')
True
>>> os.path.isdir('C:\\Users\\ravkrish\\Desktop\\Folder1\\Folder2')
True
>>> os.path.isdir('C:\\Users\\ravkrish\\Desktop\\Folder3\\Folder2')
False
