

# Редактирование дневника
Для редактирования дневника необходимо запустить django shell:
```bash
python manage.py shell
```
В файле scripts.py содержатся скрипты для работы с базой данных электронного дневника. <br>
- `fix_marks(name)` - исправляет плохие оценки ученика name; <br>
- `delete_chatisements(name)` - удаляет замечаения ученику name от учителей; <br>
- `create_commendation(name, lesson)` - создаёт похвалу ученику name на последний урок lesson. <br>


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
