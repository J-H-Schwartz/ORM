from models import *


def list_all_tables():
    print(db1.tables)


def average_indication_price():
    average_indication_price_list = Plante.select(fn.round(fn.AVG(Plante.price), 2), IndicationPlante.name)\
        .join(IndicationPlante, JOIN.INNER).group_by(IndicationPlante.name)
    return average_indication_price_list


def count_plants_by_family():
    count_plants = Plante.select(fn.count(Plante.famille), Famille.name).join(Famille, JOIN.INNER).group_by(Famille.name)
    return count_plants


def minmax_price_by_sous_classe():
    minmax_price = Plante.select(fn.MIN(Plante.price), fn.MAX(Plante.price), SousClasse.name).join(Famille, JOIN.INNER).\
        join(SousClasse, JOIN.INNER).group_by(SousClasse.name)
    return minmax_price



