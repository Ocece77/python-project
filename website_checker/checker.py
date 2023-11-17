#Program that check if the website exist and if its accessible

import urllib.request as urllib

def checker():
  url = input("Enter the website url : ")

  try:
    resp = urllib.urlopen(url)
    if resp.getcode() == 200: #if the response return 200,it mean that this is accessible 
        print(f"The website \"{url}\" is accessible")
  except Exception as e :
        print("This website is invalid or not accessible \n" , e )
    
checker()