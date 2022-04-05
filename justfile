set shell := ["powershell.exe", "-c"]

root := justfile_directory()

install:
    C:\Users\simon\AppData\Local\Programs\Python\Python38\python.exe -m venv {{root}}\.pyenv
    {{root}}\.pyenv\Scripts\activate; python -m pip install -r {{root}}/requirements.txt

start:
    {{root}}\.pyenv\Scripts\activate; python {{root}}\src\main.py

build:
    cd {{root}}\src; {{root}}\.pyenv\Scripts\activate; pyinstaller -c --onefile --distpath {{root}}\target\dist --workpath {{root}}\target\build main.py