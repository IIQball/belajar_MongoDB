if __name__ == '__main__':
    import menu
    import masukan
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
            dict_user = masukan.masukan()
            col_user.insert_one(dict_user)
            print('input sukses')
            print()
            pass
        elif pilihan == 2:
            pass
        else:
            lanjut = 0