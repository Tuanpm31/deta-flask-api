# This project using Flask API and Deta cloud to deploy

Deta link: https://www.deta.sh/

Install Deta CLI: https://docs.deta.sh/docs/micros/getting_started/

## Create new Deta project(you can choose node or python)
```bash
deta new --python name_of_project
```

## Create new venv(linux, MacOS)
```bash
python3 -m venv venv
source venv/bin/activate
```

## Install all dependencies
```bash
pip install -r requirements.txt
```


## Deploy to deta
```bash
deta deploy
```

