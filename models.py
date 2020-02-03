from peewee import *


db = MySQLDatabase('herboristerie', user='jonathan', password='29072015aA',
                   host='localhost', port=3306)


class BaseModel(Model):
    class Meta:
        database = db


class SousClasse(BaseModel):
    name = CharField()
    name_french = CharField()

    class Meta:
        table_name = 'sous_classes'


class Famille(BaseModel):
    sous_classe = ForeignKeyField(SousClasse, column_name="id_sous_classe")
    name = CharField()
    name_french = CharField()

    class Meta:
        table_name = 'familles_plantes'


class Plante(BaseModel):
    name = CharField()
    indication = CharField()
    used_part = CharField()
    price = DecimalField(30, 2)
    famille = ForeignKeyField(Famille, column_name='id_famille')

    class Meta:
        table_name = 'plante'
