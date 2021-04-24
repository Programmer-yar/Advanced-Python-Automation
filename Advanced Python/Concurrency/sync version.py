"""
This program was written while learning about "Concurrency"
The topic is I/O bound programs
This is a synchronous version of the example(single threaded)
"""

import requests
import time

def download_site(url, session):
    """
    It is possible to simply use get() from requests directly,
    but creating a Session object allows requests to do some fancy
    networking tricks and really speed things up.
    """
    with session.get(url) as response:
        print(f'Read {response.content} from {url}')

def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)

if __name__ == '__main__':
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
        ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f'Downloaded {len(sites)} sites in {duration} seconds')


#result = Downloaded 160 in 78.60311031341553 seconds
    












    
