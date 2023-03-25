from peewee import *

db = SqliteDatabase('HoshHongAlice.db')


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    id = IntegerField(primary_key=True)
    user_id = TextField(unique=True)
    task = IntegerField()

    class Meta:
        table_name = "Пользователи"


class Tasks(BaseModel):
    id = IntegerField(primary_key=True)
    text = TextField()
    image = TextField()
    answer = TextField()
    explanation = TextField()
    topic = TextField()

    class Meta:
        table_name = "Задания"


Tasks.create_table()
