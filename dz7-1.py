# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок
# под конкретный проект; можно ли будет при этом расширять конфигурацию и
# хранить данные о вложенных папках и файлах (добавлять детали)?

#делал уже по разбору

import os
folder_tree = {'my_project': [{'settings': []}, {'mainapp': []}, {'adminapp': []}, {'authapp': []}]}

for key, value in folder_tree.items():
    if not os.path.exists(key):
        for item in value:
            for k in item.keys():
                os.makedirs(os.path.join(key, k))