from db_manage import DbManage
import os


def main():
    dbm = DbManage(
        dbms_name='postgresql', 
        login='postgres', 
        password='elephant', 
        host='localhost', 
        port='5432', 
        db_name='netology_test'
    )

    print(os.getcwd())
    publisher_name = input('enter publisher name: ')
    publisher_id = input('enter publisher id: ')

    dbm.populate_database_with_data_from_file(os.path.join(os.getcwd(), 'tests_data.json'))
    dbm.find_store_by_publisher_name(publisher_name)
    dbm.find_store_by_publisher_id(publisher_id)


if __name__ == "__main__":
    main()