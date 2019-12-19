# Google cloud functions

## Deploy

Для удобства разработки рекомендуется установить Google SDK: https://cloud.google.com/sdk/docs/downloads-apt-get

Далее требуется авторизоваться. В рамках данной разработки, в отсутствии реального конечного пользователся было принято решение использовать **service account** для авторизации разработчика. авторизация осуществляется с помощью json-файла, содержащего все необходимое для авторизации. Для этого используется следующая команда:

```
gcloud auth activate-service-account --key-file=/path/to/json
```

Где **/path/to/json** - путь до json-файла, содержащего данные о **service account**.

Активировать проект для разработки
```
gcloud config set project myProject
```
где **myProject** - это активный проект. В нашем случае это polytech-lab.

Для того, чтобы развернуть написанную функцию на google cloud требуется выполнить следующую команду:

```
sudo gcloud functions deploy function_name --source=/path/to/source --runtime python37 --trigger-http
```

Где:

- **function_name** - имя функции в google cloud ([как создать функцию в google cloud](https://cloud.google.com/functions/docs/quickstart-console)). В нашем случае название функции - **resize**.
- **/path/to/source** (В нашем случае **src/resize**) - путь к директории, содержащей исходный код функции. Сама функция должна содержаться в файле **main.py**. Если были использованы дополнительные библиотеки, то их следует указать в **requirements.txt**, файл должен содержаться в той же директории, где **main.py**. Подробнее о написании функций - https://cloud.google.com/functions/docs/writing/

## Test

Для тестирования можно использовать скрипт **src_client/client.py**.

Описание флагов скрипта:
- -h, --help

    Отображает меню с помощью.
- -e, --extract

    Флаг указывает, требуется ли разархивировать полученный от сервера архив с изображениями.

- -i INPUT, --input INPUT

    INPUT указывает путь к файлу, который требуется отправить. По умолчанию **INPUT=data/example.jpg**
- -o OUTPUT, --output OUTPUT

    OUTPUT указывает путь для сохранения изображений / архива из ответа сервера. По умолчанию, если указан флаг -e **OUTPUT=data/resized_images**, иначе **OUTPUT=data/resized_images.zip**

-  -l, --local

    Флаг для тестирования локально. Для этого требуется запустить скрипт **src/test.py**, необходимые пакеты для скрипта содержаться в файле **requirements.txt** в корне проекта. Когда флаг указан - запрос осуществляется на локальную точку доступа http://127.0.0.1:8888/resize, иначе запрос отправляется на google cloud.
