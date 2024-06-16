import os
import requests

# Définition de l'adresse de l'API
api_address = 'api'
api_port = 8000

def test_authorization(username, password, endpoint, expected_status):
    r = requests.get(
        url=f'http://{api_address}:{api_port}{endpoint}',
        params={'username': username, 'password': password, 'sentence': 'test'}
    )
    
    status_code = r.status_code
    test_status = 'SUCCESS' if status_code == expected_status else 'FAILURE'
    
    output = f'''
    ============================
        Authorization test
    ============================
    
    request done at "{endpoint}"
    | username="{username}"
    | password="{password}"
    
    expected result = {expected_status}
    actual result = {status_code}
    
    ==>  {test_status}
    '''
    
    print(output)
    
    if os.environ.get('LOG') == '1':
        with open('api_test.log', 'a') as file:
            file.write(output)

if __name__ == '__main__':
    test_authorization('bob', 'builder', '/v1/sentiment', 200)
    test_authorization('bob', 'builder', '/v2/sentiment', 403)
    test_authorization('alice', 'wonderland', '/v1/sentiment', 200)
    test_authorization('alice', 'wonderland', '/v2/sentiment', 200)
