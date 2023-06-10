import urllib.request,urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

def html_read(url):
  html = urllib.request.urlopen(url).read()
  soup=BeautifulSoup(html,'html.parser')
  return soup

# Web scrap les href de toutes les pages d'un site à partir d'un DNS donné 
# ! ne s'occupe pas des sous-domaines
def get_dns_href(dns):
  soup=html_read(dns)
  href=[] #liste qui contiendra tout les href 'externes'
  in_href=[] # liste qui contiendra tout les href 'internes'
  checked_href=[] # liste qui va permettre de vérifier les url  déjà 'scrappées'
  counts_href={} # dict qui permettra de compter le nombre de fois donc certaines url sont répétées
  counts_dns={} # variante pour compter le nombre de référence à un dns
  # première boucle à partir du DNS 'mère' pour initialiser 
  for link in soup.find_all('a'):
    if link.startswith(dns): #si le lien 
      in_href.append(link)
    else:  
      href.append(link.get('href'))
  checked_href.append(dns)
  in_href=list(dict.fromkeys(in_href)) # suppr doublons
  while in_href-checked_href != []: # tant que il y a des nouveaux liens internes qui n'ont pas été extraits, on web-scrap 
    for in_a in in_href:
      soup=html_read(in_a)
      for link in soup.find_all('a'):
        if link.startswith(dns):  # on pourra modifier cette ligne pour so'ccuper des sous-domaines
          in_href.append(link)
          in_href=list(dict.fromkeys(in_href)) # suppr doublons
        else:  
          href.append(link.get('href'))
      checked_href.append(in_a)
  for link in href:
    counts_href[link]=counts_href.get(link,0) + 1 
  for link in href:
    # un peu de regex ...: récupère le domaine sans le protocole ni le "www."
    ext_dns=re.findall('.*\://(?:www.)?([^\/]+)',link) 
    counts_dns[ext_dns]=counts_dns.get(ext_dns,0)+1
  return counts_href,in_href
