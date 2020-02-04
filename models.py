from peewee import *
from playhouse.dataset import DataSet

db1 = DataSet('mysql://jonathan:29072015aA@localhost/herboristerie')
db = MySQLDatabase('herboristerie', user='jonathan', password='29072015aA',
                   host='localhost', port=3306)


class BaseModel(Model):
    name = CharField()

    class Meta:
        database = db


class PartieUtilisee(BaseModel):
    used_part = CharField()

    class Meta:
        table_name = 'partie_utilisée_plantes'


class IndicationPlante(BaseModel):
    indication = CharField()

    class Meta:
        table_name = 'indications_plantes'


class SousClasse(BaseModel):
    name_french = CharField()

    class Meta:
        table_name = 'sous_classes'


class Famille(BaseModel):
    sous_classe = ForeignKeyField(SousClasse, column_name="id_sous_classe")
    name_french = CharField()

    class Meta:
        table_name = 'familles_plantes'


class Plante(BaseModel):
    price = DecimalField(30, 2)
    famille = ForeignKeyField(Famille, column_name='id_famille')
    id_indication = ForeignKeyField(IndicationPlante, column_name='id_indication')
    id_used_part = ForeignKeyField(PartieUtilisee, column_name='id_used_part')

    class Meta:
        table_name = 'plante'
