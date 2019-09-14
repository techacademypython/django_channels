# django_channels

### How to run project

First run redis docker

```bash
git clone https://github.com/techacademypython/django_channels.git
cd django_channels
docker-compose up --build -d
```

Second run mongodb database

```bash
cd mongodatabase/
docker-compose up --build -d
```

After all migrate and start project

```bash
python manage.py migrate
python manage.py runserver
```