import urllib.request as urllib

def checker():
  url = input("Enter the website url : ")

  try:
    resp = urllib.urlopen(url)
    if resp.getcode() == 200:
        print(f"The website \"{url}\" is accessible")
  except Exception as e :
        print("This website is invalid or not accessible \n" , e )
    
      
   


checker()