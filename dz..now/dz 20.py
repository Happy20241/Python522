import os


def info_files(root, folder):
    for root, dirs, files in os.walk(root):
        for file in files:
            file_path = os.path.join(root, file)
            # print(file_path)
            file_size = os.path.getsize(file_path)
            if file_size == 0:
                os.renames(file_path, os.path.join(folder, file))
                print(f"файл {file} перемещён из папки {root} в папку {folder}")
            else:
                print(f"{file_path} - {file_size} bytes")


info_files("Work", "Work/empty_files")
