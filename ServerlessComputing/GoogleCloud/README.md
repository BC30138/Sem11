# Google cloud functions

## Deploy

Для удобства разработки рекомендуется установить Google SDK: https://cloud.google.com/sdk/docs/downloads-apt-get

Далее требуется авторизоваться. В рамках данной разработки, в отсутствии реального конечного пользователся было принято решение использовать **service account** для авторизации разработчика. авторизация осуществляется с помощью json-файла, содержащего все необходимое для авторизации. Для этого используется следующая команда:

```
gcloud auth activate-service-account --key-file=/path/to/json
```

Где **/path/to/json** - путь до json-файла, содержащего данные о **service account**.

Для того, чтобы развернуть написанную функцию на google cloud требуется выполнить следующую команду:

```
sudo gcloud functions deploy function_name --source=/path/to/source --runtime python37 --trigger-http
```

Где:

- **function_name** - имя функции в google cloud ([как создать функцию в google cloud](https://cloud.google.com/functions/docs/quickstart-console)). В нашем случае название функции - **resize**.
- **/path/to/source** (В нашем случае **src/resize**) - путь к директории, содержащей исходный код функции. Сама функция должна содержаться в файле **main.py**. Если были использованы дополнительные библиотеки, то их следует указать в **requirements.txt**, файл должен содержаться в той же директории, где **main.py**. Подробнее о написании функций - https://cloud.google.com/functions/docs/writing/

## Test

Для тестирования можно использовать скрипт **src_client/client.py**.

Тестировать можно так же локально. Для этого требуется запустить скрипт **src/test.py**, необходимые пакеты для скрипта содержаться в файле **requirements.txt** в корне проекта.
