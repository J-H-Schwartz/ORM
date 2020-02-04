from peewee import *

db = MySQLDatabase('herboristerie', user='jonathan', password='29072015aA',
                   host='localhost', port=3306)


class BaseModel(Model):
    name = CharField()

    class Meta:
        database = db

    def __str__(self):
        return self.name


class PartieUtilisee(BaseModel):
    name = CharField()

    class Meta:
        table_name = 'partie_utilisée_plantes'

    def update_table(field, instance_id, update):
        if field == "N":
            PartieUtilisee.update(name=update).where(PartieUtilisee.id == instance_id).execute()
            return True
        else:
            return False


class IndicationPlante(BaseModel):
    name = CharField()

    class Meta:
        table_name = 'indications_plantes'

    def update_table(field, instance_id, update):
        if field == "N":
            IndicationPlante.update(name=update).where(IndicationPlante.id == instance_id).execute()
            return True
        else:
            return False


class SousClasse(BaseModel):
    name_french = CharField()

    class Meta:
        table_name = 'sous_classes'

    def update_table(field, instance_id, update):
        if field == "N":
            SousClasse.update(name=update).where(SousClasse.id == instance_id).execute()
            return True
        elif field == "F":
            SousClasse.update(name=update).where(SousClasse.id == instance_id).execute()
            return True
        else:
            return False


class Famille(BaseModel):
    sous_classe = ForeignKeyField(SousClasse, column_name="id_sous_classe")
    name_french = CharField()

    class Meta:
        table_name = 'familles_plantes'

    def update_table(field, instance_id, update):
        if field == "N":
            Famille.update(name=update).where(Famille.id == instance_id).execute()
            return True
        elif field == "F":
            Famille.update(name_french=update).where(Famille.id == instance_id).execute()
            return True
        elif field == "I":
            Famille.update(id_sous_classe=update).where(Famille.id == instance_id).execute()
            return True
        else:
            return False


class Plante(BaseModel):
    price = DecimalField(30, 2)
    famille = ForeignKeyField(Famille, column_name='id_famille')
    id_indication = ForeignKeyField(IndicationPlante, column_name='id_indication')
    id_used_part = ForeignKeyField(PartieUtilisee, column_name='id_used_part')

    class Meta:
        table_name = 'plante'

    def update_table(field, instance_id, update):
        if field == "N":
            Plante.update(name=update).where(Plante.id == instance_id).execute()
            return True
        elif field == "P":
            Plante.update(price=update).where(Plante.id == instance_id).execute()
            return True
        elif field == "I":
            Plante.update(id_indication=update).where(Plante.id == instance_id).execute()
            return True
        elif field == "F":
            Plante.update(id_famille=update).where(Plante.id == instance_id).execute()
            return True
        elif field == "U":
            Plante.update(id_used_part=update).where(Plante.id == instance_id).execute()
            return True
        else:
            return False
