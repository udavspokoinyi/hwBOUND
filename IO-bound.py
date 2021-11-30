from urllib.request import Request, urlopen
from urllib.parse import unquote
import requests
import concurrent.futures

links = open('res.txt', encoding='utf8').read().split('\n')

def get_wiki_page_existence(wiki_page_url, timeout=10):
    try:
        request = Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        resp = urlopen(request)
        code = resp.code
        return code
        resp.close()
    except Exception as e:
        return url,e
    
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for url in links:
        futures.append(executor.submit(get_wiki_page_existence, wiki_page_url=url))
    for future in concurrent.futures.as_completed(futures):
        print(future.result())