def input():
    dict_user = {}
    dict_user['nama'] = input('{:<8} : '.format('Nama'))
    dict_user['alamat'] = input('{:<8} : '.format('alamat'))
    dict_user['no.hp'] = input('{:<8} : '.format('No. HP'))
    return dict_user