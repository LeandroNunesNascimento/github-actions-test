import sys
import re
import json
import os
import logging
from datetime import  datetime
import requests
import shutil
import subprocess as sp
import time
import urllib3

urllib3.disable_warnings()

access_token = os.environ["access_token"]

def chamada_api_func():
    github_url='https://api.github.com/repos/LeandroNunesNascimento'

    teste1='rulesets'

    url_put=github_url+'/'+linha+'/'+teste1

    print(url_put)

    payload='{"name": {sys.argv[1]},"enforcement":"active"}'
    print(payload)

    response='
    result_expected='<Response [201]>'
    max_trying=3
    
    index=0
    while(index<max_trying):
        response = requests.post(url_put,
            headers={'Content-Type':'application/json',
                     'Authorization': f'Bearer {access_token}'},
                    data=payload,
                    verify=False)
        logging.info(response)
        logging.info(response.headers)
        logging.info(response.content)
        print(response)

        if str(response) == result_expected:
            index=3
        #index=1
        result_expected='<Response [201]>'

        time.sleep(5)

lista_repo_db = open("lista_repo.txt", "r")
linhas =  lista_repo_db.readlines()
global linha

for linha in linhas:
    linha = linha.rstrip('\n')
    print (linha)
    chamada_api_func()
    time.sleep(6)

    f = open('repo_processado.txt','at')
    f.write('{}\n'.format(linha + " - OK"))
    f.close()
