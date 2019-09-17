import os

directory = input('Enter directory: ')
directory = directory.strip('\n')

os.chdir(directory)
file_name = input('Filename:')

file_content = 'Howdy Ravi \n Whatsup'
fn = open(file_name, 'wt')
fn.write(file_content)
fn.close()
