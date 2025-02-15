# Команды VSCode для Python (?)

* __git --help__ выдаёт список и назначение команд VSCode (см. ниже)
использование: 
    git [-v | --version] [-h | --help] [-C <путь>] [-c <имя>=<значение>]
        + [--exec-path[=<path>]] [--html-путь] [--man-путь] [--info-путь]
        + [-p | --paginate (--разбивать на страницы) | -P | --no-pager]       [--no-replace-objects] [--bare]
        + [--git-dir=<путь>] [--work-tree=<путь>] [--namespace=<имя>]
        + [--config-env=<имя>=<envvar>] <команда> [<args>]

## Pаспространенные команды Git, используемые в различных ситуациях:

* запустить рабочую область (см. также: руководство по помощи git)
    1. __clone__ Клонировать репозиторий в новый каталог
    2. __init__ Создайте пустой репозиторий Git или повторно инициализируйте существующий.

* работайте над текущими изменениями (см. также: git help каждый день)
    1. add Добавить содержимое файла в индекс
    2. mv Переместить или переименовать файл, каталог или символическую ссылку
    3. restore Восстановить файлы рабочего дерева
    4. rm Удалить файлы из рабочего дерева и из индекса

* просмотреть историю и состояние (см. также: изменения в справке git)
    __bisect__ Используйте двоичный поиск, чтобы найти коммит, в котором возникла ошибка.
    __diff__ Показать изменения между коммитами, коммитами и рабочим деревом и т. д.
    __grep__ Распечатать строки, соответствующие шаблону
    __log__ Показать журналы коммитов
    __show__ Показать различные типы объектов
    __status__ Показать статус рабочего дерева

* растите, отмечайте и корректируйте свою общую историю
    __branch__ Список, создание или удаление ветвей
    __commit__ Записать изменения в репозиторий
    __merge__ Соединить две или более истории развития вместе
    __rebase__ Повторно применить коммиты поверх другого базового совета
    __reset__ Сбросить текущий HEAD в указанное состояние
    __switch__ Переключить ветки
    __tag__ Создание, перечисление, удаление или проверка объекта тега, подписанного с помощью GPG.

* сотрудничать (см. также: рабочие процессы помощи git)
    __fetch__ объекты загрузки и ссылки из другого репозитория
    __pull__ Fetch из и интегрировать с другим репозиторием или локальной веткой
    __push__ Обновить удаленные ссылки вместе со связанными объектами на GitHub

* __'git help -a'__ и __'git help -g'__ перечисляют доступные подкоманды и некоторые концептуальные руководства. 
* См. «__git help <команда>__» или «__git help <концепция>__», чтобы прочитать о конкретной подкоманде или концепции.
* См. __«git help git»__ для обзора системы.