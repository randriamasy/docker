import os
import requests

# Définition de l'adresse de l'API
api_address = 'api'
api_port = 8000

def test_content(username, password, sentence, expected_sentiment):
    for version in ['v1', 'v2']:
        r = requests.get(
            url=f'http://{api_address}:{api_port}/{version}/sentiment',
            params={'username': username, 'password': password, 'sentence': sentence}
        )
        
        try:
            response_json = r.json()
            score = response_json.get('score', 0)
            sentiment = 'positive' if score > 0 else 'negative'
        except ValueError:
            sentiment = 'undefined'
        
        test_status = 'SUCCESS' if sentiment == expected_sentiment else 'FAILURE'
        
        output = f'''
        ============================
            Content test ({version})
        ============================
        
        request done at "/{version}/sentiment"
        | username="{username}"
        | password="{password}"
        | sentence="{sentence}"
        
        expected sentiment = {expected_sentiment}
        actual sentiment = {sentiment}
        
        ==>  {test_status}
        '''
        
        print(output)
        
        if os.environ.get('LOG') == '1':
            with open('api_test.log', 'a') as file:
                file.write(output)

if __name__ == '__main__':
    test_content('alice', 'wonderland', 'life is beautiful', 'positive')
    test_content('alice', 'wonderland', 'that sucks', 'negative')
