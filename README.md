# mqtt-consumer
A simple MQTT consumer example template using paho-mqtt.

![Integration](https://github.com/DarkbordermanTemplate/mqtt-consumer/workflows/Integration/badge.svg)
![Build](https://github.com/DarkbordermanTemplate/mqtt-consumer/workflows/Build/badge.svg)

## Development

### Prerequisitive

| Name | Version |
| --- | --- |
| Python | 3.7 |
| pipenv(Python module) | 2018.11.26 or up |

### Environment setup

0. Initialize environment variable

```
cp sample.env .env
```

1. Initialize Python environment

```
make init
```

2. Enter the environment and start developing

```
pipenv shell
```

3. Start mqtt-consumer service

```
cd mqtt/
python3 app.py
```
The service will start at 127.0.0.1:1883

### Formatting

This project uses `black` and `isort` for formatting

```
make reformat
```

### Linting

This project uses `pylint` and `flake8` for linting

```
make lint
```

### Testing

This project uses `pytest` and its extension(`pytest-cov`) for testing

## Deployment

### Prerequisitive

| Name | Version |
| --- | --- |
| Docker | 19.03.6 |
| docker-compose | 1.17.1 |

### Building image

```
docker-compose build
```
This will build the image with tag `mqtt-consumer:latest`

## Contribution

* Darkborderman/Divik(reastw1234@gmail.com)
