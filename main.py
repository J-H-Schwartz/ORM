from controlers import *


def main():
    list_all_tables()

    result = average_indication_price()
    for average_price, indication in result.tuples():
        print(indication, average_price)

    result2 = count_plants_by_family()
    for plant_count, famille in result2.tuples():
        print(famille, plant_count)

    result3 = minmax_price_by_sous_classe()
    for minprice, maxprice, sous_classe in result3.tuples():
        print(sous_classe, minprice, maxprice)


if __name__ == '__main__':
    main()
