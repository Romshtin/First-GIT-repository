# Git Homework №2
1. Созданный репозиторий склонирован на локальный компьютер в отдельную папку `git clone`
2. Создать файл “new.json” `> new.json`
3. Добавить файл под гит `git add new.json`
4. Закоммитить файл `git commit -m 'created new.json'`
5. Отправить файл на внешний GitHub репозиторий `git push`
6. Создать файлы new2.json, new2.xml, new2.txt `touch new2.json new2.xml new2.txt`
7. Добавить файлы под гит `git add .`
8. Закоммитить файлы `git commit -m 'created files'`
9. Отправить файлы на внешний GitHub репозиторий `git push`
10. Отредактировать содержание файла “new2.txt” - написать информацию о себе (ФИО, возраст, количество домашних животных, будущая желаемая зарплата).
```sh
vim new2.txt ; i ; Kirillov Roman Aleksandrovich, age 25, 1 pet, 60000 rubles ; Esc ; :wq
```
11. Отредактировать содержание файла “new2.json” - написать информацию о себе (ФИО, возраст, количество домашних животных, будущая желаемая зарплата). Всё написать в формате JSON. 
```sh
vim new2.json ; 
 {
        "name": "Kirillov Roman Aleksandrovich",
        "age": 25,
        "pets": 1,
        "desired salary": "60000 rubles"
} 
; File ; Save ; Закрыть
```
12. Добавить и закоммитить “new2.txt” одной строчкой `git add new2.txt && git commit -m 'changes'`
13. Добавить и закоммитить “new2.json” одной строчкой `git add new2.json && git commit -m 'changes'`
14. Отправить изменения на внешний репозиторий `git push`
15. Отредактировать содержание файла “new2.xml” - написать информацию о себе (ФИО, возраст, количество домашних животных, будущая желаемая зарплата). Всё написать в формате XML.
```sh
subl new2.xml ;
 <?xml version="1.0" encoding="UTF-8"?>
	<root>
		<Name>Kirillov Roman Aleksandrovich</Name>
		<Age>25</Age>
		<Pets>1</Pets>
		<Desired_salary>60000 rubles</Desired_salary>
	</root>
; File ; Save ; Закрыть
```
16. Добавить и закоммитить “new2.xml” одной строчкой `git add new2.xml && git commit -m 'changes in new2.xml'`
17. Отправить изменения на внешний репозиторий `git push`
18. Отправить предыдущее домашнее задание по GitBash Terminal на внешний репозиторий.
```sh
mv ~/Desktop/GitBash_HomeWork_1.txt ./' ; 'git add Git_HomeWork_1.txt && git commit -m 'adding homework' && git push
```
19. В веб интерфейсе GitHub создать файл new3.txt `Add file ; Create new file ; new3.txt ; Commit new file`
20. Отредактировать в веб интерфейсе содержание файла “new3.txt” - написать информацию о своих предпочтениях (Любимый фильм, любимый сериал, любимая еда, любимое время года, страна которую хотели бы посетить).
```sh
new3.txt ; Edit this file ; Мост в Терабитию, Декстер, Пангасиус обжаренный в муке и яйце, лето, Канада.
```
21. Сделать Commit changes (сохранить) изменения на веб интерфейсе `Прокрутить страницу вниз ; Commit changes`
22. Синхронизировать внешний и локальный репозитории (слить изменения с внешнего репозитория) `git pull`
23. Отредактировать в веб интерфейсе содержание файла “new2.json” - добавить информацию о своих предпочтениях (Любимый фильм, любимый сериал, любимая еда, любимое время года, страна которую хотели бы посетить). Всё в формате JSON.
```sh
new2.json ; Edit this file ; 
 {
        "name": "Kirillov Roman Aleksandrovich",
        "age": 25,
        "pets": 1,
        "desired salary": "60000 rubles"
	"favourite film": "Мост в Терабитию",
	"favourite serial": "Декстер",
	"favourite food": "Пангасиус обжаренный в муке и яйце",
	"favourite time of year": "лето",
	"country to visit": "Канада"
}
```
24. Сделать Commit changes (сохранить) изменения на веб интерфейсе `Прокрутить страницу вниз ; Commit changes`
25. Синхронизировать внешний и локальный репозитории `git pull` 
26. Отредактировать в веб интерфейсе содержание файла “new2.xml” - добавить информацию о своих предпочтениях (Любимый фильм, любимый сериал, любимая еда, любимое время года, страна которую хотели бы посетить). Всё в формате XML.
```sh
new2.xml ; Edit this file ; 
 <?xml version="1.0" encoding="UTF-8"?>
	<root>
		<Name>Kirillov Roman Aleksandrovich</Name>
		<Age>25</Age>
		<Pets>1</Pets>
		<Desired_salary>60000 rubles</Desired_salary>
		<Favourite film>Мост в Терабитию</Favourite film>
		<Favourite serial>Декстер<Favourite serial>
		<Favourite food>Пангасиус обжаренный в муке и яйце</Favourite food>
		<Favourite time of year>лето</Favourite time of year>
		<Country to visit>Канада</Country to visit>'"
	</root>
 	
```
27. Сделать Commit changes (сохранить) изменения на веб интерфейсе `Проврутить страницу вниз ; Commit changes`
28. Синхронизировать внешний и локальный репозитории `git fetch ; git pull`
