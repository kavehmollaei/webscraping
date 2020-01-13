
from requests_futures import sessions
import requests
import time

session = sessions.FuturesSession()
futures = [
session.get('https://www.tasnimnews.com')
    for i in range(0,16)

]

results =[
#f.result().status_code
f.result().content  
    for f in futures:

] 
print('results : %s' % results)










'''
tic =time.time() 
url ='https://www.yahoo.com'

for i in range(0,10):
    requests.get(url)
    toc=time.time() - tic
    print(toc)
'''


'''
import requests
import time
session = requests.session()

if __name__ == "__main__":

    sites = [
            'https://www.tabnak.com',
            'https://www.yahoo.com',
        ]
    start_time = time.time()
    print(sites)

    
    
    sites = [
            'https://www.tabnak.com',
            'https://www.yahoo.com',
        
        ] *80
    for url in sites:
        print(url)
        print(f"Read {len(session.get(url).content)} from {url}")

    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")    
    '''