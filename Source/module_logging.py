import os
import logging
import module_os
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('test.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)
stream_handler=logging.StreamHandler()
logger.addHandler(stream_handler)
# logging.basicConfig(filename="/test.log",level=logging.DEBUG,format='%(asctime)s:%(name)s:%(message)s')

def add(x,y):
    logger.debug("Add:{} ".format(x+y))

def subs(x,y):
    try:
        if x<y:
            raise Exception(ZeroDivisionError)

        else:
            logger.debug("Substract:{}".format(x-y))
    except :
        logger.exception("dddsdsd")

add(10,12)
subs(10,12)
# for dirpath,foldepath,filepath in os.walk('C:\\Python37\\Learnings'):
#     print("Dirpath: ",dirpath)
#     print("Folderpath: ",foldepath)
#     print("Filepath: ",filepath)
#     print()
# print()