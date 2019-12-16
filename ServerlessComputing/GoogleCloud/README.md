# Google cloud functions

you need install gcloud SDK, than
```
gcloud init
```

to change account:
```
gcloud auth login
```

Also you can use .json credentials (API -> credentials)

To deploy function:
```
sudo gcloud functions deploy resize --source=src --runtime python37 --trigger-http
```

To trigger:
```
curl -X POST https://us-central1-polytech-lab.cloudfunctions.net/resize -F "image=@data/igor-nikolaev.jpg" --output "data/server.jpg" -H "Authorization: bearer $(sudo gcloud auth print-identity-token)"
```
