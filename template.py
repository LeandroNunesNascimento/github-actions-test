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
repository_name = sys.argv[1]

def chamada_api_func():
    github_url='https://api.github.com/repos/LeandroNunesNascimento'

  


    url_put=github_url+'/'+repository_name

    print(url_put)


    response=''
    result_expected='<Response [201]>'
    max_trying=3
    
    
    response = requests.get(url_put,
            headers={'Content-Type':'application/json',
                     'Authorization': f'Bearer {access_token}'},
                    verify=False)
    logging.info(response)
    logging.info(response.headers)
    logging.info(response.content)
    response_data = response.json()
    print(response_data["template_repository"]["name"])

chamada_api_func()
