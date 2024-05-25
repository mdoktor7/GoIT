## build image
```docker build . -t mdoktor7/hw4:0.0.1```

## push image to dockerhub
```docker push mdoktor7/hw4:0.0.1```

## pull image to server
```docker pull mdoktor7/hw4:0.0.1```

## run container
```docker run --name hw4_app -v /home/storage:/storage -p 3000:3000 -p 5000:5000 mdoktor7/hw4:0.0.1```