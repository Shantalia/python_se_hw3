from pathlib import Path
from shutil import copyfile
from threading import Thread
import time

folders = []

def get_folders(path: Path) -> None:
    root_path = Path(source_directory)
    for el in root_path.rglob('*'):
        if el.is_dir():
            folders.append(el)


def sorter(path: Path) -> None:
    root_path = Path(source_directory)
    for el in root_path.rglob('*'):
        if el.is_file():
            ext = el.suffix[1:]
            ext_folder = final_directory / ext
            try:
                ext_folder.mkdir(parents=True, exist_ok=True)
                copyfile(el, ext_folder / el.name)
            except OSError as error:
                print(error)
 

if __name__ == "__main__":
    current_directory = Path(__file__).parent
    source_directory = current_directory / 'picture'
    final_directory = current_directory / 'dist'

    get_folders(source_directory)
    print(folders)

    threads = []
    start_time = time.perf_counter()
    for folder in folders:
        th = Thread(target=sorter, args=(folder, ))
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    end_time = time.perf_counter()
    print(f'Finish. Час виконання сортування: {end_time - start_time} секунд')