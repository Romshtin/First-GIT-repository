# Homework #1 
## Linux terminal (GitBash) commands
1) Посмотреть где я `pwd`
2) Создать папку `mkdir folder_1`
3) Зайти в папку `cd /f/qa/lesson_1_terminal/folder_1`
4) Создать 3 папки `mkdir f_1 f_2 f_3`
5) Зайти в любоую папку `cd f_1` (прописать путь к папке)
6) Создать 5 файлов (3 txt, 2 json) `touch 1.txt 2.txt 3.json 4.json 5.xml`
7) Создать 3 папки `mkdir - p d_1/d_2/d_3` (создание папки матрёшкой)
8) Вывести список содержимого папки `ls", "ls -la`
9) + Открыть любой txt файл `vim 1.txt`
10) + Написать туда что-нибудь, любой текст `i Insert text`
11) + Сохранить и выйти `Esc + :wq + Enter`
12) Выйти из папки на уровень выше `cd ..`
13) переместить любые 2 файла, которые вы создали, в любую другую папку `mv f_1/{1.txt,5.xml}  f_2`
14) скопировать любые 2 файла, которые вы создали, в любую другую папку `cp {1.txt,5.xml}  /f/qa/lesson_1_terminal/folder_1/f_2`
15) Найти файл по имени -> "find /f/ -type f -name "1.txt" "
16) просмотреть содержимое в реальном времени
```sh
grep -i insert HomeWork_1_GitBash.txt
```
```sh
tail -f  HomeWork_1_GitBash.txt
```
17) вывести несколько первых строк из текстового файла `head -n 3 HomeWork_1_GitBashtxt`

18) вывести несколько последних строк из текстового файла `tail -n 3 HomeWork_1_GitBash.txt`

19) просмотреть содержимое длинного файла (команда less) изучите как она работает `less HomeWork_1_GitBash.txt`
20) вывести дату и время -> "date"
```sh
dt=$(date '+%d/%m/%Y %H:%M:%S')
echo "$dt"
```
***

Задание со *
1) Отправить http запрос на сервер.
http://162.55.220.72:5005/object_info_3?name=Vadim&age=32&salary=1000 
```sh
curl 'http://162.55.220.72:5005/object_info_3?name=Vadim&age=32&salary=1000
```
2) Написать скрипт который выполнит автоматически пункты 3, 4, 5, 6, 7, 8, 13 ->
```sh
#!/bin/bash
cd /f/qa/lesson_1_terminal/folder_1
mkdir f_1 f_2 f_3
cd f_1
touch 1.txt 2.txt 3.json 4.json 5.xml
mkdir -p d_1/d_2/d_3
ls
ls -la
mv {1.txt,5.xml} ../f_2
```
