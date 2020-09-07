# bash-microservice

This is sample dummy API microservice scraping bash.org.pl for latest quotes

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

## Usage

```bash
gunicorn -b 0.0.0.0:8000 app:app
```

## License
[MIT](https://choosealicense.com/licenses/mit/)