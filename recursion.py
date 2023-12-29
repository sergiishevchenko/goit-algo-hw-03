import argparse
import os
import shutil


class DoesNotExistDirectory(Exception):
    pass


class IsNotFile(Exception):
    pass


def read_dir(path, to_dir):
    if not os.path.isdir(path):
        raise DoesNotExistDirectory('Нет такой директории.')

    elements = os.listdir(path)
    for element in elements:
        element_path = os.path.join(path, element)
        if os.path.isdir(element_path):
            try:
                read_dir(element_path, to_dir)
            except Exception as e:
                raise e
        else:
            copy_file_to_dir(element_path, to_dir)


def copy_file_to_dir(path, to_dir):
    if not os.path.isfile(path):
        raise IsNotFile('Не является файлом.')

    split_path = os.path.splitext(path)[1][1:]
    to_subdir = os.path.join(to_dir, split_path)
    os.makedirs(to_subdir, exist_ok=True)

    try:
        shutil.copy(path, to_subdir)
    except Exception as e:
       raise e


def copy_from_dir_to_dir(from_dir, to_dir):
    if not os.path.isdir(from_dir):
        raise DoesNotExistDirectory('Нет такой директории.')

    try:
        read_dir(from_dir, to_dir)
    except Exception as e:
        raise e


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('from_dir', type=str)
    parser.add_argument('to_dir', type=str)

    args = parser.parse_args()

    from_dir = args.from_dir
    to_dir = args.to_dir

    copy_from_dir_to_dir(from_dir, to_dir)

if __name__ == "__main__":
    main()

