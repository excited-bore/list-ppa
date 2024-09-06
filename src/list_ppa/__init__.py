import requests
from bs4 import BeautifulSoup

def get_ppas_and_archive(url):
    """
    Scrapes the list of available PPAs from the Launchpad website.

    Args:
        url (str): The URL of the Launchpad page to scrape.

    Returns:
        list: A list of PPA names.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    ppas = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('/~'):
            user = str(href.split('/')[1]).replace('~', '') 
            pack = str(href.split('/ubuntu')[1]) 
            #print(user) 
            #print(pack)
            ppas.append(user+pack)
             
    return ppas


def main():
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    for lttr in alphabet:
        for lttr1 in alphabet:
            url = 'https://launchpad.net/ubuntu/+ppas?name_filter=' + lttr + lttr1
            ppas = get_ppas_and_archive(url)
            
            unique_ppas = []

            # traverse for all elements
            for x in ppas:
                # check if exists in unique_list or not
                if x not in unique_ppas:
                    unique_ppas.append(x) 

            for ppa in unique_ppas:
                print(ppa)

if __name__ == '__main__':
    main()

