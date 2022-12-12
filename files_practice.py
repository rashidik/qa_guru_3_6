#Запаковать в zip архив несколько разных файлов: pdf, xlsx, csv;

#Положить его в ресурсы;

#Реализовать чтение и проверку содержимого каждого файла из архива в виде тестов
import os, zipfile, csv, shutil
import pathlib
from pathlib import Path

path_files = 'files'  # переменная с путём до папки где лежат файлы которые будем архивировать
file_dir = os.listdir(path_files) # переменная возвращает список  содержащий имена файлов и директорий в каталоге path
file_source = pathlib.Path.cwd()
file_destination = 'resources'
get_files = os.listdir(file_source)

with zipfile.ZipFile('test.zip', mode='w', \
                     compression=zipfile.ZIP_DEFLATED) as zf: #оборачиваем процесс архивирования в zf
    for file in file_dir:  #цикл архивирования файлов из папки files в 1 архивный файл
        add_file = os.path.join(path_files, file)
        zf.write(add_file)

for file in Path(file_source).glob('test.zip'):
    shutil.move(os.path.join(file_source, file), file_destination)





#print(os.path.getsize('files/notam.pdf'))