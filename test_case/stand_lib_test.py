import glob
import shutil
import os
import sys

from api.baseApi import log
logger = log()

sys.stderr.write('one two\n')
sys.exit(101)

file_list = glob.glob('*.py')
logger.info(file_list)
logger.info(sys.argv)


cwd = os.getcwd()
logger.info('cwd: %s' % cwd)
os.chdir('../report')
cwd_1 = os.getcwd()
logger.info('cwd_1: %s' % cwd_1)
os.system('mkdir wsp_dir')
# print(dir(os))
# print(help(os))

# os.chmod('D:/pycharm/iptv/test_case', 777)
# shutil.copyfile('log.txt', 'mmm.txt')
if os.path.exists('D:/pycharm/iptv/test_case/log.txt'):
    os.unlink('D:/pycharm/iptv/test_case/log.txt')

