#Запаковать в zip архив несколько разных файлов: pdf, xlsx, csv;

#Положить его в ресурсы;

#Реализовать чтение и проверку содержимого каждого файла из архива в виде тестов
import os, zipfile, csv, shutil
import pathlib
from pathlib import Path

import PyPDF2
from PyPDF2 import PdfFileReader

path_files = 'files'  # переменная с путём до папки где лежат файлы которые будем архивировать
file_dir = os.listdir(path_files) # переменная возвращает список  содержащий имена файлов и директорий в каталоге path
file_source = pathlib.Path.cwd() #путь до папки проекта
file_destination = 'resources' # путь до папки ресурсы
get_files = os.listdir(file_source)
extract_dir = 'extract_dir' # папка куда будем извлекать файлы из созданного архива

with zipfile.ZipFile('test.zip', mode='w', \
                     compression=zipfile.ZIP_DEFLATED) as zf: #оборачиваем процесс архивирования в zf
    for file in file_dir:  #цикл архивирования файлов из папки files в 1 архивный файл
        add_file = os.path.join(path_files, file)
        zf.write(add_file)

for file in Path(file_source).glob('test.zip'):     #перемещаем созданный архив в папку ресурсы
    shutil.move(os.path.join(file_source, file), file_destination)

with zipfile.ZipFile('resources/test.zip') as ext:   # экстракция файлов в папку  extract_dir
    ext.extractall(extract_dir)


with open('extract_dir/files/notam.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    pdf_page = pdf_reader.getPage(0)
    print(pdf_page.extractText())

