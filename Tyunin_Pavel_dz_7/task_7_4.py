import os


def show_stat(folder_path):
    stat = get_stat(folder_path)
    keys = list(stat)
    keys.sort()
    for key in keys:
        print(f'{key} : {stat[key]}')


def get_stat(folder_path):
    stat = {}
    list_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            size = os.stat(os.path.join(root, file))
            key = 10 ** len(str(size))
            if key in stat:
                stat[key] += 1
            else:
                stat[key] = 1
    if stat == {}:
        raise Exception('В директироии нет файлов')
    return stat


if __name__ == '__main__':
    try:
        my_folder_path = r'.'
        show_stat(my_folder_path)
    except Exception as e:
        print(e)
