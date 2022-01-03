# Git_HW_3
1. На локальном репозитории сделать ветки для:
- Postman `git branch Postman`
- Jmeter `git branch Jmeter`
- CheckLists `git branch CheckLists`
- Bag Reports `git branch Bag_Reports`
- SQL `git branch SQL`
- Charles `git branch Charles`
- Mobile testing `git branch Mobile_testing`
***
2. Запушить все ветки на внешний репозиторий `git push --all origin -u`
3. В ветке Bag Reports сделать текстовый документ со структурой баг репорта 
```sh
git checkout Bag_reports ; > Bag_report_structure.txt ; vim  Bag_report_structure.txt ; i ; Написать структуру баг репорта ; Esc ; :wq
```
4. Запушить структуру багрепорта на внешний репозиторий `git add . && git commit -m 'Create file' && git push`
5. Вмержить ветку Bag Reports в Main `git checkout master`
6. Запушить main на внешний репозиторий `git push`
7. В ветке CheckLists набросать структуру чек листа `git checkout CheckLists ; vim CheckList_structure.txt ; i ; Набросать структуру чек листа ; Esc ; :wq`
8. Запушить структуру на внешний репозиторий `git add . && git commit -m 'Create file CheckList_structure.txt' && git push`
9. На внешнем репозитории сделать Pull Request ветки CheckLists в main `Compare & pull request ; Create pull request ; Merge ; Comment merge`
10. Синхронизировать Внешнюю и Локальную ветки Main `git checkout master ; git pull`
