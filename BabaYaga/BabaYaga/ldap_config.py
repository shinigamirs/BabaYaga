import subprocess
import hashlib

def check_ldap_connection(data):
    try:
        ldap_server_uri = data.get("ldap_server_uri")
        ldap_bind_dn = data.get("ldap_bind_dn")
        ldap_search = data.get("ldap_search")
        ldap_bind_password = data.get("ldap_bind_password")
    except KeyError:
        return False
    cmd = "ldapsearch -H \"" + ldap_server_uri + "\" -D \"" + ldap_bind_dn + "\" -w \"" +  ldap_bind_password \
          + "\" -b \"" + ldap_search + "\" | " + "grep result"
    try:
        connection = ""
        connection = subprocess.check_output(cmd, shell=True).decode()
        connection = connection.split()
        if "0" and "Success" in connection:
            return True
        return False
    except Exception as e:
        return False

def md5_generator(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
