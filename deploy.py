
import os

import time

import shutil
import zipfile
from os.path import join, getsize


def zip_file(src_dir, zip_name):
    z = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(src_dir):
        fpath = dirpath.replace(src_dir, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath+filename)
    z.close()


if __name__ == "__main__":
    paths = os.listdir('elevator_dispatch_algorithm')

    for path in paths:
        if '.py' in path:
            new_path = './elevator_dispatch_GUI/bin/Release/'+path
            shutil.copyfile('elevator_dispatch_algorithm/'+path, new_path)
    print()
    zip_file('./elevator_dispatch_GUI/bin/Release/', f'{time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()) }.zip')
