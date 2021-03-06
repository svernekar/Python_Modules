import os
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('os.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
#
# logging.basicConfig(filename="os.log",level=logging.DEBUG,format='%(asctime)s:%(name)s:%(message)s')

print(dir(os))
print(os.getcwd())

os.chdir('C:\\Python37\\Learnings\\Scripts')
print(os.getcwd())
os.chdir('C:\\Python37\\Learnings\\Source')
print(os.getcwd())
# print(os.listdir('testdir'))
# os.removedirs('testdir\\testdir1')
os.rename("Module_OS.py","module_os.py")
mtime=os.stat('module_os.py').st_mtime
logger.debug(datetime.fromtimestamp(mtime))
# os.makedirs('testdir\\testdir1')


#Using os.walk()

for dirpath,foldepath,filepath in os.walk('C:\\Python37\\Learnings'):
    print("Dirpath: ",dirpath)
    print("Folderpath: ",foldepath)
    print("Filepath: ",filepath)
    print()
print()
newpath=os.path.join(os.environ.get('HOMEPATH'),"testpath.txt")
with open(newpath,'w') as f:
    f.write(("Hello \n How are you?"))

print(os.path.basename('C:\\Python37\\Learnings'))
print(os.path.split('C:\\Python37\\Learnings'))
print(os.path.dirname('C:\\Python37\\Learnings'))

print(os.path.exists('C:\\Python37\\Learning'))
print(os.path.splitext('C:\Python37\Learnings\Source\module_os.py'))
