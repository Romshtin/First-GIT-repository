1. Отобразить подключённый девайс в консоли `adb devices`
2. Вывести адрес приложения todolist в системе Android 
```sh
adb shell pm list packages -f | findstr todolist (найти в системе андройда название приложения)
adb shell pm path com.android.todolist (вывести его адрес)
```
3. Установить .apk файл приложениия todolist на телефон с компьютера через  ADB `adb install -t E:\001_ToDoList-master\app\build\outputs\apk\debug\ToDoList.apk`
4. Сделать скриншот запущенного приложения todolist и сразу скопировать на компьютер в одной команде 
```sh
adb shell screencap /storage/emulated/0/DCIM/todolist.png ; adb pull /storage/emulated/0/DCIM/todolist.png C:/Users/Роман/Desktop/QA/todolist.png
```
5. Вывести в консоль логи приложения todolist `adb logcat | findstr com.android.todolist`
6. Скопировать логи приложения todolist на компьютер `adb logcat com.android.com > log.txt`
7. Удалить приложение todolist с телефона через ADB `adb uninstall com.android.todolist`
