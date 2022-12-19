import os, zipfile, csv, shutil, openpyxl, pytest
import pathlib
from pathlib import Path
import PyPDF2

check_file_before_run_test = 'resources/test.zip'
if os.path.exists(check_file_before_run_test):
    os.remove(check_file_before_run_test)
else:
    pass

path_files = 'files'  # переменная с путём до папки где лежат файлы которые будем архивировать
file_dir = os.listdir(path_files)  # переменная возвращает список  содержащий имена файлов и директорий в каталоге path
file_source = pathlib.Path.cwd()  # путь до папки проекта
file_destination = 'resources'  # путь до папки ресурсы
get_files = os.listdir(file_source)
extract_dir = 'extract_dir'  # папка куда будем извлекать файлы из созданного архива

with zipfile.ZipFile('test.zip', mode='w',\
                     compression=zipfile.ZIP_DEFLATED) as zf:  # оборачиваем процесс архивирования в zf
    for file in file_dir:  # цикл архивирования файлов из папки files в 1 архивный файл
        add_file = os.path.join(path_files, file)
        zf.write(add_file)

for file in Path(file_source).glob('test.zip'):  # перемещаем созданный архив в папку ресурсы
    shutil.move(os.path.join(file_source, file), file_destination)

with zipfile.ZipFile('resources/test.zip') as ext:  # экстракция файлов в папку  extract_dir
    ext.extractall(extract_dir)

with open('extract_dir/files/notam.pdf', 'rb') as pdf_file:  # открываем пдф файл
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    pdf_page = pdf_reader.getPage(0)  # открытие только 0 страницы
    pdf_text_search = pdf_page.extractText()  # оборачиваем открытый текст из пдф файла в переменную

    # функция теста поиска слова в пдф файле
def test_search_word_in_pdf():
    assert 'UTTTYOYX' in pdf_text_search


with open('extract_dir/files/ceesve.csv', newline='') as csvfile:  # открываем csv файл
    ceesve = csv.reader(csvfile)
    csv_list = ' '.join(' '.join(map(str, l)) for l in ceesve)  # записываем содержание файла в строчную переменную

    # Тест поиска слова в csv
def test_search_word_in_csv():
    assert 'trollolo' in csv_list

xlsx = openpyxl.load_workbook('extract_dir/files/excel.xlsx')
sheet = xlsx.active
#тест поиска слова в xlsx файле
def test_search_word_in_xlsx():
    assert sheet.cell(row=4, column=2).value == 'james brown'


extract_path = 'extract_dir/files'
shutil.rmtree(extract_path)


