from django.shortcuts import render
from django.http import HttpResponse
from . import models
import random,json


from hashlib import sha256

# Create your views here.

def sign_in_page_load(request):
    return render(request,'Wallet/Sign-in-page.html',{})


def words_provider(request):
    words_list=[' aberration','abhor','acquiesce','alacrity','amiable','appease','arcane','avarice','brazen','brusque','cajole','callous','candor','chide','circumspect','coerce','coherent','complacency']
    random.shuffle(words_list)
    params={
        "words_list":words_list[:12]
    }
    return HttpResponse(json.dumps(params))




def New_Account(request):
    Netword_list=["Solana","Ethereum","Bitcoin","Matic","Cardano","Avalanche","Terra"]
    Network_Pub_keys={
    }

    TokenList={
        "Solana":["SOL"],
        "Bitcoin":["BTC"],
        "Ethereum":["ETH","UNI","USDT","USDC","LUNA","BUSD","SHIB"],
        "Matic":["MATIC"],
        "Cardano":["ADA"],
        "Avalanche":[],
        "Terra":[]


    }

    # Generating Public Keys for each individual network
    obj_1=json.loads(request.GET.get('json_field'))
    
    text=""
    for i in obj_1['words']:
        text+=i
    
    print(text)


    for i in Netword_list:
        Network_Pub_keys[i]={
        
        "Public_Key": sha256((i+str(random.randint(random.randint(1,10000),random.randint(10001,200000)))).encode('utf-8')).hexdigest(),
        "Token":[{"Name":i,"Balance":0} for i in TokenList[i]]
        
        }

    


    # Generating Common Public Key Based on the Security Words

    
    # user['Common_Public_Key']=sha256(text.encode('utf-8')).hexdigest()


    if len(models.Account.objects.filter(Common_Public_Key=sha256(text.encode('utf-8')).hexdigest()))>1:
        return HttpResponse(sha256(text.encode('utf-8')).hexdigest())

    user=models.Account(Password=obj_1['password'],Network_Public_keys=Network_Pub_keys,Common_Public_Key=sha256(text.encode('utf-8')).hexdigest())

    user.save()

    

    return HttpResponse(sha256(text.encode('utf-8')).hexdigest())



def display_account_summary(request):
    return render(request,'Wallet/Account_Summary.html',{})



from Wallet.models import Account

def provide_info(request):


    pub_key=request.GET.get('pub_key')

    print("Hello world")
    user=Account.objects.filter(Common_Public_Key=pub_key)[0]
    # print(Account.objects.get(Common_Public_Key=pub_key))
    return HttpResponse(json.dumps(user.Network_Public_keys))


def import_wallet(request):
    
    obj=json.loads(request.GET.get('json'))
    user=Account.objects.filter(Common_Public_Key=sha256(''.join(obj['words']).encode('utf-8')).hexdigest())

    if(len(user)>0):
        return HttpResponse(json.dumps({"status":"Success"}))
    else:
        return HttpResponse(json.dumps({"status":"Failed"}))



