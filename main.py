from controlers import *


def main():
    while True:
        list_all_tables()

        choix_action = input("(C)réer / (A)fficher / (M)odifier / (S)upprimer : ").upper()

        if choix_action == "M":
            choix_tableau = input("Quel tableau souhaitez-vous modifier ? (P)lante / (F)amille / (S)ous-classe / (I)ndication / Partie (U)tilisée ").upper()
            if choix_tableau == "P":
                table = Plante.select()
                for row in table:
                    print(row.id, row.name)
                choix_id = input("Entrez l'id de la ligne à modifier: ")
                field = input("Que souhaitez-vous modifier ? (N)om / (P)rix / (I)ndication / Partie (U)tilisée / (F)amille").upper()
                update = input("Entrez la nouvelle valeur à appliquer: ")
                if field == "N" or field == "P" or field == "I" or field == "U" or field == "F":
                    validation = update_table(field=field, table=choix_tableau, update=update, instance_id=choix_id)
                    print(validation)
                    continue
                else:
                    print("Commande non reconnue. Recommencez.")
                    continue

            elif choix_tableau == "F":
                table = Famille.select()
                for row in table:
                    print(row.id, row.name)
                choix_id = input("Entrez l'id de la ligne à modifier: ")
                field = input("Que souhaitez-vous modifier ? (N)om / Nom (F)rançais / (S)ous-classe").upper()
                update = input("Entrez la nouvelle valeur à appliquer: ")
                if field == "N" or field == "F" or field == "S":
                    validation = update_table(field=field, table=choix_tableau, update=update, instance_id=choix_id)
                    print(validation)
                    continue
                else:
                    print("Commande non reconnue. Recommencez.")
                    continue

            elif choix_tableau == "S":
                table = SousClasse.select()
                for row in table:
                    print(row.id, row.name)
                choix_id = input("Entrez l'id de la ligne à modifier: ")
                field = input("Que souhaitez-vous modifier ? (N)om / Nom (F)rançais").upper()
                update = input("Entrez la nouvelle valeur à appliquer: ")
                if field == "N" or field == "F":
                    validation = update_table(field=field, table=choix_tableau, update=update, instance_id=choix_id)
                    print(validation)
                    continue
                else:
                    print("Commande non reconnue. Recommencez.")
                    continue

            elif choix_tableau == "I":
                table = IndicationPlante.select()
                for row in table:
                    print(row.id, row.name)
                choix_id = input("Entrez l'id de la ligne à modifier: ")
                field = input("Que souhaitez-vous modifier ? (N)om").upper()
                update = input("Entrez la nouvelle valeur à appliquer: ")
                if field == "N":
                    validation = update_table(field=field, table=choix_tableau, update=update, instance_id=choix_id)
                    print(validation)
                    continue
                else:
                    print("Commande non reconnue. Recommencez.")
                    continue

            elif choix_tableau == "U":
                table = PartieUtilisee.select()
                for row in table:
                    print(row.id, row.name)
                choix_id = input("Entrez l'id de la ligne à modifier: ")
                field = input("Que souhaitez-vous modifier ? (N)om ").upper()
                update = input("Entrez la nouvelle valeur à appliquer: ")
                if field == "N":
                    validation = update_table(field=field, table=choix_tableau, update=update, instance_id=choix_id)
                    print(validation)
                    continue
                else:
                    print("Commande non reconnue. Recommencez.")
                    continue

            else:
                print("Commande invalide. Recommencez.")
                continue

        elif choix_action == "A":
            choix_tableau = input("Quel tableau souhaitez-vous afficher ? (P)lante / (F)amille / (S)ous-classe / "
                                  "(I)ndication / Partie (U)tilisée").upper()
            if choix_tableau == "P":
                table = Plante.select()
                for row in table:
                    print(row.id, row.name, row.price, row.id_indication, row.id_famille, row.id_used_part)
            elif choix_tableau == "F":
                table = Famille.select()
                for row in table:
                    print(row.id, row.name, row.name_french, row.id_sous_classe)
            elif choix_tableau == "S":
                table = SousClasse.select()
                for row in table:
                    print(row.id, row.name, row.name_french)
            elif choix_tableau == "I":
                table = IndicationPlante.select()
                for row in table:
                    print(row.id, row.name)
            elif choix_tableau == "U":
                table = PartieUtilisee.select()
                for row in table:
                    print(row.id, row.name)
            else:
                print("Commande non reconnue. Recommencez.")
        result = average_indication_price()
        for average_price, indication in result.tuples():
            print(indication, average_price)

        result2 = count_plants_by_family()
        for plant_count, famille in result2.tuples():
            print(famille, plant_count)

        result3 = minmax_price_by_sous_classe()
        for minprice, maxprice, sous_classe in result3.tuples():
            print(sous_classe, minprice, maxprice)

            update_table("P", "P", 9, 10)


if __name__ == '__main__':
    main()
