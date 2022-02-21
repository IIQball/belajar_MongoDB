def cetak():
    import pymongo

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db_belajar = client['belajar']
    col_user = db_belajar['user']
    
    #print data
    nomor = 1
    for user in col_user.find():
        print('user ', nomor)
        print('{:<8} : {}'.format('Nama',user['nama']))
        print('{:<8} : {}'.format('Alamat',user['alamat']))
        print('{:<8} : {}'.format('No. HP',user['no.hp']))
        nomor+=1
        print()
    pass