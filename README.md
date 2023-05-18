# Log


### Description


### Installation
Clone the repository to your working directory

```
git clone git@github.com:shulga-alexey/api_final_yatube.git
```

Create and activate virtual environment:

```
cd api_final_yatube
python3 -m venv venv
source env/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Check migrations:

```
python3 manage.py migrate
```

Run project:

```
python3 manage.py runserver
```