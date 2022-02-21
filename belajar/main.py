if __name__ == '__main__':
    import menu
    import input
    import pymongo

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db_belajar = client['belajar']
    col_user = db_belajar['user']

    print()
    
    lanjut = 1
    while lanjut == 1 :
        menu.menu()
        pilihan = int(input('Pilih : '))
        if pilihan == 1:


            pass
        elif pilihan == 2:
            pass
    
    # col_user.insert_one(dict_user)

    #hapus data
    hapus_data = {'nama': 'iqbal'}
    # col_user.delete_one(hapus_data)

    