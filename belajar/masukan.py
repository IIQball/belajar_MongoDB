def masukan():
    dict_user = {}
    dict_user['nama'] = input('{:<8} : '.format('Nama'))
    dict_user['nim'] = input('{:<8} : '.format('NIM'))
    dict_user['angkatan'] = input('{:<8} : '.format('angkatan'))
    dict_user['alamat'] = input('{:<8} : '.format('alamat'))
    dict_user['no.hp'] = int(input('{:<8} : '.format('No. HP')))
    dict_user['nilai'] = []
    return dict_user