import os
import time
import shutil

source = ['/media/zebra/Data/projects']
bkp_dir = '/media/zebra/Data/backup'
bkp_dir_name = bkp_dir + os.sep + time.strftime('%d_%m_%Y')
now = time.strftime('%H_%M')
if not os.path.exists(bkp_dir_name):
    os.mkdir(bkp_dir_name)
print('Make a directory ', bkp_dir_name)

#zip_name = now + '.zip'
for s in source:
    zip_command = shutil.make_archive(now, 'zip', root_dir=bkp_dir_name, base_dir=s)
    move = shutil.move(now + '.zip', bkp_dir_name)

print('Your backup is create')