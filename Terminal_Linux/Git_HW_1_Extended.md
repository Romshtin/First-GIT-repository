# Git Extended Homework №1
1. Есть файл GitBash_HomeWork_1.txt (файл где описаны шаги выполнения первой домашки), сохранить этот файл локально на компьютере на диск D:\ (чтобы путь был D:\GitBash_HomeWork_1.txt). 
```sh
cp ~/Desktop/Git_repository/qa/Terminal_Linux/GitBash_HomeWork_1.txt /d/
```
2. Написать команды в одну строку в терминале, которая найдет этот файл, на основании найденного файла (GitBash_HomeWork_1.txt) скопирует содержимое файла, создаст скрипт (script_new.sh), вставит в скрипт содержимое HW1.txt и запустит его на выполнение (не более 3-х команд одной строкой в терминале).
```sh
find /d/ -type f -name GitBash_HomeWork_1.txt 2>/dev/null -exec cp {} script_new.sh \;; script_new.sh
```
