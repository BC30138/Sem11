# Google cloud functions

Для удобства разработки рекомендуется установить Google SDK: https://cloud.google.com/sdk/docs/downloads-apt-get

Далее требуется авторизоваться. В рамках данной разработки, в отсутствии реального конечного пользователся было принято решение использовать service account для авторизации разработчика. авторизация осуществляется с помощью json-файла, содержащего все необходимое для авторизации. Для этого используется следующая команда:

```
gcloud auth activate-service-account --key-file=/path/to/json
```

To deploy function:
```
sudo gcloud functions deploy resize --source=src --runtime python37 --trigger-http
```

To trigger:
```
curl -X POST https://us-central1-polytech-lab.cloudfunctions.net/resize -F "image=@data/igor-nikolaev.jpg" --output "data/server.jpg" -H "Authorization: bearer $(sudo gcloud auth print-identity-token)"
```
