# game-recommnendation-dnn


### Building docker image

For Raspberry:
```docker build -t game-recommend -f ./docker/Dockerfile .```

For x64:
```docker build -t game-recommend -f ./docker/Dockerfile_x64 .```


### Launching built docker image

```docker run -p 8501:9099 game-recommend```
