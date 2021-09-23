user = raw_input("Username pembuat: ")

import getpass

sandi = getpass.getpass()

if sandi == 'update' and user == 'riskiakbar279':

    print "Anda Telah Login"

else:

    print "Username atau Password Anda Salah"
