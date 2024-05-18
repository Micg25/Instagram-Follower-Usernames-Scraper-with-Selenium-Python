from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Firefox()
profile_link=" "  #add the link to the profile you want to scrape from
#log and adding cookies
browser.get("https://www.instagram.com/")
browser.delete_all_cookies()
browser.add_cookie({
    'name': 'csrftoken',
    'value': '', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': False,
    'secure': True,
    
})

browser.add_cookie({
    'name': 'datr',
    'value': '', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': True,
    'secure': True,
    
})
browser.add_cookie({
    'name': 'ds_user_id',
    'value': '', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': False,
    'secure': True,
    
})
browser.add_cookie({
    'name': 'ig_did',
    'value': '', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': True,
    'secure': True,
    
})
browser.add_cookie({
    'name': 'mid',
    'value': '', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': False,
    'secure': True,
    
})
browser.add_cookie({
    'name': 'ps_l',
    'value': '', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': True,
    'secure': True,
    
})
browser.add_cookie({
    'name': 'ps_n',
    'value': '', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': True,
    'secure': True,
    
})
browser.add_cookie({
    'name': 'rur',
    'value': '" "', #add value here
    'domain': '.instagram.com',
    'path': '/', 
    'expires': 'Session',
    'httponly': True,
    'secure': True,
    
})
browser.add_cookie({
    'name': 'sessionid',
    'value': '', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': True,
    'secure': True,
    
})
browser.add_cookie({
    'name': 'shbid',
    'value': '" "', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': True,
    'secure': True,
    
})
browser.add_cookie({
    'name': 'shbts',
    'value': '" "', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': True,
    'secure': True,
    
})
browser.add_cookie({
    'name': 'wd',
    'value': '', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': False,
    'secure': True,
    
})
#cookie loading over
#getting to the profile
time.sleep(2)
browser.get(profile_link) 
time.sleep(2)
#finding the "follower" element in order to click on it
elem=browser.find_element(By.XPATH,"//a[@class='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _alvs _a6hd']")
time.sleep(1)
elem.click()
time.sleep(3)
follower_scroll=browser.find_element(By.XPATH,"//div[@class='x7r02ix xf1ldfh x131esax xdajt7p xxfnqb6 xb88tzc xw2csxc x1odjw0f x5fp0pe']")  #finding the follower scroll page
time.sleep(3)
chunk=1
usernames = browser.find_elements(By.XPATH,"//span[starts-with(@class, '_ap3a')]")
while True:
    print("Taking chunk number ",chunk)
    chunk+=1
    pivot = browser.find_elements(By.XPATH,"//span[starts-with(@class, '_ap3a')]")  
    try: 
        browser.execute_script('arguments[0].scrollIntoView({block: "center", behavior: "smooth"});', usernames[len(usernames)-1]) #scrolling
    except:
        pass
    time.sleep(3)
    usernames = browser.find_elements(By.XPATH,"//span[starts-with(@class, '_ap3a')]")   
    if(usernames[len(usernames)-1].text==pivot[len(pivot)-1].text): #if the last element of the usernames fetched is the same as 
        break                                                       #the last element of the previous usernames fetched (pivot)
    print("Chunk taken")                                            #there are no more followers left to fetch
          
#saving all the usernames in a txt file   
with open("usernames.txt","w") as file:
    for username in usernames:
        file.write(username.text+"\n")

