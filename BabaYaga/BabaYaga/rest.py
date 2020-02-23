from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status

from lib.decorator import rest_process_exception

import json
import subprocess
from BabaYaga.ldap_config import *

class LDAPDataSet(APIView):

    @rest_process_exception
    def post(self, request):
        data = request.data
        try:
            ldap_file_name = 'BabaYaga/ldap.json'
            md5_file_name = 'BabaYaga/md5.txt'

            if check_ldap_connection(data):
                with open(ldap_file_name, 'w') as outfile:
                    json.dump(data, outfile)

                md5_hash = md5_generator(ldap_file_name)
                with open(md5_file_name, 'w') as outfile:
                    outfile.write(md5_hash)
                subprocess.call('bash BabaYaga/restart.sh', shell=True)
                return Response(status=status.HTTP_201_CREATED)
            else:
                error = {'error' : 'LDAP connectivity error'}
                return Response(error, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            raise e
