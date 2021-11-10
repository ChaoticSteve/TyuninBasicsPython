import os
from shutil import rmtree


def create_starter(dir_path, dir_name, folders):
    current_path = os.path.join(dir_path, dir_name)
    if not os.path.exists(current_path):
        os.mkdir(current_path)
    for folder in folders:
        current_folder = os.path.join(current_path, folder)
        if not os.path.exists(current_folder):
            os.mkdir(current_folder)


def delete_starter(dir_path, dir_name):
    current_path = os.path.join(dir_path, dir_name)
    rmtree(current_path)


if __name__ == '__main__':
    my_name = 'my_project'
    my_path = '.'
    my_folders = ('settings', 'mainapp', 'adminapp', 'authapp')
    try:
        create_starter(my_path, my_name, my_folders)
        # delete_starter(my_path, my_name)
    except Exception as e:
        print(e)
