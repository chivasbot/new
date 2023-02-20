# -*- coding: utf-8 -*-
from linepy import *
from thrift.protocol import TCompactProtocol
from thrift.transport import THttpClient
from akad.ttypes import IdentityProvider, LoginResultType, LoginRequest, LoginType
from akad.ttypes import Message, Location
from line.ttypes import *
from line import SecondaryQrCodeLoginService, SecondaryQrCodeLoginPermitNoticeService
import axolotl_curve25519 as Curve25519
import axolotl_curve25519 as curve
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from multiprocessing import Pool, Process
from humanfriendly import format_timespan, parse_timespan, format_size, format_number, format_length
from threading import Thread
#from urllib.parse import (
 #   urlparse, urlsplit, urljoin, unwrap, quote, unquote,
  #  _splittype, _splithost, _splitport, _splituser, _splitpasswd,
   # _splitattr, _splitquery, _splitvalue, _splittag, _to_bytes,
    #unquote_to_bytes, urlunparse)
from urllib.error import URLError, HTTPError, ContentTooShortError
from urllib.response import addinfourl, addclosehook
from urllib.request import urlopen, urlretrieve, urlcleanup, request_host
from gtts import gTTS
#from googletrans import Translator
#from google_trans_new import google_translator
from deep_translator import GoogleTranslator
from subprocess import Popen, PIPE
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
from os.path import getmtime
#from tiktok_downloader import snaptik,ssstik,tikmate,mdown
#from TikTokApi import TikTokApi 
import pyqrcode
import png
import pyshorteners, pyimgflip, time, subprocess, youtube_dl, threading, string, requests,urllib, urllib3, urllib.parse, random, sys, json, codecs, re, os, requests, ast, pytz, atexit, traceback, base64, pafy, livejson, timeago, math, humanize, argparse
_session = requests.session()
#client = LINE("epuput4@gmail.com", passwd="setiaq15")
client = LINE("FhgaYHVNOulzAe8RGXB8.29LnzXxoCFmfH97+dCT3Ia.Y/m86hQzyNBxVTvGCKuKLHkzNCaSOxOaMFlYwy")
#client = LINE("haydenprakoso@gmail.com", passwd="setiaq15")
#client = LINE("F8lce0cdWNZMeagKzgd7.1SywK/hZsLABL4LneAuNzW.SfqQn4Pv7+Xlrv3Bb0zTo+F0Z7Ybvp67FbcRZKibhKM=")
#client = LINE("hermanfebrian1507@gmail.com", passwd="setiaq15")
#client = LINE("hermanandrian04@gmail.com", passwd="setiaq15")
#client = LINE("")
#f = open('token.txt','r')
#tkn1 = f.read()
#mid u8b0528b2c835cdd197d4b5c3d3b22d5b
client.log("Auth Token : " + str(client.authToken))
client.log("Mid : " + str(client.profile.mid))
client.log("Timeline Token : " + str(client.tl.channelAccessToken))
#f.close()
clientMid = client.profile.mid
clientProfile = client.getProfile()
clientSettings = client.getSettings()
clientPoll = OEPoll(client)
Call = client
mid = client.getProfile().mid
Bots = [mid]
botStart = time.time()
pesansOpen = codecs.open("jsons/hayden/pesan.json","r","utf-8")
audiosOpen = codecs.open("jsons/hayden/audio.json","r","utf-8")
videosOpen = codecs.open("jsons/hayden/video.json","r","utf-8")
imagesOpen = codecs.open("jsons/hayden/image.json","r","utf-8")
stickersOpen = codecs.open("jsons/hayden/sticker.json","r","utf-8")
bahasasOpen = codecs.open("jsons/hayden/bahasa.json","r","utf-8")
settingsOpen = codecs.open("jsons/hayden/settings.json","r","utf-8")
tagmeOpen = codecs.open("jsons/hayden/tag.json","r","utf-8")
drtOpen = codecs.open("jsons/hayden/dtr.json","r","utf-8")
laguanimesOpen = codecs.open("tmp/anime.json","r","utf-8")
komikanimesOpen = codecs.open("tmp/komik.json","r","utf-8")
hakusetOpen = codecs.open("cctv.json","r","utf-8")
detect2sOpen = codecs.open("jsons/hayden/detect2.json","r","utf-8")
skicksOpen = codecs.open("jsons/hayden/skick.json","r","utf-8")
detectprofile2 = json.load(detect2sOpen)
skick = json.load(skicksOpen)
pesans = json.load(pesansOpen)
audios = json.load(audiosOpen)
videos = json.load(videosOpen)
images = json.load(imagesOpen)
stickers = json.load(stickersOpen)
bahasa = json.load(bahasasOpen)
settings = json.load(settingsOpen)
tagme = json.load(tagmeOpen)
drt = json.load(drtOpen)
laguanime = json.load(laguanimesOpen)
komikanime = json.load(komikanimesOpen)
hakuset = json.load(hakusetOpen)
welcome = []
leave = []
simisimi = []
msg_dict = {}
msg_dict1 = {}
msg_dict2 = {}
msg_dict3 = {}
#temp_flood = {}
bool_dict = {
    True: ['Hidup', 'Active', 'Success', 'Open', 'On'],
    False: ['Mati', 'Not Active', 'Failed', 'Close', 'Off']
}
bot_save=[__file__]
bot_save_sc=[(f,getmtime(f)) for f in bot_save]
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
cctv = {
    "MENTION": {},
    "cyduk": False,
    "point": {},
    "sidermem": {}
}
el = {
    "stickerset":False,
    "stickers":False,
    "sid":"51626512",
    "spkg":"11538",
    "sver":"1"
    }    
status = {
    "kick": "",
    "invite": "",
    "cancel": ""
}

simple = {
    "wgetfoto": False,
    "cloneflex": False,
    "detectflex": False,
    "youtubenext":"",
    "youtubeprev":"",
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
    "convertAudio":{},
    "convertVideoFile":{},
    "convertVideo":{},
    "convertAudioFile":{},
    "convertFileVideo":{},
    "convertFileAudio":{}
}
detectprofile={
    "id":"",
    "detectprofile":[]
}
testkick={
  "group":False
}
tagmention={
  "group":False
}

#with open('jsons/hayden/pesan.j'son', 'r') as fp:
#    pesans = json.load(fp)
#with open('jsons/hayden/sticker.json', 'r') as fp:
#    stickers = json.load(fp)
#with open('jsons/hayden/image.json', 'r') as fp:
#    images = json.load(fp)
#with open('jsons/hayden/audio.json', 'r') as fp:
#    audios = json.load(fp)
#with open('jsons/hayden/video.json', 'r') as fp:
#    videos = json.load(fp)
#with open('tmp/anime.json', 'r') as fp:
#    laguanimes = json.load(fp)

myProfile["displayName"] = clientProfile.displayName
myProfile["statusMessage"] = clientProfile.statusMessage
myProfile["pictureStatus"] = clientProfile.pictureStatus

def restartBot():
    print ("[ INFO ] BOT RESTART")
    backupData()
    time.sleep(1)
    python = sys.executable
    os.execl(python, python, *sys.argv)
def saveSc():
    for f,mtime in bot_save_sc:
      if getmtime(f) != mtime:
          time.sleep(3)
          restartBot()
def backupData():
    try:
        backup = settings
        f = codecs.open('jsons/hayden/settings.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = skick
        f = codecs.open('jsons/hayden/skick.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
            
def createSecondaryQrCodeLoginService(host, headers):
    transport = THttpClient.THttpClient(host)
    transport.setCustomHeaders(headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    myclient = SecondaryQrCodeLoginService.Client(protocol)
    return myclient

def createSecondaryQrCodeLoginPermitNoticeService(host, headers):
    transport = THttpClient.THttpClient(host)
    transport.setCustomHeaders(headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    myclient = SecondaryQrCodeLoginPermitNoticeService.Client(protocol)
    return myclient
  
def genE2EESecret():
    private_key = curve.generatePrivateKey(os.urandom(32))
    public_key = curve.generatePublicKey(private_key)
    secret = urllib.parse.quote(base64.b64encode(public_key).decode())
    version = 1
    return f"?secret={secret}&e2eeVersion={version}"
    
  
def loginajs(to):
    certnya="u763c10d0fb536d8c933397453a08d662"
   # certnya="4dc2b1a7ae7a410cc96469f6821e04983300a6ae21eaad4cec89d3d3176559ee"
    host = 'https://gxx.line.naver.jp'
    qrEndpoint = '/acct/lgn/sq/v1'
    verifierEndpoint = '/acct/lp/lgn/sq/v1'
    url = host+qrEndpoint
    headers1 = {
    'User-Agent': 'Line/10.15.2',
    'X-Line-Application': 'IOSIPAD\t10.15.2\tiPad OS\t14.0.1;SECONDARY',
    'x-lal': 'en_id'
    }
    client = createSecondaryQrCodeLoginService(url, headers1)
    session = client.createSession(CreateQrSessionRequest())
    session_id = session.authSessionId
    qrcode = client.createQrCode(CreateQrCodeRequest(session_id))
    private_key = Curve25519.generatePrivateKey(os.urandom(32))
    public_key = Curve25519.generatePublicKey(private_key)
    nonce = os.urandom(16)
    secret = base64.b64encode(public_key).decode()
    e2ee = '?secret={secret}&e2eeVersion=1'.format(secret=quote(secret))
    qrcode1 = qrcode#+secret#.callbackUrl
    qrcode2 = qrcode1.callbackUrl
    Print(to,"ini link untuk induk "+qrcode2+e2ee)
    url = host+verifierEndpoint
    headers2 = {
   'User-Agent': 'Line/10.15.2',
   'X-Line-Application': 'IOSIPAD\t10.15.2\tiPad OS\t14.0.1;SECONDARY',
   'X-Line-Access': session_id,
   'x-lal': 'en_id'
    }
    client_verif = createSecondaryQrCodeLoginPermitNoticeService(url, headers2)
    qrverified = client_verif.checkQrCodeVerified(CheckQrCodeVerifiedRequest(session_id))
    certificate = certnya
    try:
      certverified = client.verifyCertificate(VerifyCertificateRequest(session.authSessionId, certificate))
    except SecondaryQrCodeException as error:
      pincode = client.createPinCode(CreatePinCodeRequest(session.authSessionId))
      #ret = "Hello @!"
      ret = "Your pincode is {}".format(pincode.pinCode)
      Print(to, ret)
      pincodeverified = client_verif.checkPinCodeVerified(CheckPinCodeVerifiedRequest(session.authSessionId))
    except Exception:
      traceback.print_exc()
    qrcodelogin = client.qrCodeLogin(QrCodeLoginRequest(session.authSessionId, 'ZidanBotsV2', True))
    mycert = qrcodelogin.certificate
    mytoken = qrcodelogin.accessToken
    ris="Header: IOSIPAD\t10.15.2\tiPad OS\t14.0.1"
    ris+="\nToken: "+str(mytoken)
    Print(to,ris)
    certnya1="u763c10d0fb536d8c933397453a08d662"
   # certnya="4dc2b1a7ae7a410cc96469f6821e04983300a6ae21eaad4cec89d3d3176559ee"
    host1 = 'https://gxx.line.naver.jp'
    qrEndpoint1 = '/acct/lgn/sq/v1'
    verifierEndpoint1 = '/acct/lp/lgn/sq/v1'
    url1 = host1+qrEndpoint1
    headers11 = {
    'User-Agent': 'Line/10.15.2',
    'X-Line-Application': 'IOSIPAD\t10.15.2\tiPad OS\t14.0.1;SECONDARY',
    'x-lal': 'en_id'
    }
    client1 = createSecondaryQrCodeLoginService(url1, headers11)
    session1 = client1.createSession(CreateQrSessionRequest())
    session_id1 = session1.authSessionId
    qrcode1 = client1.createQrCode(CreateQrCodeRequest(session_id1))
    private_key1 = Curve25519.generatePrivateKey(os.urandom(32))
    public_key1 = Curve25519.generatePublicKey(private_key1)
    secret1 = base64.b64encode(public_key1).decode()
    e2ee1 = '?secret={secret1}&e2eeVersion=1'.format(secret1=quote(secret1))
    qrcode11 = qrcode1#+secret#.callbackUrl
    qrcode21 = qrcode11.callbackUrl
    Print(to,"ini link untuk antijs "+qrcode21+e2ee1)
    url2 = host1+verifierEndpoint1
    headers21 = {
   'User-Agent': 'Line/10.15.2',
   'X-Line-Application': 'IOSIPAD\t10.15.2\tiPad OS\t14.0.1;SECONDARY',
   'X-Line-Access': session_id1,
   'x-lal': 'en_id'
    }
    client_verif1 = createSecondaryQrCodeLoginPermitNoticeService(url2, headers21)
    qrverified1 = client_verif1.checkQrCodeVerified(CheckQrCodeVerifiedRequest(session_id1))
    certificate1 = certnya1
    try:
      certverified1 = client1.verifyCertificate(VerifyCertificateRequest(session_id1, certificate1))
    except SecondaryQrCodeException as error:
      pincode1 = client1.createPinCode(CreatePinCodeRequest(session_id1))
      #ret = "Hello @!"
      ret = "Your pincode is {}".format(pincode1.pinCode)
      Print(to, ret)
      pincodeverified = client_verif1.checkPinCodeVerified(CheckPinCodeVerifiedRequest(session_id1))
    except Exception:
      traceback.print_exc()
    qrcodelogin1 = client1.qrCodeLogin(QrCodeLoginRequest(session_id1, 'ZidanBotsV2', True))
    mycert1 = qrcodelogin1.certificate
    mytoken1 = qrcodelogin1.accessToken
    ris="Header: IOSIPAD\t10.15.2\tiPad OS\t14.0.1"
    ris+="\nToken: "+str(mytoken1)
    Print(to,ris)
def kodejam(to):
    a = "Kode Jam\n"
    no = 0
    for tz in pytz.all_timezones:
      no += 1
      a += "\n"+str(no)+". "+tz
    k = len(a)//10000
    for aa in range(k+1):
       client.sendMessage(to,'{}'.format(a[aa*10000 : (aa+1)*10000]))                                
    
def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d Bulan" % (months)
    if weeks != 0: text += " %02d Minggu" % (weeks)
    if days != 0: text += " %02d Hari" % (days)
    if hours !=  0: text +=  " %02d Jam" % (hours)
    if mins != 0: text += " %02d Menit" % (mins)
    if secs != 0: text += " %02d Detik" % (secs)
    if text[0] == " ":
        text = text[1:]
    return text
        
#def delExpire():
 #   if temp_flood != {}:
  #      for tmp in temp_flood:
   #         if temp_flood[tmp]["expire"] == True:
    #            if time.time() - temp_flood[tmp]["time"] >= 3*10:
     #               temp_flood[tmp]["expi8re"] = False
      #              temp_flood[tmp]["time"] = time.time()
       #             try:
                        #userid = "https://line.me/ti/p/~" + client.profile.userid
        #                client.sendMessage(tmp, "Spam is over , Now Bots Actived !")#, str(userid), "http://dl.profile.line-cdn.net/"+client.getContact(clientMID).pictureStatus, client.getContact(clientMID).displayName)
         #           except Exception as error:
          #              logError(error9)
          
      
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
                    
def testem(to):
    appsOpen = codecs.open("tmp/app.json","r","utf-8")
    results = json.load(appsOpen)
#      {"image":"",
 #      "link":""
  #    },
#      {"image":"",
 #      "link":""
  #    },
    kw = len(results["data"])//100
    if kw >= 20:
      kw = 20
    for sd in range(kw+1):
        #time.sleep(0.7)
        kg = list(results["data"])[sd*100:(sd+1)*100]
        if kg != []:
          data = {
           "type":"carousel",
           "contents": []
          }                                
          kk = len(kg)//50
          for b in range(kk+1):
            ss = kg[b*50:(b+1)*50]   
            if ss != []:
              ii = len(ss)//5    
              data0 = {
               "type":"bubble",
               "size":"giga",
               "body":{
                  "type":"box",
                  "layout":"vertical",
                  "contents":[
                    {                      
                      "type":"box",
                      "layout":"vertical",
                      "contents":[]
                    }
                 ],
                 "borderColor": "#1E90FF",
                 "borderWidth": "2px",
                 "cornerRadius": "5px",
                 "paddingAll": "3px",
                }
              }  
              for i in range(ii+1):
                rr = ss[i*5:(i+1)*5]    
                if rr != []:
                  data1 = {
                   "type":"box",
                   "layout":"horizontal",
                   "spacing":"xs",
                   "margin":"xs",
                   "contents":[]
                  }                                                
                  for s in rr:
                    s1=s['image']
                    s2=s['link']
                    data2 ={
                       "type":"box",
                       "layout":"vertical",
                       "contents":[
                        {
                         "type": "image",
                         "url": "https://i.ibb.co/XDKG0qf/ezgif-com-gif-maker-49.png",
                         "animated":True,
                         "size": "full",
                         "aspectMode": "cover",
                         "aspectRatio": "5:1",
                         "gravity": "center"
                         },
                         {
                          "type":"box",
                          "layout":"vertical",
                           "contents":[
                             {
                              "type":"image",
                              "url":s1,
                              "size":"full",
                          #"aspectRatio":"2:3",
                          #"aspectMode": "fit",
                              "action":{
                              "type":"uri",
                              "uri":s2#"line://app/1602687308-GXq4Vvk9?type=image&img={}".format(s1)
                             }
                           }
                         ]
                        }
                      ],
                      "borderColor": "#1E90FF",
                      "borderWidth": "2px",
                      "cornerRadius": "10px",
                    }
                    data1["contents"].append(data2)
                  data0["body"]["contents"][0]["contents"].append(data1)
              data["contents"].append(data0)
          client.postFlex(to, data)
def pcf(to,text):
    coba = text
    data = {"type":"flex","altText":"Copasan Flexmu","contents":coba}
    client.postTemplate(to,data)
    
def pct(to,img):
    data = {
           "type": "template",
           "altText": "HK mengirim sticker",
           "template": {
  "type": "image_carousel",
  "columns": [
     {
     "imageUrl": img,
     "size": "full",
     "action": {
        "type": "uri",
        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(img)
        #"uri": "http://line.me/ti/p/~haydenz1"
         }
       }
    ]
  }
}
    client.postTemplate(to, data)
    
def fme(to):
    isi="http://line.me/ti/p/" + client.getUserTicket().id
    bos="ud6c61693e1f34a569b97894d11a52767"
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    wkt="{}".format(datetime.strftime(timeNow,'%H:%M'))
    bg="https://i.ibb.co/XDKG0qf/ezgif-com-gif-maker-49.png"
    cover = client.getProfileCoverURL(clientMid)
    pp="https://obs.line-scdn.net/"+str(client.getContact(clientMid).pictureStatus)
    nama=""+str(client.getContact(clientMid).displayName)
    bio=""+str(client.getContact(clientMid).statusMessage)
    li="https://i.ibb.co/fG16JTb/hkupload.png"
    ja="https://i.ibb.co/GTHtvW3/ezgif-2-47847957f443.png"
    bat="https://i.ibb.co/v31r9pb/ezgif-2-70d836e3e419.png"
    hp="https://i.ibb.co/0Dxm9LH/20210304-181025.png"
    add="https://i.ibb.co/fXFR3YP/20210308-191242.png"
    data = {
"type": "flex",
"contents":{
"type": "carousel",
"contents": [
{"type": "bubble","size": "micro","body": {"type": "box","layout": "vertical",
"contents": [{"type": "image","url": bg,"animated":True,"size": "full","aspectMode": "cover","aspectRatio": "3:5","gravity": "center"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":cover,"size":"full"}],
"position":"absolute","width":"256px","offsetTop":"5px","offsetStart":"-48px","cornerRadius":"80px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":pp,"size":"full"}],
"position":"absolute","width":"50px","offsetTop":"140px","offsetStart":"55px","cornerRadius":"75px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":li,"animated":True,"size":"full"}],
"position":"absolute","width":"11px","offsetTop":"5px","offsetStart":"75px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":ja,"animated":True,"size":"full"}],
"position":"absolute","width":"12px","offsetTop":"8px","offsetStart":"120px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":hp,"animated":True,"size":"full"}],
"position":"absolute","width":"260px","offsetTop":"2px","offsetStart":"-50px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":bat,"animated":True,"size":"full"}],
"position":"absolute","width":"15px","offsetTop":"8px","offsetStart":"130px"},
{"type":"box","layout":"horizontal","contents":[{"type":"text","text":nama,"color":"#ffffff","size":"10px","align":"center"}],
"paddingTop":"190px","position":"absolute","paddingAll":"40px"},
{"type":"box","layout":"horizontal","contents":[{"type":"text","text":bio,"color":"#ffffff","size":"8px","align":"center","wrap": False,}],
"paddingTop":"205px","position":"absolute","paddingAll":"20px"},
{"type":"box","layout":"horizontal","contents":[{"type":"text","text":wkt,"color":"#ffffff","size":"6px","wrap": False,}],
"paddingAll":"10px","position":"absolute","offsetStart":"2px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":add,"size":"full","action":{"type":"uri","uri":isi}}],
"position":"absolute","width":"30px","offsetTop":"215px","offsetStart":"65px"},
],
"paddingAll": "0px",
}}]}}
    client.postTemplate(to, data)

def fcctv(to,tmid):
    cover="https://i.ibb.co/gMJwcQ6/ezgif-2-4f58f422d12d.png"
    url="https://i.ibb.co/W2CD9df/ezgif-2-929000e97ae6.png"
    url1="https://i.ibb.co/jrGgCXG/ezgif-2-1e53be5cc864.png"
    url2="https://i.ibb.co/DVKpXX9/ezgif-2-8f08bbad797a.png"
    url3="https://obs.line-scdn.net/{}".format(client.getContact(tmid).pictureStatus)
    url4="https://i.ibb.co/bH2DyVT/ezgif-7-670fad5c343e.png"
    txt="cie masuk cctv"
    txt1=settings["mention"]
    nama="{}".format(client.getContact(tmid).displayName)
    data={
"type": "bubble",
"size": "micro",
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{"type": "image","url":cover,"size": "full","animated":True,"aspectMode": "cover","aspectRatio": "1:1","gravity": "center"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":url,"animated":True,"size":"full"}],
"position":"absolute","width":"150px","offsetTop":"5px","offsetStart":"5px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":url1,"animated":True,"size":"full"}],
"position":"absolute","width":"70px","offsetTop":"5px","offsetStart":"90px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":url2,"animated":True,"size":"full"}],
"cornerRadius": "250px","position":"absolute","width":"75px","offsetTop":"72px","offsetStart":"10px"},
{"type": "box","layout": "vertical","contents": [{"type": "image","url":url3,"size": "full"}],
"position": "absolute","cornerRadius": "50px","offsetTop": "78px","offsetStart": "16px","width": "62px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":url4,"animated":True,"size":"full"}],"cornerRadius": "250px",
"position":"absolute","width":"80px","offsetTop":"72px","offsetStart":"80px"},
{"type":"box","layout":"horizontal","contents":[{"type":"text","text":txt,"color":"#FFFFFF","weight":"bold","size":"xxs"}],
"offsetTop":"10px","position":"absolute","offsetStart":"10px"},
{"type":"box","layout":"horizontal","contents":[{"type":"text","text":txt1,"color":"#FFFFFF","weight":"bold","size":"xxs"}],
"offsetTop":"20px","position":"absolute","offsetStart":"10px"},
{"type":"box","layout":"horizontal","contents":[{"type":"text","text":nama,"color":"#FFFFFF","weight":"bold","size":"xs"}],
"offsetTop":"40px","position":"absolute","offsetStart":"10px"},
],
  "paddingAll": "0px"
 }
}
    client.postFlex(to,data)    
    
def fsmule(to,imgs,title,desc,isi):
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    wkt="{}".format(datetime.strftime(timeNow,'%H:%M'))
    fotoku="https://obs.line-scdn.net/{}".format(client.getContact(clientMid).pictureStatus)
    nama="{}".format(client.getContact(clientMid).displayName)
    txt1=title
    txt2=desc
    url="https://i.ibb.co/XDKG0qf/ezgif-com-gif-maker-49.png"
    url1="https://i.ibb.co/d5PZRnt/hkupload.jpg"
    url2="https://i.ibb.co/XF6XZWq/hkupload.jpg"
    bola="https://i.ibb.co/JBfT8Z4/ezgif-2-1f2cfed82907.png"
    foto=imgs
    url3="https://i.ibb.co/0Dxm9LH/20210304-181025.png"
    url4="https://i.ibb.co/6F8CDbC/ezgif-com-gif-maker-1.png"
    url5="https://i.ibb.co/PjjxMcd/ezgif-com-gif-maker-11.png"
    vip="https://i.ibb.co/vZzzRKY/1608833385796.png"
    play="https://i.ibb.co/M1Hj9jL/ezgif-1-61269e9e1b17.png"
    data={
"type": "bubble",
"size": "micro",
"body": 
{"type": "box","layout":"vertical","contents":[{"type":"image","url":url,"size":"full","animated":True,"aspectMode": "cover","aspectRatio":"3:5","gravity": "center"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":url1,"size":"full"}],
"position":"absolute","cornerRadius":"80px","width":"153px","offsetTop":"-41px","offsetStart":"3px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":url2,"size":"full"}],
"position":"absolute","width":"152px","offsetTop":"149px","offsetStart":"4px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":bola,"animated":True,"size":"full"}],
"position":"absolute","width":"150px","offsetTop":"50px","offsetStart":"5px","backgroundColor": "#00000040"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":url3,"size":"full"}],
"position":"absolute","width":"265px","offsetTop":"0px","offsetStart":"-52px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":url4,"size":"full","animated":True}],
"position":"absolute","width":"20px","offsetTop":"0px","offsetStart":"122px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":url5,"size":"full","animated":True}],
"position":"absolute","width":"10px","offsetTop":"4px","offsetStart":"110px"},
{"type":"box","layout":"horizontal","contents":[
  {"type":"box","layout":"horizontal","contents":[{"type":"image","url":foto,"size":"full","animated":True}],
  "offsetStart":"1px","borderWidth": "2px","borderColor": "#ffffff","cornerRadius": "2px","height": "39px","width": "39px"},
  {"type":"box","layout":"horizontal","contents":[{"type":"text","text":txt1,"color":"#ffffff","size":"8px"}],"offsetStart":"4px","paddingTop":"20px","offsetTop":"-10px",}],
  "offsetTop":"158px","position":"absolute","offsetStart":"10px","backgroundColor": "#00000040","height": "40px","width": "140px"},
{"type":"box","layout":"horizontal","contents":[
  {"type":"box","layout":"horizontal","contents":[{"type":"text","text": txt2,"color":"#000000","size":"8px",}],
  "offsetTop":"0px","offsetStart":"0px","paddingTop":"10px"}],"offsetTop":"210px","position":"absolute","offsetStart":"10px","backgroundColor": "#ffffff40","height": "40px","width": "140px"},
{"type":"box","layout":"horizontal","contents":[{"type":"text","text":nama,"color":"#000000","size":"8px",}],
"offsetTop":"33px","position":"absolute","offsetStart":"65px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":fotoku,"size":"full"}],
"position":"absolute","cornerRadius":"200px","width":"20px","offsetTop":"32px","offsetStart":"10px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":vip,"size":"full"}],
"position":"absolute","width":"10px","offsetTop":"42px","offsetStart":"22px"},
{"type":"box","layout":"horizontal","contents":[{"type":"text","text":wkt,"color":"#ffffff","weight":"bold","size":"8px",}],
"offsetTop":"4px","position":"absolute","offsetStart":"13px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":play,"animated":True,"size":"full","action":{"type":"uri","uri":isi}}],
"position":"absolute","width":"50px","offsetTop":"100px","offsetStart":"50px"},
],
  "paddingAll": "0px"
 }
}
    client.postFlex(to,data) 
    
def fjoox(to,foto,audi,title,artist):
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    jam="{}".format(datetime.strftime(timeNow,'%H:%M'))
    tit=title
    art=artist
    url="https://i.ibb.co/XDKG0qf/ezgif-com-gif-maker-49.png"
    url1="https://i.ibb.co/R4BK1MV/hkupload.jpg"
    url2="https://i.ibb.co/QQrfhzg/hkupload.jpg"
    hp="https://i.ibb.co/0Dxm9LH/20210304-181025.png"
    img1=foto
    nada="https://i.ibb.co/FXWMSsv/ezgif-2-b7af7f64d980.png"
    bat="https://i.ibb.co/v31r9pb/ezgif-2-70d836e3e419.png"
    play="https://i.ibb.co/M1Hj9jL/ezgif-1-61269e9e1b17.png"
    data={
"type": "bubble",
"size": "micro",
"body": 
{"type": "box","layout":"vertical","contents":[{"type":"image","url":url,"size":"full","animated":True,"aspectMode": "cover","aspectRatio":"3:5","gravity": "center"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":url1,"size":"full"}],
"position":"absolute","width":"250px","offsetTop":"8px","offsetStart":"-44px","cornerRadius":"70px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":url2,"size":"full"}],"position":"absolute","width":"150px","offsetTop":"-48px","offsetStart":"5px","cornerRadius":"100px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":hp,"size":"full"}],"position":"absolute","width":"265px","offsetTop":"0px","offsetStart":"-52px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":img1,"size":"full"}],
"position":"absolute","width":"148px","offsetTop":"25px","offsetStart":"6px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":nada,"animated":True,"size":"full"}],
"position":"absolute","width":"60px","offsetTop":"180px","offsetStart":"52px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":bat,"animated":True,"size":"full"}],
"position":"absolute","width":"10px","offsetTop":"13px","offsetStart":"140px"},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":play,"animated":True,"size":"full","action":{"type":"uri","uri":audi}}],
"position":"absolute","width":"10px","offsetTop":"225px","offsetStart":"78px"},
{"type":"box","layout":"horizontal","contents":[{"type":"text","text":jam,"color":"#ffffff","size":"5px",}],
"offsetTop":"14px","position":"absolute","offsetStart":"10px"},
{"type":"box","layout":"horizontal","contents":[{"type":"text","text":tit,"color":"#ffffff","size":"8px","align":"center"}],
"offsetTop":"175px","position":"absolute","offsetStart":"0px"},
{"type":"box","layout":"horizontal","contents":[{"type":"text","text":art,"color":"#ffffff","size":"6px","align":"center"}],
"offsetTop":"188px","position":"absolute","offsetStart":"0px"},
],
  "paddingAll": "0px"
 }
}
    client.postFlex(to,data)    
    
def fgr1(to,u):
    url="https://i.ibb.co/K2650QP/20210308-225656.png"
    url1=u
    data={
"type": "bubble",
"size": "micro",
"body": {"type": "box","layout": "vertical","contents":
 [
{"type": "image","url":url,"size": "full","animated":True,"aspectMode": "cover","aspectRatio": "1:1","gravity": "center"},
{"type": "box","layout": "vertical","contents": [{"type": "image","url":url1,"size": "full","animated":True,}], "position": "absolute"},#,"width": "120px"},
#{"type":"box","layout":"vertical","contents":[{"type":"image","url":"https://obs.line-scdn.net/{}".format(client.getContact(tmid).pictureStatus),"size":"full"}],"cornerRadius": "250px","position":"absolute","width":"34px","offsetTop":"78px","offsetStart":"32px"},
#{"type":"box","layout":"vertical","contents":[{"type":"image","url":url2,"size":"full","animated":True}],"position":"absolute","width":"39px","offsetTop":"76px","offsetStart":"29px"},
],"paddingAll": "0px"}}
    client.postFlex(to,data)    
    
def detectpp(to,name,image,image1):
        data = {
         "type":"carousel",
         "contents": [
               {
               "type":"bubble",
               "size":"kilo",
               "body":{
                  "type":"box",
                  "layout":"vertical",
                  "contents":[
                    {
                      "type":"text",
                      "text":"Cie kak {}\nUpadte foto profile".format(name),
                      "size": "xs",
                      "color": "#000000",
                      "wrap": True, 
                      "weight": "bold",# regular, bold
                      "align": "center",
                    },
                    {                      
                      "type":"box",
                      "layout":"horizontal",
                      "contents":[
                        {
                          "type":"box",
                          "layout":"horizontal",
                          "spacing":"xs",
                          "margin":"xs",
                          "contents":[
                            {
                              "type":"box",
                              "layout":"vertical",
                              "contents":[
                                {
                                  "type":"image",
                                  "url":image,
                                  "size":"full",
                                  "aspectRatio":"1:1",
                                  "aspectMode": "cover",
                                  "gravity": "center",
                                },
                                {
                                  'type': 'box',
                                  'layout': 'vertical',
                                  'contents': [
                                    {
                                      'type': 'text',
                                      'text': 'Before',
                                      "size": "xs",
                                      "color": "#000000",
                                      "wrap": True, 
                                      "weight": "bold",# regular, bold
                                      "align": "center",
                                      "offsetTop": "2px",
                                      "action":{
                                        "type":"uri",
                                        "uri":image
                                      }
                                    }
                                  ],
                                  "position": "absolute",
                                  "backgroundColor": "#ffffff40",
                                  "borderColor": "#FF0000",
                                  "borderWidth": "2px",
                                  "cornerRadius": "10px",
                                  "offsetTop": "90px",#foto turun
                                  "offsetStart": "2px",#foto samping
                                  "height": "30px",#panjang foto
                                  "width": "70px"# samping foto
                                }
                              ],
                              "borderColor": "#1E90FF",
                              "borderWidth": "2px",
                              "cornerRadius": "10px",
                              'paddingAll': '0px',
                            }
                          ]
                        },
                        {
                          "type":"box",
                          "layout":"horizontal",
                          "spacing":"xs",
                          "margin":"xs",
                          "contents":[
                            {
                              "type":"box",
                              "layout":"vertical",
                              "contents":[
                                {
                                  "type":"image",
                                  "url":image1,
                                  "size":"full",
                                  "aspectRatio":"1:1",
                                  "aspectMode": "cover",
                                  "gravity": "center",
                                },
                                {
                                  'type': 'box',
                                  'layout': 'vertical',
                                  'contents': [
                                    {
                                      'type': 'text',
                                      'text': 'After',
                                      "size": "xs",
                                      "color": "#000000",
                                      "wrap": True, 
                                      "weight": "bold",# regular, bold
                                      "align": "center",
                                      "offsetTop": "2px",
                                      "action":{
                                        "type":"uri",
                                        "uri":image1
                                      }
                                    }
                                  ],
                                  "position": "absolute",
                                  "backgroundColor": "#ffffff40",
                                  "borderColor": "#00ff80",
                                  "borderWidth": "2px",
                                  "cornerRadius": "10px",
                                  "offsetTop": "90px",#foto turun
                                  "offsetStart": "2px",#foto samping
                                  "height": "30px",#panjang foto
                                  "width": "70px"# samping foto
                                }
                              ],
                              "borderColor": "#1E90FF",
                              "borderWidth": "2px",
                              "cornerRadius": "10px",
                              'paddingAll': '0px',
                            }
                          ]
                        }                                                                                                
                      ]
                    }
                 ],
                 "borderColor": "#1E90FF",
                 "borderWidth": "2px",
                 "cornerRadius": "10px",
                 "paddingAll": "2px",
               }
            }           
         ]
        }                                
        client.postFlex(to, data)
def detectcv(to,name,image,image1):
        data = {
         "type":"carousel",
         "contents": [
               {
               "type":"bubble",
               "size":"kilo",
               "body":{
                  "type":"box",
                  "layout":"vertical",
                  "contents":[
                    {
                      "type":"text",
                      "text":"Cie kak {}\nUpadte foto cover".format(name),
                      "size": "xs",
                      "color": "#000000",
                      "wrap": True, 
                      "weight": "bold",# regular, bold
                      "align": "center",
                    },
                    {                      
                      "type":"box",
                      "layout":"horizontal",
                      "contents":[
                        {
                          "type":"box",
                          "layout":"horizontal",
                          "spacing":"xs",
                          "margin":"xs",
                          "contents":[
                            {
                              "type":"box",
                              "layout":"vertical",
                              "contents":[
                                {
                                  "type":"image",
                                  "url":image,
                                  "size":"full",
                                  "aspectRatio":"1:1",
                                  "aspectMode": "cover",
                                  "gravity": "center",
                                },
                                {
                                  'type': 'box',
                                  'layout': 'vertical',
                                  'contents': [
                                    {
                                      'type': 'text',
                                      'text': 'Before',
                                      "size": "xs",
                                      "color": "#000000",
                                      "wrap": True, 
                                      "weight": "bold",# regular, bold
                                      "align": "center",
                                      "offsetTop": "2px",
                                      "action":{
                                        "type":"uri",
                                        "uri":image
                                      }
                                    }
                                  ],
                                  "position": "absolute",
                                  "backgroundColor": "#ffffff40",
                                  "borderColor": "#FF0000",
                                  "borderWidth": "2px",
                                  "cornerRadius": "10px",
                                  "offsetTop": "90px",#foto turun
                                  "offsetStart": "2px",#foto samping
                                  "height": "30px",#panjang foto
                                  "width": "70px"# samping foto
                                }
                              ],
                              "borderColor": "#1E90FF",
                              "borderWidth": "2px",
                              "cornerRadius": "10px",
                              'paddingAll': '0px',
                            }
                          ]
                        },
                        {
                          "type":"box",
                          "layout":"horizontal",
                          "spacing":"xs",
                          "margin":"xs",
                          "contents":[
                            {
                              "type":"box",
                              "layout":"vertical",
                              "contents":[
                                {
                                  "type":"image",
                                  "url":image1,
                                  "size":"full",
                                  "aspectRatio":"1:1",
                                  "aspectMode": "cover",
                                  "gravity": "center",
                                },
                                {
                                  'type': 'box',
                                  'layout': 'vertical',
                                  'contents': [
                                    {
                                      'type': 'text',
                                      'text': 'After',
                                      "size": "xs",
                                      "color": "#000000",
                                      "wrap": True, 
                                      "weight": "bold",# regular, bold
                                      "align": "center",
                                      "offsetTop": "2px",
                                      "action":{
                                        "type":"uri",
                                        "uri":image1
                                      }
                                    }
                                  ],
                                  "position": "absolute",
                                  "backgroundColor": "#ffffff40",
                                  "borderColor": "#00ff80",
                                  "borderWidth": "2px",
                                  "cornerRadius": "10px",
                                  "offsetTop": "90px",#foto turun
                                  "offsetStart": "2px",#foto samping
                                  "height": "30px",#panjang foto
                                  "width": "70px"# samping foto
                                }
                              ],
                              "borderColor": "#1E90FF",
                              "borderWidth": "2px",
                              "cornerRadius": "10px",
                              'paddingAll': '0px',
                            }
                          ]
                        }                                                                                                
                      ]
                    }
                 ],
                 "borderColor": "#1E90FF",
                 "borderWidth": "2px",
                 "cornerRadius": "10px",
                 "paddingAll": "2px",
               }
            }           
         ]
        }                                
        client.postFlex(to, data)
      
def ttg(to,name,image,image1):
        data = {
         "type":"template",
         "template":{
         "type":"carousel",
         "contents": [
               {
               "type":"bubble",
               "size":"kilo",
               "body":{
                  "type":"box",
                  "layout":"vertical",
                  "contents":[
                    {
                      "type":"text",
                      "text":"Cie kak {}\nUpadte foto cover".format(name),
                      "size": "xs",
                      "color": "#000000",
                      "wrap": True, 
                      "weight": "bold",# regular, bold
                      "align": "center",
                    },
                    {                      
                      "type":"box",
                      "layout":"horizontal",
                      "contents":[
                        {
                          "type":"box",
                          "layout":"horizontal",
                          "spacing":"xs",
                          "margin":"xs",
                          "contents":[
                            {
                              "type":"box",
                              "layout":"vertical",
                              "contents":[
                                {
                                  "type":"image",
                                  "url":image,
                                  "size":"full",
                                  "aspectRatio":"1:1",
                                  "aspectMode": "cover",
                                  "gravity": "center",
                                },
                                {
                                  'type': 'box',
                                  'layout': 'vertical',
                                  'contents': [
                                    {
                                      'type': 'text',
                                      'text': 'Before',
                                      "size": "xs",
                                      "color": "#000000",
                                      "wrap": True, 
                                      "weight": "bold",# regular, bold
                                      "align": "center",
                                      "offsetTop": "2px",
                                      "action":{
                                        "type":"uri",
                                        "uri":image
                                      }
                                    }
                                  ],
                                  "position": "absolute",
                                  "backgroundColor": "#ffffff40",
                                  "borderColor": "#FF0000",
                                  "borderWidth": "2px",
                                  "cornerRadius": "10px",
                                  "offsetTop": "90px",#foto turun
                                  "offsetStart": "2px",#foto samping
                                  "height": "30px",#panjang foto
                                  "width": "70px"# samping foto
                                }
                              ],
                              "borderColor": "#1E90FF",
                              "borderWidth": "2px",
                              "cornerRadius": "10px",
                              'paddingAll': '0px',
                            }
                          ]
                        },
                        {
                          "type":"box",
                          "layout":"horizontal",
                          "spacing":"xs",
                          "margin":"xs",
                          "contents":[
                            {
                              "type":"box",
                              "layout":"vertical",
                              "contents":[
                                {
                                  "type":"image",
                                  "url":image1,
                                  "size":"full",
                                  "aspectRatio":"1:1",
                                  "aspectMode": "cover",
                                  "gravity": "center",
                                },
                                {
                                  'type': 'box',
                                  'layout': 'vertical',
                                  'contents': [
                                    {
                                      'type': 'text',
                                      'text': 'After',
                                      "size": "xs",
                                      "color": "#000000",
                                      "wrap": True, 
                                      "weight": "bold",# regular, bold
                                      "align": "center",
                                      "offsetTop": "2px",
                                      "action":{
                                        "type":"uri",
                                        "uri":image1
                                      }
                                    }
                                  ],
                                  "position": "absolute",
                                  "backgroundColor": "#ffffff40",
                                  "borderColor": "#00ff80",
                                  "borderWidth": "2px",
                                  "cornerRadius": "10px",
                                  "offsetTop": "90px",#foto turun
                                  "offsetStart": "2px",#foto samping
                                  "height": "30px",#panjang foto
                                  "width": "70px"# samping foto
                                }
                              ],
                              "borderColor": "#1E90FF",
                              "borderWidth": "2px",
                              "cornerRadius": "10px",
                              'paddingAll': '0px',
                            }
                          ]
                        }                                                                                                
                      ]
                    }
                 ],
                 "borderColor": "#1E90FF",
                 "borderWidth": "2px",
                 "cornerRadius": "10px",
                 "paddingAll": "2px",
               }
            }           
         ]
         }
        }                                
        client.postTemplate(to, data)
      
def wgetfoto(msg_id):
    img = client.downloadObjectMsg(msg_id, saveAs='LineAPI/tmp/hkupload.jpg')
    files={
      'source': open(img,'rb')
    }
    params={
      'type': 'file',
      'action': 'upload',
      'timestamp': '1569686655293',
      #'timestamp': '1569679350983',
      'auth_token': 'cff98c38e014a91f9f4de2bf2a7bc8363e62099f',
      'album_id': 'bJMe8v'
      #'auth_token': '0'
    }
    url='https://eka-puput.imgbb.com/json'
    req=requests.post(url,data=params,files=files).text
    hasil=json.loads(req)
    a=hasil['image']['url']
    client.deleteFile('LineAPI/tmp/hkupload.jpg')
    return a
def linkfoto2(her):
    files={
      'source': open(her,'rb')
    }
    params={
      'type': 'file',
      'action': 'upload',
      'timestamp': '1569686655293',
      #'timestamp': '1569679350983',
      'auth_token': 'cff98c38e014a91f9f4de2bf2a7bc8363e62099f',
      'album_id': 'bJMe8v'
      #'auth_token': '0'
    }
    url='https://eka-puput.imgbb.com/json'
    req=requests.post(url,data=params,files=files).text
    hasil=json.loads(req)
    a=hasil['image']['url']
    #client.deleteFile('LineAPI/tmp/hkupload.jpg')
    return a
def linkfoto(her):
    img = client.downloadFileURL(her, saveAs='LineAPI/tmp/hkupload.jpg')
    files={
      'source': open(img,'rb')
    }
    params={
      'type': 'file',
      'action': 'upload',
      'timestamp': '1569686655293',
      #'timestamp': '1569679350983',
      'auth_token': 'cff98c38e014a91f9f4de2bf2a7bc8363e62099f',
      'album_id': 'bJMe8v'
      #'auth_token': 'b110d9c9f0dfdb2383946897dfc6cca2eba383f1'
    }
    url='https://eka-puput.imgbb.com/json'
    req=requests.post(url,data=params,files=files).text
    hasil=json.loads(req)
    a=hasil['image']['url']
    client.deleteFile('LineAPI/tmp/hkupload.jpg')
    return a
def linkaudio(her):
    from pydub import AudioSegment
    AudioSegment.ffprobe ="C:\\ffmpeg\\ffmpeg\\bin\\ffprobe.exe"
    nama="tmp/input.mp3"
    ubah="tmp/output.mp3"
    aud = client.downloadFileURL(her, saveAs=nama)
    song = AudioSegment.from_mp3(nama)
    song.export(ubah, format='mp3', bitrate='30k')
    audi={'uploadedFile': open(ubah,'rb')}
    param={"uploadBtn":"Upload"}
    url="https://hkupload.herokuapp.com/upload.php"
    r="https://hkupload.herokuapp.com/"+BeautifulSoup(requests.post(url,data=param,files=audi).text,"lxml").find("a")["href"].replace("/./","")
    #client.deleteFile(nama)
    #client.deleteFile(ubah)
    return r
  
def videohk(link):
    with youtube_dl.YoutubeDL() as ydl:
      url = ydl.extract_info(link, download=False)
      try:
        download_link = url["entries"][-1]["formats"][-1]["url"]
      except:
        download_link = url["formats"][-1]["url"]
      if ".mp4" in download_link:
        return download_link
      else:
        data=download_link+"&dl=1"
        return data
  
def linkqr(to,her):
    url =pyqrcode.create(her, error='L', version=8, mode='binary')
    url.png("big-number.png",scale=8) 
    client.sendImage(to,"big-number.png")  
def ezgifapngtogif(txt):
    r=BeautifulSoup(requests.get("https://ezgif.com/apng-to-gif?url={}".format(txt)).text,"lxml")
    d=r.findAll("form")
    l=d[0].get("action")
    u=d[0].findAll("input")[0].get("value")
    t=d[0].findAll("input")[1].get("value")
    s=d[0].findAll("input")[2].get("value")
    param={
      "file":u,
      "token":t,
      "submit":s,
    }
    r1=BeautifulSoup(requests.post(l,data=param).text,"lxml")
    data="https:"+r1.findAll("p",{"class":"outfile"})[0].find("img")["src"]
    return data
  
def ezgifgiftoapng(txt):
    r=requests.get("https://ezgif.com/gif-to-apng?url={}".format(txt)).text
    b=BeautifulSoup(r,"lxml")
    s=b.findAll("form",{"class":"form ajax-form"})
    s1=s[0].get('action')
    s2=s[0].findAll('input')[0].get('value')
    s3=s[0].findAll('input')[1].get('value')
    s4=s[0].findAll('input')[2].get('value')
    url=s1
    param={
      "file":str(s2),
      "token":str(s3),
      "submit":str(s4),
    }
    r2=requests.post(url,data=param).text
    b2=BeautifulSoup(r2,"lxml")
    link="https:"+b2.find("p",{"class":"outfile"}).find("img").get("src")
    return link
    
def ezgifapngmaker(txt):
    r=BeautifulSoup(requests.get("https://ezgif.com/apng-to-gif?url={}".format(txt)).text,"lxml")
    d=r.find("a",{"class":"m-btn-apng-maker"}).get("href")
    r1=BeautifulSoup(requests.get(d).text,"lxml")
    fr=r1.findAll("form",{"class":"form ajax-form"})
    fr1=r1.find("form").get("action")
    jns="/"+r1.find("form").get("action").split("/")[2].replace("-png-split",".png")
    url="https://ezgif.com"+fr1
    fr2=fr[0].findAll("input")[0].get("value")
    fr3=fr[0].findAll("input")[1].get("value")
    lif=[i.find("input",{"class":"filename-holder"}).get("value") for i in r1.findAll("li",{"class":"frame"})]
    lid=[i1.find("input",{"class":"text tiny"}).get("value") for i1 in r1.findAll("li",{"class":"frame"})]
    d1=r1.find("a",{"class":"m-btn-apng-maker active"}).get("href")
    param={
      "file":fr2,
      "token":fr3,
      "files[]":lif,
      "delays[]":lid,
      "dfrom":"1",
      "dto":"5",
      #"disable":"Skip",
      #"enable":"Enable",
      "delay":"20",
      "loop":"",
      #"fader":"checkbox",
      #"fader-delay":"6",
      #"fader-frames":"8",
      #"fader-skip-last":"checkbox",
      #"skipfirst":"checkbox",
      "nostack":"checkbox",
      #"keep-first":"checkbox",
      "submit":"Make APNG!",
    }
    r2=BeautifulSoup(requests.post(url,data=param).text,"lxml")
    outf="https:"+r2.find("p",{"class":"outfile"}).find("img")["src"]
    return outf
  
def ezgifvideotogif(txt):
    a=BeautifulSoup(requests.get("https://ezgif.com/video-to-jpg?url={}".format(txt)).text,'lxml')
    d=a.findAll("form")
    url=d[0].get('action')
    fil=d[0].findAll("input")[0].get("value")
    tok=d[0].findAll("input")[1].get("value")
    st=d[0].findAll("input")[2].get("value")
    idst=d[0].findAll("input")[3].get("value")
    en=d[0].findAll("input")[4].get("value")
    ide=d[0].findAll("input")[5].get("value")
    sub=d[0].findAll("input")[6].get("value")
    param={
      'file':fil,
      'token':tok,
      'start':st,
      'read_pos_start':idst,
      'end':en,
      'read_pos_end':ide,
      'size':'original',
      'fps':'5',
      'method':'ffmpeg',
      'diff':'checkbox',
      'submit':sub
    }
    a1="https:"+BeautifulSoup(requests.post(url,data=param).text,'lxml').find('video',{'id':'convert_video'}).get('poster')
    return a1

def danbooru(to,text):
    r=BeautifulSoup(requests.get("https://danbooru.donmai.us/posts?page={}".format(text)).text,"html5lib")
    a=r.findAll("a",{"class":"post-preview-link"})
    data=[]
    for i in range(5):
      nama="{}.jpg".format(i)
      b="https://danbooru.donmai.us"+str(a[i].get("href"))
      c=BeautifulSoup(requests.get(b).text,"html5lib")
      d=c.findAll("li",{"id":"post-info-size"})[0].find("a")["href"]
      client.downloadFileURL(d, saveAs=nama)
      data.append(nama)
    client.uploadMultipleImageToTalk(data,to)
    
def primbonpasangan(nama1,nama2): 
    url = 'http://www.primbon.com/kecocokan_nama_pasangan.php?nama1={}&nama2={}&proses=+Submit%21+'.format(nama1,nama2)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    div = soup.findAll('div',{'class':'width'})[2].get_text().split('\n')
    cari=div[2]+'\n'+div[3].replace('Nama Pasangan:','\nNama Pasangan:').replace('Sisi Positif Anda:','\nSisi Positif Anda:').replace('Sisi Negatif Anda:','\nSisi Negatif Anda:')
    return cari

def primbonnama(nama): 
    host="http://www.primbon.com/arti_nama.php?nama1={}&proses=+Submit%21+".format(nama)
    respon=requests.get(host).text
    soup=BeautifulSoup(respon,"lxml")
    text=soup.findAll("div", {"id":"body"})[0].text.split("\n")
    cari=text[2]+"\n"+text[3]+"\n"+text[5]
    return cari
def primbonweton(tanggal): 
    l1=tanggal.split('-')
    tgl=l1[0]
    bln=l1[1]
    thn=l1[2]
    url="http://www.primbon.com/ramalan_weton.php"
    params={
      "tgl": tgl,
      "bln": bln,
      "thn": thn,
      "submit": " Submit!"
    }
    req=requests.post(url,data=params).text
    soup=BeautifulSoup(req,"lxml")
    div=soup.findAll("div",{"id":"body"})[0].get_text().split("\n")
    a=div[2]+"\n"+div[3].replace(thn,thn+"\n")
    return a 
def primbonjodoh(nama1,tanggal1,nama2,tanggal2):
    l1=tanggal1.split('-')
    tgl1=l1[0]
    bln1=l1[1]
    thn1=l1[2]
    l2=tanggal2.split('-')
    tgl2=l2[0]
    bln2=l2[1]
    thn2=l2[2]
    url='http://www.primbon.com/ramalan_jodoh.php'
    params={
      'nama1':nama1,
      'tgl1':tgl1,
      'bln1':bln1,
      'thn1':thn1,
      'nama2':nama2,
      'tgl2':tgl2,
      'bln2':bln2,
      'thn2':thn2,
      'submit':' Submit!'
    }
    req = requests.post(url,data=params)
    soup = BeautifulSoup(req.text,'lxml')
    div = soup.findAll('div',{'id':'body'})[0].get_text().split("\n")
    hasil=div[2]
    hasil+="\n"+div[3].replace(nama1,"Nama : "+nama1+"\n").replace(nama2,"\n"+"Nama : "+nama2+"\n").replace(thn2,thn2+"\n")
    hasil+="\n"+div[16].replace(".2","\n2").replace(".3","\n3").replace(".4","\n4").replace(".5","\n5").replace(".6","\n6")
    return hasil
def primbonsuami_istri(nama1,tanggal1,nama2,tanggal2):
    l1=tanggal1.split('-')
    tgl1=l1[0]
    bln1=l1[1]
    thn1=l1[2]
    l2=tanggal2.split('-')
    tgl2=l2[0]
    bln2=l2[1]
    thn2=l2[2]
    url='http://www.primbon.com/suami_istri.php'
    params={
      'nama1':nama1,
      'tgl1':tgl1,
      'bln1':bln1,
      'thn1':thn1,
      'nama2':nama2,
      'tgl2':tgl2,
      'bln2':bln2,
      'thn2':thn2,
      'submit':' Submit!'
    }
    req = requests.post(url,data=params)
    soup = BeautifulSoup(req.text,'lxml')
    tex=soup.findAll("div", {"id":"body"})[0].text.split("\n")
    cari=tex[2]
    cari+="\n"+tex[3].replace(nama1,nama1+"\n").replace(thn1,thn1+"\n").replace(nama2,nama2+"\n")
    cari+="\n"+tex[4]
    cari+="\n"+tex[6]+"\n"+tex[7]+"\n"+tex[8]+"\n"+tex[9]+"\n"+tex[10]+"\n"+tex[11]+"\n"+tex[12]+"\n"+tex[13]+"\n"+tex[14]+"\n"+tex[15]+"\n"+tex[16]+"\n"+tex[17]+"\n"+tex[18]+"\n"+tex[19]
    cari+="\n"+tex[21]
    return cari
  
def tesfotobulat(to,her):
    h=fotobulat(her)
    a="LineAPI/tmp/btes.jpg"
    b="LineAPI/tmp/tes1.png"
    a1=Image.open(a).resize((500,500))
    b1=Image.open(b).resize((320,320))
    a1.paste(b1,(90,90),b1)
    a1.save("LineAPI/tmp/coba.jpg")
    client.sendImage(to,"LineAPI/tmp/coba.jpg")
    
def fotobulat(her):
    client.downloadFileURL(her,saveAs="LineAPI/tmp/tes.jpg")
    a=Image.open("LineAPI/tmp/tes.jpg")
    a1="LineAPI/tmp/tes1.jpg"
    a2="LineAPI/tmp/tes1.png"
    thumb_width = 200
    img_width, img_height = a.size
    a.crop(((img_width - thumb_width) // 2,
           (img_height - thumb_width) // 2,
           (img_width + thumb_width) // 2,
           (img_height + thumb_width) // 2))
    a.resize((thumb_width,thumb_width),Image.LANCZOS)
    a.save(a1, quality=95)
    off = 1 * 2 + 0
    b=Image.open(a1)
    mask = Image.new("L", b.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((off, off, b.size[0] - off, b.size[1] - off), fill=255)
    mas = mask.filter(ImageFilter.GaussianBlur(1))
    result = b.copy()
    result.putalpha(mas)
    result.save(a2)
    return linkfoto2(a2)
  
def wanted(to,her,txt,txt1):
    foto=client.downloadFileURL(her,saveAs="LineAPI/tmp/coba.jpg")
    f1=Image.open("LineAPI/tmp/coba.jpg")
    f2=f1.resize((265,  270))
    f3=Image.open("LineAPI/tmp/images13.jpg")
    f3.paste(f2,(88,200))
    f3.save("LineAPI/tmp/contoh1.jpg")
    f4=Image.open("LineAPI/tmp/contoh1.jpg")
    f5 =  ImageDraw.Draw(f4)
    co="black"
    text=txt
    text1=txt1
    font = ImageFont.truetype("LineAPI/tmp/NASHVILL.TTF", 50)
    font1 = ImageFont.truetype("LineAPI/tmp/NASHVILL.TTF", 30)
    shadow="black"
    tebal= 1
    text=txt
    text1=txt1
    imgX,imgY=f3.size
    txtX,txtY=f5.textsize(text,font=font)
    txtX1,txtY1=f5.textsize(text1,font=font1)
    x=imgX/2-txtX/2
    y=imgY/485-txtY/485-(imgY/485-(txtY/485)-485)
    x1=imgX/2-txtX1/2
    y1=imgY/555-txtY1/555-(imgY/555-(txtY1/555)-555)
    for ba in range(tebal):
        f5.text((x-ba,y), text, fill=shadow, font=font)
        f5.text((x+ba,y), text, fill=shadow, font=font)
        f5.text((x,y-ba), text, fill=shadow, font=font)
        f5.text((x-ba,y+ba), text, fill=shadow, font=font)
        f5.text((x+ba,y+ba), text, fill=shadow, font=font)
        f5.text((x-ba,y-ba), text, fill=shadow, font=font)
        f5.text((x+ba,y-ba), text, fill=shadow, font=font)
    f5.text((x,y), text, fill=co, font=font)
    for ba1 in range(tebal):
        f5.text((x1-ba1,y1), text1, fill=shadow, font=font1)
        f5.text((x1+ba1,y1), text1, fill=shadow, font=font1)
        f5.text((x1-ba1,y1+ba1), text1, fill=shadow, font=font1)
        f5.text((x1+ba1,y1+ba1), text1, fill=shadow, font=font1)
        f5.text((x1-ba1,y1-ba1), text1, fill=shadow, font=font1)
        f5.text((x1+ba1,y1-ba1), text1, fill=shadow, font=font1)
    f5.text((x1,y1), text1, fill=co, font=font1)
    f4.save("LineAPI/tmp/contoh2.jpg")
    f6=Image.open("LineAPI/tmp/contoh2.jpg")
    f7=f6.convert("L")
    f7.save("LineAPI/tmp/contoh3.jpg")
    client.sendImage(to,"LineAPI/tmp/contoh3.jpg")
    client.deleteFile("LineAPI/tmp/contoh1.jpg") 
    client.deleteFile("LineAPI/tmp/contoh2.jpg") 
    client.deleteFile("LineAPI/tmp/contoh3.jpg")  
  
def love(to,her,txt,her1,txt1):
    pfc1(her,txt)
    pfc2(her1,txt1)
    f1=Image.open("LineAPI/tmp/cover.jpg").resize((850,800))
    f2=Image.open("LineAPI/tmp/contoh1.jpg").resize((250,360))
    f3=Image.open("LineAPI/tmp/contoh2.jpg").resize((250,360))
    drawing =  ImageDraw.Draw(f1)
    colour="white"
    text="Hayden Bot"
    pos=400,650
    font = ImageFont.truetype("LineAPI/tmp/Chocolatine du Dimanche.ttf", 80)
    drawing.text(pos, text, fill=colour, font=font)
    f1.paste(f2,(275,130))
    f1.paste(f3,(560,45))
    f1.save("LineAPI/tmp/contoh3.jpg")
    client.sendImage(to,"LineAPI/tmp/contoh3.jpg")
    
def pfc1(her,txt):
    foto=client.downloadFileURL(her,saveAs="LineAPI/tmp/coba.jpg")
    f1=Image.open("LineAPI/tmp/coba.jpg").resize((300,300))
    f1.save("LineAPI/tmp/contoh.jpg")
    f2=Image.open("LineAPI/tmp/contoh.jpg")
    l=(6,6,6,70)
    c="white"
    f3=ImageOps.expand(f2,border=l,fill=c)
    f5 =  ImageDraw.Draw(f3)
    co="black"
    text=txt
    font = ImageFont.truetype("LineAPI/tmp/NASHVILL.TTF", 40)
    shadow="black"
    tebal= 1
    text=txt
    imgX,imgY=f3.size
    txtX,txtY=f5.textsize(text,font=font)
    x=imgX/2-txtX/2
    y=imgY/320-txtY/320-(imgY/320-(txtY/320)-320)
    for ba in range(tebal):
        f5.text((x-ba,y), text, fill=shadow, font=font)
        f5.text((x+ba,y), text, fill=shadow, font=font)
        f5.text((x,y-ba), text, fill=shadow, font=font)
        f5.text((x-ba,y+ba), text, fill=shadow, font=font)
        f5.text((x+ba,y+ba), text, fill=shadow, font=font)
        f5.text((x-ba,y-ba), text, fill=shadow, font=font)
        f5.text((x+ba,y-ba), text, fill=shadow, font=font)
    f5.text((x,y), text, fill=co, font=font)
    f3.save("LineAPI/tmp/contoh1.jpg")
    #client.sendImage(to,"LineAPI/tmp/contoh1.jpg")
    client.deleteFile("LineAPI/tmp/contoh.jpg")
    #client.deleteFile("LineAPI/tmp/contoh1.jpg")
def pfc2(her,txt):
    foto=client.downloadFileURL(her,saveAs="LineAPI/tmp/coba.jpg")
    f1=Image.open("LineAPI/tmp/coba.jpg").resize((300,300))
    f1.save("LineAPI/tmp/contoh.jpg")
    f2=Image.open("LineAPI/tmp/contoh.jpg")
    l=(6,6,6,70)
    c="white"
    f3=ImageOps.expand(f2,border=l,fill=c)
    f5 =  ImageDraw.Draw(f3)
    co="black"
    text=txt
    font = ImageFont.truetype("LineAPI/tmp/NASHVILL.TTF", 40)
    shadow="black"
    tebal= 1
    text=txt
    imgX,imgY=f3.size
    txtX,txtY=f5.textsize(text,font=font)
    x=imgX/2-txtX/2
    y=imgY/320-txtY/320-(imgY/320-(txtY/320)-320)
    for ba in range(tebal):
        f5.text((x-ba,y), text, fill=shadow, font=font)
        f5.text((x+ba,y), text, fill=shadow, font=font)
        f5.text((x,y-ba), text, fill=shadow, font=font)
        f5.text((x-ba,y+ba), text, fill=shadow, font=font)
        f5.text((x+ba,y+ba), text, fill=shadow, font=font)
        f5.text((x-ba,y-ba), text, fill=shadow, font=font)
        f5.text((x+ba,y-ba), text, fill=shadow, font=font)
    f5.text((x,y), text, fill=co, font=font)
    f3.save("LineAPI/tmp/contoh2.jpg")
    #client.sendImage(to,"LineAPI/tmp/contoh1.jpg")
    client.deleteFile("LineAPI/tmp/contoh.jpg")
    #client.deleteFile("LineAPI/tmp/contoh1.jpg")
def couple(to,her,her1):
    cover=Image.open("LineAPI/tmp/ft.jpg").resize((1000,1000))
    foto=client.downloadFileURL(her,saveAs="LineAPI/tmp/coba.jpg")
    f1=Image.open("LineAPI/tmp/coba.jpg").resize((560,900))
    foto1=client.downloadFileURL(her1,saveAs="LineAPI/tmp/coba1.jpg")
    f2=Image.open("LineAPI/tmp/coba1.jpg").resize((280,390)).rotate(15,expand=True)
    f3=Image.open("LineAPI/tmp/s1.png").resize((1000,1000))
    cover.paste(f1,(40,40))
    cover.paste(f2,(640,90))
    cover.paste(f3,f3)
    cover.save("LineAPI/tmp/contoh1.jpg")
    client.sendImage(to,"LineAPI/tmp/contoh1.jpg")
  
def pf1a(to,her):
    foto=client.downloadFileURL(her,saveAs="LineAPI/tmp/coba.jpg")
    f1=Image.open("LineAPI/tmp/coba.jpg")
    f2=f1.resize((141,  215))
    f3=Image.open("LineAPI/tmp/images3.jpg")
    f3.paste(f2,(260,40))
    f3.save("LineAPI/tmp/contoh1.jpg")
    client.sendImage(to,"LineAPI/tmp/contoh1.jpg")
    client.deleteFile("LineAPI/tmp/contoh1.jpg") 
    
def pf1b(to,her):
    foto=client.downloadFileURL(her,saveAs="LineAPI/tmp/coba.jpg")
    f1=Image.open("LineAPI/tmp/coba.jpg")
    f2=f1.resize((232,  314))
    f3=Image.open("LineAPI/tmp/images4.jpg")
    f3.paste(f2,(223,120))
    f3.save("LineAPI/tmp/contoh1.jpg")
    client.sendImage(to,"LineAPI/tmp/contoh1.jpg")
    client.deleteFile("LineAPI/tmp/contoh1.jpg") 
def pf1c(to,her):
    foto=client.downloadFileURL(her,saveAs="LineAPI/tmp/coba.jpg")
    f1=Image.open("LineAPI/tmp/coba.jpg")
    f2=f1.resize((174,  246))
    f3=Image.open("LineAPI/tmp/images6.jpg")
    f3.paste(f2,(152,55))
    f3.save("LineAPI/tmp/contoh1.jpg")
    client.sendImage(to,"LineAPI/tmp/contoh1.jpg")
    client.deleteFile("LineAPI/tmp/contoh1.jpg") 
def pf1d(to,her):
    foto=client.downloadFileURL(her,saveAs="LineAPI/tmp/coba.jpg")
    f1=Image.open("LineAPI/tmp/coba.jpg")
    f2=f1.resize((264,  170))
    f3=Image.open("LineAPI/tmp/images7.jpg")
    f3.paste(f2,(130,54))
    f3.save("LineAPI/tmp/contoh1.jpg")
    client.sendImage(to,"LineAPI/tmp/contoh1.jpg")
    client.deleteFile("LineAPI/tmp/contoh1.jpg") 
def pf1e(to,her):
    foto=client.downloadFileURL(her,saveAs="LineAPI/tmp/coba.jpg")
    f1=Image.open("LineAPI/tmp/coba.jpg")
    f2=f1.resize((265,  270))
    f3=Image.open("LineAPI/tmp/images10.jpg")
    f3.paste(f2,(193,110))
    f3.save("LineAPI/tmp/contoh1.jpg")
    client.sendImage(to,"LineAPI/tmp/contoh1.jpg")
    client.deleteFile("LineAPI/tmp/contoh1.jpg") 
def pf1(to,her,no):
    a = [pf1a,pf1b,pf1c,pf1d,pf1e]
    a[int(no)-1](to,her)
    
def pf2(to,her1,her2):
    foto=client.downloadFileURL(her1,saveAs="LineAPI/tmp/coba1.jpg")
    f1=Image.open("LineAPI/tmp/coba1.jpg")
    p1=f1.resize((88,  139))
    foto1=client.downloadFileURL(her2,saveAs="LineAPI/tmp/coba2.jpg")
    f2=Image.open("LineAPI/tmp/coba2.jpg")
    p2=f2.resize((88,  139))
    f3=Image.open("LineAPI/tmp/images5.jpg")
    f3.paste(p1,(212,58))
    f3.paste(p2,(354,116))
    f3.save("LineAPI/tmp/contoh1.jpg")
    client.sendImage(to,"LineAPI/tmp/contoh1.jpg")
    client.deleteFile("LineAPI/tmp/contoh1.jpg") 
    
def pf3(to,her1,her2,her3):
    foto1=client.downloadFileURL(her1,saveAs="LineAPI/tmp/coba1.jpg")    
    f1=Image.open("LineAPI/tmp/coba1.jpg")
    p1=f1.resize((84,  162))
    foto2=client.downloadFileURL(her2,saveAs="LineAPI/tmp/coba2.jpg")    
    f2=Image.open("LineAPI/tmp/coba2.jpg")
    p2=f2.resize((84,  162))
    foto3=client.downloadFileURL(her3,saveAs="LineAPI/tmp/coba3.jpg")    
    f3=Image.open("LineAPI/tmp/coba3.jpg")
    p3=f3.resize((84,  162))
    f4=Image.open("LineAPI/tmp/images2.jpg")
    f4.paste(p1,(98,72))
    f4.paste(p2,(222,72))
    f4.paste(p3,(347,72))
    f4.save("LineAPI/tmp/contoh1.jpg")
    client.sendImage(to,"LineAPI/tmp/contoh1.jpg")
    client.deleteFile("LineAPI/tmp/contoh1.jpg") 

def pf4(to,her1,her2,her3,her4):
    foto1=client.downloadFileURL(her1,saveAs="LineAPI/tmp/coba1.jpg")    
    f1=Image.open("LineAPI/tmp/coba1.jpg")
    p1=f1.resize((73,  100))
    foto2=client.downloadFileURL(her2,saveAs="LineAPI/tmp/coba2.jpg")    
    f2=Image.open("LineAPI/tmp/coba2.jpg")
    p2=f2.resize((73,  100))
    foto3=client.downloadFileURL(her3,saveAs="LineAPI/tmp/coba3.jpg")    
    f3=Image.open("LineAPI/tmp/coba3.jpg")
    p3=f3.resize((73,  100))
    foto4=client.downloadFileURL(her4,saveAs="LineAPI/tmp/coba4.jpg")    
    f4=Image.open("LineAPI/tmp/coba4.jpg")
    p4=f4.resize((73,  100))
    f5=Image.open("LineAPI/tmp/images1.jpg")
    f5.paste(p1,(21,83))
    f5.paste(p2,(154,83))
    f5.paste(p3,(281,83))
    f5.paste(p4,(406,83))
    f5.save("LineAPI/tmp/contoh1.jpg")
    client.sendImage(to,"LineAPI/tmp/contoh1.jpg")
    client.deleteFile("LineAPI/tmp/contoh1.jpg")  
    
def memegenerator(to,url,txt,txt1):
    foto=client.downloadFileURL(url,saveAs="LineAPI/tmp/coba.jpg")
    f3=Image.open("LineAPI/tmp/coba.jpg")
    f4=f3.resize((400,  400))
    drawing =  ImageDraw.Draw(f4)
    font = ImageFont.truetype("LineAPI/tmp/Afterkilly.ttf", 50)
    textcolour="white"
    shadow="black"
    tebal= 3
    text=txt
    text1=txt1
    imgX,imgY=f4.size
    txtX,txtY=drawing.textsize(text,font=font)
    txtX1,txtY1=drawing.textsize(text1,font=font)
    x=imgX/2-txtX/2
    y=imgY/2-txtY/2-(imgY/2-(txtY/2)-2)
    x1=imgX/2-txtX1/2
    y1=imgY/2-txtY1/2+(imgY/2-(txtY1/2)-2)
    for ba in range(tebal):
        drawing.text((x-ba,y), text, fill=shadow, font=font)
        drawing.text((x+ba,y), text, fill=shadow, font=font)
        drawing.text((x,y-ba), text, fill=shadow, font=font)
        drawing.text((x-ba,y+ba), text, fill=shadow, font=font)
        drawing.text((x+ba,y+ba), text, fill=shadow, font=font)
        drawing.text((x-ba,y-ba), text, fill=shadow, font=font)
        drawing.text((x+ba,y-ba), text, fill=shadow, font=font)
    drawing.text((x,y), text, fill=textcolour, font=font)
    for ba1 in range(tebal):
        drawing.text((x1-ba1,y1), text1, fill=shadow, font=font)
        drawing.text((x1+ba1,y1), text1, fill=shadow, font=font)
        drawing.text((x1-ba1,y1+ba1), text1, fill=shadow, font=font)
        drawing.text((x1+ba1,y1+ba1), text1, fill=shadow, font=font)
        drawing.text((x1-ba1,y1-ba1), text1, fill=shadow, font=font)
        drawing.text((x1+ba1,y1-ba1), text1, fill=shadow, font=font)
    drawing.text((x1,y1), text1, fill=textcolour, font=font)
    nama = "LineAPI/tmp/tes1.jpg"
    f4.save(nama)
    client.sendImage(to,nama)
    client.deleteFile(nama)    
    client.deleteFile("LineAPI/tmp/coba.jpg")
    
def ktext2(to,text):
    txt="LineAPI/tmp/text.png"
    cover="LineAPI/tmp/frame pidato.jpg"
    hasil="LineAPI/tmp/frame pidato1.jpg"
    f1 = Image.new('RGBA', ((3000,3000)), (0,0,0,0))
    drawing =  ImageDraw.Draw(f1)
    shadow="black"
    colour="white"
    texts=text
    tebal=1
    font = ImageFont.truetype("LineAPI/tmp/arial.ttf", 100)
    imgX,imgY=f1.size
    txtX,txtY=drawing.textsize(texts,font=font)
    x=imgX/2-txtX/2
    y=imgY/750-txtY/750-(imgY/750-(txtY/750)-750)
    for ba in range(tebal):
        drawing.text((x-ba,y), texts, fill=shadow, font=font)
        drawing.text((x+ba,y), texts, fill=shadow, font=font)
        drawing.text((x,y-ba), texts, fill=shadow, font=font)
        drawing.text((x-ba,y+ba), texts, fill=shadow, font=font)
        drawing.text((x+ba,y+ba), texts, fill=shadow, font=font)
        drawing.text((x-ba,y-ba), texts, fill=shadow, font=font)
        drawing.text((x+ba,y-ba), texts, fill=shadow, font=font)
    drawing.text((x,y), texts, fill=colour, font=font,align="center")
    f1.save(txt)
    f2=Image.open(cover).resize((3000,3000))
    f2.paste(f1,f1)
    f2.save(hasil)
    client.sendImage(to,hasil)
    
def logo1(to,her):
    foto=client.downloadFileURL(her,saveAs="LineAPI/tmp/coba.jpg")
    n="LineAPI/tmp/coba1.png"
    n1="LineAPI/tmp/tes.jpg"
    f1=Image.open("LineAPI/tmp/coba.jpg").resize((1500,1500))
    f2=Image.open(n).resize((600,450))
    f1.paste(f2,f2)
    f1.save(n1)
    client.sendImage(to,n1)
     
def ktext(to,text):
    cari=text.replace(" ","+")
    r=requests.get('https://flamingtext.com/Free-Logo-Designs?text={}'.format(cari))
    b=BeautifulSoup(r.text,'lxml')
    i=['https://flamingtext.com'+il.find('img')['logo-src'] for il in b.findAll('div',{'class':'ft-logo-2x ft-white'})]
    a = random.randint(0,8)
    sendIL(to,i[a])
    
def hkfs(to,txt):
    cound = txt.split("|")
    img = ["fs0","fs1","fs2","fs3","fs4","fs5","fs6","fs7","fs8","fs9","fs10"]
    a = ["120","520","300","165","275","200","270","150","450","200","170"]
    b = ["340","320","150","550","500","70","300","320","310","220","230"]
    c = ["30","50","35","100","50","60","60","50","40","30","20"]
    nu = int(cound[1])#random.randint(0,2)
    x = int(a[nu])
    y = int(b[nu])
    s = int(c[nu])
    pos = (x,y)
    text = str(cound[0])
    black = (10, 20, 50)
    photo = Image.open("Foto/{}.jpg".format(img[nu]))
    drawing =  ImageDraw.Draw(photo)
    font = ImageFont.truetype("LineAPI/tmp/Afterkilly.ttf", s)
    drawing.text(pos, text, fill=black, font=font)
    nama = "Foto/tes1.jpg"
    photo.save(nama)
    client.sendImage(to,nama)
    client.deleteFile(nama)    
def hkfs1(to,txt):
    img = ["fs0","fs1","fs2","fs3","fs4","fs5","fs6","fs7","fs8","fs9","fs10"]
    a = ["120","520","300","165","275","200","270","150","450","200","170"]
    b = ["340","320","150","550","500","70","300","320","310","220","230"]
    c = ["30","50","35","100","50","60","60","50","40","30","20"]
    nu = random.randint(0,10)
    x = int(a[nu])
    y = int(b[nu])
    s = int(c[nu])
    pos = (x,y)
    text = txt
    black = (10, 20, 50)
    photo = Image.open("Foto/{}.jpg".format(img[nu]))
    drawing =  ImageDraw.Draw(photo)
    font = ImageFont.truetype("LineAPI/tmp/Afterkilly.ttf", s)
    drawing.text(pos, text, fill=black, font=font)
    nama = "Foto/tes1.jpg"
    photo.save(nama)
    client.sendImage(to,nama)
    client.deleteFile(nama)
     
def youtubesearch(to,text):
    with open("tmp/komik.json","w") as error:
        error.write("{}")
    page = simple["youtubenext"]
    #page1 = simple["youtubeprev"]
    r=requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&q={}&type=video&key=AIzaSyBgLiO8GoVAXggNkuT9Ps0wjjgsBCuRTrw".format(text)).text
    d=json.loads(r)
    del page
    #del page1
    simple["youtubenext"]=d["nextPageToken"]
    #simple["youtubeprev"]=d["prevPageToken"]
    #print("Sukses mengganti page : "+simple["youtube"])
    j="listnya gaes"
    no=0
    data =[]
    for i in d["items"]:
        linkvideo = "https://youtu.be/" + i["id"]["videoId"]
        linkchannel = "https://m.youtube.com/channel/" + i["snippet"]["channelId"]
        title = i["snippet"]["title"]
        description = i["snippet"]["description"]
        foto = i["snippet"]["thumbnails"]["high"]["url"]
        namachannel = i["snippet"]["channelTitle"]
        data.append({"videoid":linkvideo,"channelid":linkchannel,"title":title,"dec":description,"img":foto,"upload":namachannel})
        komikanime = {"result":data}
        f = codecs.open("tmp/komik.json","w","utf-8")
        json.dump(komikanime, f, sort_keys=True, indent=4, ensure_ascii=False)
    for yout in komikanime["result"]:
        no += 1
        j+="\n"+str(no)+"."+yout["title"]
    client.sendMessage(to,j)
def youtubenextpage(to,text):
    with open("tmp/komik.json","w") as error:
        error.write("{}")
    page = simple["youtubenext"]
    page1 = simple["youtubeprev"]
    r=requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&q={}&type=video&pageToken={}&key=AIzaSyBgLiO8GoVAXggNkuT9Ps0wjjgsBCuRTrw".format(text,page)).text
    d=json.loads(r)
    del page
    del page1
    simple["youtubenext"]=d["nextPageToken"]
    simple["youtubeprev"]=d["prevPageToken"]
    #print("Sukses mengganti page : "+simple["youtube"])
    j="listnya gaes"
    no=0
    data =[]
    for i in d["items"]:
        linkvideo = "https://youtu.be/" + i["id"]["videoId"]
        linkchannel = "https://m.youtube.com/channel/" + i["snippet"]["channelId"]
        title = i["snippet"]["title"]
        description = i["snippet"]["description"]
        foto = i["snippet"]["thumbnails"]["high"]["url"]
        namachannel = i["snippet"]["channelTitle"]
        data.append({"videoid":linkvideo,"channelid":linkchannel,"title":title,"dec":description,"img":foto,"upload":namachannel})
        komikanime = {"result":data}
        f = codecs.open("tmp/komik.json","w","utf-8")
        json.dump(komikanime, f, sort_keys=True, indent=4, ensure_ascii=False)
    for yout in komikanime["result"]:
        no += 1
        j+="\n"+str(no)+"."+yout["title"]
    client.sendMessage(to,j)
def youtubeprevpage(to,text):
    with open("tmp/komik.json","w") as error:
        error.write("{}")
    page = simple["youtubeprev"]
    page1 = simple["youtubenext"]
    r1=requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&q={}&type=video&pageToken={}&key=AIzaSyBgLiO8GoVAXggNkuT9Ps0wjjgsBCuRTrw".format(text,page)).text
    d1=json.loads(r1)
    del page
    del page1
    simple["youtubenext"]=d1["nextPageToken"]
    simple["youtubeprev"]=d1["prevPageToken"]
    #print("Sukses mengganti page : "+simple["youtube"])
    j1="listnya gaes"
    no1=0
    data = []
    for i in d1["items"]:
        linkvideo = "https://youtu.be/" + i["id"]["videoId"]
        linkchannel = "https://m.youtube.com/channel/" + i["snippet"]["channelId"]
        title = i["snippet"]["title"]
        description = i["snippet"]["description"]
        foto = i["snippet"]["thumbnails"]["high"]["url"]
        namachannel = i["snippet"]["channelTitle"]
        data.append({"videoid":linkvideo,"channelid":linkchannel,"title":title,"dec":description,"img":foto,"upload":namachannel})
        komikanime = {"result":data}
        f = codecs.open("tmp/komik.json","w","utf-8")
        json.dump(komikanime, f, sort_keys=True, indent=4, ensure_ascii=False)
    for yout in komikanime["result"]:
        no1 += 1
        j1+="\n"+str(no1)+"."+yout["title"]
    client.sendMessage(to,j1)
    
def wesing(to,url):
    cari=url.replace('https://wesingapp.com/','')
    r=requests.get('https://singdownloader.com/wesing/{}#result'.format(cari)).text
    b=BeautifulSoup(r,'lxml')
    s=b.find('video')
    img=s.get('poster')
    vido=s.find('source')['src']
    client.sendImageWithURL(to,img)
    client.sendAudioWithURL(to,vido)
    
def extraxtiktok(html):
        nonce_start = '<head nonce="'
        nonce_end = '">'
        nonce = html.split(nonce_start)[1].split(nonce_end)[0]
        j_raw = html.split(
            '<script id="__NEXT_DATA__" type="application/json" nonce="%s" crossorigin="anonymous">'
            % nonce
        )[1].split("</script>")[0]
        return j_raw

def tiktoklist(to,tex):
    text=tex.split("|")
    url="https://www.tiktok.com/@{}?lang=id-ID".format(text[0])
    header={
        "user-agent": "Mozilla/5.0 (Macstrosh; strel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36",
        "referer": "https://www.tiktok.com/",
        "cookie": "tt_webid_v2=689854141086886123"
     }
    r=requests.get(url,headers=header)
    baca=extraxtiktok(r.text)
    data=json.loads(baca)
    a="https://www.tiktok.com/@"+text[0]+"/video/"+data["props"]["pageProps"]["items"][int(text[1])]["id"]
    Print(to,a)
def tiktokuser(to,text):
  url="https://www.tiktok.com/@{}?lang=id-ID".format(text)
  header={
        "user-agent": "Mozilla/5.0 (Macstrosh; strel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36",
        "referer": "https://www.tiktok.com/",
        "cookie": "tt_webid_v2=689854141086886123"
     }
  req=requests.get(url,headers=header)
  baca=extraxtiktok(req.text)
  data=json.loads(baca)
  data1=data["props"]["pageProps"]["userInfo"]["user"]
  data2=data["props"]["pageProps"]["userInfo"]["stats"]
  img=data1["avatarLarger"]
  if "bioLink" in data1:
      res="nickname: "+data1["nickname"]
      res+="\nuniqueId: "+data1["uniqueId"]
      res+="\nbiolink: "+data1["bioLink"]["link"]
      res+="\nfollowerCount: "+str(data2["followerCount"])
      res+="\nfollowingCount: "+str(data2["followingCount"])
      res+="\nheart: "+str(data2["heart"])
      res+="\nheartCount: "+str(data2["heartCount"])
      res+="\nvideoCount: "+str(data2["videoCount"])
      res+="\ndiggCount: "+str(data2["diggCount"])
      sendIL(to,img)
      sendFooter(to,res)
  else:
      res="nickname: "+data1["nickname"]
      res+="\nuniqueId: "+data1["uniqueId"]
      res+="\nsignature: "+data1["signature"]
      res+="\nfollowerCount: "+str(data2["followerCount"])
      res+="\nfollowingCount: "+str(data2["followingCount"])
      res+="\nheart: "+str(data2["heart"])
      res+="\nheartCount: "+str(data2["heartCount"])
      res+="\nvideoCount: "+str(data2["videoCount"])
      res+="\ndiggCount: "+str(data2["diggCount"])
      sendIL(to,img)
      sendFooter(to,res)
    
def testiktokaq():
    url="https://t.tiktok.com/api/item/detail/?itemId=7032582930652204290&language=en"
    header={
        "user-agent": "Mozilla/5.0 (Macstrosh; strel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36",
        "referer": "https://www.tiktok.com/",
        "cookie": "tt_webid_v2=689854141086886123"
    }
    req=requests.get(url,headers=header)
    baca=extraxtiktok(req.text)
    return baca
    
def isgd(url):
    r=requests.get("https://is.gd/create.php?format=json&callback=myfunction&url="+url+"&shorturl").text[26:-5]
    return(r)
  
def TimelineCreate(to,msg,cmd):
    h = []
    s = []
    if cmd == 'tagtimeline':
        sakui = client.getProfile()
        group = client.getGroup(msg.to);nama = [contact.mid+'||//{}'.format(contact.displayName) for contact in group.members];nama.remove(sakui.mid+'||//{}'.format(sakui.displayName))
        data = nama
        k = len(data)//300
        for aa in range(k+1):
            nos = 0
            if aa == 0:dd = '╭──Tagall timeline──';no=aa
            else:dd = '╭──Tagall timeline──';no=aa*300
            msgas = dd
            for i in data[aa*300 : (aa+1)*300]:
                no+=1
                if no == len(data):msgas+='\n╰{}. @'.format(no)
                else:msgas+='\n├{}. @'.format(no)
            msgas = msgas
            for i in data[aa*300 : (aa+1)*300]:
                gg = []
                dd = ''
                for ss in msgas:
                    if ss == '@':
                        dd += str(ss)
                        gg.append(dd.index('@'))
                        dd = dd.replace('@',' ')
                    else:
                        dd += str(ss)
                s.append({'type': "RECALL", 'start': gg[nos], 'end': gg[nos]+1, 'mid': str(i.split('||//')[0])})
                nos +=1
            h = client.createPost2(msgas,holdingTime=None,textMeta=s)
            client.sendMessage(to,"done tag timeline")
def NoteCreate(to,msg,cmd):
    s = []
    if cmd == 'tagnote':
        sakui = client.getProfile()
        group = client.getGroup(msg.to);nama = [contact.mid+'||//{}'.format(contact.displayName) for contact in group.members];nama.remove(sakui.mid+'||//{}'.format(sakui.displayName))
        data = nama
        k = len(data)//300
        for aa in range(k+1):
            nos = 0
            if aa == 0:dd = '╭──Absen──';no=aa
            else:dd = '╭──Absen──';no=aa*300
            msgas = dd
            for i in data[aa*300 : (aa+1)*300]:
                no+=1
                if no == len(data):msgas+='\n╰{}. @'.format(no)
                else:msgas+='\n├{}. @'.format(no)
            msgas = msgas
            for i in data[aa*300 : (aa+1)*300]:
                gg = []
                dd = ''
                for ss in msgas:
                    if ss == '@':
                        dd += str(ss)
                        gg.append(dd.index('@'))
                        dd = dd.replace('@',' ')
                    else:
                        dd += str(ss)
                s.append({'type': "RECALL", 'start': gg[nos], 'end': gg[nos]+1, 'mid': str(i.split('||//')[0])})
                nos +=1
            client.createGroupPostMention(msg.to,msgas,holdingTime=None,textMeta=s)
    else:
      if cmd.startswith("createnote "):
        sep = msg.text.split(" ")
        pesan = msg.text.replace(sep[0] + " ","")
        client.createGroupPostText(to,pesan,holdingTime=None)#,textMeta=s)
          
def youtube(query):
        search_url="https://www.youtube.com/results?search_query="
        mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
        sb_url = search_url + query
        sb_get = requests.get(sb_url, headers = mozhdr)
        soupeddata = BeautifulSoup(sb_get.content, "html.parser")
        yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
        x = (yt_links[1])
        yt_href =  x.get("href")
        yt_href = yt_href.replace("watch?v=", "")
        yt_final = "https://youtu.be" + str(yt_href)
        return yt_final
      
def cdet(to,query):
    time.sleep(1)
    home = client.getProfileCoverDetail(query)
    if "videoCoverObsInfo" in home['result']:
      cv = "https://obs.line-apps.com/r/myhome/vc/"+home['result']['videoCoverObsInfo']['objectId']
      c = "https://obs.line-apps.com/r/myhome/c/"+home['result']['coverObsInfo']['objectId']
      sendIL(to,c)
      sendVLP(to,cv,c)
    else:
      c = "https://obs.line-apps.com/r/myhome/c/"+home['result']['coverObsInfo']['objectId']
      sendIL(to,c)
  
def pdet(to,query):
    time.sleep(1)
    a=client.getContact(query)
    if a.videoProfile == None:
      fotomu = "https://obs.line-scdn.net/{}".format(a.pictureStatus)
      sendIL(to,fotomu)
    else:
      fotomu = ("https://obs.line-scdn.net/{}".format(a.pictureStatus))
      videomu = ("https://obs.line-scdn.net/{}/vp".format(a.pictureStatus))
      fotov=ezgifvideotogif(videomu)
      sendIL(to,fotomu)
      sendVLP(to,videomu,fotov)
          
def pafyaudio(to,txt):
    pa=pafy.new(txt)
    au=pa.getbestaudio()
    audi=au.url
    idm=txt.replace("https://youtu.be/","")
    imag="https://i.ytimg.com/vi/{}/hqdefault.jpg".format(idm)
    Print(to,pa)
    sendIL(to,imag)
    sendAL(to,audi)
    #sendVLP(to,vidi,imag)
  
def pafyvideo(to,txt):
    pa=pafy.new(txt)
    au=pa.getbestvideo()
    audi=au.url
    idm=txt.replace("https://youtu.be/","")
    imag="https://i.ytimg.com/vi/{}/hqdefault.jpg".format(idm)
    Print(to,pa)
    sendIL(to,imag)
    sendVLP(to,audi,imag)
  
def pafyall(to,txt):
    pa=pafy.new(txt)
    au=pa.getbest()
    audi=au.url
    au1=pa.getbestvideo()
    audi1=au1.url
    idm=txt.replace("https://youtu.be/","")
    imag="https://i.ytimg.com/vi/{}/hqdefault.jpg".format(idm)
    Print(to,pa)
    sendIL(to,imag)
    sendAL(to,audi)
    sendVLP(to,audi1,imag)
def ims(to,tex):
    query=tex.split("|")
    url="https://id.images.search.yahoo.com/search/images;_ylt=AwrPh0r0jlhgVGYAdxQpUSQ5?p={}&fr=yfp-hrmob&fr2=piv-web&.tsrc=yfp-hrmob".format(query[0])
    b=BeautifulSoup(requests.get(url).text,"lxml")
    i2=[a.get("data") for a in b.findAll("li",{"class":"ld"})]
    data=[]
    for l in i2:
      if "ourl" in l:
        l1=json.loads(l)
      #link=l1["rurl"]
        im=l1["ourl"]
        tit=l1["alt"]
        data.append({"image":im,"title":tit})
    result={"data":data}
    if len(query) == 1:
      title="List image"
      no=0
      for isi in result["data"]:
          no+=1
          title+="\n"+str(no)+"."+isi["title"]
      client.sendMessage(to,title)
    if len(query) == 2:
      num = int(query[1])
      b = result["data"][num - 1]
      if ".gif" in b["image"]:
        sendVL2(to,b["image"])
      else:
        sendIL2(to,b["image"])
    
def tenor(to,tex):
    query=tex.split("|")
    r=BeautifulSoup(requests.get("https://tenor.com/search/{}".format(query[0])).text,"lxml").find("script",{"id":"store-cache"})
    with open('print.txt', 'w') as er:
      er.write("{}".format(r))
    with open('print.txt', 'r') as er:
      a=er.read()
      a1=a.split('>')[1].split("<")[0]
      a2=json.loads(a1)
      data=[]
      for isi in a2['gifs']['search'][str(query[0]+'-low')]['results']:
        t=''+isi['h1_title']
        l=''+isi['media'][0]['gif']['url']
        data.append({'title':t,'link':l})
      result={'data':data}
      if len(query) == 1:
        title="List tenor gif"
        no=0
        for isis in result["data"]:
          no+=1
          title+="\n"+str(no)+"."+isis["title"]
        client.sendMessage(to,title)
      if len(query) == 2:
        num = int(query[1])
        b = result["data"][num - 1]
        sendVL2(to,b["link"])
  
def soundcloud(to,text):
  query=text.split("|")
  con=query[0].replace(" ","+")
  lists=[]
  urllib.request.urlretrieve("https://api-v2.soundcloud.com/search?q={}&sc_a_id=2ff50c8a9820376e92b6ab445474ccc6fe4c78db&variant_ids&facet=model&user_id=753413-427755-281581-627480&client_id=8ktYdIulPGr22O1qYsErYTFuret5nAHj&limit=31&offset=0&linked_partitioning=1&app_version=1637765321&app_locale=en".format(con),'tmp/hasil.txt')
  with open('tmp/hasil.txt',"r") as er:
    error = er.read()
    hasil = "{}".format(error)
  data=json.loads(hasil)
  data1=data["collection"]
  for am in range(1,31):
    t=data1[int(am)]["title"]
    #t=data1[int(am)]["permalink"].replace("-"," ")
    l=data1[int(am)]["permalink_url"]
    #i=data1[int(am)]["artwork_url"]
    d=data1[int(am)]["created_at"].split("T")[0]
    lists.append({"title":t,"link":l,"date":d})
  result={"data":lists}
  if len(query) == 1:
    title="List soundcloud"
    no=0
    for isi in result["data"]:
        no+=1
        title+="\n"+str(no)+"."+isi["title"]#.replace("-"," ")
    client.sendMessage(to,title)
  if len(query) == 2:
    try:
        num = int(query[1])
        b = result["data"][num - 1]
        res="Title: "+b["title"]
        res+="\nDate create: "+b["date"]
        res+="\nWeb: "+b["link"]
        Print(to,res)
        for ur in data1[num]["media"]["transcodings"]:
          if "stream/progressive" in ur["url"]:
            urllib.request.urlretrieve(ur["url"]+"?client_id=8ktYdIulPGr22O1qYsErYTFuret5nAHj",'tmp/hasil.txt')
            with open('tmp/hasil.txt',"r") as er:
              err = er.read()
              hal = "{}".format(err)
              dat=json.loads(hal)
              mp3=dat["url"]
              sendAL(to,mp3)
    except Exception as e:
        print(e)      
  
def animemp3(to, link):
    kk = "hk"
    hh=subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output {}.mp3 {}'.format(kk,'{}'.format(link)))
    try:
      client.sendAudio(to,'{}.mp3'.format(kk))
    except Exception as e:
      client.sendMessage(to,' 「 ERROR 」\nCoba link lainnya')
    os.remove('{}.mp3'.format(kk))
def laguanimemp3(to, url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    title = soup.select('p')[4].get_text().replace('  ','')
    lagu = soup.select('a')[89].get('href')
    sendFooter(to, title)
    sendAL(to, lagu)
  
def bitly(url):
    from pyshorteners import Shortener 
    ACCESS_TOKEN = 'aa7b766e403d139377fda5890e7d789b38a36ae0'
    url_shortener = Shortener('Bitly', bitly_token = ACCESS_TOKEN) 
    return url_shortener.short(url)
  
def urlsmule(to,link):
    kata=link.split("/")
    #link='https://www.smule.com/c/984842053_3873245271'
    url='https://sownloader.com/index.php?url={}#support-sownloader'.format(link)
    web=requests.get(url)
    soup=BeautifulSoup(web.text,'lxml')
    img=soup.find('img',{'class':'img-fluid sownloader-web-thumbnail'}).get('src')
    title=soup.find('img',{'class':'img-fluid sownloader-web-thumbnail'}).get('title')
    tag=soup.find('div',{'class':'col-xs-12 col-sm-9 col-md-8'}).find('p').text
    tipe=soup.find('div',{'class':'col-xs-12 col-sm-9 col-md-8'}).get_text().split('\n\n\n')[3]
    if ' Download video' in tipe:
      judul=tipe+'\nJudul: '+title+'\nDesc: '+tag
      #audio='https'+soup.findAll('a',{'class':'btn btn-block'})[0].get('href').split('https')[1].split('&')[0]
      #sendFooter(to,judul)
      #sendAL(to,audio)
      video='https'+soup.findAll('a',{'class':'btn btn-block'})[2].get('href').split('https')[1].split('&')[0]
      hasil="line://app/1602687308-GXq4Vvk9?type=video&ocu={}&piu={}".format(video,img)
      fsmule(to,img,title,tag,hasil)
    else:
      judul=' Download audio\nJudul: '+title+'\nDesc: '+tag
      audio='https'+soup.findAll('a',{'class':'btn btn-block'})[0].get('href').split('https')[1].split('&')[0]
      hasil = "line://app/1602687308-GXq4Vvk9?type=audio&link={}".format(audio)
      fsmule(to,img,title,tag,hasil)
      #sendFooter(to,judul)
      #sendIL(to,img)
      #sendAL(to,audio)
  
def songbook(to,query):
    cond = query.split('|')
    url="https://www.smule.com/{}/songs/json?offset={}&size=0&limit=24".format(str(cond[0]),int(cond[1]))
    r=requests.get(url).text
    data=json.loads(r)
    if len(cond) == 2:
      j="List songbook"
      no=0
      for h in data["list"]:
        no+=1
        j+="\n"+str(no)+"."+h["title"]
      client.sendMessage(to,j)
    if len(cond) == 3:
        num = int(cond[2])
        b = data["list"][num - 1]
        c = " Judul Songbook: "+str(b["title"])
        c += "\n Artis: "+str(b["artist"])
        c += "\n Pembuat: "+str(b["owner"]["handle"])
        c += "\n Sampul: "+str(b["owner"]["pic_url"])+" comment"
        c += "\n Id smule: https://www.smule.com"+str(b["owner"]["url"])
        c += "\n Sampul songbook: "+str(b["cover_url"])
        c += "\n Dibuat: {}".format(b["created_at"])
        c += "\n Songbook: https://www.smule.com{}".format(b["web_url"])
        hasil = "Detail Soongbook\n\n"+str(c)
        dl = str(b["cover_url"])
        sendIL(to,dl)
        sendFooter(to, hasil)
def hksmule(to,query):
    cond = query.split('|')
    mos ={
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
"Accept": "*/*",
"Sec-Fetch-Site": "none",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Accept-Encoding":    "gzip, deflate, br",
"Accept-Language":    "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
"Cookie": "L=N; connection_info=eyJjb3VudHJ5IjoiSUQiLCJob21lUG9wIjoic2YifQ%3D%3D--d082fcefd1992fd66c9f5ea3498fb86b865214b3; smule_id_production=eyJ3ZWJfaWQiOiJiYzBlNzc4MC04MjY4LTQ1MDAtYjViMS1jMWVkNzk1YjI0YmQiLCJzZXNzaW9uX2lkIjoiZzRfOV83Z0o0MHoyZjQ4YVlxblJQRG04Yy8xOXY2K0o4OW1nd0poSGMvMWUvSm1jUjlqRE4xbFRjQ3c9PSIsInBsYXllcl9pZCI6MjQxOTI1NTcxMH0%3D--11e4d5a3cba734fc4ad894180ece1606a6ddf13c"
    }
    r = requests.get("https://www.smule.com/{}/performances/json".format(cond[0]),headers=mos)
    data = json.loads(r.text)
    if len(cond) == 1:
        for li in data["list"]:
            time.sleep(7)
            tayo = "https://www.smule.com{}".format(str(li["web_url"]))
            sendFooter(to,tayo)
        
        
def logError(text):
    client.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))        

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                client.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def urlEncode(url):
        import base64
        return base64.b64encode(url.encode()).decode('utf-8')
def urlDecode(url):
        import base64
        return base64.b64decode(url.encode()).decode('utf-8')
def B64e(to, url):
    import base64
    return client.sendMessage(to, base64.b64encode(url.encode()).decode('utf-8'))
def B64e2(to, url):
    import base64
    return Print(to, base64.b64encode(url.encode()))

def B64d(to, url):
    import base64
    return client.sendMessage(to, base64.b64decode(url.encode()).decode('utf-8'))
          
def Musik(to):
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+client.getContact(clientMid).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': client.getContact(clientMid).statusMessage if client.getContact(clientMid).statusMessage != '' else 'creator By meMots |ID LINE|\nadiputra.95', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': client.getContact(clientMid).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+clientMid,'MSG_SENDER_NAME':  client.getContact(clientMid).displayName,}
    return client.sendMessage(to, client.getContact(clientMid).displayName, contentMetadata, 19)
def Musik1(to,mus):
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+client.getContact(mus).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': client.getContact(mus).statusMessage if client.getContact(mus).statusMessage != '' else 'Supproted By : ƬΣΛM HK BӨƬ ', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': client.getContact(mus).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+mus,'MSG_SENDER_NAME':  client.getContact(mus).displayName,}
    return client.sendMessage(to, client.getContact(mus).displayName, contentMetadata, 19)
               
def kisahnabi(to,text):
    cond = text.split('|')
    r=requests.get("https://islamdownload.net/126154-download-kisah-para-nabi-dan-rasul.html")
    b=BeautifulSoup(r.text,"lxml")
    c=b.findAll("div",{"align":"left"})
    if len(cond) == 1:
        judul=" Cerita Para Nabi"
        #no=0
        for a in c:
          #no+=1
          judul+="\n"+a.find("a")["href"].replace("http://islamdownload.net/files/126154/","").replace("%20"," ").replace("%26","").replace("%27","").replace("%28","").replace("%29","").replace("Abdullah Shaleh Hadrami","").replace("Abu Abdil Muhsin Firanda Andirja","").replace("Syafiq Basalamah","").replace("-","").replace(".mp3","")#.text
        sendFooter(to,judul)  
def animesexy(to, query):
        cond = query.split('|')
        url = 'https://weheartit.com/pictures/anime%20sexy%20girl?landing=false&page={}&before=77267195'.format(query)
        print(url)
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'lxml')
        a = soup.findAll('a',{'class':'js-entry-detail-link js-blc js-blc-t-entry'})
        data = []
        for i in a:
            t = i.find('img')['alt']
            f = i.find('img')['src']
            l = 'https://weheartit.com'+i.get('href')
            data.append({'judul':t,'link':l,'foto':f})        
        if len(cond) == 1:
            ret_ = '╭───「 Hasil anime sexy 」'
            no = 0
            for res in data:
                no += 1
                ret_ += '\n├ %s. %s' % (no, res['judul'])
            ret_ += '\n╰───「 By : Hk Bot 」'
            client.sendMessage(to, ret_)
        elif len(cond) == 2:
            no = int(cond[1])
            if no <= len(data):
                gets = data[no - 1]
                url1 = str(gets['link'])
                req1 = requests.get(url1)
                soup1 = BeautifulSoup(req1.text, 'lxml')
                img = soup1.findAll('img')[3].get('src')
                client.sendImageWithURL(to, img)

def tts(to, query):
        cond = query.split('|')
        url = 'http://weduskopok.blogspot.com/?m=1'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        data = soup.findAll('h2',{'class':'post-title entry-title'})
        if len(cond) == 1:
            ret_ = '╭───「 Hasil link kuis 」'
            no = 0
            for res in data:
                no += 1
                ret_ += '\n├ %s. %s' % (no, 'https:'+res.find('a')['href'])
            ret_ += '\n╰───「 By : Hk Bot 」'
            client.sendMessage(to, ret_)
        elif len(cond) == 2:
            no = int(cond[1])
            if no <= len(data):
                get = data[no - 1]
                with requests.session() as s:
                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                    r = s.get(get.find('a')['href'])
                    soup = BeautifulSoup(r.content, 'lxml')
                    a = '╭───「 Hasil kuis 」'
                    no = 0
                    for i in soup.findAll('p'):
                        no += 1 
                        a += '\n'+i.text
                    a += '\n╰───「 By : Hk Bot 」'
                    client.sendMessage(to,a)

def bukuanak(to, query):
        cond = query.split('|')
        url = 'http://www.bukabuku.com/browses/index/dept:book/cid:44/page:%s/anak-anak.html' % cond[0]
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        data = []
        for div in soup.findAll('div',{'class':'product_list_grid'}):
          for img in div.findAll('img',{'class':'product_image_small'}):
            g = img.get('src')
          for tit in div.findAll('div',{'class':'content'}):
            j = tit.find('a').text
            l = 'http://www.bukabuku.com'+tit.find('a')['href']
            data.append({'image':g,'judul':j,'link':l})
        result = {'data':data}    
        if len(cond) == 1:
              ret_ = '╭───「 Hasil List Buku 」'
              no = 0
              for res in result['data']:
                  no += 1
                  ret_ += '\n├ %s. %s' % (no, res['judul'])
              ret_ += '\n╰───「 By : Hk Bot 」'
              client.sendMessage(to, ret_)
        elif len(cond) == 2:
            no = int(cond[1])
            if no <= len(result['data']):
                get = result['data'][no - 1]
                res = 'Judul : {}'.format(get['judul'])
                res += '\nImage : {}'.format(get['image'])
                res += '\nLink : {}'.format(get['link'])
                client.sendImageWithURL(to, get['image'])
                client.sendMessage(to, res)
                    
def soal(to, query):
        cond = query.split('|')
        url = 'https://blog.ruangguru.com/tag/ujian-nasional'  
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        data = soup.findAll('h2',{'class':'title-list-web'})
        if len(cond) == 1:
            ret_ = '╭───「 Hasil link UN 」'
            no = 0
            for res in data:
                no += 1
                ret_ += '\n├ %s. %s' % (no, res.find('a').text)
            ret_ += '\n╰───「 By : Hk Bot 」'
            client.sendMessage(to, ret_)
        elif len(cond) == 2:
            no = int(cond[1])
            if no <= len(data):
                get = data[no - 1]
                with requests.session() as s:
                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                    r = s.get(get.find('a')['href'])
                    soup = BeautifulSoup(r.content, 'lxml')
                    a = '╭───「 Hasil ulangan 」'
                    no = 0
                    for i in soup.findAll('p'):
                        no += 1 
                        a += '\n'+i.text
                    k = len(a)//10000
                    for aa in range(k+1):
                         client.sendMessage(to,'{}'.format(a[aa*10000 : (aa+1)*10000]))                                    
                    #a += '\n╰───「 By : Hk Bot 」'
                    #client.sendMessage(to,a)
                    
def deanime(to, query):
        cond = query.split('|')
        url = 'https://anime.desktopnexus.com/all/%s' % cond[0]
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        data = soup.findAll('td',{'style':'height: 122px;'})
        if len(cond) == 1:
            ret_ = '╭───「 Hasil anime image 」'
            no = 0
            for res in data:
                no += 1
                ret_ += '\n├ %s. %s' % (no, 'https:'+res.find('a')['href'])
            ret_ += '\n╰───「 By : Hk Bot 」'
            client.sendMessage(to, ret_)
        elif len(cond) == 2:
            no = int(cond[1])
            if no <= len(data):
                get = data[no - 1]
                with requests.session() as s:
                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                    r = s.get('https:'+get.find('a')['href'])
                    soup = BeautifulSoup(r.content, 'lxml')
                    img = 'https:'+soup.findAll('img')[6].get('src')
                    client.sendImageWithURL(to, img)
def drakor(to, query):
    cond = query.split('|')
    url='https://drakorindo.best/category/drama-korea/drama-korea-complete/page/{}/'.format(cond[0])
    h={
      'User-Agent': 'WebSniffer/1.0 (+http://websniffer.cc/)',
      'Accept': '*/*',
      'Referer': 'https://websniffer.cc/'
    }
    r=BeautifulSoup(requests.get(url,headers=h).text,'lxml')
    h3=r.findAll('h3', {'class':'entry-title mh-loop-title'})    
    if len(cond) == 1:
      ret_ = '╭───「 Hasil drakor 」'
      no = 0
      for res in h3:
        no += 1
        ret_ += '\n├ %s. %s' % (no, res.find('a').text.replace('\n',''))
      ret_ += '\n╰───「 By : Hk Bot 」'
      client.sendMessage(to, ret_)
    if len(cond) == 2: 
      num = int(cond[1])
      ur=h3[num-1]
      r1=BeautifulSoup(requests.get(ur.find('a')['href'],headers=h).text,'lxml')
      dat=r1.select('p > a')
      no=0
      ep='{}'.format(ur.find('a').text.replace('\n',''))
      data=[]
      for i in dat:
        if 'Zippyshare' in i.text:
            no+=1
            ep+='\n\nepisode ke'+str(no)+'\n'+i.get('href')
      client.sendMessage(to,ep)
  
def playlist(to, query):
        cond = query.split('|')
        r=requests.get("https://downloadlagu123.mobi/search.html?q=%s" % cond[0])
        soup = BeautifulSoup(r.text,'lxml')
        data = soup.findAll('div', attrs={'class':'detail-thumb'})
        if len(cond) == 1:
            ret_ = '╭───「 Hasil Joox 」'
            no = 0
            for l in data:
                no += 1
                ret_ += '\n├ %s. %s' % (no, (l.find("img")["alt"]))
            ret_ += '\n╰───「 By : Hk Bot 」'
            client.sendMessage(to, ret_)
        elif len(cond) == 2:
          try:
              no = int(cond[1])
              if no <= len(data):
                hasil = data[no - 1]
                link=str('https://downloadlagu123.mobi'+hasil.find('a')['href'])
                #print(link)
                url = requests.get(link)
                sou = BeautifulSoup(url.text,'lxml')
                img=sou.find('div',attrs={'class':'bh-thumb detail-thumb'})
#                inf=sou.find('div',attrs={'class':'bh-info'})
 #               wkt=sou.find('b',attrs={'class':'play-count'})
                #lrk=sou.findAll('script')[2].text.split('\n')
                foto=img.find('img')['src']
                audi='https://downloadlagu123.mobi'+sou.find('source')['src']
                #liriknya=lrk[1]('''"''')
                client.sendImageWithURL(to, foto)
                client.sendAudioWithURL(to, audi)
                #client.sendMessage(to, liriknya[1].replace("<br \\/>\\r\\n","\n"))
          except Exception as e:
            print(e)
#        client.sendMessage(to, "「 Result Error 」\n"+str(e))
          llrik=str('https://downloadlagu123.mobi'+hasil.find('a')['href'])
          #print(llrik)
          rl = requests.get(llrik)
          sl = BeautifulSoup(rl.text,'lxml')
          if sl.findAll('script')[2].text:
            lrk=sl.findAll('script')[2].text.split('\n')
            #print(lrk)
            liriknya=lrk[1].split('''"''')
            #print(liriknya)
            client.sendMessage(to, liriknya[1].replace("<br \\/>\\r\\n","\n"))
          else:
            client.sendMessage(to,"Maaf lirik tidak tersedia")
            
        
            
def searchjoox(to, query):
    cond = query.split('|')
    url='https://hkjooxv1.herokuapp.com/websearch.php'
    data=[]
    d={
      'q':cond[0],
      'w':1,
      'e':0,
      'r':29
    }
    req=requests.post(url,data=d).json()
    r9=req["content"]
    b6=BeautifulSoup(r9,"lxml")
    a6=b6.select("td > a")
    for i5 in a6:
      if "song.php?" in i5.get("href"):
        link=i5.get("href").replace("song.php?id=","")
        title=i5.text
        data.append({"kode":link,"judul":title})
    res={"data":data}
    if len(cond) == 1:
      ret_ = '╭───「 Hasil Joox 」'
      no = 0
      for l in res["data"]:
        no += 1
        ret_ += '\n├ %s. %s' % (no, l["judul"])
      ret_ += '\n╰───「 By : Hk Bot 」'
      client.sendMessage(to, ret_)
    elif len(cond) == 2:
      no = int(cond[1])
      if no <= len(res["data"]):
        gets = res["data"][no - 1]
        kode = str(gets['kode'])
        url2=requests.get("https://hkjooxv1.herokuapp.com/song.php?id={}".format(kode)).text
        bs=BeautifulSoup(url2,"lxml")
        jdl=[c.find("h2").text for c in bs.findAll("div",{"class":"text-center"})]
        imag=[c1.find("img")["src"] for c1 in bs.findAll("div",{"class":"text-center"})]
        audi=[c2.find("source")["src"] for c2 in bs.findAll("div",{"class":"text-center"})]
        tex=[c3.text for c3 in bs.findAll("b")]
        ly=[c4.text for c4 in bs.findAll("pre")]
        lyr=ly[0].replace("\n\n","").replace("***Recoded By J***","")
        des="Waktu rilis: "+tex[0]
        des+="\nArtis: "+tex[1]
        des+="\nAlbum: "+tex[2]
        des+="\nTitle: "+jdl[0]
        des+="\nPlaytime: "+tex[3]
        des+="\n\n "+lyr
        sendIL(to,imag[0])
        client.sendAudioWithURL(to,audi[0])
        sendFooter(to,des)
        
def joox(to, query):
    url='https://hkjooxv1.herokuapp.com/websearch.php'
    d={
      'q':query,
      'w':1,
      'e':0,
      'r':29
    }
    req=requests.post(url,data=d).json()
    r=req["content"]
    b=BeautifulSoup(r,"lxml")
    a=b.select("td > a")
    data=[]
    for i in a:
      if "song.php?" in i.get("href"):
        link=i.get("href")
        data.append(link)
    res=data[0]
    url2=requests.get("https://hkjooxv1.herokuapp.com/{}".format(res)).text
    bs=BeautifulSoup(url2,"lxml")
    jdl=[c.find("h2").text for c in bs.findAll("div",{"class":"text-center"})]
    imag=[c1.find("img")["src"] for c1 in bs.findAll("div",{"class":"text-center"})]
    audi=[c2.find("source")["src"] for c2 in bs.findAll("div",{"class":"text-center"})]
    tex=[c3.text for c3 in bs.findAll("b")]
    ly=[c4.text for c4 in bs.findAll("pre")]
    lyr=ly[0].replace("\n\n","").replace("***Recoded By J***","")
    des="Waktu rilis: "+tex[0]
    des+="\nArtis: "+tex[1]
    des+="\nAlbum: "+tex[2]
    des+="\nTitle: "+jdl[0]
    des+="\nPlaytime: "+tex[3]
    musi=""+audi[0]
    artist=""+tex[1]
    title=""+jdl[0]
    foto=""+imag[0]
    mus="line://app/1602687308-GXq4Vvk9?type=audio&link={}".format(musi)
  #  sendIL(to,foto)
  #  Print(to,des)
  #  sendAL(to,musi)
    fjoox(to,foto,mus,title,artist)
    
def ljoox(to, query):
    url='https://hkjooxv1.herokuapp.com/websearch.php'
    d={
      'q':query,
      'w':1,
      'e':0,
      'r':29
    }
    req=requests.post(url,data=d).json()
    r=req["content"]
    b=BeautifulSoup(r,"lxml")
    a=b.select("td > a")
    data=[]
    for i in a:
      if "song.php?" in i.get("href"):
        link=i.get("href")
        data.append(link)
    res=data[0]
    url2=requests.get("https://hkjooxv1.herokuapp.com/{}".format(res)).text
    bs=BeautifulSoup(url2,"lxml")
    audi=[c2.find("source")["src"] for c2 in bs.findAll("div",{"class":"text-center"})]
    Print(to,audi[0])
    

def lirik(to, query):
    with requests.session() as web:
        web.headers["user-agent"] = "Mozilla/5.0"# (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
        url = web.get("https://www.musixmatch.com/search/{}".format(urllib.parse.quote(query)))
        data = BeautifulSoup(url.content, "html.parser")
        for trackList in data.findAll("ul", {"class":"tracks list"}):
             urls = [urlList["href"] for urlList in trackList.findAll("a")]
             lirik = urls[0]
             print(lirik)
        with requests.session() as web:
            web.headers["user-agent"] = "Mozilla/5.0"
            url1 = web.get("https://www.musixmatch.com{}".format(urllib.parse.quote(lirik)))
            data1 = BeautifulSoup(url1.content, "lxml")
            lyr = data1.findAll('p',attrs={"class":"mxm-lyrics__content"})
            lyrs = []
            hsl =''
            for i in lyr:
                lyrs.append(i)
            for i in lyrs:  
                hsl += i.text
            hsl +=''
            client.sendMessage(to, hsl)
            
def Jprint(to,text):
    Print(to,json.dumps(text, indent=4, sort_keys=True))
            
def Print(to,text):
    with open('tmp/print.txt', 'w') as er:
      er.write("{}".format(text))
    with open('tmp/print.txt',"r") as er:
      error = er.read()
      hasil = "{}".format(error)
      k = len(hasil)//10000
    for aa in range(k+1):
      client.sendMessage(to,"{}".format(hasil[aa*10000 : (aa+1)*10000]))
    with open('tmp/print.txt', 'w') as er:
      er.write("")
    
def tagdia(to, text="",ps='', mids=[]):
        arrData = ""
        arr = []
        mention = "@MentionOrang "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ''
            h = ''
            for mid in range(len(mids)):
                h+= str(texts[mid].encode('unicode-escape'))
                textx += str(texts[mid])
                if h != textx:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 13
                else:slen = len(textx);elen = len(textx) + 13
                arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ''
            slen = len(textx)
            elen = len(textx) + 18
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        client.sendMessage(to, textx, {'MSG_SENDER_NAME': client.getContact(ps).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + client.getContact(ps).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = client.genOBSParams({'oid': clientMid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = client.server.postContent('{}/talk/vp/upload.nhn'.format(str(client.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        client.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
  
def changeVideoAndPictureProfileCover(vids, pic):
    upd=client.updateProfileCover(pic)
    i1=upd['result']['homeInfo']['objectId']
    client.uploadObjHome1(vids,type="video",objId=i1)
    client.updateProfileCoverById1(i1,i1)
def changePictureProfileCover(vids,pic):
    upd=client.updateProfileCover(pic)
    i1=upd['result']['homeInfo']['objectId']
    client.uploadObjHome1(vids,type="video",objId=i1)
    client.updateProfileCoverById1(i1,i1)
        
def changeVideoAndPictureProfile2(path, path2):
    try:
        files = {'file': open(path, 'rb')}
        data = {'params':client.genOBSParams({'oid': mid,'ver': '2.0','type':'video','cat': 'vp.mp4'})}
        r_vp = client.server.postContent(client.server.LINE_OBS_DOMAIN + '/talk/vp/upload.nhn',data=data, files=files)
        if r_vp.status_code != 201:
            raise Exception('update profile video picture failure.')
        client.updateProfilePicture(path2, 'vp')
    except Exception as e:
        print(str(e))
                    
def changeProfileVideo(to):
    if settings['changeProfileVideo']['picture'] == None:
        return client.sendMessage(to, "Foto tidak ditemukan")
    elif settings['changeProfileVideo']['video'] == None:
        return client.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings['changeProfileVideo']['video']
        files = {'file': open(path, 'rb')}
        obs_params = client.genOBSParams({'oid': client.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = client.server.postContent('{}/talk/vp/upload.nhn'.format(str(client.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return client.sendMessage(to, "Gagal update profile")
        path_p = settings['changeProfileVideo']['picture']
        settings['changeProfileVideo']['status'] = False
        client.updateProfilePicture(path_p, 'vp')
            
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    
def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Hai Kak ".format(str(mid))
        arr = []
        no = 1
        num = 2
        for i in mid:
            #ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+settings["welcome"]#+"\n❄ Digroup: "+str(ginfo.name)+"\n❄ By: ƬΣΛM HK BӨƬ"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        client.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Nah kenapa itu kak  ".format(str(mid))
        arr = []
        no = 1
        num = 2
        for i in mid:
            #ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+settings["leave"]#+"\n❄ Digroup: "+str(ginfo.name)+"\n❄ By: ƬΣΛM HK BӨƬ"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        client.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+settings["mention"]
            if no < len(mid):
                no += 1
                textx += "╠ " % (num)
                num=(num+1)
            else:
                try:
                    no += "╚══[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        client.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def Members(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention#+settings["mention"]
            if no < len(mid):
                no += 1
                textx += "╠ " % (num)
                num=(num+1)
            else:
                try:
                    no += "╚══[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        client.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
def removeCmd(cmd, text):
	key = settings["keyCommand"]
	if settings["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]
    
def sendFooter(to, isi):
    bos="ud6c61693e1f34a569b97894d11a52767"
    data = {
        "type": "text",
        "text": isi,
        "sentBy": {
            "label": "ƬΣΛM HK BӨƬ",
            "iconUrl": "https://obs.line-scdn.net/{}".format(client.getContact(bos).pictureStatus),
            "linkUrl": "line://nv/profilePopup/mid=ud6c61693e1f34a569b97894d11a52767"
        }
    }
    client.postTemplate(to, data)
#    sendTemplate(to, data)
def sendIL(to, isi):
    bos="ud6c61693e1f34a569b97894d11a52767"
    data = {
    "type": "image",
    "originalContentUrl": isi,
    #"duration": 60000,
    "previewImageUrl": isi,
#    "sentBy": {
#      "label": "ƬΣΛM HK BӨƬ",
#      "iconUrl": "https://obs.line-scdn.net/{}".format(client.getContact(bos).pictureStatus),
#      "linkUrl": "line://nv/profilePopup/mid=ud6c61693e1f34a569b97894d11a52767"
#      }
    }
    client.postTemplate(to, data)
def sendIL2(to, isi):
    bos="ud6c61693e1f34a569b97894d11a52767"
    data = {
    "type": "image",
    "originalContentUrl": isi,
    #"duration": 60000,
    "previewImageUrl": isi,
    "sentBy": {
      "label": "ƬΣΛM HK BӨƬ",
      "iconUrl": "https://obs.line-scdn.net/{}".format(client.getContact(bos).pictureStatus),
      "linkUrl": "line://nv/profilePopup/mid=ud6c61693e1f34a569b97894d11a52767"
      }
    }
    client.postTemplate(to, data)
def sendAL(to, isi):
    #bos="ud6c61693e1f34a569b97894d11a52767"
    data = {
    "type": "audio",
    "originalContentUrl": isi,
    "duration": 60000
    }
    client.postTemplate(to, data)
def sendVL(to, isi):
    #bos="ud6c61693e1f34a569b97894d11a52767"
    data = {
    "type": "video",
    "originalContentUrl": isi,
    #"duration": 60000,
    "previewImageUrl": "https://i.ytimg.com/vi/jxBfCwr-2v4/maxresdefault.jpg"
    }
    client.postTemplate(to, data)
def sendVL2(to, isi):
    #bos="ud6c61693e1f34a569b97894d11a52767"
    data = {
    "type": "video",
    "originalContentUrl": isi,
    #"duration": 60000,
    #"previewImageUrl": isi
    }
    client.postTemplate(to, data)
def sendVLP(to, isi,img):
    #bos="ud6c61693e1f34a569b97894d11a52767"
    data = {
    "type": "video",
    "originalContentUrl": isi,
    #"duration": 60000,
    "previewImageUrl": img
    }
    client.postTemplate(to, data)
def sendSL(to, pkg,stk):
    #bos="ud6c61693e1f34a569b97894d11a52767"
    data = {
    "type": "sticker",
    "packageId": pkg,
    "stickerId": stk
    }
    client.postTemplate(to, data)
def helpspam():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpSpam =      "╔══[ ƬΣΛM HK BӨƬ ]" + "\n" + \
                    "╠ Gunakan 「"+ key +"」 "+ "\n" + \
                    "╠ Command Spam"+ "\n" + \
                    "╠══════════════"+"\n"+\
                    "╠ " + key + "Addvideo「kata」"+ "\n" + \
                    "╠ " + key + "Delvideo「kata」"+ "\n" + \
                    "╠ " + key + "Listvideo"+ "\n" + \
                    "╠ " + key + "Addaudio「kata」"+ "\n" + \
                    "╠ " + key + "Delaudio「kata」"+ "\n" + \
                    "╠ " + key + "Listaudio"+ "\n" + \
                    "╠ " + key + "Addfoto「kata」"+ "\n" + \
                    "╠ " + key + "Delfoto「kata」"+ "\n" + \
                    "╠ " + key + "Listfoto"+ "\n" + \
                    "╠ " + key + "Addstik「kata」"+ "\n" + \
                    "╠ " + key + "Delstik「kata」"+ "\n" + \
                    "╠ " + key + "Lstik"+ "\n" + \
                    "╠ " + key + "Addtikel「kata」"+ "\n" + \
                    "╠ " + key + "Deltikel「kata」"+ "\n" + \
                    "╠ " + key + "Listtikel"+ "\n" + \
                    "╠ " + key + "Addsc「kata」|「kata」"+ "\n" + \
                    "╠ " + key + "Delsc「kata」"+ "\n" + \
                    "╠ " + key + "Listsc"+ "\n" + \
                    "╠ " + key + "Delallsc"+ "\n" + \
                    "╠ " + key + "Addtext「kata」|「kata」"+ "\n" + \
                    "╠ " + key + "Deltext「kata」"+ "\n" + \
                    "╠ " + key + "Listext"+ "\n" + \
                    "╠ " + key + "Delalltext"+ "\n" + \
                    "╠ " + key + "Addmes「kata」"+ "\n" + \
                    "╠ " + key + "Delmes「kata」"+ "\n" + \
                    "╠ " + key + "Listmes"+ "\n" + \
                    "╠ " + key + "Broadcast"+ "\n" + \
                    "╠ " + key + "Say"+ "\n" + \
                    "╠ " + key + "Spam limit"+ "\n" + \
                    "╠ " + key + "Spam via num"+ "\n" + \
                    "╠ " + key + "Spam via mid"+ "\n" + \
                    "╠ " + key + "Spam via tag"+ "\n" + \
                    "╠ " + key + "Setting limit"+ "\n" + \
                    "╚══[ ƬΣΛM HK BӨƬ ]"
    return helpSpam
def helpself():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpSelf =      "╔══[ ƬΣΛM HK BӨƬ ]" + "\n" + \
                    "╠ Gunakan 「"+ key +"」 "+ "\n" + \
                    "╠ Command Self"+ "\n" + \
                    "╠══════════════"+"\n"+\
                    "╠ " + key + "Me"+ "\n" + \
                    "╠ " + key + "Name"+ "\n" + \
                    "╠ " + key + "Mid"+ "\n" + \
                    "╠ " + key + "Bio"+ "\n" + \
                    "╠ " + key + "Pict"+ "\n" + \
                    "╠ " + key + "Cover"+ "\n" + \
                    "╠ " + key + "Video"+ "\n" + \
                    "╠ " + key + "Detail"+ "\n" + \
                    "╠ " + key + "Cpp"+ "\n" + \
                    "╠ " + key + "Cvp"+ "\n" + \
                    "╠ " + key + "Cvp2「link」"+ "\n" + \
                    "╠ " + key + "Cn:「nama」"+ "\n" + \
                    "╠ " + key + "Cb:「status」"+ "\n" + \
                    "╠ " + key + "Sname「@」"+ "\n" + \
                    "╠ " + key + "Smid「@」"+ "\n" + \
                    "╠ " + key + "Sbio「@」"+ "\n" + \
                    "╠ " + key + "Spict「@」"+ "\n" + \
                    "╠ " + key + "Scover「@」"+ "\n" + \
                    "╠ " + key + "Scontact「@」"+ "\n" + \
                    "╠ " + key + "Svideo「@」"+ "\n" + \
                    "╠ " + key + "Smusic「@」"+ "\n" + \
                    "╠ " + key + "Sdetail「@」"+ "\n" + \
                    "╠ " + key + "Friendlist"+ "\n" + \
                    "╠ " + key + "Addfriend「@」"+ "\n" + \
                    "╠ " + key + "Delfriend「@」"+ "\n" + \
                    "╠ " + key + "Friendinfo「nomor」"+ "\n" + \
                    "╠ " + key + "Chatriend|「nomor」|「kata」"+ "\n" + \
                    "╠ " + key + "Unfriend「nomor」"+ "\n" + \
                    "╠ " + key + "Clearfriend"+ "\n" + \
                    "╠ " + key + "Addblock「@」"+ "\n" + \
                    "╠ " + key + "Blocklist"+ "\n" + \
                    "╠ " + key + "Blockinfo「nomor」"+ "\n" + \
                    "╠ " + key + "Unblock「nomor」"+ "\n" + \
                    "╠ " + key + "Favoritelist"+ "\n" + \
                    "╠ " + key + "Favoritinfo「nomor」"+ "\n" + \
                    "╚══[ ƬΣΛM HK BӨƬ ]"
    return helpSelf
  
def helpgrup():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpGrup =      "╔══[ ƬΣΛM HK BӨƬ ]" + "\n" + \
                    "╠ Gunakan 「"+ key +"」 "+ "\n" + \
                    "╠ Command Group"+ "\n" + \
                    "╠══════════════"+"\n"+\
                    "╠ " + key + "Gid"+ "\n" + \
                    "╠ " + key + "Gpict"+ "\n" + \
                    "╠ " + key + "Gname"+ "\n" + \
                    "╠ " + key + "Gn:「nama」"+ "\n" + \
                    "╠ " + key + "Ginfo"+ "\n" + \
                    "╠ " + key + "Gcreator"+ "\n" + \
                    "╠ " + key + "Gcreate「nama」"+ "\n" + \
                    "╠ " + key + "Glist"+ "\n" + \
                    "╠ " + key + "Gmember"+ "\n" + \
                    "╠ " + key + "Gpending"+ "\n" + \
                    "╠ " + key + "Buka/Tutup「Qr grup」"+ "\n" + \
                    "╠ " + key + "Url"+ "\n" + \
                    "╠ " + key + "Cgp"+ "\n" + \
                    "╠ " + key + "Mention"+ "\n" + \
                    "╠ " + key + "Lurk「on/off/reset」"+ "\n" + \
                    "╠ " + key + "Lurk"+ "\n" + \
                    "╠ " + key + "Sambut「on/off」"+ "\n" + \
                    "╠ " + key + "Cam「on/off」"+ "\n" + \
                    "╠ " + key + "Bye「on/off」"+ "\n" + \
                    "╠ " + key + "Sider「on/off」"+ "\n" + \
                    "╠ " + key + "Likepost「@」"+ "\n" + \
                    "╠ " + key + "Micadd「@」"+ "\n" + \
                    "╠ " + key + "Micdel「@」"+ "\n" + \
                    "╠ " + key + "Mimic「@」"+ "\n" + \
                    "╠ " + key + "Miclist「@」"+ "\n" + \
                    "╠ " + key + "Kick「@」"+ "\n" + \
                    "╠ " + key + "Invite「@」"+ "\n" + \
                    "╠ " + key + "Pancal「@」"+ "\n" + \
                    "╠ " + key + "Cancel"+ "\n" + \
                    "╠ " + key + "Reject"+ "\n" + \
                    "╚══[ ƬΣΛM HK BӨƬ ]"
    return helpGrup
  
def helpmedia():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpMedia =     "╔══[ ƬΣΛM HK BӨƬ ]" + "\n" + \
                    "╠ Gunakan 「"+ key +"」 "+ "\n" + \
                    "╠ Command Media"+ "\n" + \
                    "╠══════════════"+"\n"+\
                    "╠ " + key + "Stickers「num」"+ "\n" + \
                    "╠ " + key + "Themas「num」"+ "\n" + \
                    "╠ " + key + "Listphotofunia"+ "\n" + \
                    "╠ " + key + "Listprimbon"+ "\n" + \
                    "╠ " + key + "Github「user」"+ "\n" + \
                    "╠ " + key + "Samehadaku「title」|「num」"+ "\n" + \
                    "╠ " + key + "Samehadakuuodate"+ "\n" + \
                    "╠ " + key + "Resep「num」|「title」"+ "\n" + \
                    "╠ " + key + "Images「title」"+ "\n" + \
                    "╠ " + key + "Listpngart"+ "\n" + \
                    "╠ " + key + "Togel"+ "\n" + \
                    "╠ " + key + "Listcctv"+ "\n" + \
                    "╠ " + key + "Lirik「abjad」|「title」"+ "\n" + \
                    "╠ " + key + "Lyric「title」"+ "\n" + \
                    "╠ " + key + "Chord「title」"+ "\n" + \
                    "╠ " + key + "Playlist「title」"+ "\n" + \
                    "╠ " + key + "Soundcloud「title」"+ "\n" + \
                    "╠ " + key + "Joxx「title」"+ "\n" + \
                    "╠ " + key + "Linkjoox「link joox」"+ "\n" + \
                    "╠ " + key + "Youtube「title」"+ "\n" + \
                    "╠ " + key + "Youtubesearch「title」"+ "\n" + \
                    "╠ " + key + "Youtubenextpage「title」"+ "\n" + \
                    "╠ " + key + "Youtubeprevtpage「title」"+ "\n" + \
                    "╠ " + key + "Youtubeplay「num」"+ "\n" + \
                    "╠ " + key + "Yt-audio「title」"+ "\n" + \
                    "╠ " + key + "Yt-video「title」"+ "\n" + \
                    "╠ " + key + "Smule「id smule」|「num」"+ "\n" + \
                    "╠ " + key + "Ismule「id smule」"+ "\n" + \
                    "╠ " + key + "Asmule「link recording」"+ "\n" + \
                    "╠ " + key + "Vsmule「link recording」"+ "\n" + \
                    "╠ " + key + "Apkpure「title」"+ "\n" + \
                    "╠ " + key + "Playstore「title」"+ "\n" + \
                    "╠ " + key + "Wallpaper「title」"+ "\n" + \
                    "╠ " + key + "Listanitoki"+ "\n" + \
                    "╠ " + key + "Anitokiupdate「num」"+ "\n" + \
                    "╠ " + key + "Jurnalotaku「title」"+ "\n" + \
                    "╠ " + key + "Albumlaguanime「abjab」"+ "\n" + \
                    "╠ " + key + "Ramalan-nama「name」"+ "\n" + \
                    "╠ " + key + "Ramalan-pengagum「name」"+ "\n" + \
                    "╠ " + key + "Ramalan-hobi「name」"+ "\n" + \
                    "╠ " + key + "Ramalan-pasangan「name」|「name」"+ "\n" + \
                    "╠ " + key + "Ramalan-bintang「zodiak」"+ "\n" + \
                    "╠ " + key + "Generatorkode"+ "\n" + \
                    "╠ " + key + "Generatorpass「num」"+ "\n" + \
                    "╠ " + key + "Generatornama「kode」|「num」"+ "\n" + \
                    "╠ " + key + "Listrate"+ "\n" + \
                    "╠ " + key + "Tv「channel」"+ "\n" + \
                    "╠ " + key + "Wiki「query」"+ "\n" + \
                    "╠ " + key + "Fs「query」|「num」"+ "\n" + \
                    "╠ " + key + "Randomfs「query」"+ "\n" + \
                    "╠ " + key + "Ahli「name」"+ "\n" + \
                    "╠ " + key + "Mirip「name」"+ "\n" + \
                    "╠ " + key + "Fotext「query」"+ "\n" + \
                    "╠ " + key + "Urban「query」"+ "\n" + \
                    "╠ " + key + "Date「dd-mm-yyyy」"+ "\n" + \
                    "╠ " + key + "Say-「kode」「num」"+ "\n" + \
                    "╠ " + key + "Tr-「kode」「num」"+ "\n" + \
                    "╠ " + key + "Cuaca「city」"+ "\n" + \
                    "╠ " + key + "Sholat「city」"+ "\n" + \
                    "╠ " + key + "Dunia21「query」"+ "\n" + \
                    "╠ " + key + "Indoxxi「query」"+ "\n" + \
                    "╠ " + key + "Allxvideos「query」"+ "\n" + \
                    "╠ " + key + "Xvideos「query」"+ "\n" + \
                    "╠ " + key + "Xxnx「query」|「num」"+ "\n" + \
                    "╠ " + key + "Avgle「query」"+ "\n" + \
                    "╠ " + key + "Linkbokep「url」"+ "\n" + \
                    "╠ " + key + "Tokopedia「query」|「num」"+ "\n" + \
                    "╠ " + key + "Bukalapak「query」|「num」"+ "\n" + \
                    "╠ " + key + "Listmajalah"+ "\n" + \
                    "╠ " + key + "Listalquran"+ "\n" + \
                    "╠ " + key + "Tafsirquran「query」"+ "\n" + \
                    "╠ " + key + "Iqra「num」「num」"+ "\n" + \
                    "╠ " + key + "Listdoapendek"+ "\n" + \
                    "╠ " + key + "Ayatkursi"+ "\n" + \
                    "╠ " + key + "Yasin"+ "\n" + \
                    "╠ " + key + "Listalkitab"+ "\n" + \
                    "╠ " + key + "Alkitab「num」「num」"+ "\n" + \
                    "╠ " + key + "Bible「query」"+ "\n" + \
                    "╠ " + key + "Bibles"+ "\n" + \
                    "╠ " + key + "Listmeme"+ "\n" + \
                    "╠ " + key + "Meme「meme」|「title」|「title」"+ "\n" + \
                    "╠ " + key + "Komik「query」"+ "\n" + \
                    "╠ " + key + "Webtoon「query」"+ "\n" + \
                    "╠ " + key + "Hentai「query」"+ "\n" + \
                    "╚══[ ƬΣΛM HK BӨƬ ]"
    return helpMedia

def helpremote():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpRemote =    "╔══[ ƬΣΛM HK BӨƬ ]" + "\n" + \
                    "╠ Gunakan 「"+ key +"」 "+ "\n" + \
                    "╠ Command Remote"+ "\n" + \
                    "╠══════════════"+"\n"+\
                    "╠ " + key + "Unsends「nomor」"+ "\n" + \
                    "╠ " + key + "Infogrup「nomor」"+ "\n" + \
                    "╠ " + key + "Infomember「nomor」"+ "\n" + \
                    "╠ " + key + "Infopending「nomor」"+ "\n" + \
                    "╠ " + key + "Opengrup「nomor」"+ "\n" + \
                    "╠ " + key + "Closegrup「nomor」"+ "\n" + \
                    "╠ " + key + "Leavegrup「nomor」"+ "\n" + \
                    "╠ " + key + "Mentiongrup「nomor」"+ "\n" + \
                    "╠ " + key + "Leavenamegrup「nomor」"+ "\n" + \
                    "╠ " + key + "Chatgrup|「nomor」|「kata」"+ "\n" + \
                    "╠ " + key + "Chatowner「kata」"+ "\n" + \
                    "╠ " + key + "Chatidline「idline」|「kata」"+ "\n" + \
                    "╚══[ ƬΣΛM HK BӨƬ ]"
    return helpRemote

def helpsett():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpSett =      "╔══[ ƬΣΛM HK BӨƬ ]" + "\n" + \
                    "╠ Gunakan 「"+ key +"」 "+ "\n" + \
                    "╠ Command Setting"+ "\n" + \
                    "╠══════════════"+"\n"+\
                    "╠ " + key + "Tikelspam"+ "\n" + \
                    "╠ " + key + "Tikelsider"+ "\n" + \
                    "╠ " + key + "Tikeltag"+ "\n" + \
                    "╠ " + key + "Tikelbc"+ "\n" + \
                    "╠ " + key + "Cektikelspam"+ "\n" + \
                    "╠ " + key + "Cektikelsider"+ "\n" + \
                    "╠ " + key + "Cektikeltag"+ "\n" + \
                    "╠ " + key + "Cektikelbc"+ "\n" + \
                    "╠ " + key + "Fotospam"+ "\n" + \
                    "╠ " + key + "Fotobc"+ "\n" + \
                    "╠ " + key + "Cekfotospam"+ "\n" + \
                    "╠ " + key + "Cekfotobc"+ "\n" + \
                    "╠ " + key + "Setmidbc"+ "\n" + \
                    "╠ " + key + "Setnamagrupspam"+ "\n" + \
                    "╠ " + key + "Setrestag"+ "\n" + \
                    "╠ " + key + "Setresfo"+ "\n" + \
                    "╠ " + key + "Setrestik"+ "\n" + \
                    "╠ " + key + "Setchatspam"+ "\n" + \
                    "╠ " + key + "Setsider"+ "\n" + \
                    "╠ " + key + "Setlike"+ "\n" + \
                    "╠ " + key + "Cekrespon"+ "\n" + \
                    "╚══[ ƬΣΛM HK BӨƬ ]"
    return helpSett

def helpmeme():
    helpMeme =      "╔═══[ List Name ]═══" + "\n" + \
                    "╠ 1.tenguy" + "\n" + \
                    "╠ 2.afraid" + "\n" + \
                    "╠ 3.older" + "\n" + \
                    "╠ 4.aag" + "\n" + \
                    "╠ 5.tried" + "\n" + \
                    "╠ 6.biw" + "\n" + \
                    "╠ 7.stew" + "\n" + \
                    "╠ 8.blb" + "\n" + \
                    "╠ 9.kermit" + "\n" + \
                    "╠ 10.bd" + "\n" + \
                    "╠ 11.ch" + "\n" + \
                    "╠ 12.cbg" + "\n" + \
                    "╠ 13.wonka" + "\n" + \
                    "╠ 14.cb" + "\n" + \
                    "╠ 15.keanu" + "\n" + \
                    "╠ 16.dsm" + "\n" + \
                    "╠ 17.live" + "\n" + \
                    "╠ 18.ants" + "\n" + \
                    "╠ 19.doge" + "\n" + \
                    "╠ 20.drake" + "\n" + \
                    "╠ 21.ermg" + "\n" + \
                    "╠ 22.facepalm" + "\n" + \
                    "╠ 23.firsttry" + "\n" + \
                    "╠ 24.fwp" + "\n" + \
                    "╠ 25.fa" + "\n" + \
                    "╠ 26.fbf" + "\n" + \
                    "╠ 27.fmr" + "\n" + \
                    "╠ 28.fry" + "\n" + \
                    "╠ 29.ggg" + "\n" + \
                    "╠ 30.hipster" + "\n" + \
                    "╠ 31.icanhas" + "\n" + \
                    "╠ 32.crazypills" + "\n" + \
                    "╠ 33.mw" + "\n" + \
                    "╠ 34.noidea" + "\n" + \
                    "╠ 35.regret" + "\n" + \
                    "╠ 36.boat" + "\n" + \
                    "╠ 37.hagrid" + "\n" + \
                    "╠ 38.sohappy" + "\n" + \
                    "╠ 39.captain" + "\n" + \
                    "╠ 40.bender" + "\n" + \
                    "╠ 41.inigo" + "\n" + \
                    "╠ 42.iw iw" + "\n" + \
                    "╠ 43.ackbar" + "\n" + \
                    "╠ 44.happening" + "\n" + \
                    "╠ 45.joker joker" + "\n" + \
                    "╠ 46.ive" + "\n" + \
                    "╠ 47.ll" + "\n" + \
                    "╠ 48.away" + "\n" + \
                    "╠ 49.mb" + "\n" + \
                    "╠ 50.badchoice" + "\n" + \
                    "╠ 51.mmm" + "\n" + \
                    "╠ 52.jetpack" + "\n" + \
                    "╠ 53.imsorry" + "\n" + \
                    "╠ 54.red" + "\n" + \
                    "╠ 55.mordor" + "\n" + \
                    "╠ 56.oprah" + "\n" + \
                    "╠ 57.oag" + "\n" + \
                    "╠ 58.remembers" + "\n" + \
                    "╠ 59.philosoraptor" + "\n" + \
                    "╠ 60.jw" + "\n" + \
                    "╠ 61.patrick" + "\n" + \
                    "╠ 62.rollsafe" + "\n" + \
                    "╠ 63.sad-obama" + "\n" + \
                    "╠ 64.sad-clinton" + "\n" + \
                    "╠ 65.sadfrog" + "\n" + \
                    "╠ 66.sad-bush" + "\n" + \
                    "╠ 67.sad-biden" + "\n" + \
                    "╠ 68.sad-boehner" + "\n" + \
                    "╠ 69.saltbae" + "\n" + \
                    "╠ 70.sarcasticbear" + "\n" + \
                    "╠ 71.dwight" + "\n" + \
                    "╠ 72.sb"  "\n" + \
                    "╠ 73.ss" + "\n" + \
                    "╠ 74.sf" + "\n" + \
                    "╠ 75.dodgson" + "\n" + \
                    "╠ 76.money" + "\n" + \
                    "╠ 77.snek" + "\n" + \
                    "╠ 78.sk" + "\n" + \
                    "╠ 79.sohot" + "\n" + \
                    "╠ 80.nice" + "\n" + \
                    "╠ 81.awesome-awkward" + "\n" + \
                    "╠ 82.awesome" + "\n" + \
                    "╠ 83.awkward-awesome" + "\n" + \
                    "╠ 84.awkward" + "\n" + \
                    "╠ 85.fetch" + "\n" + \
                    "╠ 86.success" + "\n" + \
                    "╠ 87.scc" + "\n" + \
                    "╠ 88.ski" + "\n" + \
                    "╠ 89.officespace" + "\n" + \
                    "╠ 90.interesting" + "\n" + \
                    "╠ 91.toohigh" + "\n" + \
                    "╠ 92.bs" + "\n" + \
                    "╠ 93.fine" + "\n" + \
                    "╠ 94.sparta" + "\0n" + \
                    "╠ 95.whatyear" + "\n" + \
                    "╠ 96.center" + "\n" + \
                    "╠ 97.both" + "\n" + \
                    "╠ 98.winter" + "\n" + \
                    "╠ 99.xy" + "\n" + \
                    "╠ 100.buzz" + "\n" + \
                    "╠ 101.yodawg" + "\n" + \
                    "╠ 102.yuno" + "\n" + \
                    "╠ 103.yallgot" + "\n" + \
                    "╠ 104.bad" + "\n" + \
                    "╠ 105.elf" + "\n" + \
                    "╠ 106.chosen" + "\n" + \
                    "╠══════════════════╗" + "\n" + \
                    "╠ Meme away| kata1 | kata2" + "\n" + \
                    "╚═══════════════════"
    return helpMeme
  
majalahlist ="""# SPECIAL MAJALAH
#
# kompas | num
# terpopuler | num
# gaya hidup  | num
# barat | num
# asia | num
# wisata-kuliner | num
# extra | num
# photo | num
# menu makanan | num
# videos | num
# zodiak | num
# lagu lirik | num
# lifestyle | num
# berita | num
# komunitas | num
# tip trik | num
# galeri | num
# snapshot | num

Cara menggunakan
Manu makanan
Manu makanan|1"""
nilaitukaruang ="""# arab = SAR
# brunai dolar = BND
# china yuan = CNY
# dinar irak = IQD
# dirham uni emirat arab = AED
# dolar amerika serikat = USD
# dolar australi = AUD
# dolar hongkong = HKD
# dolar singapur = SGD 
# dolar taiwan baru = TWD
# euro = EUR
# peso philipina = PHP
# pound streling = GBP
# ringgit malaysia = MYR
# rupe india = INR
# rupiah indonesia = IDR
# thai bath = THB
# vietnam dong = VND
# won korea = KRW
# yen jepang = JPY

Cara menggunakan
Rate IDR USD 100000"""
pngart="""# accessories
# alphabets-letters
# animals
# appliances
# internet/web-elements/arrows
# art
# automobiles
# beauty
# business
# car
# cartoons
# celebrity
# clothing
# education
# electronics
# fantasy
# fashion-lifestyle
# fictional-characters
# flowers
# food
# furniture
# gaming
# holidays-events
# internet
# love
# medical
# movies
# electronics/musical-instruments
# nature
# objects
# people
# quotes
# religion
# sports
# symbols
# internet/web-elements

Cara menggunakan
Pngart love|1"""

photofunia='''「 List Photofunia 」

1. beach_sign「text」
2. neon_sign「text」
3. neon_writing「text1」|「text2」
4 .brussels_museum「@」
5. two_valentines「@」|「text1」|「@」|「text2」
6. valentine「@」|「text1」
7. watercolour_splash「@」
8. wanted「@」|「text1」|「text2」|「text3」
9. black_white_gallery「@」「@」「@」「@」「@」
10. three_paintings「@」「@」「@」
11. drawing「@」
12. brooches「@」「@」 
13. love_letter「@」
14. flowers「@」|「text」
15. golden_valentine「@
16. missing_person「@」|「text1」|「text2」|「text3」
17. night_motion「@」''' 

primbon='''「 List Primbon 」
1. primbonnama「nama1」
2. primbonweton 「tanggal」
3. primbonpasangan「nama1」|「nama2」
4. primbonjodoh「nama1」|「tanggal1」|「nama2」|「tanggal2」
5. primbonsuami_istri「nama1」|「tanggal1」|「nama2」|「tanggal2」'''  
  

listalkitab="""「 List kitab 」

1.  Kejadian
2.  Keluaran 
3.  Imamat 
4.  Bilangan
5.  Ulangan
6.  Yosua 
7.  Hakim-hakim
8.  Rut
9.  1 Samuel
10.  2 Samuel
11.  1 Raja-raja 
12.  2 Raja-raja
13.  1 Tawarikh 
14.  2 Tawarikh
15.  Ezra
16.  Nehemia
17.  Ester 
18.  Ayub
19.  Mazmur
20.  Amsal 
21.  Pengkhotbah
22.  Kidung Agung
23.  Yesaya 
24.  Yeremia 
25.  Ratapan 
26.  Yehezkiel
27.  Daniel 
28.  Hosea 
29.  Yoel 
30.  Amos 
31.  Obaja 
32.  Yunus 
33.  Mikha 
34.  Nahum 
35.  Habakuk 
36.  Zefanya 
37.  Hagai 
38.  Zakharia 
39.  Maleakhi 
40.  Matius 
41.  Markus
42.  Lukas
43.  Yohanes
44.  Kisah Rasul-rasul
45.  Roma
46.  1 Korintus 
47.  2 Korintus
48.  Galatia
49.  Efesus 
50.  Filipi
51.  Kolose
52.  1 Tesalonika 
53.  2 Tesalonika
54.  1 Timotius
55.  2 Timotius
56.  Titus
57.  Filemon 
58.  Ibrani
59.  Yakobus
60.  1 Petrus
61.  2 Petrus
62.  1 Yohanes
63.  2 Yohanes
64.  3 Yohanes
65.  Yudas 
66.  Wahyu"""
listdoapendek=""" 01 muqaddimah
 02 doa bangun tidur
 03 doa masuk kamar mandi
 04 doa keluar kamar mandi
 05 doa setelah wudhu
 06 doa keluar rumah
 07 doa masuk rumah
 08 doa pergi ke masjid
 09 doa masuk masjid
 10 doa keluar masjid
 11 doa ketika mendengarkan adzan
 12 doa istiftah
 13 doa istiftah ketika shalat qiyamu
 14 doa ruku
 15 doa bangun dari ruku'
 16 doa sujud
 17 doa sujud ketika shalat qiyamul l
 18 doa sujud tilawah
 19 doa duduk di antara dua sujud
 20 doa tasyahud
 21 doa setelah tasyahud akhir sebelu
 22 dzikir setelah shalat
 23 doa shalat istikharah
 24 dzikir pagi dan petang
 25 doa ketika di malam hari
 26 doa sebelum tidur
 27 doa apabila merasa takut dan kese
 28 doa qunut witir
 29 doa setelah shalat witir
 30 doa perlindungan kepada anak
 31 doa penawar hati yang duka
 32 doa orang yang mengalami kesulita
 33 doa untuk kesedihan yang mendalam
 34 doa apabila ada orang meninggal d
 35 mengajari orang yang akan meningg
 36 doa memejamkan mayat dan takziyah
 37 doa dalam shalat jenazah
 38 doa untuk mayat anak kecil
 39 doa untuk belasungkawa
 40 doa ketika memasukkan mayat ke li
 41 doa setelah mayat dimakamkan
 42 doa ziarah kubur
 43 doa apabila ada angin ribut
 44 doa ketika ada halilintar
 45 doa untuk minta hujan
 46 doa apabila hujan turun
 47 doa melihat bulan tanggal satu
 48 doa berbuka puasa
 50 doa sebelum makan
 51 doa apabila lupa berdoa sebelum m
 52 doa setelah makan
 53 doa tamu kepada orang yang member
 54 doa apabila melihat permulaan bua
 55 doa pengantin kepada dirinya
 56 doa kepada pengantin
 57 doa ketika bersin dan jawabannya
 58 doa pelebur dosa majelis
 59 tuntunan dan doa ketika marah
 60 bacaan apabila mencintai orang ka
 61 doa naik kendaraan dan bepergian
 63 doa masuk pasar
 64 doa agar bisa melunasi utang
 65 doa musafir kepada orang yang dit
 66 doa orang mukim kepada musafir
 67 doa musafir ketika kembali
 68 doa apabila ada sesuatu yang meny
 69 doa apabila ada sesuatu yang tida
 70 doa talbiyah
 71 doa antara rukun yamani dan hajar
 72 doa ketika di atas bukit shafa da
 73 doa pada hari arafah
 74 doa ketika di masy_aril haram"""
def clientBot(op):
    try:
        if op.type == 2:
          group=detectprofile["id"]
          #print(group)
          if group in detectprofile["detectprofile"]:
            a2=client.getGroup(group)
            tp=[m.mid for m in a2.members]
            for i in tp:
              if op.param1 in i:
                a1=client.getContact(op.param1)
                ma=a1.mid
                nama=a1.displayName
                ca = client.getProfileCoverURL(op.param1)
                for data in detectprofile2[group]:
                  if ma in data:
                    if str(ca) not in data[ma]["cover"]:
                        after=ca
                        befro=data[ma]["cover"]
                        detectcv(group,nama,befro,after)
                        data[ma]["cover"] = ca
        if op.type == 2:
          group=detectprofile["id"]
          if group in detectprofile["detectprofile"]:
#          if group in detectprofile["detectprofile"]:
            a2=client.getGroup(group)
            tp=[m.mid for m in a2.members]
            for i in tp:
              if op.param1 in i:
                a1=client.getContact(op.param1)
                ma=a1.mid
                nama=a1.displayName
                pa="https://obs.line-scdn.net/"+str(a1.pictureStatus)
                for data in detectprofile2[group]:
                  if ma in data:
                    if str(pa) not in data[ma]["foto"]:
                        after=pa
                        befro=data[ma]["foto"]
                        detectpp(group,nama,befro,after)
                        data[ma]["foto"] = pa
        if op.type == 2:
          group=detectprofile["id"]
          if group in detectprofile["detectprofile"]:
#          if group in detectprofile["detectprofile"]:
            a2=client.getGroup(group)
            tp=[m.mid for m in a2.members]
            for i in tp:
              if op.param1 in i:
                a1=client.getContact(op.param1)
                ma=a1.mid
                na=a1.displayName
                for data in detectprofile2[group]:
                  if ma in data:
                    if str(na) not in data[ma]["name"]:
                        after=na
                        befro=data[ma]["name"]
                        ret="Before name: "+befro+"\nAfter name: "+after
                        sendMention(group,"Cie kak @!    ganti nama\n\n"+ret,[ma])
                        data[ma]["name"] = na
        if op.type == 2:
          group=detectprofile["id"]
          if group in detectprofile["detectprofile"]:
#          if group in detectprofile["detectprofile"]:
            a2=client.getGroup(group)
            tp=[m.mid for m in a2.members]
            for i in tp:
              if op.param1 in i:
                a1=client.getContact(op.param1)
                ma=a1.mid
                ba=a1.statusMessage
                for data in detectprofile2[group]:
                  if ma in data:
                    if str(ba) not in data[ma]["bio"]:
                        after=ba
                        befro=data[ma]["bio"]
                        ret="Before bio: "+befro+"\nAfter bio: "+after
                        sendMention(group,"Cie kak @!    ganti bio\n\n"+ret,[ma])
                        data[ma]["bio"] = ba
                
        if op.type == 5:
            if settings["autoAdd"] == True:
                G = client.getContact(op.param1)
                client.findAndAddContactsByMid(G.mid) 
                client.sendMessage(op.param1, "Hai {} Thanks for add me\nƬΣΛM HK BӨƬ\nOpen Order Sewa Bot\n\nSelfbot\nSelfbot + Assist\nSelfbot + Assist + Gost\nSelfbot + Assist + Gost + Antijs\nBot Protect".format(str(client.getContact(op.param1).displayName)))

            if settings["autoBlock"] == True:
                G = client.getContact(op.param1)
                client.blockContact(G.mid)
                #client.sendMessage(op.param1, "Hai {} Thanks for add me\nƬΣΛM HK BӨƬ\nOpen Order Sewa Bot\n\nSelfbot\nSelfbot + Assist\nSelfbot + Assist + Gost\nSelfbot + Assist + Gost + Antijs\nBot Protect".format(str(client.getContact(op.param1).displayName)))
                client.sendMessage(op.param1, "Halo {} anda tidak saya kenal\nJadi maaf anda saya blokir".format(str(client.getContact(op.param1).displayName)))
                
        if op.type == 13:
            if mid in op.param3:
                if settings["autoLeave"] == True:
                        client.acceptGroupInvitation(op.param1)
                        ginfo = client.getGroup(op.param1)
                        client.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        client.leaveGroup(op.param1)

            if mid in op.param3:
                if settings["autoJoin"] == True:
                        client.acceptGroupInvitation(op.param1)
                        ginfo = client.getGroup(op.param1)
                        client.sendMessage(op.param1,"Assalamualaikum\n Group " +str(ginfo.name))
                        
        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    return                
                ginfo = client.getGroup(op.param1)
                contact = client.getContact(op.param2)
                image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
                welcomeMembers(op.param1, [op.param2])
                client.sendImageWithURL(op.param1, image)

        if op.type == 15:
            if op.param1 in leave:
                if op.param2 in Bots:
                    return
                ginfo = client.getGroup(op.param1)
                contact = client.getContact(op.param2)
                image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
                leaveMembers(op.param1, [op.param2])
                client.sendImageWithURL(op.param1, image)
                
#=======================================================================================================
        if op.type == 25 or op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                return     
            if msg.contentType == 16:
                if settings["checkPost"] == True:
                    if 'text' not in msg.contentMetadata:
                        if 'mediaOid' in msg.contentMetadata:
                            Object = msg.contentMetadata['mediaOid'].replace("svc=myhome|sid=h|","")
                            if msg.contentMetadata['mediaType'] == 'V':
                                if msg.contentMetadata['serviceType'] == 'GB':
                                    client.sendMessage(msg.to,"━━━━「Detect Post」━━━━\n\n[Nama]: " +client.getContact(msg._from).displayName + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&oid=" + msg.contentMetadata['mediaOid'] + "\n[MediaURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
                                else:
                                    client.sendMessage(msg.to, "━━━━「Detect Post」━━━━\n\n[Nama]: "+client.getContact(msg._from).displayName + "\n[Postnya] : " + msg.contentMetadata['serviceName'] + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&" + Object + "\n[MediaURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
                            else:
                                if msg.contentMetadata['serviceType'] == 'GB':
                                    client.sendMessage(msg.to, "━━━━「Detect Post」━━━━\n\n[Nama]: "+client.getContact(msg._from).displayName + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obsi-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
                                else:
                                    client.sendMessage(msg.to,"━━━━「Detect Post」━━━━\n\n[Nama]: " +client.getContact(msg._from).displayName + "\n[Postnya] : " + msg.contentMetadata['serviceName'] + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
                        elif 'stickerId' in msg.contentMetadata:
                            if msg.contentMetadata['serviceType'] == 'GB':
                                client.sendMessage(msg.to,"━━━━「Detect Post」━━━━\n\n[Nama]: " +client.getContact(msg._from).displayName + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
                            else:
                                client.sendMessage(msg.to,"━━━━「Detect Post」━━━━\n\n[Nama]: " +client.getContact(msg._from).displayName + "\n[Postnya] : " + msg.contentMetadata['serviceName'] + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
                        else:
                            if msg.contentMetadata['serviceType'] == 'GB':
                                client.sendMessage(msg.to,"━━━━「Detect Post」━━━━\n\n[Nama]: " +client.getContact(msg._from).displayName + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'])
                            else:
                                client.sendMessage(msg.to,"━━━━「Detect Post」━━━━\n\n[Nama]: " +client.getContact(msg._from).displayName + "\n[Postnya] : " + msg.contentMetadata['serviceName'] + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'])
                    else:
                        if 'mediaOid' in msg.contentMetadata:
                            Object = msg.contentMetadata['mediaOid'].replace("svc=myhome|sid=h|","")
                            if msg.contentMetadata['mediaType'] == 'V':
                               if msg.contentMetadata['serviceType'] == 'GB':
                                    client.sendMessage(msg.to,"━━━━「Detect Post」━━━━\n\n[Nama]: " +client.getContact(msg._from).displayName + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n\n[text]\n" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&oid=" + msg.contentMetadata['mediaOid'] + "\n[MediaURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
                               else:
                                    client.sendMessage(msg.to,"━━━━「Detect Post」━━━━\n\n[Nama]: " +client.getContact(msg._from).displayName + "\n[Postnya] : " + msg.contentMetadata['serviceName'] + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n\n[text]\n" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&" + Object + "\n[MediaURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
                            else:
                                if msg.contentMetadata['serviceType'] == 'GB':
                                    client.sendMessage(msg.to, "━━━━「Detect Post」━━━━\n\n[Nama]: "+client.getContact(msg._from).displayName + "\n[postURL]\n" + msg.contentMetadata['postEndUrl']+ "\n\n[text]\n" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
                                else:
                                    client.sendMessage(msg.to,"━━━━「Detect Post」━━━━\n\n[Nama]: " +client.getContact(msg._from).displayName + "\n[Postnya] : " + msg.contentMetadata['serviceName'] + "\n[postURL]\n" + msg.contentMetadata['postEndUrl']+ "\n\n[text]\n" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
                        elif 'stickerId' in msg.contentMetadata:
                            if msg.contentMetadata['serviceType'] == 'GB':
                                client.sendMessage(msg.to,"━━━━「Detect Post」━━━━\n\n[Nama]: " +client.getContact(msg._from).displayName + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n\n[text]\n" + msg.contentMetadata['text'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
                            else:
                                client.sendMessage(msg.to, "━━━━「Detect Post」━━━━\n\n[Nama]: " +client.getContact(msg._from).displayName + "\n[Postnya] : " + msg.contentMetadata['serviceName'] + "\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n\n[text]\n" + msg.contentMetadata['text'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
                        else:
                            if msg.contentMetadata['serviceType'] == 'GB':
                                client.sendMessage(msg.to, client.getContact(msg._from).displayName + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[text]\n" + msg.contentMetadata['text'])
                            else:
                                client.sendMessage(msg.to, "━━━━「Detect Post」━━━━\n\n[Nama]l: " +client.getContact(msg._from).displayName + "\n[Postnya] : " + msg.contentMetadata['serviceName'] + "\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n\n[text]\n" + msg.contentMetadata['text'])
        if op.type == 65:
            if settings["cekUnsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ryan = client.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Waktu kirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict2[msg_id]["text"]))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                client.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                client.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ryan = client.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Pesan Dihapus 」\n• Pengirim : "
                                ret_ = "• Waktu kirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                client.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                client.sendContact(at, msg_dict1[msg_id]["text"])
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if settings["cekUnsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ryan = client.getContact(msg_dict1[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Sticker Dihapus 」\n• Pengirim : "
                                ret_ = "Waktu kirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict1[msg_id]["text"]))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                client.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                client.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if settings["cekUnsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict2:
                        if msg_dict2[msg_id]["from"]:
                                ryan = client.getContact(msg_dict2[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Video Dihapus 」\n• Pengirim : "
                                ret_ = "Waktu kirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict2[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict2[msg_id]["text"]))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                client.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                client.sendVideo(at, msg_dict2[msg_id]["data"])
                        del msg_dict2[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if settings["cekUnsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict3:
                        if msg_dict3[msg_id]["from"]:
                                ryan = client.getContact(msg_dict3[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Audio Dihapus 」\n• Pengirim : "
                                ret_ = "\n• Waktu kirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict3[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict3[msg_id]["text"]))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                client.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                client.sendAudio(at, msg_dict3[msg_id]["data"])
                        del msg_dict3[msg_id]
                except Exception as e:
                    print(e)
        if op.type == 25 or op.type == 26:
          if settings["cekUnsend"] == True:
            try:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 2:
                #if msg.toType == 2:
                    if msg.toType == 0:
                         to = msg._from
                    elif msg.toType == 2:
                         to = msg.to
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                    if msg.contentType == 1:
                        path = client.downloadObjectMsg(msg_id)
                        msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
                    if msg.contentType == 2:
                        path = client.downloadObjectMsg(msg_id)
                        msg_dict2[msg.id] = {"text":'Videonya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
                    if msg.contentType == 3:
                        path = client.downloadObjectMsg(msg_id)
                        msg_dict3[msg.id] = {"text":'Audionya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
                    if msg.contentType == 7:
                        stk_id = msg.contentMetadata["STKID"]
                        stk_ver = msg.contentMetadata["STKVER"]
                        pkg_id = msg.contentMetadata["STKPKGID"]
                        ret_ = "\n\n「 Sticker Info 」"
                        ret_ += "\n• Sticker ID : {}".format(stk_id)
                        ret_ += "\n• Sticker Version : {}".format(stk_ver)
                        ret_ += "\n• Sticker Package : {}".format(pkg_id)
                        ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                        query = int(stk_id)
                        if type(query) == int:
                                data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                                path = client.downloadFileURL(data)
                                msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                        #client.sendMessage(msg.to,"Sukses like")
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            setKey = settings["keyCommand"].title()
            if msg.toType == 0 or msg.toType == 2:
#                if msg.contentType == 7:
 #                 if 'MENTION' in msg.contentMetadata:
  #                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
   #                   mentionees = mention['MENTIONEES']
    #                  for mention in mentionees:
     #                   if mention ['M'] in clientMid:
      #                    ret="Detect fakemention sticker"
       #                   ret+="\nTersangka @!"
        #                  sendMention(msg.to,ret,[sender])
          
#                if msg.contentType == 7:
 #                 if 'MENTION' in msg.contentMetadata:
  #                    a=client.getContact(sender).displayName
   #                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
    #                  mentionees = mention['MENTIONEES']
     #                 for mention in mentionees:
      #                  if mention ['M'] in clientMid:
       #                   ret="Detect fakemention sticker"
        #                  ret+="\nTersangka {}".format(a)
         #                 client.sendReplyMessage(msg.id,msg.to,ret)
                        
                if msg.contentType == 13:
                        mids = msg.contentMetadata["mid"]
                        con=client.getContact(mids)
                        conmid=con.mid
                        msg_dict1[msg.id] = {"text":str(conmid),"from":msg._from,"createdTime":msg.createdTime}
                if msg.contentType == 4:
                    if simple["detectflex"] == True:
                        data = {
                            "type": "text",
                            "text": "IYA TAU , ITU TEMPLATE 🤔",
                        }
                        client.postTemplate(msg.to, data)
                if msg.contentType == 22:
                    if simple["detectflex"] == True:
                        data = {
                            "type": "text",
                            "text": "IYA TAU , ITU FLEX 🤔",
                        }
                        client.postTemplate(msg.to, data)
                        
                if msg.contentType == 22:
                    if simple["cloneflex"] == True:
                        fnama = msg.contentMetadata["FLEX_JSON"]
                        igs = json.loads(fnama)
                        client.postFlex(msg.to, igs)
                        #data1="""{}""".format(fnama)
                        #client.postFlex(to, data1)
                        #'Print("cd75260e2c5a348838e7ed9f341513713",data1)
                        
                if msg.contentType == 16:
                    if settings["likeOn"] == True:
                        url = msg.contentMetadata["postEndUrl"]
                        b=url.split("=")
                        h=b[1][:33]
                        p=b[2]                        
                        client.likePost(h,p, likeType = 1003)
                        client.createComment(h, p, settings["comment"])
                        client.sendMessage(msg.to,"sukses like and comment")
        if op.type == 25:
            try:
                #print ("[ 25 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.getProfile().mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 2:
                       if msg._from in simple["ChangeVideoProfilevid"]:
                            simple["ChangeVideoProfilePicture"][msg._from] = True
                            del simple["ChangeVideoProfilevid"][msg._from]
                            clientn.downloadObjectMsg(msg_id,'path','video.mp4')
                            client.sendMessage(msg.to,"Send gambarnya...")
                            
                    if msg.contentType == 1:
                       if msg._from in simple["ChangeVideoProfilePicture"]:
                            del simple["ChangeVideoProfilePicture"][msg._from]
                            client.downloadObjectMsg(msg_id,'path','image.jpg')
                            changeVideoAndPictureProfile2('video.mp4','image.jpg')
                            client.sendMessage(msg.to,"Change Video Profile Success!!!") 
                          
                    if msg.contentType == 2:
                       if msg._from in simple["convertAudio"]:
                            simple["convertAudio"][msg._from] = True
                            del simple["convertAudio"][msg._from]
                            audi = client.downloadObjectMsg(msg_id, saveAs="tmp/hayden.mp3")
                            client.sendMessage(msg.to,"Sedang diconvert ke audio!!!")
                            client.sendAudio(msg.to, audi)
                            client.deleteFile(audi)
                            
                    if msg.contentType == 2:
                       if msg._from in simple["convertVideoFile"]:
                            simple["convertVideoFile"][msg._from] = True
                            del simple["convertVideoFile"][msg._from]
                            audi = client.downloadObjectMsg(msg_id, saveAs="tmp/hayden.mp4")
                            client.sendMessage(msg.to,"Sedang diconvert ke File!!!")
                            client.sendFile(to, audi, file_name='{}.mp4'.format(time.time()))
                            client.deleteFile(audi)
                            
                    if msg.contentType == 3:
                       if msg._from in simple["convertVideo"]:
                            simple["convertVideo"][msg._from] = True
                            del simple["convertVideo"][msg._from]
                            audi = client.downloadObjectMsg(msg_id, saveAs="tmp/hayden.mp4")
                            client.sendMessage(msg.to,"Sedang diconvert ke video!!!")
                            client.sendVideo(msg.to, audi)
                            client.deleteFile(audi)
                            
                    if msg.contentType == 3:
                       if msg._from in simple["convertAudioFile"]:
                            simple["convertAudioFile"][msg._from] = True
                            del simple["convertAudioFile"][msg._from]
                            audi = client.downloadObjectMsg(msg_id, saveAs="tmp/hayden.mp3")
                            client.sendMessage(msg.to,"Sedang diconvert ke File!!!")
                            client.sendFile(to, audi, file_name='{}.mp3'.format(time.time()))
                            client.deleteFile(audi)
                            
                    if msg.contentType == 14:
                       if msg._from in simple["convertFileVideo"]:
                            simple["convertFileVideo"][msg._from] = True
                            del simple["convertFileVideo"][msg._from]
                            audi = client.downloadObjectMsg(msg_id, saveAs="tmp/hayden.mp4")
                            client.sendMessage(msg.to,"Sedang diconvert ke video!!!")
                            client.sendVideo(msg.to, audi)
                            client.deleteFile(audi)
                            
                    if msg.contentType == 14:
                       if msg._from in simple["convertFileAudio"]:
                            simple["convertFileAudio"][msg._from] = True
                            del simple["convertFileAudio"][msg._from]
                            audi = client.downloadObjectMsg(msg_id, saveAs="tmp/hayden.mp3")
                            client.sendMessage(msg.to,"Sedang diconvert ke audio!!!")
                            client.sendAudio(to, audi)
                            client.deleteFile(audi)
                          
                          
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                          
        if op.type == 26 or op.type == 25:
          to = msg.to
          if to in settings["sniff"]:
            try:
                #print(msg.contentMetadata)
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                        if msg.contentMetadata in ({},{'EMTVER': '4'}):
                            pass
                        else:
                            client.sendMessage("ua92924bed83ff151fdba75a24ac9b437", str(msg.contentMetadata))
            except Exception as error:
                logError(error)
                
        if op.type == 26:
              msg = op.message
              text = msg.text
              msg_id = msg.id
              receiver = msg.to
#        if op.type == 25 or op.type == 26:
 #           try:
  #              print ("[ 25 ] SEND MESSAGE")
   #             msg = op.message
    #            text = msg.text
     #           msg_id = msg.id
      #          receiver = msg.to
       #         sender = msg._from
        #        setKey = settings["keyCommand"].title()
         #       if settings["setKey"] == False:
          #          setKey = ''
           #     if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
            #        if msg.toType == 0:
             #           if sender != client.getProfile().mid:
              #              to = sender
               #         else:
                #            to = receiver
                 #   elif msg.toType == 1:
                  #      to = receiver
                   # elif msg.toType == 2:
                    #    to = receiver
                    #if msg.contentType == 0:
                     #  if text is None:
                      #      return
                       #else:
#                            cmd = command(text)
 #                           if receiver in temp_flood:
  #                              if temp_flood[receiver]["expire"] == True:
   #                                if cmd == "the bot is back active":
    #                                    temp_flood[receiver]["expire"] = False
     #                                   temp_flood[receiver]["time"] = time.time()
                                        #client.sendMessage(to,"Bot Actived")
      #                             return
       #                         elif time.time() - temp_flood[receiver]["time"] <= 5:
        #                            temp_flood[receiver]["flood"] += 1
         #                           if temp_flood[receiver]["flood"] >= 10:
          #                              temp_flood[receiver]["flood"] = 0
           #                             temp_flood[receiver]["expire"] = True
            #                            ret_ = "I will be off for 15 seconds, type open to re-enable"
             #                           client.sendMessage(to, "Flood Detect !\n"+str(ret_))
              #                          time.sleep(15)
               #                         client.sendMessage(to, "The bot is back active")
                #                else:
                 #                    temp_flood[receiver]["flood"] = 0
                  #              temp_flood[receiver]["time"] = time.time()
                   #         else:
                    #            temp_flood[receiver] = {
    	               #             "time": time.time(),
    	                #            "flood": 0,
    	                 #           "expire": False
                        #        }

#            except Exception as error:
 #               logError(error)
  #              traceback.print_tb(error.__traceback__)

        if op.type == 25 or op.type == 26:
            try:
                #print ("[ 25 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.getProfile().mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 6:# and to not in muted["botMute"]:
                        if settings["responGc"] == True:# and sender != clientMID:
                            contact = client.getContact(sender)
                            if msg.toType == 0:
                                if msg.contentMetadata["GC_EVT_TYPE"] == "I":
                                    sendMention(sender, "Kak @! Jangan spam panggilan donk", [sender])
                                    #arg = "   Info : Invited Group Call"
                            if msg.toType == 2:# and to not in muted["botMute"]:
                                group = client.getGroup(to)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                b=datetime.strftime(timeNow,'%H:%M:%S')
                                callgrup=time.time()
                                timegrup=time.time() - callgrup
                                if msg.contentMetadata["GC_EVT_TYPE"] == "S":
                                    arg = "Group Call Begins"
                                    #arg += "\n   Group Name : {}".format(str(group.name))
                                    arg += "\nCalling : @!"#.format(str(contact.displayName))
                                    arg += "\nType Call : {}".format(str(msg.contentMetadata["GC_MEDIA_TYPE"]))
                                    arg += "\nTime Calling : {}".format(b)
                                    sendMention(to,arg, [sender])
                                elif msg.contentMetadata["GC_EVT_TYPE"] == "E":
                                    arg = "Group Call Ends"
                                    arg += "\nExecutor @!"
                                    arg += "\nCalling Ends : {}".format(b)
                                    arg += "\nDuration : {}".format(format_timespan(int(msg.contentMetadata["DURATION"])//1000))#.replace(" hours,",":").replace(" minutes and "," menit").replace(" seconds"," detik"))
                                    sendMention(to,arg, [sender])
                    if msg.contentType == 0:
                      if msg.toType != 0 and msg.toType == 2:
                            contact = client.getContact(sender)
                            smid = contact.mid
                            if to not in skick['ROM']:
                               skick['ROM'][to] = {}
                            if sender not in skick['ROM'][to]:
                               skick['ROM'][to][sender] = {}
                            if msg.id not in skick['ROM'][to][sender]:
                               skick['ROM'][to][sender][msg.id] = []
                            skick['ROM'][to][sender][msg.id].append(smid)
                    if msg.contentType == 7:
                        if 'STKOPT' in msg.contentMetadata:
                          stk_id = msg.contentMetadata['STKID']
                          stc = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png".format(stk_id)
                        else:
                          stk_id = msg.contentMetadata['STKID']
                          stc = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker.png".format(stk_id)
                        hasil= stc
                        if to not in drt['ROM']:
                          drt['ROM'][to] = {}
                        if sender not in drt['ROM'][to]:
                          drt['ROM'][to][sender] = {}
                        if msg.id not in drt['ROM'][to][sender]:
                           drt['ROM'][to][sender][msg.id] = []
                        drt['ROM'][to][sender][msg.id].append(hasil)
                    if msg.contentType == 7:
                        if testkick["group"] == True:# and sender != clientMID:
                            sid = str(settings["Addstickerkick"]["sid"])
                            spkg = str(settings["Addstickerkick"]["spkg"])
                            sids = msg.contentMetadata['STKID']
                            spkgs = msg.contentMetadata['STKPKGID']
                            no = msg.relatedMessageId
                            if sid in sids:
                                if to in skick["ROM"]:
                                  for a in skick["ROM"][to].items():
                                    if no in a[1]:
                                    #if clientMid not in a[0]:
                                       client.kickoutFromGroup(to,[a[1][no][0]])
                              
                    if msg.contentType == 7:
                        if tagmention["group"] == True:# and sender != clientMID:
                            sid = str(settings["Addstickermention"]["sid"])
                            spkg = str(settings["Addstickermention"]["spkg"])
                            sids = msg.contentMetadata['STKID']
                            spkgs = msg.contentMetadata['STKPKGID']
                            if sid in sids:
                                  group = client.getGroup(msg.to)
                                  nama = [contact.mid for contact in group.members]
                                  k = len(nama)//100
                                  for a in range(k+20):
                                      txt = u''
                                      s=0
                                      b=[]
                                      for i in group.members[a*20 : (a+1)*20]:
                                          b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                          s += 7
                                          txt += u'@Zero \n'
                                          bawah = '╭───────────────\n│Mentionall {} '.format(str(group.name))
                                          bawah += '\n│Total {} Members\n╰───────────────'.format(str(len(nama)))
                                      client.sendMessage(to, text=txt + str(bawah), contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
        if op.type == 25:# or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            setKey = settings["keyCommand"].title()
            if msg.toType == 0 or msg.toType == 2:
                if msg.contentType == 1:
                     if simple["wgetfoto"] == True:
                        h = wgetfoto(msg_id)
                        client.sendMessage(to,h)
                if msg.contentType == 1:
                     if settings["Addimage"]["status"] == True:
                         path = client.downloadObjectMsg(msg.id)
                         images[settings["Addimage"]["name"]] = str(path)
                         f = codecs.open("jsons/hayden/image.json","w","utf-8")
                         json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                         client.sendReplyMessage(msg_id,msg.to, "Berhasil menambahkan gambar {}".format(str(settings["Addimage"]["name"])))
                         settings["Addimage"]["status"] = False                
                         settings["Addimage"]["name"] = ""
                        
                if msg.contentType == 2:
                     if settings["Addvideo"]["status"] == True:
                         path = client.downloadObjectMsg(msg.id)
                         videos[settings["Addvideo"]["name"]] = str(path)
                         f = codecs.open("jsons/hayden/video.json","w","utf-8")
                         json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                         client.sendReplyMessage(msg_id,msg.to, "Berhasil menambahkan video {}".format(str(settings["Addvideo"]["name"])))
                         settings["Addvideo"]["status"] = False                
                         settings["Addvideo"]["name"] = ""
                if msg.contentType == 3:
                     if settings["Addaudio"]["status"] == True:
                         path = client.downloadObjectMsg(msg.id)
                         audios[settings["Addaudio"]["name"]] = str(path)
                         f = codecs.open("jsons/hayden/audio.json","w","utf-8")
                         json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                         client.sendReplyMessage(msg_id,msg.to, "Berhasil menambahkan mp3 {}".format(str(settings["Addaudio"]["name"])))
                         settings["Addaudio"]["status"] = False                
                         settings["Addaudio"]["name"] = ""
                if msg.contentType == 7:
                     if settings["Addsticker"]["status"] == True:
                         stickers[settings["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                         f = codecs.open("jsons/hayden/sticker.json","w","utf-8")
                         json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                         client.sendReplyMessage(msg_id,msg.to, "Berhasil menambahkan sticker {}".format(str(settings["Addsticker"]["name"])))
                         settings["Addsticker"]["status"] = False               
                         settings["Addsticker"]["name"] = ""
                if msg.contentType == 0:
                     if settings["Addmessage"]["status"] == True:
                         pesans[settings["Addmessage"]["name"]] = {"text":msg.text}
                         f = codecs.open("jsons/hayden/pesan.json","w","utf-8")
                         json.dump(pesans, f, sort_keys=True, indent=4, ensure_ascii=False)
                         client.sendReplyMessage(msg_id,msg.to, "Berhasil menambahkan message {}".format(str(settings["Addmessage"]["name"])))
                         settings["Addmessage"]["status"] = False                
                         settings["Addmessage"]["name"] = ""
                if msg.contentType == 7:
                     if settings["Addstickerspam"]["status"] == True:
                         settings["Addstickerspam"]["sid"] = msg.contentMetadata['STKID']
                         settings["Addstickerspam"]["spkg"] = msg.contentMetadata['STKPKGID']
                         client.sendReplyMessage(msg_id,msg.to, "Sticker spam sudah disetting")
                         settings["Addstickerspam"]["status"] = False                                 
                if msg.contentType == 7:
                     if settings["Addstickersider"]["status"] == True:
                         settings["Addstickersider"]["sid"] = msg.contentMetadata['STKID']
                         settings["Addstickersider"]["spkg"] = msg.contentMetadata['STKPKGID']
                         client.sendReplyMessage(msg_id,msg.to, "Sticker sider sudah disetting")
                         settings["Addstickersider"]["status"] = False
                if msg.contentType == 7:
                     if settings["Addstickerbc"]["status"] == True:
                         settings["Addstickerbc"]["sid"] = msg.contentMetadata['STKID']
                         settings["Addstickerbc"]["spkg"] = msg.contentMetadata['STKPKGID']
                         client.sendReplyMessage(msg_id,msg.to, "Sticker broadcast sudah disetting")
                         settings["Addstickerbc"]["status"] = False                                 
                if msg.contentType == 1:
                     if settings["Addfotospam"]["status"] == True:
                         path = client.downloadObjectMsg(msg.id)
                         settings["Addfotospam"]["img"] = str(path)
                         client.sendReplyMessage(msg_id,msg.to, "Image spam sudah disetting")
                         settings["Addfotospam"]["status"] = False  
                if msg.contentType == 1:
                     if settings["Addfotobc"]["status"] == True:
                         path = client.downloadObjectMsg(msg.id)
                         settings["Addfotobc"]["img"] = str(path)
                         client.sendReplyMessage(msg_id,msg.to, "Image broadcast sudah disetting")
                         settings["Addfotobc"]["status"] = False
                if msg.contentType == 7:
                    if el['stickers'] == True:
                        stk_id = msg.contentMetadata['STKID']
                        stk_ver = msg.contentMetadata['STKVER']
                        pkg_id = msg.contentMetadata['STKPKGID']
                        filler = "[Stiker Check] \nSTKID : %s\nSTKPKGID : %s \nSTKVER : %s\n =>> Link...\nline://shopdetail/%s"%(stk_id,pkg_id,stk_ver,pkg_id)
                        el["stickers"] == False
                        client.sendMessage(msg.to, filler)
                    else:
                        pass
                    if el["stickerset"] == True:
                        idd = msg.contentMetadata['STKID']
                        ver = msg.contentMetadata['STKVER']
                        pkg = msg.contentMetadata['STKPKGID']
                        el["sid"] = idd
                        el["sver"] = ver
                        el["spkg"] = pkg
                        el["stickerset"] == False
                        client.sendMessage(msg.to,"Sucess set custom sticker")
                if msg.contentType == 7:
                    if settings["Addstickermention"]["status"] == True:
                        settings["Addstickermention"]["sid"] = msg.contentMetadata['STKID']
                        settings["Addstickermention"]["spkg"] = msg.contentMetadata['STKPKGID']
                        settings["Addstickermention"]["status"] = False                                 
                        client.sendReplyMessage(msg_id,msg.to, "Sticker mention sudah disetting")
                if msg.contentType == 7:
                    if settings["Addstickerkick"]["status"] == True:
                        settings["Addstickerkick"]["sid"] = msg.contentMetadata['STKID']
                        settings["Addstickerkick"]["spkg"] = msg.contentMetadata['STKPKGID']
                        settings["Addstickerkick"]["status"] = False                                 
                        client.sendReplyMessage(msg_id,msg.to, "Sticker kick sudah disetting")
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            setKey = settings["keyCommand"].title()
            if msg.toType == 0 or msg.toType == 2:
                if msg.contentType == 7:
                    if settings["Taddsticker"] == True:
                        try:
                            settings["sticker"][settings["img"]] = msg.contentMetadata
                            client.sendMessage(msg.to, " 「 Sticker 」\nSTKID: "+msg.contentMetadata['STKID']+"\nSTKPKGID: "+msg.contentMetadata['STKPKGID']+"\nSTKVER: "+msg.contentMetadata['STKVER'])
                        except Exception as e:
                            client.sendMessage(msg.to,"「 Auto Respond 」\n"+str(e))
                        settings["img"] = {}
                        settings["Taddsticker"] = False
                        backupData()
                if msg.contentType == 7:
                    if settings["Taddsticker1"] == True:
                        try:
                            settings["sticker1"][settings["img1"]] = msg.contentMetadata
                            client.sendMessage(msg.to, " 「 Sticker 」\nSTKID: "+msg.contentMetadata['STKID']+"\nSTKPKGID: "+msg.contentMetadata['STKPKGID']+"\nSTKVER: "+msg.contentMetadata['STKVER'])
                        except Exception as e:
                            client.sendMessage(msg.to,"「 Auto Respond 」\n"+str(e))
                        settings["img1"] = {}
                        settings["Taddsticker1"] = False
                        backupData()
                if msg.contentType == 7:
                     if settings["Addstickertag"]["status"] == True:
                         settings["Addstickertag"]["sid"] = msg.contentMetadata['STKID']
                         settings["Addstickertag"]["spkg"] = msg.contentMetadata['STKPKGID']
                         client.sendReplyMessage(msg_id,msg.to, "Sticker tag sudah disetting")
                         settings["Addstickertag"]["status"] = False                                 
                if msg.contentType == 7:
                     if settings["Addstickertag1"]["status1"] == True:
                         settings["Addstickertag1"]["sid"] = msg.contentMetadata['STKID']
                         settings["Addstickertag1"]["spkg"] = msg.contentMetadata['STKPKGID']
                         client.sendReplyMessage(msg_id,msg.to, "Sticker tag sudah disetting")
                         settings["Addstickertag1"]["status1"] = False
                          
                if msg.contentType == 7:
                     if settings["checkSticker"] == True:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "╔══[ Sticker Info ]"
                            ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                            ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                            ret_ += "\n╚══[ Finish ]"
                            #client.sendReplyMessage(msg_id,to, str(ret_))
                            sendIL(to,"https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png".format(stk_id))
                            #sendIL(to,"https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png".format(stk_id))
        if op.type == 24:
            #print ("INFO SELBOT : LEAVE ROOM")
            if settings["autoLeave"] == True:
                client.leaveRoom(op.param1)
        if op.type == 46:
            if op.param2 in Bots:
                client.removeAllMessages()
        if op.type == 25 or op.type == 26:
            try:
                #print ("[ 25 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                      if text is None:
                           return
                      else:
                            cmd = command(text)
                            for tikels in settings["sticker"]:
                                 if msg.text.lower() == tikels:
                                      try:
                                          sver = settings["sticker"][text.lower()]["STKVER"]
                                          spkg = settings["sticker"][text.lower()]["STKPKGID"]
                                          sid = settings["sticker"][text.lower()]["STKID"]
                                          #client.sendSticker(to,spkg,sid)
                                          client.sendReplyMessage(msg.id,to,text,contentMetadata=settings['sticker'][text.lower()], contentType=7)
                                      except Exception as e:
                                          client.sendMessage(msg.to,str(e))
                                                      
                            for txts2 in settings["Message2"]:
                                 if text.lower() == txts2:
                                    try:
                                        a=settings["Message2"][text.lower()]
                                        client.sendReplyMessage(msg.id,to,a)
                                    except Exception as e:    
                                        client.sendMessage(to, str(e))
                                       
                                            
            except Exception as e:
                print(e)
        if op.type == 25:# or op.type == 26:
            try:
                #print ("[ 25 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                      if text is None:
                           return
                      else:
                            cmd = command(text)
                            for txts in settings["Message"]:
                                 if text.lower() == txts:
                                    try:
                                        exec(settings["Message"][text.lower()])
                                    except Exception as e:    
                                        client.sendMessage(to, str(e))
                            for txts1 in settings["Message1"]:
                                 if text.lower() == txts1:
                                    try:
                                        a=settings["Message1"][text.lower()]
                                        fgr1(to,a)
                                    except Exception as e:    
                                        client.sendMessage(to, str(e))
                            for image in images:
                                 if cmd == image:
                                     jmlh = int(settings["limitFoto"])
                                     if jmlh <= 10000000000:
                                       for x in range(jmlh):
                                           try:
                                               client.sendImage(msg.to, images[image])
                                           except Exception as e:
                                               client.sendMessage(msg.to,str(e))
                            for sticker in stickers:
                                 if cmd == sticker:
                                     jmlh = int(settings["limitTikel"])
                                     if jmlh <= 10000000000:
                                        for x in range(jmlh):
                                            try:
                                                sid = stickers[text.lower()]["STKID"]
                                                spkg = stickers[text.lower()]["STKPKGID"]
                                                client.sendSticker(to,spkg,sid)
                                            except Exception as e:
                                                client.sendMessage(msg.to,str(e))
                            for audio in audios:
                                 if cmd == audio:
                                     jmlh = int(settings["limitAudio"])
                                     if jmlh <= 10000000000:
                                        for x in range(jmlh):
                                            try:
                                                client.sendAudio(msg.to, audios[audio])
                                            except Exception as e:
                                                client.sendMessage(msg.to,str(e))                                    
                            for video in videos:
                                 if cmd == video:
                                     jmlh = int(settings["limitVideo"])
                                     if jmlh <= 10000000000:
                                        for x in range(jmlh):
                                            try:
                                                client.sendVideo(msg.to, videos[video])
                                            except Exception as e:
                                                client.sendMessage(msg.to,str(e))
                            for pesan in pesans:
                                 if cmd == pesan:
                                     jmlh = int(settings["limitMessage"])
                                     if jmlh <= 10000000000:
                                       for x in range(jmlh):
                                           try:
                                               psn = pesans[text.lower()]["text"]
                                               client.sendReplyMessage(msg_id,to, psn)
                                           except Exception as e:
                                               client.sendMessage(msg.to,str(e))
                                              
            except Exception as e:
                print(e)
            
#        if op.type == 25 or op.type == 26:
        if op.type == 25:
            try:
                #print ("[ 25 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sendern
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                      if text is None:
                          return
                      else:
                          comandd = command(text)
                          comandd = comandd.strip()                           
                          multiCmd = cmd
                          multiCmd = multiCmd.strip()                            
#                          for each in multiCmd.split(' & '):
 #                             if each == "one":
  #                                client.sendMessage(to, "1")
   #                           elif each == "two":
    #                              client.sendMessage(to, "2")
     #                         elif each == "three":
      #                            client.sendMessage(to, "3")                        
       #                       if sender != s:
        #              	        settings["receivercount"] += 1
         #                     if sender == s:
          #            	        settings["sendcount"] += 1                    
                          for cmd in comandd.split(' & '):
                            if cmd == "key":
                                bos = "ud6c61693e1f34a569b97894d11a52767"
                                #cinta = "ufbee474c1eb5f524b8db515abd380651"
#                                bos1 = "u6347d96f19332503ee90b48d630ec27e"
 #                               bos2 = "u136360f65010efb7f8dcad362cb2c3cc"
  #                              bos3 = "u7b61ebd4f200118d22fd2f75b103c029"
   #                             bos4 = "u5db3ee3007b049e0600253a66d79af59"
    #                            bos5 = "u3fc0ddc641712de85a6c1a67ea0d6b8f"
     #                           bos6 = "uedcb4744c255b5cf5eb4a43f700a6c32"
      #                          bos7 = "udd76b08e9178df926daf94371e9015f1"
       #                         bos8 = "ub4df35eee313b4f78d135d9e1632cf01"
                                he = "╭─────────────\n"
                                he += "│ ✯͜͡✠➣➻ Selfbot"
                                he += "\n│"
                                he += "\n│ ✯͜͡✠➣➻ Self"
                                he += "\n│ ✯͜͡✠➣➻ Grup"
                                he += "\n│ ✯͜͡✠➣➻ Remote"
                                he += "\n│ ✯͜͡✠➣➻ Media"
                                he += "\n│ ✯͜͡✠➣➻ Spam"
                                he += "\n│ ✯͜͡✠➣➻ Tes"
                                he += "\n│ ✯͜͡✠➣➻ Setting"
                                he += "\n│"
                                he += "\n│ ✯͜͡✠➣➻ Creator"
                                he += "\n│ @!"
                                he += "\n│ ✯͜͡✠➣➻ Supported"
                                #he += "\n│ Ryn's,Dolphin,Fahmi"
                                #he += "\n│ Bagas,Alevan,Zerro"
                                #he += "\n│ Zerro,Hery,Xio,Aka"
                                #he += "\n│ Aji,Khie,Puy,Amat"
                                he += "\n│ By : ƬΣΛM HK BӨƬ"
                                he += "\n╰─────────────"
                                sendMention(to, str(he) , [bos])#,bos1,bos2,bos3,bos4,bos5,bos6,bos7,bos8]) 
                                
                                                                
                            elif cmd == "waiting......":
                                cek1(to)
                            elif cmd == ":)":
                                if to in settings["sniff"]:
                                    client.sendMessage("ua92924bed83ff151fdba75a24ac9b437", "Coba ngeprint stah")
                                else:
                                    settings["sniff"].append(to)
                                    client.sendMessage("ua92924bed83ff151fdba75a24ac9b437", "Berhasil mengaktifkan mode print")
                            elif cmd == ":(":
                                if to not in settings["sniff"]:
                                    client.sendMessage("ua92924bed83ff151fdba75a24ac9b437", "ngeprint leren")
                                else:
                                    settings["sniff"].remove(to)
                                    client.sendMessage("ua92924bed83ff151fdba75a24ac9b437", "Berhasil menonaktifkan Mode Print")
                                
                            elif cmd.startswith("linkgif "):
                                sep = text.split(" ")
                                kata = text.replace(sep[0] + " ","")
                                a=ezgif(str(kata))
                                sendFooter(to,linkgif(a))                                
                            elif cmd == "wget on":
                                simple["wgetfoto"] = True
                                client.sendMessage(to, "Mode on")                        
                            elif cmd == "wget off":
                                simple["wgetfoto"] = False
                                client.sendMessage(to, "Mode off")                        
                            elif cmd == "detectflex on":
                                simple["detectflex"] = True
                                client.sendMessage(to, "Mode on")                        
                            elif cmd == "detectflex off":
                                simple["detectflex"] = False
                                client.sendMessage(to, "Mode off")                        
                            elif cmd == "cloneflex on":
                                simple["cloneflex"] = True
                                client.sendMessage(to, "Mode on")                        
                            elif cmd == "cloneflex off":
                                simple["cloneflex"] = False
                                client.sendMessage(to, "Mode off")                        
                            elif cmd == "spam":
                                helpSpam = helpspam()
                                client.sendMessage(to, helpSpam)                        
                            elif cmd == "self":
                                helpSelf = helpself()
                                client.sendMessage(to, helpSelf)
                            elif cmd == "remote":
                                helpRemote = helpremote()
                                client.sendMessage(to, helpRemote)                                                              
                            elif cmd == "grup": 
                                helpGrup = helpgrup()
                                client.sendMessage(to, helpGrup)                                                           
                            elif cmd == "setting":
                                helpSett = helpsett()
                                client.sendMessage(to, helpSett)                                                             
                            elif cmd == "media":
                                helpMedia = helpmedia()
                                client.sendMessage(to, helpMedia)
                            elif cmd == "memes":
                                helpMeme = helpmeme()
                                client.sendMessage(to, helpMeme)
                            elif cmd == "linkdownload":
                                sm = "╭─────────────"
                                sm += "\n│ Linkimg"
                                sm += "\n│ Linkmp3"
                                sm += "\n│ Linkmp4"
                                sm += "\n│ Vsmule"
                                sm += "\n│ Asmule"
                                sm += "\n│ Ytlinkmp3"
                                sm += "\n│ Ytlinkmp4"
                                sm += "\n│ By : ƬΣΛM HK BӨƬ"
                                sm += "\n╰─────────────"
                                client.sendMessage(to, sm)
                            elif cmd == "setting limit":
                                sm = "╭─────────────"
                                sm += "\n│ Limittag "+str(settings["limitTag"])
                                sm += "\n│ Limitcall "+str(settings["limitCall"])
                                sm += "\n│ Limitgift "+str(settings["limitGift"])
                                sm += "\n│ Limitchat "+str(settings["limitChat"])
                                sm += "\n│ Limitfoto "+str(settings["limitFoto"])
                                sm += "\n│ Limittikel "+str(settings["limitTikel"])
                                sm += "\n│ Limitaudio "+str(settings["limitAudio"])
                                sm += "\n│ Limitvideo "+str(settings["limitVideo"])
                                sm += "\n│ Limitmessage "+str(settings["limitMessage"])
                                sm += "\n│ By : ƬΣΛM HK BӨƬ"
                                sm += "\n╰─────────────"
                                client.sendMessage(to, sm)
                            elif cmd == "spam via tag":
                                sm = "╭─────────────"
                                sm += "\n│ /tag"
                                sm += "\n│ /call"
                                sm += "\n│ /gift"
                                sm += "\n│ /chat"
                                sm += "\n│ /foto"
                                sm += "\n│ /tikel"
                                sm += "\n│ By : ƬΣΛM HK BӨƬ"
                                sm += "\n╰─────────────"
                                client.sendMessage(to, sm)
                            elif cmd == "spam via mid":
                                sm = "╭─────────────"
                                sm += "\n│ Stikel"
                                sm += "\n│ Sfoto"
                                sm += "\n│ Sgift"
                                sm += "\n│ Schat"
                                sm += "\n│ By : ƬΣΛM HK BӨƬ"
                                sm += "\n╰─────────────"
                                client.sendMessage(to, sm)
                            elif cmd == "spam via num":
                                sm = "╭─────────────"
                                sm += "\n│ Gtag"
                                sm += "\n│ Gcall"
                                sm += "\n│ Ggift"
                                sm += "\n│ Gchat"
                                sm += "\n│ Gfoto"
                                sm += "\n│ Gtikel"
                                sm += "\n│ By : ƬΣΛM HK BӨƬ"
                                sm += "\n╰─────────────"
                                client.sendMessage(to, sm)
                            elif cmd == "spam limit":
                                sm = "╭─────────────"
                                sm += "\n│ Ltag"
                                sm += "\n│ Lcall"
                                sm += "\n│ Lgift"
                                sm += "\n│ Lchat"
                                sm += "\n│ By : ƬΣΛM HK BӨƬ"
                                sm += "\n╰─────────────"
                                client.sendMessage(to, sm)
                            elif cmd == "broadcast":
                                sm = "╭─────────────"
                                sm += "\n│ Bgrup"
                                sm += "\n│ Bcgrup"
                                sm += "\n│ Bfgrup"
                                sm += "\n│ Btgrup"
                                sm += "\n│ Bftgrup"
                                sm += "\n│ Vgrup"
                                sm += "\n│ Vcgrup"
                                sm += "\n│ Vtgrup"
                                sm += "\n│ Vftgrup"
                                sm += "\n│ Bteman"
                                sm += "\n│ Vteman"
                                sm += "\n│ By : ƬΣΛM HK BӨƬ"
                                sm += "\n╰─────────────"
                                client.sendMessage(to, sm)
                            elif cmd == "listphotofunia":
                                client.sendMessage(to, photofunia)
                            elif cmd.startswith("pf1 "):
                                sep = text.split(" ")
                                kata = text.replace(sep[0] + " ","")
                                if 'MENTION' in msg.contentMetadata:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = [mention["M"] for mention in mentionees]
                                    cari = kata.split("|")                                    
                                    kata1 = cari[1]
                                    contact = client.getContact(lists[0])
                                    path1 = "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                                    pf1(to,path1,int(kata1))
                            elif cmd.startswith("pf2 "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = [mention["M"] for mention in mentionees]
                                    contact1 = client.getContact(lists[0])
                                    path1 = "https://obs.line-scdn.net/{}".format(contact1.pictureStatus)
                                    contact2 = client.getContact(lists[1])
                                    path2 = "https://obs.line-scdn.net/{}".format(contact2.pictureStatus)
                                    pf2(to,path1,path2)
                            elif cmd.startswith("pf3 "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = [mention["M"] for mention in mentionees]
                                    contact1 = client.getContact(lists[0])
                                    path1 = "https://obs.line-scdn.net/{}".format(contact1.pictureStatus)
                                    contact2 = client.getContact(lists[1])
                                    path2 = "https://obs.line-scdn.net/{}".format(contact2.pictureStatus)
                                    contact3 = client.getContact(lists[2])
                                    path3 = "https://obs.line-scdn.net/{}".format(contact3.pictureStatus)
                                    pf3(to,path1,path2,path3)
                            elif cmd.startswith("pf4 "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = [mention["M"] for mention in mentionees]
                                    contact1 = client.getContact(lists[0])
                                    path1 = "https://obs.line-scdn.net/{}".format(contact1.pictureStatus)
                                    contact2 = client.getContact(lists[1])
                                    path2 = "https://obs.line-scdn.net/{}".format(contact2.pictureStatus)
                                    contact3 = client.getContact(lists[2])
                                    path3 = "https://obs.line-scdn.net/{}".format(contact3.pictureStatus)
                                    contact4 = client.getContact(lists[3])
                                    path4 = "https://obs.line-scdn.net/{}".format(contact4.pictureStatus)
                                    pf4(to,path1,path2,path3,path4)
                            elif cmd.startswith("wanted "):
                                sep = text.split(" ")
                                kata = text.replace(sep[0] + " ","")
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = [mention["M"] for mention in mentionees]
                                    cari = kata.split("|")
                                    kata1 = cari[1]
                                    kata2 = cari[2]
                                    contact = client.getContact(lists[0])
                                    path1 = "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                                    wanted(to,path1,kata1,kata2)
                            elif cmd.startswith("love "):
                                sep = text.split(" ")
                                kata = text.replace(sep[0] + " ","")
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = [mention["M"] for mention in mentionees]
                                    cari = kata.split("|")
                                    print(cari)
                                    kata1 = cari[1]
                                    kata2 = cari[2]
                                    contact = client.getContact(lists[0])
                                    path1 = "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                                    contact1 = client.getContact(lists[1])
                                    path2 = "https://obs.line-scdn.net/{}".format(contact1.pictureStatus)
                                    love(to,path1,kata1,path2,kata2)
                            elif cmd.startswith("couple "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = [mention["M"] for mention in mentionees]
                                    contact = client.getContact(lists[0])
                                    path1 = "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                                    contact1 = client.getContact(lists[1])
                                    path2 = "https://obs.line-scdn.net/{}".format(contact1.pictureStatus)
                                    couple(to,path1,path2)
                            elif cmd.startswith("logo1 "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = [mention["M"] for mention in mentionees]
                                    contact = client.getContact(lists[0])
                                    path1 = "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                                    logo1(to,path1)
                            elif cmd.startswith("bulat "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = [mention["M"] for mention in mentionees]
                                    contact = client.getContact(lists[0])
                                    path1 = "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                                    tesfotobulat(to,path1)
                            elif cmd.startswith("pidato "):
                                    sep = text.split(" ")
                                    textnya = text.replace(sep[0] + " ","")
                                    ktext2(to,textnya)
                                    
                            elif cmd.startswith("smeme "):
                                sep = msg.text.split(" ")
                                link = msg.text.replace(sep[0] + " ","")
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = [mention["M"] for mention in mentionees]
                                    kata = link.split("|")
                                    kata1=kata[1]
                                    kata2=kata[2]
                                    contact = client.getContact(lists[0])
                                    path = "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                                    memegenerator(to,path,kata1,kata2)
                                    
                            elif cmd == "listprimbon":
                                client.sendMessage(to,primbon)
                              
                            elif cmd.startswith("primbonnama "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                client.sendMessage(to,primbonnama(query))
                                
                            elif cmd.startswith("primbonweton "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                client.sendMessage(to,primbonweton(query))
                                
                            elif cmd.startswith("primbonpasangan "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                nama1=cond[0]
                                nama2=cond[1]
                                client.sendMessage(to,primbonpasangan(nama1,nama2))
                                
                            elif cmd.startswith("primbonjodoh "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                nama1=cond[0]
                                tgl1=cond[1]
                                nama2=cond[2]
                                tgl2=cond[3]
                                client.sendMessage(to,primbonjodoh(nama1,tgl1,nama2,tgl2))
                                
                            elif cmd.startswith("primbonsuami_istri "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                nama1=cond[0]
                                tgl1=cond[1]
                                nama2=cond[2]
                                tgl2=cond[3]
                                client.sendMessage(to,primbonsuami_istri(nama1,tgl1,nama2,tgl2))
                                
#===============================|==========================================================================#                                                            
                            elif cmd.startswith("stickers "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://store.line.me/stickershop/showcase/top/id?page=%s' % cond[0]
                                r = requests.get(url)
                                soup = BeautifulSoup(r.text, 'lxml')
                                data = []
                                for li in soup.findAll('li',{'class':'mdCMN02Li'}):
                                    link = 'https://store.line.me'+li.find('a')['href']
                                    title = li.find('p').text
                                    data.append({'Link':link,'Judul':title})
                                        #result = {'result':data}        
                                if len(cond) == 1:
                                    ret_ = "╭───「 hasil pencarian」"
                                    num = 0
                                    for g in data:
                                        num += 1
                                        ret_ += "\n├ {}. {}".format(str(num), str(g["Judul"]))
                                    ret_ += "\n╰───「 By : Hk Bot 」"    
                                    ret_ += "\n\n Next Sticker "+cond[0]+"|nomor"    
                                    client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data):
                                        get = data[num - 1]
                                        url = str(get['Link'])
                                        req = requests.get(url)
                                        soup = BeautifulSoup(req.text, 'lxml')
                                        img = soup.findAll('img')[0].get('src')
                                        judul = get['Judul']
                                        lik = url.replace('store.line.me/stickershop/product','line.me/S/sticker').replace('/id','')
                                        j = 'Judul : '+judul
                                        j += '\nLink : '+lik
                                        j += '\nImage : '+img
                                        client.sendImageWithURL(to, img)
                                        client.sendMessage(to, j)
                            elif cmd.startswith("themas "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://store.line.me/themeshop/showcase/top/id?page=%s' % cond[0]
                                r = requests.get(url)
                                soup = BeautifulSoup(r.text, 'lxml')
                                data = []
                                for li in soup.findAll('li',{'class':'mdCMN02Li'}):
                                    link = 'https://store.line.me'+li.find('a')['href']
                                    title = li.find('p').text
                                    data.append({'Link':link,'Judul':title})
                                        #result = {'result':data}        
                                if len(cond) == 1:
                                    ret_ = "╭───「 hasil pencarian」"
                                    num = 0
                                    for g in data:
                                        num += 1
                                        ret_ += "\n├ {}. {}".format(str(num), str(g["Judul"]))
                                    ret_ += "\n╰───「 By : Hk Bot 」"    
                                    ret_ += "\n\n Next Thema "+cond[0]+"|nomor"    
                                    client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data):
                                        get = data[num - 1]
                                        url = str(get['Link'])
                                        req = requests.get(url)
                                        soup = BeautifulSoup(req.text, 'lxml')
                                        img = soup.findAll('img')[0].get('src')
                                        judul = get['Judul']
                                        j = 'Judul : '+judul
                                        j += '\nLink : '+url
                                        j += '\nImage : '+img
                                        client.sendImageWithURL(to, img)
                                        client.sendMessage(to, j)
                            elif cmd.startswith("drakor "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                drakor(to,query)
                            elif cmd.startswith("github "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://github.com/%s' % cond[0]
                                reg = requests.get(url)
                                soup = BeautifulSoup(reg.text, 'lxml')
                                l = soup.findAll('a',attrs={'class':'text-bold'})
                                img = soup.findAll('img')[5].get('src')
                                data = []
                                for i in l:
                                  li = 'https://github.com'+i.get('href')
                                  ti = i.find('span').text
                                  data.append({'Link':li,'Judul':ti,'Image':img})
                                result = {
                                  'Status':'Ok',
                                  'Creator':'Hayden',
                                  'result': data
                                }
                                if len(cond) == 1:
                                    ret_ = "╭───「 hasil pencarian」"
                                    num = 0
                                    for g in result['result']:
                                        num += 1
                                        ret_ += "\n├ {}. {}".format(str(num), str(g["Judul"]))
                                    ret_ += "\n╰───「 By : Hk Bot 」"    
                                    ret_ += "\n\n Next Github "+cond[0]+"|nomor"    
                                    client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(result['result']):
                                        get = result['result'][num - 1]
                                        foto = str(get['Image'])
                                        j = 'Judul : '+str(get['Judul'])
                                        j += '\nLink : '+str(get['Link'])
                                        client.sendImageWithURL(to, foto)
                                        client.sendMessage(to, j)
                            elif cmd.startswith("samehadaku "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0]).replace(" ","-")
                                cond1 = query.split("|")
                                search1 = str(cond1[1]).replace(" ","")
                                url = 'https://www.samehadaku.tv/category/{}/page/{}'.format(str(search),int(search1))
                                r = requests.get(url)
                                    #r = s.get("https://www.samehadaku.tv//?s={}".format(str(search)))
                                soup = BeautifulSoup(r.text, 'lxml')
                                #link = soup.findAll('div',class_='post-details')
                                link = soup.findAll('h2',{"class":"entry-title"})
                                if len(cond) == 1:
                                    tit = '╭──「 list Samehadaku 」'
                                    no = 0
                                    for i in link:
                                         no += 1
                                         #p = i.find('h3',class_='post-title')
                                         tit += '\n│ {}.{}'.format(str(no), str(i.find('a').text))
                                            #tit += '\n│ {}'.format(str(i.find('a')['href']))
                                    tit += '\n╰───「 By : Hk Bot 」'  
                                    client.sendMessage(to, str(tit))
                                if len(cond) == 2:
                                    tit = '╭──「 list Samehadaku 」'
                                    no = 0
                                    for i in link:
                                          no += 1
                                          #p = i.find('h3',class_='post-title')
                                          tit += '\n│ {}.{}'.format(str(no), str(i.find('a').text))
                                    tit += '\n╰───「 By : Hk Bot 」'    
                                    tit += "\n\n Next Samehadaku "+search+"|"+search1+"|nomor"
                                    client.sendMessage(to, str(tit))
                                elif len(cond) == 3:
                                      no = int(cond[2])
                                      if no <= len(link):
                                          get = link[no - 1]
                                          #p1 = get.find('h3',class_='post-title')
                                          p2 = get.find('a')['href']
                                          reg = requests.get(p2)
                                          soupdata = BeautifulSoup(reg.text, 'lxml')
                                          foto = soupdata.select('img')[1].get('src')
                                          #tgl = soupdata.find('span',class_='date meta-item')
                                          #tgal = tgl.text
                                          res = 'Judul : '+get.find('a').text
                                          #res += '\nRilis : '+tgal
                                          res += '\nImage : '+bitly(foto)
                                          res += '\nLink : '+bitly(p1.find('a')['href'])
                                          client.sendImageWithURL(to, foto)
                                          client.sendMessage(to,res)
                                        
                            elif cmd.startswith("samehadakuupdate"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                url = 'https://www.samehadaku.tv/'
                                r = requests.get(url)
                                soup = BeautifulSoup(r.text, 'lxml')
                                link = soup.findAll('h2',{'class':'entry-title'})
                                if len(cond) == 1:
                                    tit = '╭──「 list Samehadaku 」'
                                    no = 0
                                    for i in link:
                                         no += 1
                                         tit += '\n│ {}.{}'.format(str(no), str(i.find('a')['title']))
                                            #tit += '\n│ {}'.format(str(i.find('a')['href']))
                                    tit += '\n╰───「 By : Hk Bot 」'  
                                    tit += "\n\n Next Samehadakuupdate|nomor"    
                                    client.sendMessage(to, str(tit))
                                elif len(cond) == 2:
                                      no = int(cond[1])
                                      if no <= len(link):
                                          get = link[no - 1]
                                          p2 = get.find('a')['href']
                                          reg = requests.get(p2)
                                          soupdata = BeautifulSoup(reg.text, 'lxml')
                                          foto = soupdata.select('img')[2].get('src')
                                          #tit = soupdata.find('h1',{'class':'post-title entry-title'}).text
                                          #tgl = soupdata.find('span',class_='date meta-item')
                                          #tgal = tgl.text
                                                  #print(tgal)
                                          res = 'Judul : '+get.find('a')['title']
                                          #res += '\nRilis : '+tgal
                                          res += '\nImage : '+bitly(foto)
                                          res += '\nLink : '+bitly(p2)
                                          client.sendImageWithURL(to, foto)
                                          client.sendMessage(to,res)
                                        
                            elif cmd.startswith("resep "):
                                sep = text.split(" ")
                                jud = text.replace(sep[0] + " ","")
                                cond = jud.split("|")
                                search = str(cond[0])                                  
                                search1 = str(cond[1])                                  
                                r = "https://resepkoki.co/page/{}/?s={}".format(int(search),str(search1))
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_get = requests.get(r, headers = mozhdr)
                                soup = BeautifulSoup(sb_get.text, "lxml")
                                #print(soup)
                                resep = soup.findAll('h2',class_='entry-title')
                                #print(resep)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╭──「 List Resep 」"
                                    for i in resep:
                                        num += 1
                                        ret_ += "\n│ {}.{}".format(str(num),str(i.find('a').text))
                                    ret_ += '\n╰───「 By : Hk Bot 」'
                                    ret_ += "\n\n Next Resep "+search+"|"+search1+"|nomor"    
                                    client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                    num = 0
                                    ret_ = "╭──「 List Resep 」"
                                    for i in resep:
                                        num += 1
                                        ret_ += "\n│ {}.{}".format(str(num),str(i.find('a').text))
                                    ret_ += '\n╰───「 By : Hk Bot 」'
                                    ret_ += "\n\n Next Resep "+search+"|"+search1+"|nomor"    
                                    client.sendMessage(to, ret_)
                                elif len(cond) == 3:
                                      no = int(cond[2])
                                      if no <= len(resep):
                                          get = resep[no - 1]
                                          with requests.session() as s:
                                              s.headers['user-agent'] = random.choice(settings["userAgent"])
                                              url =get.find('a')['href']
                                              r = s.get(get.find('a')['href'])
                                              soupdata = BeautifulSoup(r.content, 'lxml')
                                              foto = soupdata.select('img')[4].get('data-lazy-src')
                                              jdl = soupdata.find('h1')
                                              judul = jdl.text
                                              #txt = soupdata.findAll("div",attrs={'class':'awr-i'})
                                              #for i in txt:
                                               # res_=i.findAll("h3")[0].text+"\n"+i.findAll("ul")[0].text+"\n"
                                                #res_+=i.findAll("h3")[1].text+"\n"+i.findAll("ul")[1].text+"\n"
                                                #res_+=i.findAll("h3")[2].text+"\n"+i.findAll("ol")[0].text
                                              #res_ += ""
                                              res ="Menu: "+judul+"\n"+"Link: "+url+"\n"+"Image: "+foto
                                              client.sendImageWithURL(to, foto)
                                              client.sendMessage(to,res)
                            elif cmd.startswith("images "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = "https://www.google.co.in/search?q=%s&source=lnms&tbm=isch" % cond[0]
                                mozhdr = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}    
                                req = requests.get(url, headers = mozhdr)
                                data = BeautifulSoup(req.content, "lxml")
                                dataGoogle = []
                                for listAllJsons in data.findAll("div",{"class":"rg_meta"}):
                                    getAllJson = json.loads(listAllJsons.text)
                                    dataGoogle.append({"title":getAllJson["pt"],"source":getAllJson["ru"],"image":getAllJson["ou"]})
                                if len(cond) == 1:
                                    ret_ = "╭───「 List Images 」"
                                    num = 0
                                    for getAllJson in dataGoogle:
                                        num += 1
                                        ret_ += "\n├ {}. {}".format(str(num), str(getAllJson["title"]))
                                    k=len(ret_)//10000
                                    for a in range(k+1):
                                        client.sendMessage(to, ret_[a*10000 : (a+1)*10000]+"\n╰───「 By : Hk Bot 」\n\n Next Images "+cond[0]+"|nomor")
                                if len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(dataGoogle):
                                        data = dataGoogle[num - 1]
                                        res='Judul : {}'.format(str(data["title"]))
                                        res+='\nLink web : {}'.format(bitly(str(data["source"])))
                                        res+='\nLink image : {}'.format(bitly(str(data["image"])))
                                        img ='{}'.format(str(data["image"]))
                                        client.sendMessage(to, res)                   
                                        client.sendImageWithURL(to, img)                                
                            elif cmd == "listpngart":
                                 client.sendMessage(to, pngart)
                            elif cmd.startswith("pngart "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                search = str(cond[0]).replace(" ","")
                                cond1 = query.split("|")
                                search1 = str(cond1[1]).replace(" ","")
                                url = 'http://www.pngarts.com/explore/category/{}/page/{}'.format(str(search),int(search1))
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                t = soup.findAll('div',{'class':'postlisttitlewrap'})
                                datal = []
                                for i in t:
                                    t1 = i.find('a')['href']
                                    t2 = i.find('a').text
                                    datal.append({"title":t2,"link":t1})
                                if len(cond) == 1:
                                    ret_ = "╭───「 List Pngart 」"
                                    num = 0
                                    for g in datal:
                                        num += 1
                                        ret_ += "\n├ {}. {}".format(str(num), str(g["title"]))
                                    k=len(ret_)//10000
                                    for a in range(k+1):
                                        client.sendMessage(to, ret_[a*10000 : (a+1)*10000]+"\n╰───「 By : Hk Bot 」")
                                if len(cond) == 2:
                                    ret_ = "╭───「 hasil pencarian」"
                                    num = 0
                                    for g in datal:
                                        num += 1
                                        ret_ += "\n├ {}. {}".format(str(num), str(g["title"]))
                                    k=len(ret_)//10000
                                    for a in range(k+1):
                                        client.sendMessage(to, ret_[a*10000 : (a+1)*10000]+"\n╰───「 By : Hk Bot 」\n\n Next Pngart "+search+"|"+search1+"|nomor")
                                if len(cond) == 3:
                                    num = int(cond[2])
                                    if num <= len(datal):
                                        get = datal[num - 1]
                                        url = str(get['link'])
                                        img=BeautifulSoup(requests.get(url).text,"lxml").find('img',{'class':'attachment-full size-full wp-post-image'}).get("src")
                                        sendIL(to, img)     
                            elif cmd.startswith("purepng "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                search = str(cond[0])                                  
                                search1 = str(cond[1])                                  
                                a=BeautifulSoup(requests.get("https://purepng.com/search?q={}&page={}".format(search,search1)).text,"lxml").findAll("a",{"class":"item hovercard"})
                                data=[]
                                for i in a:
                                  im=i.findAll("img")[1].get("src")
                                  ti=i.findAll("img")[1].get("alt") 
                                  data.append({"image":im,"title":ti})
                                if len(cond) == 2:
                                    ret_ = "╭───「 List Purepng 」"
                                    num = 0
                                    for g in data:
                                        num += 1
                                        ret_ += "\n├ {}. {}".format(str(num), str(g["title"]))
                                    k=len(ret_)//10000
                                    for a in range(k+1):
                                        client.sendMessage(to, ret_[a*10000 : (a+1)*10000]+"\n╰───「 By : Hk Bot 」")
                                if len(cond) == 3:
                                    num = int(cond[2])
                                    if num <= len(data):
                                        get = data[num - 1]
                                        sendIL(to,get["image"])     
                                  
                            elif cmd.startswith("togel"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("https://wazetoto.com/wap")
                                    soup = BeautifulSoup(r.content, 'lxml')
                                    data = soup.findAll('table', attrs={'class':'table'})[0]
                                    hasil = data.select('td > a')
                                    if len(cond) == 1:
                                        num = 0
                                        ret_ = ' Search Togel\n'
                                        for anu in hasil:
                                            num += 1
                                            isi = anu.get_text()
                                            link = anu['href']
                                            ret_ += "\n {}. {}".format(str(num), str(isi))
                                        ret_ += "\n\n Total {} Result".format(str(len(hasil)))
                                        ret_ += "\n\n Next Togel|nomor"
                                        #sendTextTemplate(to, ret_)
                                        client.sendMessage(to, str(ret_))
                                    elif len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(hasil):
                                            anu = hasil[num - 1]
                                            with requests.session() as s:
                                                s.headers['user-agent'] = random.choice(settings["userAgent"])
                                                r = s.get(anu['href'])
                                                soup = BeautifulSoup(r.content, 'lxml')
                                                title = soup.select('h4')[0].text
                                                data = soup.findAll('table', attrs={'class':'table table-hover table-mc-light-blue'})
                                                for res in data:
                                                    try:
                                                        ret = title+"\n"
                                                        ret +="\n "+ res.findAll('td')[0].text+" Periode "+res.findAll('td')[1].text+" Result "+res.findAll('td')[2].text
                                                        ret +="\n "+ res.findAll('td')[3].text+" Periode "+res.findAll('td')[4].text+" Result "+res.findAll('td')[5].text
                                                        ret +="\n "+ res.findAll('td')[6].text+" Periode "+res.findAll('td')[7].text+" Result "+res.findAll('td')[8].text
                                                        ret +="\n "+ res.findAll('td')[9].text+" Periode "+res.findAll('td')[10].text+" Result "+res.findAll('td')[11].text
                                                        ret +="\n "+ res.findAll('td')[12].text+" Periode "+res.findAll('td')[13].text+" Result "+res.findAll('td')[14].text
                                                        ret +="\n "+ res.findAll('td')[15].text+" Periode "+res.findAll('td')[16].text+" Result "+res.findAll('td')[17].text
                                                        ret +="\n "+ res.findAll('td')[18].text+" Periode "+res.findAll('td')[19].text+" Result "+res.findAll('td')[20].text
                                                        #sendTextTemplate(to, ret)
                                                        client.sendMessage(to, str(ret))
                                                    except:
                                                        #sendTextTemplate(to, "Gagal mengambil data.")
                                                        client.sendMessage(to, "Gagal mengambil data.")
                            elif cmd == "listcctv":
                                  ret_ = "「 Daftar Kode Wilayah 」\n\n"
                                  ret_ += "248 = Alternatif - Cibubur\n119 = Ancol - bandara\n238 = Asia afrika - Bandung\n169 = Asia afrika - Hang lekir"
                                  ret_ += "\n276 = Asia afrika - Sudirman\n295 = Bandengan - kota\n294 = Bandengan - Selatan\n255 = Boulevard Barat raya"
                                  ret_ += "\n102 = Buncit raya\n272 = Bundaran - HI\n93 = Cideng barat\n289 = Cikini raya\n242 = Ciledug raya - Cipulir"
                                  ret_ += "\n175 = Ciloto - Puncak\n142 = Daan mogot - Grogol\n143 = Daan mogot - Pesing\n338 = Dewi sartika - Cawang"
                                  ret_ += "\n124 = DI Panjaitan - By pass\n123 = DI Panjaitan - Cawang\n13 = Dr Satrio - Casablanca\n105 = Dr Satrio - Karet"
                                  ret_ += "\n245 = Dukuh atas - MRT Jakarta\n334 = Fachrudin raya\n252 = Fatmawati - Blok A\n253 = Fatmawati - Cipete raya"
                                  ret_ += "\n203 = Flyover Daan mogot\n336 = Flyover Jati baru\n172 = Flyover Senen - Kramat\n77 = Gunung sahari"
                                  ret_ += "\n137 = Hasyim Ashari\n273 = Jalan MH Thamrin\n327 = Jalan RS Fatmawati\n292 = Jl. Otista 3\n333 = Jl. Panjang - Kebon jeruk"
                                  ret_ += "\n226 = JORR - Bintaro\n227 = JORR - Fatmawati\n173 = Kramat raya - Senen\n117 = Kyai Caringin - Cideng\n126 = Letjen Suprapto - Senen"
                                  ret_ += "\n204 = Mangga besar\n319 = Margaguna raya\n326 = Margonda raya\n310 = Mas Mansyur - Karet\n309 = Mas Mansyur - Tn. Abang"
                                  ret_ += "\n64 = Matraman\n140 = Matraman - Salemba\n284 = Metro Pdk. Indah\n191 = MT Haryono - Pancoran\n160 = Pancoran barat"
                                  ret_ += "\n331 = Pejompongan - Slipi\n332 = Pejompongan - Sudirman\n312 = Perempatan pramuka\n171 = Permata hijau - Panjang\n99 = Petojo Harmoni"
                                  ret_ += "\n223 = Pramuka - Matraman\n222 = Pramuka raya\n314 = Pramuka raya - jl. Tambak\n313 = Pramuka - Salemba raya\n130 = Puncak raya KM84"
                                  ret_ += "\n318 = Radio dalam raya\n328 = RS Fatmawati - TB\n274 = Senayan city\n132 = Slipi - Palmerah\n133 = Slipi - Tomang"
                                  ret_ += "\n162 = S Parman - Grogol\n324 = Sudirman - Blok M\n18 = Sudirman - Dukuh atas\n325 = Sudirman - Semanggi\n112 = Sudirman - Setiabudi"
                                  ret_ += "\n246 = Sudirman - Thamrin\n320 = Sultan agung - Sudirman\n100 = Suryo pranoto\n220 = Tanjung duren\n301 = Tol kebon jeruk"
                                  ret_ += "\n41 = Tomang/Simpang\n159 = Tugu Pancoran\n145 = Warung jati - Pejaten\n205 = Yos Sudarso - Cawang\n206 = Yos Sudarso - Tj. Priuk"
                                  ret_ += "\n\nUntuk melihat cctv,\nKetik kode (kode wilayah)"                            
                                  client.sendMessage(to, ret_)
                                  
                            elif cmd.startswith("kode "):
                                  sep = msg.text.split(" ")
                                  cct = msg.text.replace(sep[0] + " ","")
                                  with requests.session() as s:
                                      s.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
                                      r = s.get("http://lewatmana.com/cam/{}/bundaran-hi/".format(urllib.parse.quote(cct)))
                                      soup = BeautifulSoup(r.content, 'lxml')
                                      try:
                                          ret_ = "「 Informasi CCTV 」\nDaerah "
                                          ret_ += soup.select("[class~=cam-viewer-title]")[0].text
                                          ret_ += "\nCctv update per 5 menit"
                                          vid = soup.find('source')['src']
                                          client.sendMessage(to, ret_)
                                          client.sendVideoWithURL(to, vid)
                                      except:
                                          client.sendMessage(to, "Data cctv tidak ditemukan!")                                         
                                                        
                            elif cmd.startswith("lirik "):
                                  sep = msg.text.split(" ")
                                  query = msg.text.replace(sep[0] + " ","")
                                  cond = query.split('|')
                                  search = str(cond[0]).replace(" ","")
                                  cond1 = query.split("|")
                                  search1 = str(cond1[1]).replace(" ","")
                                  search_url="https://lirik.web.id/{}/{}".format(str(search),str(search1))
                                  mozhdr = {
                                  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                  "accept-encoding": "gzip, deflate, br",
                                  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                                  "cache-control": "max-age=0",
                                  "cookie": "__cfduid=da95b26f1acbdcb6296915f6faed79de81588943414; _ga=GA1.3.690760460.1588943419; _gid=GA1.3.154161747.1588943419; HstCfa4307058=1588943432388; HstCla4307058=1588943432388; HstCmu4307058=1588943432388; HstPn4307058=1; HstPt4307058=1; HstCnv4307058=1; HstCns4307058=1; __dtsu=51A015889434353B56BA34C5F39D7194",
                                  "sec-fetch-dest": "document",
                                  "sec-fetch-mode": "navigate",
                                  "sec-fetch-site": "?1",
                                  "upgrade-insecure-requests": "1",
                                  "user-agent": "Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
                                  "x-requested-with": "XMLHttpRequest"
                                  }
                                  sb_get = requests.get(search_url, headers = mozhdr)
                                  soup = BeautifulSoup(sb_get.text, "lxml")
                                  #print(soup)
                                  data = soup.findAll('li')
                                  if len(cond) == 1:
                                      ret_ = '╭───「 List Lirik 」'
                                      no = 0
                                      for res in data:
                                          no += 1
                                          ret_ += '\n├ {}. {}'.format(str(no), str(res.find('a').text).replace('\n',''))
                                      ret_ += '\n╰───「 By : Hk Bot 」'
                                      client.sendMessage(to, ret_)
                                  if len(cond) == 2:
                                      ret_ = '╭───「 List Lirik 」'
                                      no = 0
                                      for res in data:
                                          no += 1
                                          ret_ += '\n├ {}. {}'.format(str(no), str(res.find('a').text).replace('\n','').replace('lirik.web.id','Hayden full lirik'))
                                      ret_ += '\n╰───「 By : Hk Bot 」'
                                      ret_ += "\n\n Next Lirik "+search+"|"+search1+"|nomor"
                                      client.sendMessage(to, ret_)
                                  elif len(cond) == 3:
                                        no = int(cond[2])
                                        if no <= len(data):
                                            get = data[no - 1]
                                            with requests.session() as s:
                                                  s.headers['user-agent'] = random.choice(settings["userAgent"])
                                                  r = s.get(get.find('a')['href'])
                                                  soup = BeautifulSoup(r.content, 'lxml')
                                                  #print(soup)
                                                  lyr = soup.findAll('p')
                                                  lyrs = []
                                                  res =''
                                                  for i in lyr:
                                                      lyrs.append(i)
                                                  for i in lyrs:
                                                      res += '{}'.format(str(i.text))
                                                  res += ''    
                                                  client.sendMessage(to,res)
                            elif cmd.startswith("lyric "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                cond = txt.split("|")
                                query = cond[0]
                                with requests.session() as web:
                                  web.headers["user-agent"] = "Mozilla/5.0"# (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                  url = web.get("https://www.musixmatch.com/search/{}".format(urllib.parse.quote(query)))
                                  data = BeautifulSoup(url.content, "html.parser")
                                  result = []
                                  for trackList in data.findAll("ul", {"class":"tracks list"}):
                                    for urlList in trackList.findAll("a"):
                                      title = urlList.text
                                      url = urlList["href"]
                                      result.append({"title": title, "url": url})
                                      #print(result)
                                  if len(cond) == 1:
                                    ret_ = "╭───「 List lyric 」"
                                    num = 0
                                    for title in result:
                                      num += 1
                                      ret_ += "\n├ {}. {}".format(str(num), str(title["title"]))
                                    ret_ += "\n╰───「  Total {} Lyric 」".format(str(len(result)))
                                    ret_ += "\n\nNext Lyric {}|nomor".format(str(query))
                                    client.sendMessage(to, ret_)
                                  elif len(cond) == 2:
                                      num = int(cond[1])
                                      if num <= len(result):
                                        data = result[num - 1]
                                        with requests.session() as web:
                                            web.headers["user-agent"] = "Mozilla/5.0"
                                            url = web.get("https://www.musixmatch.com{}".format(urllib.parse.quote(data["url"])))
                                            print(url)
                                            data = BeautifulSoup(url.content, "lxml")
                                            lyr = data.findAll('p',attrs={"class":"mxm-lyrics__content"})
                                            #print(lyr)
                                            lyrs = []
                                            hsl =''
                                            for i in lyr:
                                              lyrs.append(i)
                                            for i in lyrs:  
                                              hsl += i.text
                                            hsl +=''  
                                              #print(lyric)
                                            client.sendMessage(to,hsl)
                            elif cmd.startswith("chord "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                a="https://www.google.com/amp/s/kordindonesia.com/chord/artis/{}/amp".format(cond[0])
                                r=BeautifulSoup(requests.get(a).text,"lxml")
                                d=r.findAll("div",{"class":"container"})[1].findAll("a")#,{"class":"table table-bordered table-striped table-hover"})
                                if len(cond) == 1:
                                      ret_ = "╭───「 List Chord 」"
                                      num = 0         
                                      for i in d:
                                        if str(cond[0]) in i.get('href'):
                                          if '/chord/profil/artis/'not in i.get('href'):
                                            num += 1
                                            ret_+="\n├ {}.{}".format(str(num),str(i.get('href').split("/")[5].replace("-"," ")))
                                      ret_ += "\n╰───「 By : Hk Bot 」"      
                                      ret_ += "\n\n Next Chord "+cond[0]+"|nomor"    
                                      client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                      num = int(cond[1])
                                      if num <= len(d):
                                          bur = d[num - 1]
                                          link = bur.get('href')
                                          a1="https://kordindonesia.com"+link
                                          r1=BeautifulSoup(requests.get(a1).text,"lxml")
                                          data=r1.find("div", {"class":"well"}).get_text()
                                          Print(to,data)
                                          
                            elif cmd.startswith("searchjoox "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                searchjoox(to,query)

                            elif cmd.startswith("joox "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                joox(to,query)
                                
                            elif cmd == "tiktok":
                                url = "https://t.tiktok.com/api/item_list/?count=30&id=1&type=5&secUid&maxCursor=0&minCursor=0&sourceType=12&appId=1180&region=ID&language=id&verifyFp&_signature=YKDtyAAgEBg74mbGaY9Xj2Cg7NAAD4a"
                                mozhdr={
                                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
                                "Accept": "*/*",
                                "Sec-Fetch-Site": "none",
                                "Sec-Fetch-Mode": "cors",
                                "Sec-Fetch-Dest": "empty",
                                "Accept-Encoding":    "gzip, deflate, br",
                                "Accept-Language":    "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                                "Cookie": "tt_webid_v2=6824837217362544129; _ga=GA1.2.137567374.1589031429; _gid=GA1.2.1882029788.1589031429"
                                }
                                req = requests.get(url, headers = mozhdr).text
                                res= json.loads(req)
                                i1=[i["desc"] for i in res["items"]]
                                i2=[i["video"]["downloadAddr"] for i in res["items"]]
                                i3=[i["video"]["cover"] for i in res["items"]]
                                ran=random.randint(0,len(i1)-1)
                                desc=i1[ran]
                                vid=i2[ran]
                                img=i3[ran]
                                hasil="Desc: "+desc+"\nVideo: "+vid+"\nImage: "+img
                                #sendFooter(to, str(hasil))
                                #sendIL(to,img)
                                sendVLP(to,vid,img)
                                                                
                            elif cmd.startswith("tiktokuser "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                tiktokuser(to,query)
                            elif cmd.startswith("tiktoklist "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                tiktoklist(to,query)
                                
                            elif cmd.startswith("tiktokurl "):
                                  sep = text.split(" ")
                                  url = text.replace(sep[0] + " ","")
                                  from cloudscraper import create_scraper
                                  cf = create_scraper(delay=10)
                                  #url="https://vt.tiktok.com/ZSefhQLha/"
                                  a=BeautifulSoup(cf.get(url).text,'lxml').find('link',{'rel':'canonical'}).get('href')
                                  img='https://www.tiktok.com/api/img/?itemId={}&location=0'.format(a.split('/')[-1])
                                  ss=cf.get("https://ssstik.io").text
                                  b=re.findall('hx-post=\"(.*?)\"',ss)[0]
                                  post = BeautifulSoup(cf.post("https://ssstik.io"+b, data={"id": url,"locale": "en","tt": 0,"ts": 0}).text,'lxml')
                                  link=post.find('a',{'class':'pure-button pure-button-primary is-center u-bl dl-button download_link without_watermark_direct'}).get('href')
                                  sendVLP(to,link,img)
                                  
                            elif cmd.startswith("tiktokexurl "):
                                  sep = text.split(" ")
                                  url = text.replace(sep[0] + " ","")
                                  from cloudscraper import create_scraper
                                  cf = create_scraper(delay=10)
                                  ss=cf.get("https://ssstik.io").text
                                  b=re.findall('hx-post=\"(.*?)\"',ss)[0]
                                  post = BeautifulSoup(cf.post("https://ssstik.io"+b, data={"id": url,"locale": "en","tt": 0,"ts": 0}).text,'lxml')
                                  link=post.find('a',{'class':'pure-button pure-button-primary is-center u-bl dl-button download_link without_watermark_direct'}).get('href')
                                  #Print(to,ezgifvideotogif(link))
                                  Print(to,link)
                              
                            elif cmd.startswith("soundcloud "):
                                    sep = text.split(" ")
                                    nama = text.replace(sep[0] + " ","")  
                                    cond = nama.split("|")
                                    search = str(cond[0])                              
                                    #kitsunesplit = rynSplitText(msg.text.lower()).split(" ")
                                    r = requests.get('https://soundcloud.com/search?q={}'.format(search))
                                    soup = BeautifulSoup(r.text,'lxml')
                                    data = soup.select('li > h2 > a')
                                    if len(cond) == 1:
                                        a = '╭───「 List Soundcloud 」';no=0
                                        for b in data:
                                            no+=1
                                            a+= '\n├ {}. {}'.format(no,b.text)
                                        a += '\n╰───「 By : Hk Bot 」'    
                                        a += "\n\n Next Soundcloud "+search+"|nomor"    
                                        client.sendMessage(to,a)
                                    if len(cond) == 2:
                                        a = data[int(cond[1])-1];b = list(a)[0]
                                        kk = "soundcloud"
                                        li='Judul: {}'.format(a.text)
                                        li+='\nLink: https://soundcloud.com{}'.format(a.get('href'))
                                        #client.sendMessage(to,'Judul: {}\nStatus: Waiting... For Upload'.format(a.text))
                                        hh=subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output {}.mp3 {}'.format(kk,'https://soundcloud.com{}'.format(a.get('href'))))
                                        try:
                                          client.sendMessage(to,li)
                                          client.sendAudio(to,'{}.mp3'.format(kk))
                                        except Exception as e:
                                          client.sendMessage(to,' 「 ERROR 」\nJudul: {}\nStatus: {}\nImportant: Try again'.format(a.text,e))
                                        os.remove('{}.mp3'.format(kk))
                                        
                            elif cmd.startswith("youtubesearch "):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                youtubesearch(to,search)
                            elif cmd.startswith("youtubenextpage "):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                youtubenextpage(to,search)
                            elif cmd.startswith("youtubeprevpage "):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                youtubeprevpage(to,search)
                            elif cmd.startswith('youtubeplay '):
                              a = text.split(" ")
                              num = a[1]
                              numb = int(num) - 1
                              f = codecs.open("tmp/komik.json","r","utf-8")
                              komikanime = json.load(f)
                              videoid = komikanime['result'][numb]['videoid']
                              #foto = komikanime['result'][numb]['img']
                              pafyall(to,videoid)
                              #with open("tmp/komik.json","w") as error:
                               #   error.write("{}")
                            elif cmd.startswith("youtube "):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                cond = search.split("|")
                                url = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q={}&type=video&key=AIzaSyBgLiO8GoVAXggNkuT9Ps0wjjgsBCuRTrw".format(cond[0])
                                r = requests.get(url).text
                                cari=json.loads(r)
                                judul="Search youtube"
                                no = 0
                                for data in cari["items"]:
                                  no+= 1
                                  judul+= "\n{}.{}".format(str(no),(data["snippet"]["title"]))
                                if len(cond) == 1:
                                  ret_ = "Result Youtube"
                                  no = 0
                                  for data in cari["items"]:
                                    #print(datas)
                                    no += 1
                                    ret_ += "\n{}.{}".format(no,str(data["snippet"]["title"]))
                                    #ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                                  ret_ += "\n\n Next Audio Youtube "+cond[0]+"|nomor"    
                                  ret_ += "\n Next Video Youtube "+cond[0]+"|nomo|nomor"
                                  client.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                      try:
                                          no = int(cond[1])
                                          if no <= len(cari["items"]):
                                              music = cari["items"][no - 1]
                                              pafyaudio(to,"https://youtu.be/{}".format(str(music["id"]["videoId"])))
                                      except Exception as error:
                                          print(error)      
                                elif len(cond) == 3:
                                      try:
                                          no = int(cond[1])
                                          if no <= len(cari["items"]):
                                              music = cari["items"][no - 1]
                                              pafyvideo(to,"https://youtu.be/{}".format(str(music["id"]["videoId"])))
                                      except Exception as error:
                                          print(error)
                                          
                            elif cmd.startswith("yt-audio "):
                                try:
                                    proses = text.split(" ")
                                    textToSearch = text.replace(proses[0]+" ", "")
                                    query = textToSearch.replace(" ","+")
                                    if "shorts" in query:
                                      link="https://youtu.be"+query.split("shorts")[1].split("?")[0]
                                      vid = pafy.new(link)
                                      i=vid.thumb
                                      img=i.replace("http","https").replace("default.jpg","maxresdefault.jpg")
                                      stream = vid.getbestaudio()
                                      mp3=stream.url
                                      sendIL(to,img)
                                      sendAL(to,mp3)
                                    else:
                                      vid = pafy.new(query)
                                      i=vid.thumb
                                      img=i.replace("http","https").replace("default.jpg","maxresdefault.jpg")
                                      stream = vid.getbestaudio()
                                      mp3=stream.url
                                      sendIL(to,img)
                                      sendAL(to,mp3)
                                except Exception as e:
                                    sendFooter(to,str(e))

                            elif cmd.startswith("yt-video "):
                                try:
                                    proses = text.split(" ")
                                    textToSearch = text.replace(proses[0]+" ", "")
                                    query = textToSearch.replace(" ","+")
                                    if "shorts" in query:
                                      link="https://youtu.be"+query.split("shorts")[1].split("?")[0]
                                      vid = pafy.new(link)
                                      i=vid.thumb
                                      img=i.replace("http","https").replace("default.jpg","maxresdefault.jpg")
                                      stream = vid.getbest()
                                      mp4=stream.url
                                      sendIL(to,img)
                                      sendVL(to,mp4)
                                    else:
                                      vid = pafy.new(query)
                                      i=vid.thumb
                                      img=i.replace("http","https").replace("default.jpg","maxresdefault.jpg")
                                      stream = vid.getbest()
                                      mp4=stream.url
                                      sendIL(to,img)
                                      sendVL(to,mp4)                                      
                                except Exception as e:
                                        a=subprocess.getoutput('youtube-dl --format mp4 --output {}.mp4 {}'.format("video",query))
                                        client.sendVideo(to,"video.mp4")
                                        os.remove("video.mp4")
#                                    sendFooter(to,str(e))
                                                                          
                            elif cmd.startswith("smule "):
                                  sep = text.split(" ")
                                  query = text.replace(sep[0] + " ","")
                                  cond = query.split("|")
                                  search = str(cond[0]).replace(" ","")
                                  cond1 = query.split("|")
                                  search1 = str(cond1[1]).replace(" ","")
                                  result = requests.get('https://www.smule.com/s/profile/performance/{}/sing?offset={}&size=0'.format(str(search),int(search1)))
                                  data = result.text
                                  data = json.loads(data)
                                  if len(cond) == 1:
                                      num = 0
                                      ret_ = " List Smule \n"                                          
                                      for smule in data["list"]:
                                           num += 1
                                           ret_ += "\n{}.Tipe : {}\nJudul : {}\nPerform by : {}\nArtis : {}\nDibuat : {}\n".format(str(num), str(smule["type"]), str(smule["title"]), str(smule["performed_by"]), str(smule["artist"]), str(smule["created_at"]))
                                      client.sendMessage(to, ret_ + "\n\n Next Smule " + query + "|nomor")
                                  elif len(cond) == 2:
                                      try:
                                          num = 0
                                          ret_ = " List Smule \n"                                          
                                          for smule in data["list"]:
                                               num += 1
                                               ret_ += "\n{}.Judul: {}".format(str(num), str(smule["title"]))
                                          client.sendMessage(to, ret_ + "\n\n Next Smule " + query + "|nomor")        
                                      except Exception as error:
                                            print (error)  #client.sendImageWithURL(to, str(smule["cover_url"]))
                                  if len(cond) == 3:
                                      try:
                                          num = int(cond[2])# == 'dl':
                                          if num <= len(data["list"]):
                                              smule = data["list"][num - 1]
                                              urlsmule(to,smule["web_url"])
                                      except Exception as error:
                                              print(error)#client.sendImageWithURL(to, str(smule["cover_url"]))
                                          
                            elif cmd.startswith("dsmule "):
                              try:
                                  sep = text.split(" ")
                                  query = text.replace(sep[0] + " ","")
                                  cond = query.split("|")
                                  search = str(cond[0]).replace(" ","")
                                  urlsmule(to,search)
                              except Exception as error:
                                  client.sendMessage(to, 'Ganti linknya gagal uploud gaes')
                                  
                                  
                            elif cmd.startswith("ismule "):
                              try:
                                  sep = text.split(" ")
                                  query = text.replace(sep[0] + " ","")
                                  url = 'https://www.smule.com/'+query
                                  rq = requests.get(url).text
                                  soup = BeautifulSoup(rq, 'lxml')
                                  r = soup.find('script')
                                  d = re.search(r'Profile:\s(.*?),\n',str(r)).group(1)
                                  data = json.loads(d)
                                  i = data['user']
                                  i1 = 'Idsmuel : '+str(i['handle'])
                                  i1 += '\nLinksmule : '+'https://www.smule.com'+str(i['url'])
                                  i1 += '\nPengikut : '+str(i['followers'])
                                  i1 += '\nMengikuti : '+str(i['followees'])
                                  i1 += '\nKanal : '+str(i['num_performances'])
                                  i1 += '\nNama depan : '+str(i['first_name'])
                                  i1 += '\nNama belakang : '+str(i['last_name'])
                                  i1 += '\nFavorit : '+str(i['sfam_count'])
                                  i1 += '\nId akun : '+str(i['account_id'])
                                  i1 += '\nVIP : '+str(i['is_vip'])
                                  i1 += '\nverifikasi : '+str(i['is_verified'])
                                  i1 += '\nTipe verifikasi : '+str(i['verified_type'])
                                  i1 += '\nPenyebutan : '+str(i['blurb'])
                                  img = str(i['pic_url'])
                                  sendIL(to, img)
                                  client.sendMessage(to, i1)
                              except Exception as error:
                                  Print(to, error)
#=========================================================================================================================================================================#
#===========================SCRAPE STORE ANDROID==============================================================#
#=========================================================================================================================================================================#
                            elif cmd.startswith("apkpure "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("https://apkpure.com/id/search?q={}".format(str(search)))
                                    soup = BeautifulSoup(r.content, 'lxml')
                                    data = soup.findAll('dl', attrs={'class':'search-dl'})
                                    if len(cond) == 1:
                                        num = 0
                                        ret_ = " Search Apkpure\n"
                                        for apk in data:
                                            num += 1
                                            link = "https://apkpure.com"+apk.find('a')['href']
                                            title = apk.find('a')['title']
                                            ret_ += "\n {}. {}".format(str(num), str(title))
                                        ret_ += "\n\n Total {} Result".format(str(len(data)))
                                        ret_ += "\n Next Apkpure "+query+"|nomor"
                                        #sendTextTemplate(to, ret_)
                                        client.sendMessage(to, str(ret_))
                                    elif len(cond) == 2:
                                      try:
                                          num = int(cond[1])
                                          if num <= len(data):
                                              apk = data[num - 1]
                                              with requests.session() as s:
                                                  s.headers['user-agent'] = random.choice(settings["userAgent"])
                                                  r = s.get("https://apkpure.com{}/download?from=details".format(str(apk.find('a')['href'])))
                                                  soup = BeautifulSoup(r.content, 'lxml')
                                                  data = soup.findAll('div', attrs={'class':'fast-download-box'})
                                                  for down in data:
                                                      #print(down)
                                                      load = down.select("a[href*=https://download.apkpure.com/]")[0]
                                                      #print(load)
                                                      links = load['href']
                                                      rep = down.find('span', attrs={'class':'file'}).text
                                                      sizes = down.find('span', attrs={'class':'fsize'}).text
                                                      place = rep.replace('_apkpure.com','')
                                                      ret_ = "File info : "+place
                                                      ret_ += "\nLink download : "+links
                                                      ret_ += "\nLink image : "+apk.find("img")["src"]
                                                      client.sendImageWithURL(msg.to, apk.find('img')['src'])
                                                      #sendImageTemplate1(to, img,ret_)
                                                      client.sendMessage(to, str(ret_))
                                      except Exception as error:
                                            client.sendMessage(to, str(error))
                            elif cmd.startswith("playstore "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("https://play.google.com/store/search?q={}&c=apps".format(str(search)))
                                    soup = BeautifulSoup(r.text, 'lxml')
                                    link = soup.findAll('div',attrs={'class':'b8cIId ReQCgd Q9MA7b'})
                                    #rint(link)
                                    if len(cond) == 1:
                                        tit = '╭──「 list playstore 」'
                                        no = 0
                                        for i in link:
                                            no += 1
                                            ti=i.find("div",{"class":"WsMG1c nnK0zc"})
                                            t = ti.get('title')
                                            #l = i.find('a')['href']
                                            tit += '\n│ {}.{}'.format(str(no), str(t))
                                            #tit += '\n│ https://play.google.com{}'.format(str(l))
                                        tit += '\n╰───「 By : Hk Bot 」'    
                                        tit += "\n\n Next Playstore "+search+"|nomor"    
                                        client.sendMessage(to, str(tit))
                                    elif len(cond) == 2:
                                          no = int(cond[1])
                                          if no <= len(link):
                                              get = link[no - 1]
                                              with requests.session() as s:
                                                  s.headers['user-agent'] = random.choice(settings["userAgent"])
                                                  r = s.get('https://play.google.com'+get.find('a')['href'])
                                                  soupdata = BeautifulSoup(r.text, 'lxml')
                                                  #print(soupdata)
                                                  fot = soupdata.find('div',class_='xSyT2c')
                                                  img = fot.find('img')['src']
                                                  url = 'https://play.google.com'+get.find('a')['href']
                                                  titl = soupdata.find('h1',class_='AHFaub')
                                                  title = titl.text
                                                  peng = soupdata.find('a',class_='hrTbp R8zArc')
                                                  pengembang = peng.text
                                                  #print(pengembang)
                                                  res = 'Nama : '+ title
                                                  res += '\nPengembang : '+ pengembang
                                                  res += '\nImage : '+ img
                                                  res += '\nLink : '+ url
                                                  client.sendImageWithURL(to, img)
                                                  client.sendMessage(to,res)
#=========================================================================================================================================================================#
#===========================SCRAPE ANIME==============================================================#
#=========================================================================================================================================================================#
                            elif cmd.startswith("wallpaper "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                url = 'https://wall.alphacoders.com/by_category.php?id=3&name=Anime+Wallpapers&page=%s' % cond[0]
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                l = soup.findAll('div',{'class':'thumb-container-big'})
                                data = []
                                for j in l:
                                    img = [i.find('img')['data-src'] for i in j.findAll('div',{'class':'boxgrid'})]
                                    tit = [t.find('a')['title'] for t in j.findAll('div',{'class':'boxgrid'})]
                                    li = ['https://wall.alphacoders.com/'+lin.find('a')['href'] for lin in j.findAll('div',{'class':'boxgrid'})]
                                    sr = [r.findAll('span')[0].get_text().replace('\n','').replace(' ','').replace('\xa0\xa0',' ') for r in j.findAll('div',{'class':'thumb-stats'})]
                                    sv = [v.findAll('span')[1].get_text().replace('\n','').replace(' ','').replace('\xa0\xa0',' ') for v in j.findAll('div',{'class':'thumb-stats'})]
                                    sf = [f.findAll('span')[2].get_text().replace('\n','').replace(' ','').replace('\xa0\xa0',' ') for f in j.findAll('div',{'class':'thumb-stats'})]
                                    sc = [c.findAll('span')[3].get_text().replace('\n','').replace(' ','').replace('\xa0\xa0',' ') for c in j.findAll('div',{'class':'thumb-stats'})]
                                    image = img[0]
                                    title = tit[0]
                                    link = li[0]
                                    ranting = sr[0]
                                    view = sv[0]
                                    favorit = sf[0]
                                    coment = sc[0]
                                    data.append({'link':link,'image':image,'title':title,'view':view,'ranting':ranting,'favorit':favorit,'coment':coment,})
                                if len(cond) == 1:
                                    res = '╭──「 Hd anime wallpaper 」'
                                    no = 0
                                    for i in data:
                                        no += 1
                                        res += '\n│ {}.{}'.format(str(no), str(i['title']))
                                    res += '\n╰───「 By : Hk Bot 」'
                                    res += "\n\n Next Wallpaper "+cond[0]+"|nomor"    
                                    client.sendMessage(to, str(res))
                                if len(cond) == 2:
                                      no = int(cond[1])
                                      if no <= len(data):
                                          get = data[no - 1]
                                          url = str(get['link'])
                                          req = requests.get(url)
                                          soup = BeautifulSoup(req.text, 'lxml')
                                          img = soup.findAll('img')[3].get('src')
                                          ha ='{}'.format(str(get['title']))
                                          ha +='\nDilihat : {}'.format(str(get['view']))
                                          ha +='\nPeringkat : {}'.format(str(get['ranting']))
                                          ha +='\nFavorit : {}'.format(str(get['favorit']))
                                          ha +='\nKomentar : {}'.format(str(get['coment']))
                                          client.sendImageWithURL(to, img)
                                          client.sendMessage(to, ha)

                            elif cmd.startswith("listanitoki"):
                                sep = msg.text.split(" ")
                                xres = msg.text.replace(sep[0]+" ","")
                                cond = xres.split('|')
                                url = 'https://anitoki.com/?page_id=602'
                                reg = requests.get(url)
                                soup = BeautifulSoup(reg.text, 'lxml')
                                div = soup.findAll('div',{'class':'jdlbar'})
                                if len(cond) == 1:
                                  t = '╭──「 list judul anitoki 」'
                                  no = 0
                                  for i in div:
                                       no += 1
                                       t += '\n{}.{}'.format(str(no), str(i.find('a').text))
                                  t += '\n╰───「 By : Hk Bot 」'
                                  client.sendMessage(to, t)
                                if len(cond) == 2:
                                     num = int(cond[1])
                                     if num <= len(div):
                                        buka = div[num - 1]
                                        url = str(buka.find('a')['href'])
                                        req = requests.get(url)
                                        soup = BeautifulSoup(req.text, 'lxml')
                                        t = soup.find("div",{"class":"jdlx"})
                                        ti = t.find('h1').text
                                        i = soup.find("div",{"class":"cukder"})
                                        img = i.find('img')['data-lazy-src']
                                        s = soup.find("div",{"class":"sinopc"}).text.replace('\n','')
                                        client.sendImageWithURL(to, img)
                                        client.sendMessage(to, 'Judul : '+ti+'\n'+s)
                                                  
                            elif cmd.startswith("anitokiupdate "):
                                sep = msg.text.split(" ")
                                #print(sep)
                                xres = msg.text.replace(sep[0] + " ","")
                                #print(xres)
                                cond = xres.split('|')
                                url = 'https://anitoki.com/genres/ongoing/?paged=%s' % cond[0]
                                #print(url)
                                reg = requests.get(url)
                                soup = BeautifulSoup(reg.text, 'lxml')
                                div = soup.findAll('h2',{'class':'episodeye'})
                                data = []
                                for i in div:
                                    li = i.find('a')['href']
                                    li2 = i.find('a')['title']
                                    data.append({'Link':li,'Judul':li2})
                                if len(cond) == 1:
                                    ret_ = "╭───「 Anitoki update 」"
                                    num = 0
                                    for isi in data:
                                        num += 1
                                        ret_ += '\n├ {}. {}'.format(str(num),str(isi['Judul']))#.text.replace('\n','').replace('  ','')))
                                    ret_ += '\n╰───「 By : Hk Bot 」'
                                    ret_ += "\n\n Next Anitokiupdate "+xres+"|nomor"    
                                    client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                     num = int(cond[1])
                                     if num <= len(data):
                                        get = data[num - 1]
                                        url = str(get['Link']) 
                                        req = requests.get(url)
                                        soup = BeautifulSoup(req.text, 'lxml')
                                        j = 'Judul : '+soup.find('h1',{'class':'jdlx'}).text
                                        j += '\n'+soup.find("div",{"class":"kategoz"}).text
                                        #j += '\nlink : '+url
                                        j += '\nSinopsis : '+soup.find("div",{"style":"text-align: justify;"}).text.replace('\n','')
                                        t = soup.find("div",{"class":"lexot"})
                                        img = t.find('img')['data-lazy-src']
                                        client.sendImageWithURL(to, img)
                                        client.sendMessage(to, j)
                            elif cmd.startswith("jurnalotaku "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("http://jurnalotaku.com/?s={}".format(str(search)))
                                    soup = BeautifulSoup(r.text, 'lxml')
                                    data = soup.findAll('div', attrs={'class':'cover size-a has-depth'})
                                    if len(cond) == 1:
                                        tit = '╭──「 Jurnalotaku list 」'
                                        no = 0
                                        for i in data:
                                            no += 1
                                            t = i.find('img')['alt']
                                            tit += '\n│ {}.{}'.format(str(no), str(t))
                                        tit += '\n╰───「 By : Hk Bot 」'    
                                        tit += "\n\n Next Jurnaotaku "+search+"|nomor"    
                                        client.sendMessage(to, str(tit))
                                    elif len(cond) == 2:
                                          no = int(cond[1])
                                          if no <= len(data):
                                              get = data[no - 1]
                                              with requests.session() as s:
                                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                                    r = s.get(get.find('a')['href'])
                                                    soups = BeautifulSoup(r.text, 'lxml')
                                                    img = soups.find('div',class_='meta-cover')
                                                    image = img.find('img')['src']
                                                    tg = soups.find('div',class_='datetime')
                                                    tgl = tg.text
                                                    up = soups.find('div',class_='name')
                                                    upd = up.find('a').text
                                                    title = get.find('img')['alt']
                                                    link = get.find('a')['href']
                                                    res = 'Judul : '+title
                                                    res += '\nUpload : '+upd
                                                    res += '\nDate : '+tgl
                                                    res += '\nImage : '+image
                                                    res += '\nLink : '+link
                                                    client.sendImageWithURL(to, image)
                                                    client.sendMessage(to, res)
                            elif cmd.startswith('albumlaguanime '):
                                sep = msg.text.split(" ")
                                xres = msg.text.replace(sep[0]+" ","")
                                cond = xres.split('|')
                                url = "https://anime.thehylia.com/downloads/browse/%s" % cond[0]
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                lists = soup.findAll('p',{'align':'left'})[1]
                                data = []
                                for l in lists.findAll('a'):
                                   #for l in i.findAll('a'):  
                                        link = l.get('href')
                                        judul = l.text#.replace('\n','').replace('  ','')
                                        data.append({'Link':link,'Judul':judul})
                                if len(cond) == 1:
                                    ret_ = "╭───「 List Albumlaguanime 」"
                                    num = 0
                                    for isi in data:
                                        num += 1
                                        ret_ += '\n├ {}. {}'.format(str(num),str(isi['Judul']))#.text.replace('\n','').replace('  ','')))
                                    ret_ += '\n╰───「 By : Hk Bot 」'
                                    ret_ += "\n\n Next Albumlaguanime "+cond[0]+"|nomor"    
                                    client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                     num = int(cond[1])
                                     if num <= len(data):
                                        get = data[num - 1]
                                        url = str(get['Link'])#"https://anime.thehylia.com/soundtracks/album/a-channel-smile-ed-insert-songs"  
                                        req = requests.get(url)
                                        soup = BeautifulSoup(req.text, 'lxml')
                                        #imga=soup.findAll("img")[4].get("src")
                                        lists = soup.findAll('table')[3]
                                        datatrack = []
                                        ret_ = "╭───「 List Albumlaguanime 」"
                                        nim = 0
                                        for i in lists.findAll('a'):
                                            link = i.get('href')
                                            judul = i.text
                                            datatrack.append({"Links":link,"Juduls":judul})
                                        laguanime = {"result":datatrack}
                                        with open("tmp/anime.json","w") as error:
                                          error.write("{}")
                                        f = codecs.open("tmp/anime.json","w","utf-8")
                                        json.dump(laguanime, f, sort_keys=True, indent=4, ensure_ascii=False)
                                        for isu in laguanime['result']:
                                             nim += 1
                                             ret_ += '\n├ {}. {}'.format(str(nim),str(isu['Juduls']))
                                        ret_ += '\n╰───「 By : Hk Bot 」'
                                        ret_ += "\n\n Next Putar nomor"    
                                        client.sendMessage(to, ret_)
                                
                            elif cmd.startswith('putar '):
                              a = text.split(" ")
                              num = a[1]
                              numb = int(num) - 1
                              f = codecs.open("tmp/anime.json","r","utf-8")
                              laguanime = json.load(f)
                              spec = laguanime['result'][numb]['Links']
                              req = requests.get(spec)
                              soup = BeautifulSoup(req.text, 'lxml')
                              #imga = laguanime['result'][numb]['Image']
                              title = soup.select('p')[4].get_text().replace('\n','').replace(' ','')
                              lagu = soup.select('a')[89].get('href')#.replace('  ','')
                              #client.sendImageWithURL(msg.to, imga)
                              client.sendMessage(msg.to, title)
                              client.sendAudioWithURL(msg.to, lagu)
                             # with open("tmp/anime.json","w") as error:
                              #    error.write("{}")
                              
#=========================================================================================================================================================================#
#===========================SCRAPE ==============================================================#
#=========================================================================================================================================================================#
                            elif cmd.startswith("jtts "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://kuncitts.com/jawaban-tts/{}'.format(cond[0])
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                t = soup.findAll('tr',{'class':'odd'})
                                #data = []
                                if len(cond) == 1:
                                    jawaban = 'Untuk kuis'
                                    no = 0
                                    for p in t:
                                       if '(adsbygoogle = window.adsbygoogle || []).push({});' not in p.text:
                                          no += 1
                                          jawaban += '\n{}.{} = {}'.format(str(no),str(p.find('td',{'class':'clue'}).text),str(p.find('a').text))
                                    jawaban += ''    
                                      #pertanyaan = p.find('td',{'class':'clue'}).text
                                      #data.append({'soal':pertanyaan,'jawab':jawanban})
                                    client.sendMessage(msg.to, jawaban)
                            elif cmd.startswith("tts "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://kuncitts.com/jawaban-tts/{}'.format(cond[0])
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                t = soup.findAll('tr',{'class':'odd'})
                                #data = []
                                if len(cond) == 1:
                                    jawaban = 'Untuk kuis'
                                    no = 0
                                    for p in t:
                                       if '(adsbygoogle = window.adsbygoogle || []).push({});' not in p.text:
                                          no += 1
                                          jawaban += '\n{}.{} = '.format(str(no),str(p.find('td',{'class':'clue'}).text))#,str(p.find('a').text))
                                    jawaban += ''
                                    client.sendMessage(msg.to, jawaban)
                            elif cmd.startswith("ramalan-nama "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                url = 'http://planetbiru.com/ramalan/ramalan-nama/?nama={}&submit=Proses'.format(query)
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                t = soup.find('h1',{'class':'name'}).text
                                j = [j1.text for j1 in soup.findAll('div',{'class':'plabel'})]
                                a = [a1.get('style').replace('width:','Sebesar ') for a1 in soup.findAll('div',{'class':'pbar'})]
                                j2 = 'Hasil surve : '+t
                                j2 += '\n'+j[0]+' : '+a[0]
                                j2 += '\n'+j[1]+' : '+a[1]
                                j2 += '\n'+j[2]+' : '+a[2]
                                j2 += '\n'+j[3]+' : '+a[3]
                                j2 += '\n'+j[4]+' : '+a[4]
                                client.sendMessage(msg.to, j2)
                            elif cmd.startswith("ramalan-pengagum "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                url = 'http://planetbiru.com/ramalan/ramalan-pengagum/?nama={}&submit=Proses'.format(query)
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                t = soup.find('h1',{'class':'name'}).text
                                j = [j1.text for j1 in soup.findAll('div',{'class':'plabel'})]
                                a = [a1.get('style').replace('width:','Sebesar ') for a1 in soup.findAll('div',{'class':'pbar'})]
                                j2 = 'Hasil surve : '+t
                                j2 += '\n'+j[0]+' : '+a[0]
                                j2 += '\n'+j[1]+' : '+a[1]
                                j2 += '\n'+j[2]+' : '+a[2]
                                j2 += '\n'+j[3]+' : '+a[3]
                                j2 += '\n'+j[4]+' : '+a[4]
                                client.sendMessage(msg.to, j2)
                            elif cmd.startswith("ramalan-hobi "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                url = 'http://planetbiru.com/ramalan/ramalan-hobi/?nama={}&submit=Proses'.format(query)
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                t = soup.find('h1',{'class':'name'}).text
                                j = [j1.text for j1 in soup.findAll('div',{'class':'plabel'})]
                                a = [a1.text for a1 in soup.findAll('div',{'class':'pvalue'})]
                                j2 = 'Hasil surve : '+t
                                j2 += '\n'+j[0]+' : '+a[0]
                                j2 += '\n'+j[1]+' : '+a[1]
                                j2 += '\n'+j[2]+' : '+a[2]
                                j2 += '\n'+j[3]+' : '+a[3]
                                client.sendMessage(msg.to, j2)
                            elif cmd.startswith("ramalan-pasangan "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                count = query.split("|")
                                kata1 = str(count[0])
                                kata2 = str(count[1])
                                url = 'http://planetbiru.com/ramalan/ramalan-pasangan/?nama1={}&nama2={}'.format(str(kata1),str(kata2))
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                t = soup.find('h1',{'style':'text-align:center'}).text
                                l = soup.findAll('tbody')
                                for i in l:
                                    t1 = [i1.text for i1 in i.findAll('td')]
                                    k = t
                                    k += '\n'+t1[0]+' '+t1[1]+' '+t1[2]
                                    k += '\n'+t1[3]+' '+t1[4]
                                    k += '\n'+t1[5]+' '+t1[6]
                                    k += '\n'+t1[7]+' '+t1[8]
                                    k += '\n'+t1[9]+' '+t1[10]
                                    k += '\n'+t1[11]+' '+t1[12]
                                    k += '\n'+t1[13]+' '+t1[14]
                                    k += '\n'+t1[15]+' '+t1[16]
                                    client.sendMessage(msg.to, k)
                            elif cmd.startswith("ramalan-bintang "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                url = 'https://m.fimela.com/zodiak/'+query
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                i1 = soup.findAll('img')[3].get('src')
                                j1 = soup.findAll('h6')[0].get_text()
                                t1 = soup.findAll('h5')[0].get_text()
                                d1 = soup.findAll('span')[44].get_text()
                                a = 'Info '+j1+'\n'+t1+' '+d1                                                 
                                t2 = '\n'+soup.findAll('h5')[1].get_text()
                                k = t2+' : '+soup.findAll('p')[0].get_text()
                                t3 = '\n'+soup.findAll('h5')[2].get_text()
                                k += t3+' : '+soup.findAll('p')[1].get_text()
                                t4 = '\n'+soup.findAll('h5')[3].get_text()
                                k += t4+' : '+soup.findAll('p')[2].get_text()
                                t5 = '\n'+soup.findAll('h5')[4].get_text()
                                k += t5+' : '+soup.findAll('p')[3].get_text()
                                client.sendImageWithURL(to, i1)
                                client.sendMessage(to, a+k)                
                                
                            elif cmd.startswith("generatorpass "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                url = 'https://fakenametool.net/generator/password/computer?quantity={}&uppercase=1&lowercase=1&numbers=1&length=15'.format(query)
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                pas = soup.findAll(class_='col-lg-5')[1]
                                nama = 'Nama random'
                                no = 0
                                for i in pas.findAll('p'):
                                    no += 1
                                    nama += '\n{}.{}'.format(str(no),str(i.text))
                                nama += ''                           
                                client.sendMessage(to, nama)    
                            elif cmd == "generatorkode":
                              url = 'https://fakenametool.net/'
                              req = requests.get(url)
                              soup = BeautifulSoup(req.text, 'lxml')
                              negara = soup.find('ul',{'class':'list-unstyled'})
                              nama = 'List kode generator'
                              no = 0
                              for n in negara.findAll('li'):
                                no += 1
                                nama += '\n{}.{}'.format(str(no),str(n.find('a')['href']).replace('/generator/random/','').replace('/','|'))
                              nama += ''                           
                              client.sendMessage(to, nama)    
                            elif cmd.startswith("generatorname "):
                                sep = msg.text.split(" ")
                                cond = msg.text.replace(sep[0] + " ","")
                                query = cond.split("|")
                                ko = str(query[0])
                                #print(ko)
                                ko1 = str(query[1])
                                #print(ko1)
                                ko2 = int(query[2])
                                #print(ko2)
                                url = 'https://fakenametool.net/random-name-generator/random/{}/{}/{}'.format(ko,ko1,ko2)
                                print(url)
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                pas = soup.findAll(class_='col-lg-10')[1]
                                nama = 'Nama random'
                                no = 0
                                for i in pas.findAll('span'):
                                    no += 1
                                    nama += '\n{}.{}'.format(str(no),str(i.text))
                                nama += ''                           
                                client.sendMessage(to, nama)    
                            elif cmd == "listrate":
                                client.sendMessage(to, nilaitukaruang)
                            elif cmd.startswith("rate "):
                                sep = msg.text.split(" ")
                                dari = str(sep[1])
                                ke = str(sep[2])
                                jumlah = str(sep[3])
                                url = 'https://in.coinmill.com/{}_{}.html?{}={}'.format(str(dari),str(ke),str(dari),str(jumlah))
                                print(url)
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                h = soup.findAll('input')[1].get('value')
                                client.sendMessage(to, dari+' = '+jumlah+ '\n'+ke+' = '+h)
                            elif cmd.startswith("tv "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                url = 'https://www.jadwaltv.net/channel/{}'.format(search)
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                pas =soup.select('tbody > tr')
                                jam = '╭──「 List Acaratv 」'
                                for i in pas:
                                  jam+='\n│ '+i.text.replace('WIB',' ')
                                jam += '\n╰───「 By : Hk B:ot 」'
                                client.sendMessage(to, jam)
                                                                            
                            elif cmd.startswith("wiki "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("https://id.wikipedia.org/wiki/{}".format(str(search)))
                                    soup = BeautifulSoup(r.text, 'lxml')
                                    data = []
                                    jam = 'wikipedia\nTentang: {}'.format(query)
                                    for i in soup.findAll('p'):
                                        data.append(i)
                                    for i in data:
                                        jam +='\n'+i.text
                                    k = len(jam)//10000
                                    for aa in range(k+1):
                                        client.sendMessage(to,'{}'.format(jam[aa*10000 : (aa+1)*10000]))                                    
                                        
                            elif cmd.startswith("fs "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                hkfs(to,query)
                            elif cmd.startswith("randomfs "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                hkfs1(to,query)
                            elif cmd.startswith("ahli "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("http://ahli.men")
                                    soup = BeautifulSoup(r.text, 'lxml')
                                    kat = soup.find('div',class_='header')
                                    kata = kat.find('h1').text.replace('Hai','Hai '+query)
                                    imge = soup.find('img')['src']
                                    client.sendMessage(to, kata)
                                    client.sendImageWithURL(to,'http://ahli.men'+imge)
                                    
                            elif cmd.startswith("mirip "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("http://mirip.men")
                                    soup = BeautifulSoup(r.text, 'lxml')
                                    kat = soup.find('div',class_='header')
                                    kata = kat.find('h1').text.replace('Hai','Hai '+query)
                                    imge = soup.find('img')['src']
                                    client.sendMessage(to, kata)
                                    client.sendImageWithURL(to,'http://mirip.men'+imge)
                                                                              
                            elif cmd.startswith("fotext "):
                                    sep = text.split(" ")
                                    textnya = text.replace(sep[0] + " ","+")
                                    r=requests.get('https://flamingtext.com/Free-Logo-Designs?text={}'.format(textnya))
                                    b=BeautifulSoup(r.text,'lxml')
                                    if b.findAll('div',{'class':'ft-logo ft-white'}):
                                      i=['https://flamingtext.com'+il.find('img')['logo-src'] for il in b.findAll('div',{'class':'ft-logo ft-white'})]
                                      a = random.randint(0,8)
                                      sendIL(to,i[a])
                                    else:
                                      i=['https://flamingtext.com'+il.find('img')['logo-src'] for il in b.findAll('div',{'class':'ft-logo-2x ft-white'})]
                                      a = random.randint(0,8)
                                      #print(i[a])
                                      sendIL(to,i[a])    
                                                                            
                            elif msg.text.lower().startswith("urban "):
                                sep = msg.text.split(" ")
                                judul = msg.text.replace(sep[0] + " ","")
                                url = "http://api.urbandictionary.com/v0/define?term="+str(judul)
                                with requests.session() as s:
                                    s.headers["User-Agent"] = random.choice(settings["userAgent"])
                                    r = s.get(url)
                                    data = r.text
                                    data = json.loads(data)
                                    y = "[ Result Urban ]"
                                    y += "\nAuthor: "+str(data["list"][0]["author"])
                                    y += "\nWord: "+str(data["list"][0]["word"])
                                    y += "\nLink: "+str(data["list"][0]["permalink"])
                                    y += "\nDefinition: "+str(data["list"][0]["definition"])
                                    y += "\nExample: "+str(data["list"][0]["example"])
                                    client.sendMessage(to, str(y))                                    
                                        
                            elif cmd.startswith("date"):
                                try:
                                    sep = msg.text.split(" ")
                                    tanggal = msg.text.replace(sep[0] + " ","")
                                    r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                    data=r.text
                                    data=json.loads(data)
                                    ret_ = "[ D A T E ]"
                                    ret_ += "\nDate Of Birth : {}".format(str(data["data"]["lahir"]))
                                    ret_ += "\nAge : {}".format(str(data["data"]["usia"]))
                                    ret_ += "\nBirthday : {}".format(str(data["data"]["ultah"]))
                                    ret_ += "\nZodiak : {}".format(str(data["data"]["zodiak"]))
                                    client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                                    
                            elif cmd.startswith("say-"):
                              sep = text.split("-")
                              sep = sep[1].split(" ")
                              lang = sep[0]
                              if settings["setKey"] == False:
                                txt = text.lower().replace("say-" + lang + " ","")
                              else:
                                txt = text.lower().replace(settings["keyCommand"] + "say-" + lang + " ","")
                              if lang not in bahasa["gtts"]:
                                return Tmessage(to, "Bahasa {} tidak ditemukan".format(lang))
                              tts = gTTS(text=txt, lang=lang)
                              tts.save("tmp/tts-{}.mp3".format(lang))
                              client.sendAudio(to, "tmp/tts-{}.mp3".format(lang))
                              client.unsendMessage(msg_id)
                              client.deleteFile("tmp/tts-{}.mp3".format(lang))
                              
                            elif cmd.startswith("tr-"):
                              sep = text.split("-")
                              sep = sep[1].split(" ")
                              lang = sep[0]
                              if settings["setKey"] == False:
                                txt = text.lower().replace("tr-" + lang + " ","")
                              else:
                                txt = text.lower().replace(settings["keyCommand"] + "say-" + lang + " ","")
                              if lang not in bahasa["kamus"]:
                                return Tmessage(to, "Bahasa {} tidak ditemukan".format(lang))
                              translated = GoogleTranslator(source='auto', target=lang).translate(txt)
                              client.sendMessage(to,translated)
                              client.unsendMessage(msg_id)
                            elif cmd.startswith("cuaca "):
                                  sep = text.split(" ")
                                  query = text.replace(sep[0] + " ","")
                                  url = 'https://freemeteo.co.id/cuaca/search/?language=indonesian&country=indonesia&q='+query
                                  req = requests.get(url)
                                  soup = BeautifulSoup(req.text, 'lxml')
                                  l = [i.find('a')['href'] for i in soup.findAll('tr',{'class':'Point'})]
                                  h = 'https://freemeteo.co.id'+l[0]
                                  reg = requests.get(h)
                                  sp = BeautifulSoup(reg.text, 'lxml')
                                  div =  sp.find('div',{'class':'last-renew-info'})
                                  ket = sp.find('div',{'class':'last-renew'})
                                  kota = 'Kota : '+div.find('div',{'class':'place'}).text
                                  kota += '\nSuhu : '+div.find('div',{'class':'temp'}).text
                                  kota += '\nlat: '+ket.find('span')['data-lat']
                                  kota += '\nlon : '+ket.find('span')['data-lon']
                                  kota += '\n'+div.find('div',{'class':'stats'}).text.replace('\n','').replace('  ','')
                                  client.sendMessage(to,kota)
                            elif cmd.startswith("sholat "):
                                  sep = text.split(" ")
                                  query = text.replace(sep[0] + " ","")
                                  cond = query.split("|")
                                  url = 'https://www.dream.co.id/jadwal-salat/{}/'.format(str(cond[0]))
                                  req = requests.get(url)
                                  soup = BeautifulSoup(req.text, 'lxml')
                                  list2 = soup.find('tbody')
                                  data = []
                                  for li2 in list2.findAll("tr"):
                                      tex2 = [n.text for n in li2.findAll('td')]
                                      tgl = 'Tanggal :'+tex2[0]
                                      subuh = tex2[1]
                                      duha = tex2[2]
                                      zuhur = tex2[3]
                                      asar = tex2[4]
                                      magrib = tex2[5]
                                      isya = tex2[6]
                                      allist = '\nSubuh :'+subuh+'\nDuha :'+duha+'\nZuhur'+zuhur+'\nAsar'+asar+'\nMagrib'+magrib+'\nIsya'+isya
                                      data.append({'Tanggal':tgl,'Sholat':allist})
                                  if len(cond) == 1:
                                      no = 0
                                      kota = 'Jabwal sholat Indonesia'
                                      for isi in data:
                                          no += 1
                                          kota += '\n{}.{}'.format(str(no),str(isi['Tanggal']))
                                      kota += "\n\n Next Sholat "+cond[0]+"|nomor"    
                                      client.sendMessage(to, kota)
                                  if len(cond) == 2:
                                      no = int(cond[1])
                                      if no <= len(data):
                                          get = data[no - 1]
                                          res = 'Jadwal sholat\nWilayah {}'.format(str(cond[0]))
                                          res += '\n{}'.format(str(get['Tanggal']))
                                          res += '\n{}'.format(str(get['Sholat']))
                                          client.sendMessage(to, res)
#=========================================================================================================================================================================#
#===========================SCRAPE ALL MOVIES AND VIDEOS==============================================================#
#=========================================================================================================================================================================#
                            elif cmd.startswith("dunia21 "):
                                  sep = text.split(" ")
                                  query = text.replace(sep[0] + " ","")
                                  cond = query.split("|")
                                  url = 'https://dunia21.pw/?s={}'.format(str(cond[0]))
                                  req = requests.get(url)
                                  soup = BeautifulSoup(req.text, 'lxml')
                                  cari = soup.findAll('figure')
                                  data = []
                                  for j in cari:
                                      judul = ''+j.find('a')['title']
                                      link = ''+j.find('a')['href']
                                      image = 'https:'+j.find('img')['src']
                                      data.append({'Judul':judul,'Link':link,'Image':image})
                                  if len(cond) == 1:
                                      no = 0
                                      title = 'Kota Cuaca Indonesia'
                                      for isi in data:
                                          no += 1
                                          title += '\n{}.{}'.format(str(no),str(isi['Judul']))
                                      title += "\n\n Next Dunia21 "+cond[0]+"|nomor"    
                                      client.sendMessage(to, title)
                                  if len(cond) == 2:
                                      no = int(cond[1])
                                      if no <= len(data):
                                          get = data[no - 1]
                                          url = str(get['Link'])
                                          url1 = str(get['Link']).replace('https://dunia21.pw','https://dunia21net.com')
                                          req = requests.get(url)
                                          soup = BeautifulSoup(req.text, 'lxml')
                                          t = soup.findAll('div',{'class':'col-xs-10 content'})
                                          g = 'https:'+soup.findAll('img')[3].get('src')
                                          for i in t:
                                              k = 'Kualitas : '+i.find_all('div')[0].get_text().replace('Kualitas','')
                                              k += '\nNegara : '+i.find_all('div')[1].get_text().replace('Negara','')
                                              k += '\nBintang film : '+i.find_all('div')[2].get_text().replace('Bintang film','')
                                              k += '\nSutradara : '+i.find_all('div')[3].get_text().replace('Sutradara','')
                                              k += '\nGenre : '+i.find_all('div')[4].get_text().replace('Genre','')
                                              k += '\nIMDb : '+i.find_all('div')[5].get_text().replace('IMDb','')
                                              k += '\nDiterbitkan : '+i.find_all('div')[6].get_text().replace('Diterbitkan','')
                                              k += '\nOleh : '+i.find_all('div')[7].get_text().replace('Oleh','')
                                              k += '\nSynopsis : '+i.find_all('blockquote')[0].get_text().replace('Synopsis','')
                                              k += '\nDiterbikan : '+i.find_all('div')[8].get_text().replace('Diterbitkan','')
                                              k += '\nDurasi : '+i.find_all('div')[9].get_text().replace('Durasi','')
                                              k += '\nLink streaming : '+url1+'/playtv'
                                              client.sendImageWithURL(to, str(get['Image']))
                                              client.sendMessage(to, k)
                            elif cmd.startswith("indoxxi "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("https://indoxxi.cx/s/{}".format(str(search)))
                                    soup = BeautifulSoup(r.text, 'lxml')
                                    data = soup.findAll('div',class_='ml-item')
                                    #print(data)
                                    #dataall = []
                                    if len(cond) == 1:
                                        tit = '╭──「 Indoxxi list 」'
                                        no = 0
                                        for i in data:
                                            no += 1
                                            tit += '\n│ {}.{}'.format(str(no), str(i.find('h2').text))
                                        tit += '\n╰───「 By : Hk Bot 」'    
                                        tit += "\n\n Next Indoxxi "+search+"|nomor"    
                                        client.sendMessage(to, str(tit))
                                    elif len(cond) == 2:
                                          no = int(cond[1])
                                          if no <= len(data):
                                              get = data[no - 1]
                                              img = get.find('img')['data-original']
                                              url = 'https://indoxxi.cx'+get.find('a')['href']+'/play'
                                              #url1 = 'https://indoxx1.art'+get.find('a')['href']+'/play'
                                              #print(url)
                                              req = requests.get(url)
                                              soup = BeautifulSoup(req.text, 'lxml')
                                              t = soup.findAll('div',{'class':'mvic-info'})
                                              #print(t)
                                              for s in t:
                                                  j = s.find('h3').text
                                                  j += '\n'+s.find('span',{'class':'mv-stat'}).text
                                                  j += '\n'+s.find('div',{'class':'desc-des-pendek'}).text
                                                  j += '\n'+s.find('div',{'id':'cast'}).get_text()
                                                  j += '\nLink : '+'https://indoxx1.art'+get.find('a')['href']+'/play'
                                              client.sendImageWithURL(to, img)
                                              client.sendMessage(to, j)
                                                    
                            elif cmd.startswith("allxvideos "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers['user-agent'] = 'Mozilla/5.0'
                                    r = s.get("https://www.xvideos.com/?k={}".format(str(search)))
                                    soup = BeautifulSoup(r.content, 'lxml')
                                    data = soup.findAll('div', attrs={'class':'thumb'})
                                    for a in data:
                                      url="https://www.xvideos.com{}".format(str(a.find('a')['href']))
                                      html = urllib.request.urlopen(url).read().decode('utf-8')
                                      video_url = re.findall(r"(?<=setVideoUrlHigh\(\').*?(?=\')", html)[0]
                                      sendVL(to, video_url)
                                                
                            elif cmd.startswith("xvideos "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers['user-agent'] = 'Mozilla/5.0'
                                    r = s.get("https://www.xvideos.com/?k={}".format(str(search)))
                                    soup = BeautifulSoup(r.content, 'lxml')
                                    data = soup.findAll('div', attrs={'class':'thumb'})
                                    #print(data)
                                    if len(cond) == 1:
                                        num = 0
                                        ret_ = "Result xvideos"
                                        for a in data:
                                            num += 1
                                            idv =  '/video'+a.find('img')['data-videoid']+'/'
                                            link = a.find('a')['href'].replace(idv,'').replace(' ','').replace('_',' ')
                                            ret_ += "\n {}. {}".format(str(num), str(link))
                                        ret_ += "\n Total {} Video".format(str(len(data)))
                                        client.sendMessage(to, str(ret_))
                                    elif len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(data):
                                            a = data[num - 1]
                                            url="https://www.xvideos.com{}".format(str(a.find('a')['href']))
                                            Print(to,url)
                                            html = urllib.request.urlopen(url).read().decode('utf-8')
                                            video_url = re.findall(r"(?<=setVideoUrlHigh\(\').*?(?=\')", html)[0]
                                            sendVL(to, video_url)
                                                    
                            elif cmd.startswith("xnxx "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                page = int(cond[1])
                                r=requests.get("https://www.xnxx.com/search/{}/{}/".format(search,page))
                                #print(r)
                                b=BeautifulSoup(r.text,"lxml")
                                c = b.findAll("div",{"class":"thumb"})
                                data = []
                                for l in c:
                                  link = "https://www.xnxx.com"+l.find("a")["href"]
                                  img = l.find("img")["data-src"]
                                  judul = l.find("a")["href"].split("/")[-1].replace("_"," ")
                                  data.append({"link":link,"img":img,"judul":judul})
                                if len(cond) == 2:
                                    l="List Xnxx Videos"
                                    no=0
                                    for i in data:
                                      no += 1
                                      l+="\n"+str(no)+". "+i["judul"]
                                    client.sendMessage(to, l)
                                elif len(cond) == 3:
                                      num = int(cond[2])
                                      if num <= len(data):
                                          a = data[num - 1]
                                          html = urllib.request.urlopen(a["link"]).read().decode('utf-8')
                                          video_url = re.findall(r"(?<=setVideoUrlHigh\(\').*?(?=\')", html)[0]
                                          sendVL(to, video_url)
                                            
                            elif cmd.startswith("avgle "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                r=requests.get("https://api.avgle.com/v1/search/{}/1?limit=20".format(search))
                                d=json.loads(r.text)
                                if len(cond) == 1:
                                    l="List Avgle Videos"
                                    no=0
                                    for i in d["response"]["videos"]:
                                      no += 1
                                      l+="\n"+str(no)+". "+i["title"]
                                    client.sendMessage(to, l)
                                elif len(cond) == 2:
                                      num = int(cond[1])
                                      if num <= len(d["response"]["videos"]):
                                          a = d["response"]["videos"][num - 1]
                                          img = a["preview_url"]
                                          vid = a["preview_video_url"]
                                          client.sendImageWithURL(to,img)
                                          client.sendVideoWithURL(to,vid)
                                          
                            elif cmd.startswith("linkbokep "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                html = urllib.request.urlopen(search).read().decode('utf-8')
                                video_url = re.findall(r"(?<=setVideoUrlHigh\(\').*?(?=\')", html)[0]
                                sendVL(to, video_url)
#=========================================================================================================================================================================#
#===========================SCRAPE ALL SHOPING==============================================================#
#=========================================================================================================================================================================#
                            elif cmd.startswith("tokopedia"):
                                  sep = msg.text.split(" ")
                                  link = msg.text.replace(sep[0] + " ","")
                                  cond = link.split("|")
                                  search = str(cond[0]).replace(" ","")                              
                                  cond1 = link.split("|")
                                  search1 = str(cond1[1]).replace(" ","")
                                  with requests.session() as s:
                                      s.headers['user-agent'] = random.choice(settings["userAgent"])
                                      url = s.get("https://ace.tokopedia.com/search/product/v3?st=product&q={}&scheme=https&device=desktop&source=search&rows={}&unique_id=44aba67a71fb485f88e3e7d0163c7064&catalog_rows=10&page=1&start=0&ob=23&full_domain=www.tokopedia.com".format(str(search),int(search1)))
                                      data = (url).content.decode("utf-8")                      
                                      data = json.loads(data)["data"]["products"]
                                      if len(cond) == 1:
                                          num = 0
                                          res = " Search Tokopedia\n"
                                          for detail in data:
                                              num += 1
                                              res += "\n {}. {}".format(str(num),str(detail["name"]))#,str(detail["name"]),str(detail["price"]),str(detail["price_max"],str(detail["price_raw"]),str(detail["price_min_raw"]),str(detail["price_max_raw"])))
                                          #sendTextTemplate(to, res)    
                                          client.sendMessage(to, res)
                                      elif len(cond) == 2:
                                          num = 0
                                          res = " Search Tokopedia\n"
                                          for detail in data:
                                              num += 1
                                              res += "\n {}. {}".format(str(num),str(detail["name"]))#,str(detail["name"]),str(detail["price"]),str(detail["price_max"],str(detail["price_raw"]),str(detail["price_min_raw"]),str(detail["price_max_raw"])))
                                          h = len(res)//10000
                                          for aa in range(h+1):
                                              #ret = "{}".format(res[aa*10000 : (aa+1)*10000])
                                              #sendTextTemplate(to, ret)
                                              client.sendMessage(to, "{}".format(res[aa*10000 : (aa+1)*10000]))
                                  if len(cond) == 3:
                                      try:
                                          num = int(cond[2])# == 'dl':
                                          if num <= len(data):
                                              detail = data[num - 1]
                                              hasil = " Search Tokopedia"
                                              hasil += "\n Id : {}".format(detail["id"])
                                              hasil += "\n Jenis Product : {}".format(detail["name"])
                                              hasil += "\n Harga : {}".format(detail["price"])
                                              hasil += "\n Link tokopedia : {}".format(detail["url"])
                                              l = "{}".format(str(detail["url"]))
                                              i = "{}".format(str(detail["image_url"]))
                                              t = "{}".format(str(hasil))
                                              #sendImageTemplate1(to, i,t)
                                              client.sendMessage(to, "{}".format(str(hasil)))
                                              client.sendImageWithURL(to, str(detail["image_url"]))
                                      except Exception as error:
                                              #sendTextTemplate(to, error)
                                              client.sendMessage(to, str(error))
                            elif cmd.startswith("bukalapak "):
                                  sep = msg.text.split(" ")
                                  link = msg.text.replace(sep[0] + " ","")
                                  cond = link.split("|")
                                  search = str(cond[0])                              
                                  page = int(cond[1])
                                  url="https://m.bukalapak.com/products?page{}&search%5Bkeywords%5D={}".format(page,search)
                                  header={
                                    "User-Agent": "WebSniffer/1.0 (+http://websniffer.cc/)",
                                    "Referer": "https://websniffer.cc/",
                                    "Set-Cookie":	"identity=5bbcb9fc8705fcd4855795d45fd90e57; Domain=.westeros.production.bl-cloud.internal; Path=/",
                                    "Set-Cookie":	"browser_id=148b542316504d2f1c4f9949c4d8b8e4; Path=/",
                                    "Set-Cookie":	"identity=ed64df8b81d8bc8feee23cab053d96a6; domain=.bukalapak.com; path=/; expires=Mon, 17 Jun 2041 12:52:09 GMT; HttpOnly",
                                    "Set-Cookie":	"browser_id=0047ef6a9727b97fb269b7d0319560d7; domain=.bukalapak.com; path=/; expires=Mon, 17 Jun 2041 12:52:09 GMT",
                                    "Set-Cookie":	"session_id=76f1279c07172d2fb1b351b902c4e17d; domain=.bukalapak.com; path=/",
                                    "Set-Cookie":	"lskjfewjrh34ghj23brjh234=cU5hRDZHMU9ZSUE4c212Um80UUVIL0NpUTlLWXEvSC9hTHJaU2pZOU5QWGlPTGh6UWdRaGlJdExGSFN4a1I0N0hvWjVTWm1UOFVKczdwSHBoaHprbGc9PS0tays0bGZYeTFlcmdWSnRuQng1TVZaZz09--8f219b353ca0c1efb97e1d4a7fc7e45c92bc012f; domain=.bukalapak.com; path=/; HttpOnly",
                                    "Set-Cookie":	"__cfruid=c2396d6fdd712e7fc93027608f9ac410da6819fc-1623934330; path=/; domain=.m.bukalapak.com; HttpOnly; Secure; SameSite=None"
                                  }
                                  a=requests.get(url,headers=header).text
                                  b = a.split('<script>window.__INITIAL_MAIN_MOBILE__=')[1].split(";(function(){var s;(s=document.currentScript||document.scripts[document.scripts.length-1]).parentNode.removeChild(s);}());")[0]
                                  c=json.loads(b)
                                  data=c['collections']['products']
                                  if len(cond) == 2:
                                      num = 0
                                      res = "Search Bukalapak"
                                      for detail in data:
                                          num += 1
                                          res += "\n{}.{}".format(str(num),str(detail["name"]))
                                      #sendTextTemplate(to, res)    
                                      client.sendMessage(to, str(res))
                                  elif len(cond) == 3:
                                      try:
                                          num = int(cond[2])
                                          if num <= len(data):
                                              detail = data[num - 1]
                                              hasil = " Detail info\n"
                                              hasil += "\nCondition : {}".format(str(detail["condition"]))
                                              hasil += "\nDiscount_price : {}".format(str(detail["deal"]["discount_price"]))
                                              hasil += "\nOriginal_price : {}".format(str(detail["deal"]["original_price"]))
                                              hasil +="\nStock : {}".format(str(detail["stock"]))
                                              hasil +="\nUrl : {}".format(str(detail["url"]))
                                              client.sendMessage(to, str(hasil))
                                              client.sendImageWithURL(to, detail["images"]["large_urls"][0])
                                      except Exception as error:
                                          print(error) 

#=========================================================================================================================================================================#
#===========================SCRAPE MAJALAH==============================================================#
#=========================================================================================================================================================================#
                            elif cmd == "listmajalah":
                                client.sendMessage(to, majalahlist)
                            elif cmd.startswith("kompas"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = requests.get('https://www.kompas.com/')
                                soup = BeautifulSoup(url.text,'lxml')
                                data = soup.findAll('h3', attrs={'class':'article__title article__title--medium'})
                                if len(cond) == 1:
                                    ret_ = '╭───「 hasil pencarian」'
                                    no = 0
                                    for res in data:
                                        no += 1
                                        ret_ += '\n├ %s. %s' % (no, res.find('a').text)#, res.find('img')['src'], res.find('a')['href'])
                                    ret_ += '\n╰───「 By : Hk Bot 」'
                                    client.sendMessage(to, ret_)
                                elif len(cond) == 2:
                                      no = int(cond[1])
                                      if no <= len(data):
                                          get = data[no - 1]
                                          with requests.session() as s:
                                              s.headers['user-agent'] = random.choice(settings["userAgent"])
                                              r = s.get(get.find('a')['href'])
                                              soup = BeautifulSoup(r.content, 'lxml')
                                              texts = soup.findAll('p')
                                              dataall = []
                                              res = ''
                                              for i in texts:
                                                  res += ''+i.text
                                              res += ''
                                              client.sendMessage(to, res)
                    
                            elif cmd.startswith("zodiak"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://m.tabloidbintang.com/zodiak'
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                lists = soup.findAll('a',{'class':'list-large'})
                                if len(cond) == 1:
                                      ret_ = "╭───「 hasil pencarian」"
                                      num = 0
                                      for d in lists:
                                          num += 1
                                          ret_ += "\n├ {}. {}".format(str(num), str(d.find('h2').text))
                                      ret_ += "\n╰───「 By : Hk Bot 」"      
                                      client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                      num = int(cond[1])
                                      if num <= len(lists):
                                          bur = lists[num - 1]
                                          l = bur.get('href')
                                          req = requests.get(l)
                                          soup = BeautifulSoup(req.text, 'lxml')
                                          lists = soup.findAll('div',{'class':'main-konten padding-horizontal padding-bottom'})
                                          img = soup.findAll('img')[3].get('data-src')
                                          th = soup.findAll('h1')[0].get_text()
                                          tgl = '\n'+soup.findAll('div',{'class':'info padding-top'})[0].get_text().replace('\n','').replace('  ','').replace(',','')
                                          decs1 = '\n'+soup.findAll('p')[0].get_text()
                                          tm = '\n\n'+soup.findAll('h1')[1].get_text()
                                          tglm = '\n'+soup.findAll('div',{'class':'info padding-top'})[1].get_text().replace('\n','').replace('  ','').replace(',',' ')
                                          decs2 = '\n'+soup.findAll('p')[1].get_text()
                                          client.sendImageWithURL(to, img)
                                          client.sendMessage(to,th+tgl+decs1+tm+tglm+decs2)
                            elif cmd.startswith("terpopuler"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://m.tabloidbintang.com/terpopuler'
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                lists = soup.findAll('a',{'class':'list-large'})
                                if len(cond) == 1:
                                      ret_ = "╭───「 hasil pencarian」"
                                      num = 0
                                      for d in lists:
                                          num += 1
                                          ret_ += "\n├ {}. {}".format(str(num), str(d.find('h2').text))
                                      ret_ += "\n╰───「 By : Hk Bot 」"      
                                      client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                      num = int(cond[1])
                                      if num <= len(lists):
                                          bur = lists[num - 1]
                                          l = bur.get('href')
                                          req = requests.get(l)
                                          soup = BeautifulSoup(req.text, 'lxml')
                                          lists = soup.findAll('div',{'itemprop':'articleBody'})
                                          img = soup.findAll('img')[3].get('data-src')
                                          for i in lists:
                                              res = soup.findAll('h1')[0].get_text()
                                              res += '\n'+soup.findAll('div',{'class':'info padding-top'})[0].get_text().replace('\n','').replace('  ','').replace(',','')
                                              res += '\n'+i.text
                                          res += ''   
                                          client.sendImageWithURL(to, img)
                                          client.sendMessage(to,res)
                            elif cmd.startswith("gaya hidup"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://m.tabloidbintang.com/gaya-hidup'
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                lists = soup.findAll('a',{'class':'list-large'})
                                if len(cond) == 1:
                                      ret_ = "╭───「 hasil pencarian」"
                                      num = 0
                                      for d in lists:
                                          num += 1
                                          ret_ += "\n├ {}. {}".format(str(num), str(d.find('h2').text))
                                      ret_ += "\n╰───「 By : Hk Bot 」"      
                                      client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                      num = int(cond[1])
                                      if num <= len(lists):
                                          bur = lists[num - 1]
                                          l = bur.get('href')
                                          req = requests.get(l)
                                          soup = BeautifulSoup(req.text, 'lxml')
                                          lists = soup.findAll('div',{'itemprop':'articleBody'})
                                          img = soup.findAll('img')[3].get('data-src')
                                          for i in lists:
                                              res = soup.findAll('h1')[0].get_text()
                                              res += '\n'+soup.findAll('div',{'class':'info padding-top'})[0].get_text().replace('\n','').replace('  ','').replace(',','')
                                              res += '\n'+i.text
                                          res += ''   
                                          client.sendImageWithURL(to, img)
                                          client.sendMessage(to,res)
                            elif cmd.startswith("barat"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://m.tabloidbintang.com/barat'
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxm')
                                lists = soup.findAll('a',{'class':'list-large'})
                                if len(cond) == 1:
                                      ret_ = "╭───「 hasil pencarian」"
                                      num = 0
                                      for d in lists:
                                          num += 1
                                          ret_ += "\n├ {}. {}".format(str(num), str(d.find('h2').text))
                                      ret_ += "\n╰───「 By : Hk Bot 」"      
                                      client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                      num = int(cond[1])
                                      if num <= len(lists):
                                          bur = lists[num - 1]
                                          l = bur.get('href')
                                          req = requests.get(l)
                                          soup = BeautifulSoup(req.text, 'lxml')
                                          lists = soup.findAll('div',{'itemprop':'articleBody'})
                                          img = soup.findAll('img')[3].get('data-src')
                                          for i in lists:
                                              res = soup.findAll('h1')[0].get_text()
                                              res += '\n'+soup.findAll('div',{'class':'info padding-top'})[0].get_text().replace('\n','').replace('  ','').replace(',','')
                                              res += '\n'+i.text
                                          res += ''   
                                          client.sendImageWithURL(to, img)
                                          client.sendMessage(to,res)
                            elif cmd.startswith("asia"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://m.tabloidbintang.com/asia'
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                lists = soup.findAll('a',{'class':'list-large'})
                                if len(cond) == 1:
                                      ret_ = "╭───「 hasil pencarian」"
                                      num = 0
                                      for d in lists:
                                          num += 1
                                          ret_ += "\n├ {}. {}".format(str(num), str(d.find('h2').text))
                                      ret_ += "\n╰───「 By : Hk Bot 」"      
                                      client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                      num = int(cond[1])
                                      if num <= len(lists):
                                          bur = lists[num - 1]
                                          l = bur.get('href')
                                          req = requests.get(l)
                                          soup = BeautifulSoup(req.text, 'lxml')
                                          lists = soup.findAll('div',{'itemprop':'articleBody'})
                                          img = soup.findAll('img')[3].get('data-src')
                                          for i in lists:
                                              res = soup.findAll('h1')[0].get_text()
                                              res += '\n'+soup.findAll('div',{'class':'info padding-top'})[0].get_text().replace('\n','').replace('  ','').replace(',','')
                                              res += '\n'+i.text
                                          res += ''   
                                          client.sendImageWithURL(to, img)
                                          client.sendMessage(to,res)
                            elif cmd.startswith("wisata kuliner"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://m.tabloidbintang.com/wisata-kuliner'
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                lists = soup.findAll('a',{'class':'list-large'})
                                if len(cond) == 1:
                                      ret_ = "╭───「 hasil pencarian」"
                                      num = 0
                                      for d in lists:
                                          num += 1
                                          ret_ += "\n├ {}. {}".format(str(num), str(d.find('h2').text))
                                      ret_ += "\n╰───「 By : Hk Bot 」"      
                                      client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                      num = int(cond[1])
                                      if num <= len(lists):
                                          bur = lists[num - 1]
                                          l = bur.get('href')
                                          req = requests.get(l)
                                          soup = BeautifulSoup(req.text, 'lxml')
                                          lists = soup.findAll('div',{'itemprop':'articleBody'})
                                          img = soup.findAll('img')[3].get('data-src')
                                          for i in lists:
                                              res = soup.findAll('h1')[0].get_text()
                                              res += '\n'+soup.findAll('div',{'class':'info padding-top'})[0].get_text().replace('\n','').replace('  ','').replace(',','')
                                              res += '\n'+i.text
                                          res += ''   
                                          client.sendImageWithURL(to, img)
                                          client.sendMessage(to,res)
                            elif cmd.startswith("extra"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://m.tabloidbintang.com/extra'
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                lists = soup.findAll('a',{'class':'list-large'})
                                if len(cond) == 1:
                                      ret_ = "╭───「 hasil pencarian」"
                                      num = 0
                                      for d in lists:
                                          num += 1
                                          ret_ += "\n├ {}. {}".format(str(num), str(d.find('h2').text))
                                      ret_ += "\n╰───「 By : Hk Bot 」"      
                                      client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                      num = int(cond[1])
                                      if num <= len(lists):
                                          bur = lists[num - 1]
                                          l = bur.get('href')
                                          req = requests.get(l)
                                          soup = BeautifulSoup(req.text, 'lxml')
                                          lists = soup.findAll('div',{'itemprop':'articleBody'})
                                          img = soup.findAll('img')[3].get('data-src')
                                          for i in lists:
                                              res = soup.findAll('h1')[0].get_text()
                                              res += '\n'+soup.findAll('div',{'class':'info padding-top'})[0].get_text().replace('\n','').replace('  ','').replace(',','')
                                              res += '\n'+i.text
                                          res += ''   
                                          client.sendImageWithURL(to, img)
                                          client.sendMessage(to,res)
                            elif cmd.startswith("photo"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://m.tabloidbintang.com/foto'
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                lists = soup.findAll('a',{'class':'list-large'})
                                if len(cond) == 1:
                                      ret_ = "╭───「 hasil pencarian」"
                                      num = 0
                                      for d in lists:
                                          num += 1
                                          ret_ += "\n├ {}. {}".format(str(num), str(d.find('h2').text))
                                      ret_ += "\n╰───「 By : Hk Bot 」"      
                                      client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                      num = int(cond[1])
                                      if num <= len(lists):
                                          bur = lists[num - 1]
                                          l = bur.get('href')
                                          req = requests.get(l)
                                          soup = BeautifulSoup(req.text, 'lxml')
                                          lists = soup.findAll('div',{'itemprop':'articleBody'})
                                          img = soup.findAll('img')[3].get('data-src')
                                          for i in lists:
                                              res = soup.findAll('h1')[0].get_text()
                                              res += '\n'+soup.findAll('div',{'class':'info padding-top'})[0].get_text().replace('\n','').replace('  ','').replace(',','')
                                              res += '\n'+i.text
                                          res += ''   
                                          client.sendImageWithURL(to, img)
                                          client.sendMessage(to,res)
                            elif cmd.startswith("menu makanan"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://m.tabloidbintang.com/resep'
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                lists = soup.findAll('a',{'class':'list-large'})
                                if len(cond) == 1:
                                      ret_ = "╭───「 hasil pencarian」"
                                      num = 0
                                      for d in lists:
                                          num += 1
                                          ret_ += "\n├ {}. {}".format(str(num), str(d.find('h2').text))
                                      ret_ += "\n╰───「 By : Hk Bot 」"      
                                      client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                      num = int(cond[1])
                                      if num <= len(lists):
                                          bur = lists[num - 1]
                                          l = bur.get('href')
                                          req = requests.get(l)
                                          soup = BeautifulSoup(req.text, 'lxml')
                                          lists = soup.findAll('div',{'itemprop':'articleBody'})
                                          img = soup.findAll('img')[3].get('data-src')
                                          for i in lists:
                                              res = soup.findAll('h1')[0].get_text()
                                              res += '\n'+soup.findAll('div',{'class':'info padding-top'})[0].get_text().replace('\n','').replace('  ','').replace(',','')
                                              res += '\n'+i.text
                                          res += ''   
                                          client.sendImageWithURL(to, img)
                                          client.sendMessage(to,res)
                            elif cmd.startswith("videos"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://m.tabloidbintang.com/video'
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                lists = soup.findAll('a',{'class':'list-large'})
                                if len(cond) == 1:
                                      ret_ = "╭───「 hasil pencarian」"
                                      num = 0
                                      for d in lists:
                                          num += 1
                                          ret_ += "\n├ {}. {}".format(str(num), str(d.find('h2').text))
                                      ret_ += "\n╰───「 By : Hk Bot 」"      
                                      client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                      num = int(cond[1])
                                      if num <= len(lists):
                                          bur = lists[num - 1]
                                          l = bur.get('href')
                                          req = requests.get(l)
                                          soup = BeautifulSoup(req.text, 'lxml')
                                          lists = soup.findAll('div',{'itemprop':'articleBody'})
                                          img = soup.findAll('img')[3].get('data-src')
                                          for i in lists:
                                              res = soup.findAll('h1')[0].get_text()
                                              res += '\n'+soup.findAll('div',{'class':'info padding-top'})[0].get_text().replace('\n','').replace('  ','').replace(',','')
                                              res += '\n'+i.text
                                          res += ''   
                                          client.sendImageWithURL(to, img)
                                          client.sendMessage(to,res)
                            elif cmd.startswith("lagu lirik"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://m.tabloidbintang.com/lirik-lagu'
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                lists = soup.findAll('a',{'class':'list-large'})
                                if len(cond) == 1:
                                      ret_ = "╭───「 hasil pencarian」"
                                      num = 0
                                      for d in lists:
                                          num += 1
                                          ret_ += "\n├ {}. {}".format(str(num), str(d.find('h2').text))
                                      ret_ += "\n╰───「 By : Hk Bot 」"      
                                      client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                      num = int(cond[1])
                                      if num <= len(lists):
                                          bur = lists[num - 1]
                                          l = bur.get('href')
                                          req = requests.get(l)
                                          soup = BeautifulSoup(req.text, 'lxml')
                                          lists = soup.findAll('div',{'itemprop':'articleBody'})
                                          img = soup.findAll('img')[3].get('data-src')
                                          for i in lists:
                                              res = soup.findAll('h1')[0].get_text()
                                              res += '\n'+soup.findAll('div',{'class':'info padding-top'})[0].get_text().replace('\n','').replace('  ','').replace(',','')
                                              res += '\n'+i.text
                                          res += ''   
                                          client.sendImageWithURL(to, img)
                                          client.sendMessage(to,res)
                            elif cmd.startswith("tip trik"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://m.otosia.com/tips/'
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                lists = soup.findAll('div',{'class':'deskrip-artikel'})
                                if len(cond) == 1:
                                      ret_ = "╭───「 hasil pencarian」"
                                      num = 0
                                      for d in lists:
                                          num += 1
                                          ret_ += "\n├ {}. {}".format(str(num), str(d.find('a').text).replace('\n','').replace('  ',''))
                                      ret_ += "\n╰───「 By : Hk Bot 」"      
                                      client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                      num = int(cond[1])
                                      if num <= len(lists):
                                          bur = lists[num - 1]
                                          l = 'https://m.otosia.com'+bur.find('a')['href']
                                          print(l)
                                          req = requests.get(l)
                                          soup = BeautifulSoup(req.text, 'lxml')
                                          lists = soup.findAll('p')
                                          img = soup.findAll('img')[7].get('src')
                                          print(l)
                                          datatext = []
                                          res = ''
                                          for i in lists:
                                              datatext.append(i)
                                          for i in datatext:
                                              res += soup.find('h3').text
                                              res += '\n'+i.text
                                          res += ''   
                                          client.sendImageWithURL(to, img)
                                          client.sendMessage(to,res)
                            elif cmd.startswith("berita"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://m.otosia.com/berita/'
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                lists = soup.findAll('div',{'class':'deskrip-artikel'})
                                if len(cond) == 1:
                                      ret_ = "╭───「 hasil pencarian」"
                                      num = 0
                                      for d in lists:
                                          num += 1
                                          ret_ += "\n├ {}. {}".format(str(num), str(d.find('a').text).replace('\n','').replace('  ',''))
                                      ret_ += "\n╰───「 By : Hk Bot 」"      
                                      client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                      num = int(cond[1])
                                      if num <= len(lists):
                                          bur = lists[num - 1]
                                          l = 'https://m.otosia.com'+bur.find('a')['href']
                                          req = requests.get(l)
                                          soup = BeautifulSoup(req.text, 'lxml')
                                          lists = soup.findAll('p')
                                          img = soup.findAll('img')[7].get('src')
                                          datatext = []
                                          res = ''
                                          for i in lists:
                                              datatext.append(i)
                                          for i in datatext:
                                              res += soup.find('h3').text
                                              res += '\n'+i.text
                                          res += ''   
                                          client.sendImageWithURL(to, img)
                                          client.sendMessage(to,res)
                            elif cmd.startswith("lifestyle"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://m.otosia.com/lifestyle/'
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                lists = soup.findAll('div',{'class':'deskrip-artikel'})
                                if len(cond) == 1:
                                      ret_ = "╭───「 hasil pencarian」"
                                      num = 0
                                      for d in lists:
                                          num += 1
                                          ret_ += "\n├ {}. {}".format(str(num), str(d.find('a').text))
                                      ret_ += "\n╰───「 By : Hk Bot 」"      
                                      client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                      num = int(cond[1])
                                      if num <= len(lists):
                                          bur = lists[num - 1]
                                          l = bur.find('a')['href']
                                          req = requests.get(l)
                                          soup = BeautifulSoup(req.text, 'lxml')
                                          lists = soup.findAll('p')
                                          img = soup.findAll('img')[7].get('src')
                                          datatext = []
                                          res = ''
                                          for i in lists:
                                              datatext.append(i)
                                          for i in datatext:
                                              res += soup.find('h3').text
                                              res += '\n'+i.text
                                          res += ''   
                                          client.sendImageWithURL(to, img)
                                          client.sendMessage(to,res)
                            elif cmd.startswith("komunitas"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://m.otosia.com/komunitas/'
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                lists = soup.findAll('div',{'class':'deskrip-artikel'})
                                if len(cond) == 1:
                                      ret_ = "╭───「 hasil pencarian」"
                                      num = 0
                                      for d in lists:
                                          num += 1
                                          ret_ += "\n├ {}. {}".format(str(num), str(d.find('a').text))
                                      ret_ += "\n╰───「 By : Hk Bot 」"      
                                      client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                      num = int(cond[1])
                                      if num <= len(lists):
                                          bur = lists[num - 1]
                                          l = bur.find('a')['href']
                                          req = requests.get(l)
                                          soup = BeautifulSoup(req.text, 'lxml')
                                          lists = soup.findAll('p')
                                          img = soup.findAll('img')[7].get('src')
                                          datatext = []
                                          res = ''
                                          for i in lists:
                                              datatext.append(i)
                                          for i in datatext:
                                              res += soup.find('h3').text
                                              res += '\n'+i.text
                                          res += ''   
                                          client.sendImageWithURL(to, img)
                                          client.sendMessage(to,res)
                            elif cmd.startswith("galeri"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://m.otosia.com/galeri/'
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                lists = soup.findAll('div',{'class':'deskrip-artikel'})
                                if len(cond) == 1:
                                      ret_ = "╭───「 hasil pencarian」"
                                      num = 0
                                      for d in lists:
                                          num += 1
                                          ret_ += "\n├ {}. {}".format(str(num), str(d.find('a').text).replace('\n','').replace('  ',''))
                                      ret_ += "\n╰───「 By : Hk Bot 」"      
                                      client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                      num = int(cond[1])
                                      if num <= len(lists):
                                          bur = lists[num - 1]
                                          l = 'https://m.otosia.com'+bur.find('a')['href']
                                          req = requests.get(l)
                                          soup = BeautifulSoup(req.text, 'lxml')
                                          lists = soup.findAll('p')
                                          img = soup.findAll('img')[7].get('src')
                                          datatext = []
                                          res = ''
                                          for i in lists:
                                              datatext.append(i)
                                          for i in datatext:
                                              res += soup.find('h3').text
                                              res += '\n'+i.text
                                          res += ''   
                                          client.sendImageWithURL(to, img)
                                          client.sendMessage(to,res)
                            elif cmd.startswith("snapshot"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                url = 'https://m.otosia.com/snapshot/'
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                lists = soup.findAll('div',{'class':'deskrip-artikel'})
                                if len(cond) == 1:
                                      ret_ = "╭───「 hasil pencarian」"
                                      num = 0
                                      for d in lists:
                                          num += 1
                                          ret_ += "\n├ {}. {}".format(str(num), str(d.find('a').text).replace('\n','').replace('  ',''))
                                      ret_ += "\n╰───「 By : Hk Bot 」"      
                                      client.sendMessage(to, ret_)
                                if len(cond) == 2:
                                      num = int(cond[1])
                                      if num <= len(lists):
                                          bur = lists[num - 1]
                                          l = 'https://m.otosia.com'+bur.find('a')['href']
                                          req = requests.get(l)
                                          soup = BeautifulSoup(req.text, 'lxml')
                                          lists = soup.findAll('p')
                                          img = soup.findAll('img')[7].get('src')
                                          datatext = []
                                          res = ''
                                          for i in lists:
                                              datatext.append(i)
                                          for i in datatext:
                                              res += soup.find('h3').text
                                              res += '\n'+i.text
                                          res += ''   
                                          client.sendImageWithURL(to, img)
                                          client.sendMessage(to,res)
#=========================================================================================================================================================================#
#===========================SCRAPE ALQURAN==============================================================#
#=========================================================================================================================================================================#
                            elif cmd == "listalquran":
                                    r = requests.get("http://api.alquran.cloud/quran/en.asad")
                                    data = r.text
                                    data = json.loads(data)
                                    no = 0
                                    ret_ = "Surah Alquran\n"
                                    for xio in data["data"]["surahs"]:
                                        no += 1
                                        ret_ += "\n{}.{}".format(str(no),str(xio["englishName"]))
                                    ret_ += "\n\nKetik Alquran no|no untuk /1 surah\n\nKetik Alqurans no|no|0 untuk /10 surah\n\nKetik Al-qur'an no untuk semua surah\n\nKetik Surah no untuk mendengarkan"   
                                    client.sendMessage(msg.to, str(ret_))
                                                                                
                            elif cmd.startswith("tafsirquran "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("https://tafsirq.com/topik/{}".format(str(search)))
                                    soup = BeautifulSoup(r.content, 'lxml')
                                    data = soup.findAll('div', attrs={'class':'col-md-12'})
                                    tit = soup.findAll('h1')[0].text
                                    if len(cond) == 1:
                                        num = 0
                                        ret_ = tit+"\n"
                                        for get in data:
                                            num += 1
                                            tip = get.find('span').text
                                            isi = tip+': '+get.find('a').text
                                            link = get.find('a')['href']
                                            ret_ += "\n {}. {}".format(str(num), str(isi))
                                        ret_ += "\n Total {} Result".format(str(len(data)))
                                        ret_ += "\n\n Next Tafsirquran "+query+"|nomor"
                                        #sendTextTemplate(to, ret_)
                                        client.sendMessage(to, str(ret_))
                                    elif len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(data):
                                            get = data[num - 1]
                                            with requests.session() as s:
                                                s.headers['user-agent'] = random.choice(settings["userAgent"])
                                                r = s.get(get.find('a')['href'])
                                                soup = BeautifulSoup(r.content, 'lxml')
                                                data = soup.findAll('div', attrs={'class':'panel-body'})[0]
                                                try:
                                                    ret = get.find('a').text+"\n"
                                                    ret += data.findAll('p')[0].text
                                                    ret += "\n\n "+data.findAll('p')[1].text
                                                    #sendTextTemplate(to, ret)
                                                    client.sendMessage(to, str(ret))
                                                except:
                                                    #sendTextTemplate(to, "Gagal mengambil data")
                                                    client.sendMessage(to, "Gagal mengambil data.")
                                                    
                            elif cmd.startswith("alquran "):
                                    sep = msg.text.split(" ")
                                    query = msg.text.replace(sep[0] + " ","")
                                    cond = query.split("|")
                                    search = str(cond[0])
                                    r = requests.get("http://api.alquran.cloud/surah/{}/ar.alafasy".format(urllib.parse.quote(search)))
                                    data = r.text
                                    data = json.loads(data)
                                    if len(cond) == 1:
                                        no = 0
                                        ret_ = "Quran Surah {}/{}\nSurah Ke-{}\nJumlah surah {}".format(str(data["data"]["englishName"]),str(data["data"]["name"]),str(data["data"]["number"]),str(data["data"]["numberOfAyahs"]))
                                        client.sendMessage(msg.to, str(ret_))
                                    elif len(cond) == 2:
                                        try:                                          
                                            num = int(cond[1])
                                            if num <= len(data["data"]["ayahs"]):
                                                quran = data["data"]["ayahs"][num - 1]
                                                #if quran != []:
                                                   #for txt in quran:
                                                #hasil = " Sedang dicarikan \n"
                                                hasil = "{}".format(quran["text"])
                                                client.sendMessage(to, str(hasil))
                                                client.sendAudioWithURL(to, str(quran["audio"]))
                                        except Exception as error:
                                            print(error)  
                                            
                            elif cmd.startswith("alqurans "):
                                try:
                                    sep = text.split(" ")
                                    query = text.replace(sep[0] + " ","")
                                    cond = query.split("|")
                                    search = str(cond[0]).replace(" ","")
                                    cond1 = query.split("|")
                                    search1 = str(cond1[1]).replace(" ","")
                                    r = requests.get("http://api.alquran.cloud/surah/{}?offset={}&limit=10".format(str(search),int(search1)))
                                    data = json.loads(r.text)
                                    if len(cond) == 1:
                                        no = 0
                                        ret_ = "Quran Surah {}/{}\nSurah Ke-{}\nJumlah surah {}".format(str(data["data"]["englishName"]),str(data["data"]["name"]),str(data["data"]["number"]),str(data["data"]["numberOfAyahs"]))
                                        client.sendMessage(msg.to, str(ret_))
                                    elif len(cond) == 2:
                                        no = 0
                                        ret_ = "Quran Surah {}/{}\nSurah Ke-{}\nJumlah surah {}".format(str(data["data"]["englishName"]),str(data["data"]["name"]),str(data["data"]["number"]),str(data["data"]["numberOfAyahs"]))
                                        client.sendReplyMessage(msg_id,msg.to, str(ret_))
                                    elif len(cond) == 3:
                                          hsl = ""
                                          for txt2 in data["data"]["ayahs"]:
                                              hsl += "\n{}.{}".format(str(txt2["number"]),str(txt2["text"]))
                                          client.sendMessage(msg.to, hsl)
                                except Exception as error:
                                    client.sendMessage(msg.to, str(error))
                                    
                            elif cmd.startswith("al-qur'an "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                web = requests.get("http://api.alquran.cloud/surah/{}".format(txt))
                                data = web.json()
                                result = "~[~{}~]~".format(data["data"]["englishName"])
                                quran = data["data"]
                                result += "\n~ Surah ke {} ~".format(quran["number"])
                                result += "\n~ Nama Surah ~ {} ~".format(quran["name"])
                                result += "\n~ {} Ayat ~".format(quran["numberOfAyahs"])
                                result += "\n~ {} ~".format(quran["name"])
                                result += "\n~ Ayat Sajadah = {} ~".format(quran["ayahs"][0]["sajda"])
                                result += "\n==================\n"
                                no = 0
                                for ayat in data["data"]["ayahs"]:
                                    no += 1
                                    result += "\n{}. {}".format(no,ayat['text'])
                                k = len(result)//10000
                                for aa in range(k+1):
                                    client.sendMessage(to,'{}'.format(result[aa*10000 : (aa+1)*10000]))   
                                    
                            elif cmd.startswith("surah "):
                                  sep = text.split(" ")
                                  query = int(text.replace(sep[0] + " ",""))
                                  if len(str(query)) == 1: 
                                      surah = "https://download.quranicaudio.com/quran/huthayfi/00{}.mp3".format(query)
                                      client.sendAudioWithURL(to, surah)
                                  elif len(str(query)) == 2: 
                                      surah = "https://download.quranicaudio.com/quran/huthayfi/0{}.mp3".format(query)
                                      client.sendAudioWithURL(to, surah)
                                  else: 
                                      surah = "https://download.quranicaudio.com/quran/huthayfi/{}.mp3".format(query)
                                      client.sendAudioWithURL(to, surah) 
                            elif cmd.startswith("iqra1 "):
                                  sep = text.split(" ")
                                  query = int(text.replace(sep[0] + " ",""))
                                  url="https://www.slideshare.net/mobile/gaulBanget/buku-iqra-1-a4"
                                  r=requests.get(url).text
                                  b=BeautifulSoup(r,"lxml")
                                  c=[c.get("data-normal") for c in b.findAll("img",{"class":"slide_image"})]
                                  time.sleep(0.7)
                                  sendIL(to,c[query-1])
                                  
                            elif cmd.startswith("iqra2 "):
                                      sep = text.split(" ")
                                      query = int(text.replace(sep[0] + " ",""))
                                      url="https://www.slideshare.net/mobile/rizalfuadi/iqra-2"
                                      r=requests.get(url).text
                                      b=BeautifulSoup(r,"lxml")
                                      img=[c.get("data-normal") for c in b.findAll("img",{"class":"slide_image"})]
                                      time.sleep(0.7)
                                      sendIL(to,img[query-1])   
                                          
                            elif cmd.startswith("iqra3 "):
                                      sep = text.split(" ")
                                      query = int(text.replace(sep[0] + " ",""))
                                      url="https://www.slideshare.net/mobile/rizalfuadi/iqra-3"
                                      r=requests.get(url).text
                                      b=BeautifulSoup(r,"lxml")
                                      img=[c.get("data-normal") for c in b.findAll("img",{"class":"slide_image"})]
                                      time.sleep(0.7)
                                      sendIL(to,img[query-1])   
                                          
                            elif cmd.startswith("iqra4 "):
                                      sep = text.split(" ")
                                      query = int(text.replace(sep[0] + " ",""))
                                      url="https://www.slideshare.net/mobile/rizalfuadi/iqra-4"
                                      r=requests.get(url).text
                                      b=BeautifulSoup(r,"lxml")
                                      img=[c.get("data-normal") for c in b.findAll("img",{"class":"slide_image"})]
                                      time.sleep(0.7)
                                      sendIL(to,img[query-1])   
                                          
                            elif cmd.startswith("iqra5 "):
                                      sep = text.split(" ")
                                      query = int(text.replace(sep[0] + " ",""))
                                      url="https://www.slideshare.net/mobile/rizalfuadi/iqra-5"
                                      r=requests.get(url).text
                                      b=BeautifulSoup(r,"lxml")
                                      img=[c.get("data-normal") for c in b.findAll("img",{"class":"slide_image"})]
                                      time.sleep(0.7)
                                      sendIL(to,img[query-1])   
                                          
                            elif cmd.startswith("iqra6 "):
                                      sep = text.split(" ")
                                      query = int(text.replace(sep[0] + " ",""))
                                      url="https://www.slideshare.net/mobile/rizalfuadi/iqra-6"
                                      r=requests.get(url).text
                                      b=BeautifulSoup(r,"lxml")
                                      img=[c.get("data-normal") for c in b.findAll("img",{"class":"slide_image"})]
                                      time.sleep(0.7)
                                      sendIL(to,img[query-1])   
                                          
                            elif cmd == "listdoapendek":
                                 client.sendMessage(to,listdoapendek)
                            elif cmd.startswith("doa "):
                                sep = text.split(" ")
                                query = int(text.replace(sep[0] + " ",""))
                                r=requests.get("https://archive.org/details/MurottalDoaSehariHari").text
                                b=BeautifulSoup(r,"lxml")
                                link =[l.findAll("link")[1].get("href") for l in b.findAll("div",{"itemprop":"hasPart"})]
                                judul =[l.findAll("meta")[0].get("content").replace("Doa Hisnul Muslim -","") for l in b.findAll("div",{"itemprop":"hasPart"})]
                                sendFooter(to,judul[query-1])
                                sendAL(to,link[query-1])                                
                            elif cmd == "ayatkursi":
                                r=requests.get("https://islamdownload.net/124375-download-mp3-ayat-kursi-bacaan-dan-terjemahan.html")
                                b=BeautifulSoup(r.text,"lxml")
                                a=[l.find("a")["href"] for l in b.findAll("div",{"align":"left"})]
                                num = random.randint(0,31)
                                client.sendAudioWithURL(to,a[num])
                            elif cmd == "yasin":
                              r=requests.get("https://islamiques.net/download-mp3-surat-yasin-full/")
                              b=BeautifulSoup(r.text,"lxml")
                              a=b.findAll("audio",{"class":"wp-audio-shortcode"})
                              audio=[i.find("a").text for i in a]
                              num = random.randint(0,20)
                              Hasil = audio[num]
                              sendAL(to,Hasil)
                              
                            elif cmd == "listalkitab":
                                client.sendMessage(msg.to, listalkitab)
                            elif cmd.startswith("alkitab "):
                                proses = text.split(" ")
                                keyword = text.replace(proses[0] + " ","")
                                count = keyword.split("|")
                                ayat = int(count[0])
                                pasal = int(count[1])
                                url = "https://www.wordproject.org/bibles/id_tb/0{}/{}.htm#0".format(ayat,pasal)  
                                req = requests.get(url)
                                soup = BeautifulSoup(req.text, 'lxml')
                                #ls = soup.find("h2").text +"Pasal " + pasal
                                ls = soup.findAll('p')[2].get_text()
                                audi = soup.find('a',{"class":"sm2-inline-button download sm2-exclude"})
                                client.sendMessage(msg.to,ls)
                                client.sendAudioWithURL(to,audi.get("href"))
                                
                            elif cmd.startswith("bible "):
                                proses = text.split(" ")
                                keyword = text.replace(proses[0] + " ","")
                                count = keyword.split("|")
                                search = str(count[0])
                                r = requests.get('https://www.bible.com/id/search/bible?q='+search)
                                dataz = BeautifulSoup(r.text,"lxml")
                                dataa = []
                                for wildan in dataz.findAll("li", {"class": "reference"}):
                                  ayat=wildan.a.text
                                  link="https://bible.com"+wildan.a.get("href")
                                  isi=wildan.p.text.replace("\n","")
                                  dataa.append({"ayat":ayat,"isi": isi, "link":link})
                                if len(count) == 1:
                                    no = 0
                                    hasil = "「 Ayat bible 」\n"
                                    for aa in dataa:
                                        no += 1
                                        hasil += "\n" + str(no) + ". "+ str(aa["ayat"])
                                    hasil += " "
                                    hasil += "\n\n Next Bible "+search+"|nomor"    
                                    #hasil += "\n\n Next Memes Kata|Kata|Nomor"    
                                    client.sendMessage(msg.to,hasil)
                                if len(count) == 2:
                                      num = int(count[1])
                                      if num <= len(dataa):
                                          bur = dataa[num - 1]
                                          hasil = "{}".format(str(bur["ayat"]))
                                          hasil += "\n{}".format(str(bur["isi"]))
                                          client.sendMessage(msg.to,hasil)
                                          
                            elif cmd == "bibles":
                              r = requests.get('https://www.bible.com/id/verse-of-the-day')
                              dataz = BeautifulSoup(r.text,"lxml")
                              image = dataz.find("meta",{"property":"og:image"}).get("content")
                              isi = dataz.find("meta",{"name":"description"}).get("content")[:-1]
                              link=dataz.find("meta", {"property":"og:url"}).get("content")
                              a=requests.get(link)
                              b=BeautifulSoup(a.text,"lxml")
                              ayat = b.title.text.split(" - ")[1].split(" | ")[0]
                              client.sendImageWithURL(msg.to,image)
                              client.sendMessage(to,""+ayat+"\n"+isi)
#=========================================================================================================================================================================#
                            elif cmd.startswith("listmeme"):
                                proses = text.split(" ")
                                keyword = text.replace(proses[0] + " ","")
                                count = keyword.split("|")
                                #search = str(count[0])
                                r = requests.get("http://api.imgflip.com/get_memes")
                                data = json.loads(r.text)
                                datas = data["data"]["memes"]
                                if len(count) == 1:
                                    no = 0
                                    hasil = "「 Daftar Meme Image 」\n"
                                    for aa in datas:
                                        no += 1
                                        hasil += "\n" + str(no) + ". "+ str(aa["name"])
                                    hasil += " "
                                    hasil += "\n\n Next Listmeme|nomor"    
                                    hasil += "\n\n Next Memes Kata|Kata|Nomor"    
                                    client.sendMessage(msg.to,hasil)
                                if len(count) == 2:
                                      num = int(count[1])
                                      if num <= len(datas):
                                          bur = datas[num - 1]
                                          hasil = "{}".format(str(bur["name"]))
                                        #sendTextTemplate(to, hasil)
                                          client.sendMessage(msg.to,hasil)
                                          client.sendImageWithURL(msg.to,bur["url"])
                                        
                            elif cmd.startswith("memes "):
                                proses = text.split(" ")
                                keyword = text.replace(proses[0]+" ","")
                                query = keyword.split("|")
                                atas = query[0]
                                bawah = query[1]
                                r = requests.get("https://api.imgflip.com/get_memes")
                                data = json.loads(r.text)
                                try:
                                    num = int(query[2])
                                    namamem = data["data"]["memes"][num - 1]
                                    meme = int(namamem["id"])
                                    api = pyimgflip.Imgflip(username='andyihsan', password='ihsan848')
                                    result = api.caption_image(meme, atas,bawah)
                                    #sendMention(msg.to,"@!\nfoto sedang diproses...",[sender])
                                    client.sendImageWithURL(msg.to,result["url"])
                                except Exception as e:
                                    client.sendMessage(msg.to," "+str(e))
                                    
                            elif cmd.startswith("meme "):
                                        sep = text.split(" ")    
                                        data = text.replace(sep[0] + " ","")
                                        meme = data.split('|')
                                        meme = meme[0].replace(' ','_')
                                        atas = data.split('|')
                                        atas = atas[1].replace(' ','_')
                                        bawah = data.split('|')
                                        bawah = bawah[2].replace(' ','_')
                                        memes = 'https://memegen.link/'+meme+'/'+atas+'/'+bawah+'.jpg'
                                        client.sendImageWithURL(msg.to,memes)
                                        
#api moe
                            elif cmd.startswith("komik"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","").replace(' ','+')
                                cond = query.split("|")
                                r=requests.get("https://mangashiro.org/search/%s/feed/rss2" % cond[0])
                                s=BeautifulSoup(r.text,"lxml")
                                link = s.findAll('guid')
                                data = []
                                for i in link:
                                    l = i.text
                                    data.append({'link':l})
                                   # print(data)
                                if len(cond) == 1:
                                    res = '╭──「 Komik Sub indo 」'
                                    no = 0
                                    for i in data:
                                        no += 1
                                        res += '\n│ {}.{}'.format(str(no), str(i['link']))
                                    res += "\n│ \n│  Bacakomik|nomor"    
                                    res += '\n╰───「 By : Hk Bot 」'
                                    client.sendMessage(to, str(res))
                                if len(cond) == 2:
                                      no = int(cond[1])
                                      if no <= len(data):
                                          get = data[no - 1]
                                          url1 = str(get['link'])
                                          reg1 = requests.get(url1)
                                          soup1 =BeautifulSoup(reg1.text, "lxml")
                                          datav = []
                                          ret_ = "╭───「 hasil pencarian」"
                                          nim = 0
                                          link = soup1.findAll('span',{"class":"lchx"})
                                          for a in link:
                                              title = a.text
                                              link = a.find("a")["href"]
                                              datav.append({'title':title,'links':link})
                                          komikanime = {"result":datav}
                                          f = codecs.open("tmp/komik.json","w","utf-8")
                                          json.dump(komikanime, f, sort_keys=True, indent=4, ensure_ascii=False)
                                          for isu in komikanime['result']:
                                              nim += 1
                                              ret_ += '\n├ {}. {}'.format(str(nim),str(isu['title']))
                                          k = len(ret_)//10000
                                          for aa in range(k+1):
                                            client.sendMessage(to,"{}".format(ret_[aa*10000 : (aa+1)*10000])+'\n╰───「 By : Hk Bot 」')
                                          #ret_ += '\n╰───「 By : Hk Bot 」'
                                          #ret_ += "\n\n Next Baca "+cond[0]+"|nomor"    
                                          #client.sendMessage(to, ret_)
                                          
                            elif cmd.startswith('bacakomik '):
                              a = text.split(" ")
                              num = a[1]
                              numb = int(num) - 1
                              f = codecs.open("tmp/komik.json","r","utf-8")
                              komikanime = json.load(f)
                              spec = komikanime['result'][numb]['links']
                              reg = requests.get(spec)
                              soup =BeautifulSoup(reg.text, "lxml")
                              link = soup.findAll('img')#,{"class":"lchx"})
                              for a in link:
                                if "https://3.bp.blogspot.com/-vms00H77Dbo/XQMnWofF5vI/AAAAAAADPI4/KwMkbc0HN2IzieMnjU76wcysq_00oUv_wCLcBGAs/s1600/slot%2Biklan%2B728x90.png" not in a.get("src"):
                                  if "https://3.bp.blogspot.com/-vms00H77Dbo/XQMnWofF5vI/AAAAAAADPI4/KwMkbc0HN2IzieMnjU76wcysq_00oUv_wCLcBGAs/s1600/slot%2Biklan%2B728x90.png" not in a.get("src"):
                                    if "https://1.bp.blogspot.com/-Snz6SeNgG7o/XMRTRtU_9BI/AAAAAAACYV4/_0W6XrvKU0UFJW4Lfmx6WJAYU_3A50K-ACLcBGAs/s1600/banner-mainbet88.gif" not in a.get("src"):
                                      if "https://i2.wp.com/mangashiro.org/wp-content/uploads/2019/02/mahadewa.gif" not in a.get("src"):
                                        if "https://i0.wp.com/lh3.googleusercontent.com/-lI4_R_9aPd0/XUENJQZ9GtI/AAAAAAAEV18/X1gIFg-ct6M21GsxOj1Oxsx4IxBWzG4WQCLcBGAs/s1600/z100.png" not in a.get("src"):
                                          if "https://2.bp.blogspot.com/-Cfa5vctMxfs/XUVBnW5fW4I/AAAAAAAEZwk/WdWAGdRXrRcFHQpbqsdy1KYYNTWXpRFdgCLcBGAs/s1600/1.gif" not in a.get("src"):
                                            if "https://4.bp.blogspot.com/-n-RT-t4XnqM/XUVBnFm8jkI/AAAAAAAEZwg/SPrXrIVrwRUGSQ_yWwh-EgfHKdfIBzvdgCLcBGAs/s1600/2.gif" not in a.get("src"):
                                              if "https://3.bp.blogspot.com/-ZZSacDHLWlM/VhvlKTMjbLI/AAAAAAAAF2M/UDzU4rrvcaI/s1600/btn_close.gif" not in a.get("src"):
                                                if "https://1.bp.blogspot.com/-2P4dQHLESrI/XUUE-Q3RkDI/AAAAAAAEYkA/YpVZPwtub0oPK56Z2fwybkEHzN1s8bALQCLcBGAs/s1600/100x450-min.gi" not in a.get("src"):
                                                  if "https://i3.wp.com/mangashiro.org/wp-content/uploads/2019/08/mangashiro-org.png" not in a.get("src"):
                                                    time.sleep(0.7)
                                                    sendIL(to,a.get("src"))
                              with open("tmp/komik.json","w") as error:
                                  error.write("{}")
    
                            elif cmd.startswith("hentai "):
                                proses = text.split(" ")
                                keyword = text.replace(proses[0]+" ","")
                                count = keyword.split("|")
                                kata = str(count[0])
                                r = requests.get("http://wa-one.herokuapp.com/nhentai?q={}".format(str(kata)))
                                data = json.loads(r.text)
                                if len(count) == 1:
                                    no = 0
                                    hasil = "「 Daftar hentai 」\n"
                                    for aa in data["result"]:
                                        no += 1
                                        hasil += "\n" + str(no) + ". "+ str(aa["title"])+"\n"
                                    hasil += "\nNext Hentai "+kata+"|nomor"
                                    client.sendMessage(msg.to,hasil)
                                if len(count) == 2:
                                    try:
                                        num = int(count[1])
                                        aa = data["result"][num - 1]
                                        bb = str(aa["url"])
                                        c = requests.get("http://wa-one.herokuapp.com/readnhentai?url={}".format(str(bb)))
                                        data1 = json.loads(c.text)
                                        if data1["result"] != []:
                                           for c1 in data1["result"]:
                                               #client.sendMessage(msg.to, c1)
                                                client.sendImageWithURL(msg.to, c1)
                                    except Exception as e:
                                        client.sendMessage(msg.to," "+str(e))
                                                                                                              
                            elif cmd.startswith("webtoon"):
                                proses = text.split(" ")
                                keyword = text.replace(proses[0]+" ","")
                                count = keyword.split("|")
                                hariini=datetime.now().strftime("%A").upper()
                                r = requests.get("https://m.webtoons.com/id/dailySchedule?webtoon-platform-redirect=true")
                                b=BeautifulSoup(r.text,"lxml")
                                c=b.find("div",class_="daily_section _list_"+hariini)
                                data = []
                                for webtun in c.findAll("li"):
                                  image = webtun.img.get("src").replace("webtoo","swebtoo").split("?")[0]
                                  info = [dan.text for dan in webtun.findAll("p")]
                                  judul = info[1]
                                  link = webtun.a.get("href")
                                  data.append({"image":image,"judul":judul,"link":link})
                                if len(count) == 1:
                                    no = 0
                                    hasil = "「 Daftar webtoon 」\n"
                                    for aa in data:
                                        no += 1
                                        hasil += "\n" + str(no) + ". "+ str(aa["judul"])
                                    hasil += "\nNext Bacawebtoon|nomor"
                                    client.sendMessage(msg.to,hasil)
                                if len(count) == 2:
                                      no = int(count[1])
                                      if no <= len(data):
                                          get = data[no - 1]
                                          url1 = str(get['link'])
                                          r1=requests.get(url1)
                                          webtoon=BeautifulSoup(r1.text,"lxml")
                                          infox=webtoon.find("ul",{"id":"_listUl"})
                                          titlee="Jumlah episode"
                                          nom = 0
                                          webto = []
                                          for ep in infox.findAll("li"):
                                            tit = ep.img.get("alt")
                                            linkk=ep.a.get("href")
                                            webto.append({"episode":tit,"link":linkk})
                                            komikanime = {"result":webto}
                                            f = codecs.open("tmp/komik.json","w","utf-8")
                                            json.dump(komikanime, f, sort_keys=True, indent=4, ensure_ascii=False)
                                          for epis in komikanime["result"]:
                                            nom += 1
                                            titlee+="\n" + str(nom) + ". "+epis["episode"]
                                          client.sendMessage(msg.to,titlee)
                            elif cmd.startswith('bacawebtoon '):
                              a = text.split(" ")
                              num = a[1]
                              numb = int(num) - 1
                              f = codecs.open("tmp/komik.json","r","utf-8")
                              komikanime = json.load(f)
                              spec = komikanime['result'][numb]['link']
                              reg = requests.get(spec)
                              soup =BeautifulSoup(reg.text, "lxml")
                              ga=soup.find("div",{"id":"_imageList"})
                              #titlee=webtun.find("meta",{"property":"og:title"}).get("content")
                              for comic in ga.findAll("img"):
                                  image=comic.get("data-url").replace("webtoo","swebtoo")
                                  time.sleep(0.7)
                                  sendIL(to,image)
                              with open("tmp/komik.json","w") as error:
                                  error.write("{}")
                                          
                            elif cmd.startswith("likepost "):
                                  if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = [mention["M"] for mention in mentionees]
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    a = client.getContact(lists[0]).mid
                                    s = client.getContact(lists[0]).displayName
                                    hasil = client.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        client.likePost(str(sender), str(result), likeType=random.choice(typel))
                                        client.createComment(str(sender), str(result), settings["comment"])
                                    client.sendMessage(receiver, 'Done Like+Comment '+str(len(st))+' Post From ' + str(s))
                                                                      
                            elif cmd.startswith("unlikepost "):
                                  if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = [mention["M"] for mention in mentionees]
                                    a = client.getContact(lists[0]).mid
                                    s = client.getContact(lists[0]).displayName
                                    hasil = client.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        client.unlikePost(str(sender), str(result))
                                        client.deleteComment(str(sender), str(result), settings["comment"])
                                    client.sendMessage(receiver, 'Done Unlike+Comment '+str(len(st))+' Post From ' + str(s))
                                                                      
                            elif cmd.startswith("!exec"):
                                  sep = text.split("\n")
                                  hayden = text.replace(sep[0] + "\n","")
                                  try:
                                      exec(hayden)
                                  except Exception as e:
                                      client.sendMessage(receiver, str(e))
                    
                            elif cmd.startswith("!json"):
                                    try:                                     
                                        data = text.replace("!json ","")
                                        urllib.request.urlretrieve(data,'tmp/hasil.txt')
                                        with open('tmp/hasil.txt',"r") as er:
                                            error = er.read()
                                            hasil = "{}".format(error)
                                        k = len(hasil)//10000
                                        for aa in range(k+1):
                                            client.sendMessage(to,"{}".format(hasil[aa*10000 : (aa+1)*10000]))
                                        with open('tmp/hasil.txt', 'w') as er:
                                            er.write("")
                                    except Exception as e:
                                    	client.sendMessage(to, str(e))
                                                         
                            elif cmd == '!ls':
                                process = os.popen('ls')
                                a = process.read()
                                client.sendMessage(to, "{}".format(a))
                                process.close()
                                
                            elif cmd.startswith("sendfile "):
                                  sep = text.split(" ")
                                  query = text.replace(sep[0] + " ","")
                                  client.sendFile(to, query)
                                  
                            elif cmd == 'screen -ls':
                                  process = os.popen('screen -list')
                                  a = process.read()
                                  client.sendMessage(to, "{}".format(a))
                                  process.close()
                        
                            elif cmd.startswith("filejson"):
                                    try:                                     
                                        data = removeCmd("filejson", text)
                                        urllib.request.urlretrieve(data,'json.txt')
                                        client.sendFile(to,"json.txt")
                                        with open('json.txt', 'w') as er:
                                            er.write("")
                                    except Exception as e:
                                    	client.sendMessage(to, str(e))                                  
                                      
                            elif cmd.startswith("filemp4"):
                                    try:                                     
                                        link = removeCmd("filemp4", text)
                                        subprocess.getoutput('youtube-dl --format mp4 --output haku.mp4 {}'.format(link))
                                        vids = "haku.mp4"
                                        time.sleep(2)
                                        client.sendFile(to, vids)#, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+client.getContact(clientMid).pictureStatus, 'AGENT_NAME': '', 'AGENT_LINK': 'http://line.me/ti/p/~khiexyz'})
                                        os.remove("haku.mp4")
                                    except Exception as e:
                                    	client.sendMessage(to, str(e))
                                      
                            elif cmd.startswith("filemp3"):
                                    try:                                     
                                        link = removeCmd("filemp3", text)
                                        subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output haku.mp3 {}'.format(link),)
                                        auds = "haku.mp3"
                                        time.sleep(2)
                                        client.sendFile(to, auds)
                                        os.remove("haku.mp3")
                                    except Exception as e:
                                    	client.sendMessage(to, str(e))
                                      
                            elif cmd.startswith("en "):
                                  sep = text.split(" ")
                                  query = text.replace(sep[0] + " ","")
                                  B64e(to, query)
                            elif cmd.startswith("de "):
                                  sep = text.split(" ")
                                  query = text.replace(sep[0] + " ","")
                                  B64d(to, query)
                            
#=========================================================================================================#                                
                            elif cmd == "linkchat":
                              	client.reissueUserTicket()
                              	JEMBOT = client.profile.displayName + "\nMy id Line: http://line.me/ti/p/" + client.getUserTicket().id
                              	client.sendMessage(msg.to,str(JEMBOT))
          
                            elif cmd.startswith("line "):
                                id = cmd.replace("line ","")
                                conn = client.findContactsByUserid(id)
                                if True:                                      
                                    client.sendMessage(to,"http://line.me/ti/p/~" + id)
                                    client.sendContact(to,conn.mid)
                              
                            elif cmd.startswith("chatline "):
                                sep = text.split(" ")
                                sam = text.replace(sep[0] + " ","")
                                sam1 = sam.split("|")
                                kata = str(sam1[0])
                                kata1 = str(sam1[1])
                                id = kata
                                conn = client.findContactsByUserid(id)
                                tar = conn.mid
                                orang = client.getContact(tar)
                                midds = "{}".format(orang.mid)
                                ora = client.getContact(sender)
                                nam = ora.displayName
                                client.sendMessage(midds, "Pesannya : "+kata1+"\nDari : "+nam)
                                client.sendContact(midds, ora.mid)
                                client.sendMessage(msg.to,"Pesan sudah dikirimkan")
                              
                            elif cmd == "@bye":
                                    ginfo = client.getGroup(msg.to)
                                    try:
                                        client.leaveGroup(msg.to)
                                    except:  
                                        pass
                                    
                            elif cmd.startswith("linkimg "):
                                link = removeCmd("linkimg", text)
                                client.sendImageWithURL(to, link)#, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+client.getContact(clientMid).pictureStatus, 'AGENT_NAME': '', 'AGENT_LINK': 'http://line.me/ti/p/~khiexyz'})
            
                            elif cmd.startswith("linkmp3 "):
                                link = removeCmd("linkmp3", text)
                                client.sendAudioWithURL(to, link)#, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+client.getContact(clientMid).pictureStatus, 'AGENT_NAME': '', 'AGENT_LINK': 'http://line.me/ti/p/~khiexyz'})
                        
                            elif cmd.startswith("linkmp4 "):
                                link = removeCmd("linkmp4", text)
                                client.sendVideoWithURL(to, link)#, contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+client.getContact(clientMid).pictureStatus, 'AGENT_NAME': '', 'AGENT_LINK': 'http://line.me/ti/p/~khiexyz'})
                  
                            elif cmd.startswith("ytlinkmp3 "):
                                link = removeCmd("ytlinkmp3", text)
                                pafyaudio(to, '{}'.format(link))
            
                            elif cmd.startswith("ytlinkmp4 "):
                                link = removeCmd("ytlinkmp4", text)
                                pafyvideo(to, '{}'.format(link))
                    
                            elif cmd.startswith("sslink "):
                                link = removeCmd("sslink", text)
                                sendIL(to,"https://mini.s-shot.ru/1024x0/JPEG/1024/Z100/?{}".format(link))
                            
                            elif text.lower().startswith('chatowner '):
                                separate = msg.text.split(" ")
                                tex = msg.text.replace(separate[0]+" ","")
                                teman = client.getContact(sender)
                                nam = teman.displayName
                                namid = teman.mid
                                client.sendMessage("u8e663c64a145c778b2eef1284383f746","Pesan dari : "+nam+"\nPesannya : "+tex)
                                client.sendContact("u8e663c64a145c778b2eef1284383f746",namid)
                                client.sendMessage(msg.to,"pesan sudah dikirim ke owner kami")
                                
#=========================================================================================================#                                
#=========================================================================================================#                                
#===========================COMMAND COSTUM================================================================#                                
#=========================================================================================================#                                                                   
                            elif cmd.startswith("addrt "):
                                    sep = msg.text.split(" ")
                                    apl = msg.text.replace(sep[0] + " ","")
                                    no = msg.relatedMessageId
                                    chat2 = apl
                                    if to in drt["ROM"]:
                                      for a in drt["ROM"][to].items():
                                        if no in a[1]:
                                          settings["Message1"][str(chat2)]=linkfoto(ezgifapngmaker(a[1][no][0]))
                                          client.sendMessage(to,"Command %s created."%chat2)
                                          backupData()
                            elif cmd == "listrt":
                                    backupData()
                                    if settings["Message1"] == {}:
                                        client.sendMessage(to,"You don't have listrt")
                                    else:
                                        mc = ""
                                        jml = 1
                                        for listword in settings["Message1"]:
                                            mc += "\n"+str(jml)+". "+listword+""
                                            jml += 1
                                        client.sendMessage(to,"[ Listrt ]\n"+str(mc))
                            elif cmd.startswith("delrt "):
                                    sep = text.split(" ")
                                    xres = text.replace(sep[0] + " ","")
                                    tetx = text.replace(sep[0] + " ","")
                                    if xres in settings["Message1"]:
                                        del settings["Message1"][xres]                                        
                                        client.sendMessage(to,"Command %s has been removed."%tetx)
                                    else:
                                        client.sendMessage(to,"Command %s does not exist."%tetx)
                            elif cmd == 'delallrt':
                                settings["Message1"] = {}
                                client.sendMessage(to, "Listrt sudah bersih")
                                    
                            elif cmd.startswith("addsc "):
                                    sep = msg.text.split(" ")
                                    apl = msg.text.replace(sep[0] + " ","")
                                    sam = apl.split("|")
                                    chat1 = sam[0]
                                    chat2 = sam[1]
                                    apk = ""+chat1
                                    settings["Message"][apk] = chat2
                                    settings["msg"] = chat1
                                    anu = settings["msg"]+'.'
                                    client.sendMessage(to,"Command %s created."%chat1)
                                    settings["msg"] = {}
                                    backupData()
                            elif cmd == "listsc":
                                    backupData()
                                    if settings["Message"] == {}:
                                        client.sendMessage(to,"You don't have chat message")
                                    else:
                                        mc = ""
                                        jml = 1
                                        for listword in settings["Message"]:
                                            mc += "\n"+str(jml)+". "+listword+""
                                            jml += 1
                                        client.sendMessage(to,"[ List Text ]\n"+str(mc))
                            elif cmd.startswith("delsc "):
                                    sep = text.split(" ")
                                    xres = text.replace(sep[0] + " ","")
                                    tetx = text.replace(sep[0] + " ","")
                                    if xres in settings["Message"]:
                                        del settings["Message"][xres]                                        
                                        client.sendMessage(to,"Command %s has been removed."%tetx)
                                    else:
                                        client.sendMessage(to,"Command %s does not exist."%tetx)
                            elif cmd == 'delallsc':
                                settings["Message"] = {}
                                client.sendMessage(to, "Listrt sudah bersih")    
                            elif cmd.startswith("addtext "):
                                    sep = msg.text.split(" ")
                                    apl = msg.text.replace(sep[0] + " ","")
                                    sam = apl.split("|")
                                    chat1 = sam[0]
                                    chat2 = sam[1]
                                    apk = ""+chat1
                                    settings["Message2"][apk] = chat2
                                    client.sendMessage(to,"Command %s created."%chat1)
                                    backupData()
                            elif cmd == "listtext":
                                    backupData()
                                    if settings["Message2"] == {}:
                                        client.sendMessage(to,"You don't have chat message")
                                    else:
                                        mc = ""
                                        jml = 1
                                        for listword in settings["Message2"]:
                                            mc += "\n"+str(jml)+". "+listword+""
                                            jml += 1
                                        client.sendMessage(to,"[ List Text ]\n"+str(mc))
                            elif cmd.startswith("deltext "):
                                    sep = text.split(" ")
                                    xres = text.replace(sep[0] + " ","")
                                    tetx = text.replace(sep[0] + " ","")
                                    if xres in settings["Message2"]:
                                        del settings["Message2"][xres]                                        
                                        client.sendMessage(to,"Command %s has been removed."%tetx)
                                    else:
                                        client.sendMessage(to,"Command %s does not exist."%tetx)
                            elif cmd == 'delalltext':
                                settings["Message2"] = {}
                                client.sendMessage(to, "Listrt sudah bersih")                                        
                                
#=========================================================================================================#                                
#===========================COMMAND COSTUM================================================================#                                
#=========================================================================================================#                                
#=========================================================================================================#                                
#===========================COMMAND COSTUM================================================================#                                
#=========================================================================================================#    
#===========Settings========|====#
                            elif msg.text in ["Cekkey"]:
                                res = '╔══「 Bot Key 」'
                                res += '\n╠ Status : ' + bool_dict[settings['setKey']][1]
                                res += '\n╠ Key : ' + settings['keyCommand'].title()
                                res += '\n╠═════════════'
                                res += '\n╠ • Reskey'
                                res += '\n╠ • Cekkey'
                                res += '\n╠ • Setkey <on/off>'
                                res += '\n╠ • Setkey <key>'
                                res += '\n╚═「 ƬΣΛM HK BӨƬ 」'
                                client.sendReplyMessage(msg_id,to, str(res))
                            elif msg.text in ["Setkey off"]:
                                settings['setKey'] = False
                                client.sendReplyMessage(msg_id,to, "Key dimatikan")
                            elif msg.text in ["Setkey on"]:
                                settings['setKey'] = True
                                client.sendReplyMessage(msg_id,to, "Key dihidupkan")
                            elif cmd.startswith("setkey "):
                                  sep = text.split(" ")
                                  cos = text.replace(sep[0] + " ","")
                                  settings["keyCommand"] = cos#msg.text.replace("/setmidcontact ","")
                                  client.sendReplyMessage(msg_id,msg.to,"Berhasil menggati key\n「"+settings["keyCommand"]+"」")
                            elif msg.text in ["Reskey"]:
                                  settings["keyCommand"] = ""#msg.text.replace("/setmidcontact ","")
                                  client.sendReplyMessage(msg_id,msg.to,"Berhasil mereset key 「"+settings["keyCommand"]+"」")
                                                                      
                            elif cmd == "result":
                                    mE = client.getProfile()
                                    gT = client.getGroupIdsJoined()
                                    fT = client.getAllContactIds()
                                    ginv = client.getGroupIdsInvited()
                                    client.sendReplyMessage(msg_id,msg.to,"「"+mE.displayName+"」 \n\nGroup total : " + str(len(gT))+ "\nFriend total: " +str(len(fT))+ "\nPending Group: " + str(len(ginv)))   
                                    
#==============================================================================#https://www.smule.com/s/profile/performance/hayden_hk/sing?offset=1&size=25                  
#==============================================================================#
                            elif cmd.startswith("addmes "):
                                  sep = text.split(" ")
                                  name = text.replace(sep[0] + " ","")
                                  name = name.lower()
                                  if name not in pesans:
                                      settings["Addmessage"]["status"] = True
                                      settings["Addmessage"]["name"] = str(name.lower())
                                      pesans[str(name.lower())] = ""
                                      f = codecs.open("jsons/hayden/pesan.json","w","utf-8")
                                      json.dump(pesans, f, sort_keys=True, indent=4, ensure_ascii=False)
                            elif cmd.startswith("ganmes "):
                                  sep = text.split(" ")
                                  name = text.replace(sep[0] + " ","")
                                  name = name.lower()
                                  if name in pesans:
                                      settings["Addmessage"]["status"] = True
                                      settings["Addmessage"]["name"] = str(name.lower())
                                      pesans[str(name.lower())] = ""
                                      f = codecs.open("jsons/hayden/pesan.json","w","utf-8")
                                      json.dump(pesans, f, sort_keys=True, indent=4, ensure_ascii=False)
                            elif cmd.startswith("delmes "):
                                  sep = text.split(" ")
                                  name = text.replace(sep[0] + " ","")
                                  name = name.lower()
                                  if name in pesans:
                                     # client.delete(pesans[str(name.lower())])
                                      del pesans[str(name.lower())]
                                      f = codecs.open("jsons/hayden/pesan.json","w","utf-8")
                                      json.dump(pesans, f, sort_keys=True, indent=4, ensure_ascii=False)
                                      client.sendReplyMessage(msg_id,to, "Kata respon sudah dihapus")
                                  else:    
                                      client.sendReplyMessage(msg_id,to, "Kata respon Gagal dihapus")
                            elif cmd.startswith("listmes"):
                                   no = 0
                                   ret_ = "╭─────────────\n│Message List:\n├─────────────"
                                   for pesan in pesans:
                                       no += 1
                                       ret_ += "\n│" + str(no) + " " + pesan.title()
                                   ret_ += "\n├─────────────\n│Total message List: {}\n╰─────────────".format(str(len(pesans)))
                                   client.sendReplyMessage(msg_id,to, ret_)
                                
#=========== [ Add Video ] ============#                              
                            elif cmd.startswith("addvideo "):
                                  sep = text.split(" ")
                                  name = text.replace(sep[0] + " ","")
                                  name = name.lower()
                                  if name not in videos:
                                      settings["Addvideo"]["status"] = True
                                      settings["Addvideo"]["name"] = str(name.lower())
                                      videos[str(name.lower())] = ""
                                      f = codecs.open("jsons/hayden/video.json","w","utf-8")
                                      json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                      client.sendReplyMessage(msg_id,msg.to, "Silahkan kirim videonya...") 
                                  else:
                                      client.sendReplyMessage(msg_id,msg.to, "Video itu sudah dalam list") 
                                
                            elif cmd.startswith("ganvideo "):
                                  sep = text.split(" ")
                                  name = text.replace(sep[0] + " ","")
                                  name = name.lower()
                                  if name in videos:
                                      settings["Addvideo"]["status"] = True
                                      settings["Addvideo"]["name"] = str(name.lower())
                                      videos[str(name.lower())] = ""
                                      f = codecs.open("jsons/hayden/video.json","w","utf-8")
                                      json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                      client.sendReplyMessage(msg_id,msg.to, "Silahkan kirim pengganti videonya...") 
                                  else:
                                      client.sendReplyMessage(msg_id,msg.to, "Video gagal diganti") 
                                
                            elif cmd.startswith("delvideo "):
                                  sep = text.split(" ")
                                  name = text.replace(sep[0] + " ","")
                                  name = name.lower()
                                  if name in videos:
                                      client.deleteFile(videos[str(name.lower())])
                                      del videos[str(name.lower())]
                                      f = codecs.open("jsons/hayden/video.json","w","utf-8")
                                      json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                      client.sendReplyMessage(msg_id,msg.to, "Berhasil menghapus video {}".format( str(name.lower())))
                                  else:
                                      client.sendReplyMessage(msg_id,msg.to, "Video itu tidak ada dalam list") 
                                 
                            elif cmd.startswith("listvideo"):
                                   no = 0
                                   ret_ = "╭─────────────\n│Video List:\n├─────────────"
                                   for video in videos:
                                       no += 1
                                       ret_ += "\n│" + str(no) + " " + video.title()
                                   ret_ += "\n├─────────────\n│Total video List: {}\n╰─────────────".format(str(len(videos)))
                                   client.sendReplyMessage(msg_id,to, ret_)
#=========== [ Add Audio ] ============#                              
                            elif cmd.startswith("addaudio "):
                                  sep = text.split(" ")
                                  name = text.replace(sep[0] + " ","")
                                  name = name.lower()
                                  if name not in audios:
                                      settings["Addaudio"]["status"] = True
                                      settings["Addaudio"]["name"] = str(name.lower())
                                      audios[str(name.lower())] = ""
                                      f = codecs.open("jsons/hayden/audio.json","w","utf-8")
                                      json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                      client.sendReplyMessage(msg_id,msg.to, "Silahkan kirim audionya...") 
                                  else:
                                      client.sendReplyMessage(msg_id,msg.to, "Audio itu sudah dalam list") 
                                
                            elif cmd.startswith("ganaudio "):
                                  sep = text.split(" ")
                                  name = text.replace(sep[0] + " ","")
                                  name = name.lower()
                                  if name in audios:
                                      settings["Addaudio"]["status"] = True
                                      settings["Addaudio"]["name"] = str(name.lower())
                                      audios[str(name.lower())] = ""
                                      f = codecs.open("jsons/hayden/audio.json","w","utf-8")
                                      json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                      client.sendReplyMessage(msg_id,msg.to, "Silahkan kirim penggati audionya...") 
                                  else:
                                      client.sendReplyMessage(msg_id,msg.to, "Audio gagal diganti") 
                            elif cmd.startswith("delaudio "):
                                  sep = text.split(" ")
                                  name = text.replace(sep[0] + " ","")
                                  name = name.lower()
                                  if name in audios:
                                      client.deleteFile(audios[str(name.lower())])
                                      del audios[str(name.lower())]
                                      f = codecs.open("jsons/hayden/audio.json","w","utf-8")
                                      json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                      client.sendReplyMessage(msg_id,msg.to, "Berhasil menghapus audio {}".format( str(name.lower())))
                                  else:
                                      client.sendReplyMessage(msg_id,msg.to, "Audio itu tidak ada dalam list") 
                                 
                            elif cmd.startswith("listaudio"):
                                   no = 0
                                   ret_ = "╭─────────────\n│Audio List:\n├─────────────"
                                   for audio in audios:
                                       no += 1
                                       ret_ += "\n│" + str(no) + " " + audio.title()
                                   ret_ += "\n├─────────────\n│Total audio List: {}\n╰─────────────".format(str(len(audios)))
                                   client.sendReplyMessage(msg_id,to, ret_)
#=========== [ Add Image ] ============#                              
                            elif cmd.startswith("addfoto "):
                                  sep = text.split(" ")
                                  name = text.replace(sep[0] + " ","")
                                  name = name.lower()
                                  if name not in images:
                                      settings["Addimage"]["status"] = True
                                      settings["Addimage"]["name"] = str(name.lower())
                                      images[str(name.lower())] = ""
                                      f = codecs.open("jsons/hayden/image.json","w","utf-8")
                                      json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                      client.sendReplyMessage(msg_id,msg.to, "Silahkan kirim fotonya...") 
                                  else:
                                      client.sendReplyMessage(msg_id,msg.to, "Foto itu sudah dalam list") 
                                
                            elif cmd.startswith("ganfoto "):
                                  sep = text.split(" ")
                                  name = text.replace(sep[0] + " ","")
                                  name = name.lower()
                                  if name in images:
                                      settings["Addimage"]["status"] = True
                                      settings["Addimage"]["name"] = str(name.lower())
                                      images[str(name.lower())] = ""
                                      f = codecs.open("jsons/hayden/image.json","w","utf-8")
                                      json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                      client.sendReplyMessage(msg_id,msg.to, "Silahkan kirim pengganti fotonya...") 
                                  else:
                                      client.sendReplyMessage(msg_id,msg.to, "Foto gagal diganti") 
                                
                            elif cmd.startswith("delfoto "):
                                  sep = text.split(" ")
                                  name = text.replace(sep[0] + " ","")
                                  name = name.lower()
                                  if name in images:
                                      client.deleteFile(images[str(name.lower())])
                                      del images[str(name.lower())]
                                      f = codecs.open("jsons/hayden/image.json","w","utf-8")
                                      json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                      client.sendReplyMessage(msg_id,msg.to, "Berhasil menghapus foto {}".format( str(name.lower())))
                                  else:
                                      client.sendReplyMessage(msg_id,msg.to, "Foto itu tidak ada dalam list") 
                                 
                            elif cmd.startswith("listfoto"):
                                   no = 0
                                   ret_ = "╭─────────────\n│Foto List:\n├─────────────"
                                   for image in images:
                                       no += 1
                                       ret_ += "\n│" + str(no) + " " + image.title()
                                   ret_ += "\n├─────────────\n│Total Foto List: {}\n╰─────────────".format(str(len(images)))
                                   client.sendReplyMessage(msg_id,to, ret_)
#=========== [ Add Sticker ] ============#          
                            elif cmd == 'delallstik':
                                settings["sticker"] = {}
                                client.sendMessage(to, "Lstik sudah bersih")
                                
                            elif cmd.startswith('delstik '):
                                separate = msg.text.split(" ")
                                xres = msg.text.replace(separate[0]+" ","")
                                text = msg.text.replace(separate[0]+" ","") 
                                del settings["sticker"][xres]
                                client.sendMessage(msg.to," 「 Delete Sticker 」\nBerhasil menghapus %s" % str(text))

                            elif cmd.startswith('addstik '):
                                separate = msg.text.split(" ")
                                text = msg.text.replace(separate[0]+" ","")
                                settings["sticker"][text] = '%s' % text
                                settings["img"] = '%s' % text
                                settings["Taddsticker"] = True
                                client.sendMessage(msg.to, " 「 Sticker 」\nkirim stickernya..")
                            elif cmd == "lstik":
                                if settings["sticker"] == {}:
                                    client.sendMessage(msg.to, " 「 Sticker List 」\nNo Sticker")
                                else:
                                    num=1
                                    msgs="╭─────────────\n│Sticker List:\n├───────────── "
                                    for a in settings["sticker"]:
                                        msgs+="\n│%i. %s" % (num, a)
                                        num=(num+1)
                                    msgs+="\n├─────────────\n│Total Sticker List: %i\n╰─────────────" % len(settings["sticker"])
                                    client.sendMessage(msg.to, msgs)

                            elif cmd.startswith("addtikel "):
                                  sep = text.split(" ")
                                  name = text.replace(sep[0] + " ","")
                                  name = name.lower()
                                  if name not in stickers:
                                      settings["Addsticker"]["status"] = True
                                      settings["Addsticker"]["name"] = str(name.lower())
                                      stickers[str(name.lower())] = ""
                                      f = codecs.open("jsons/hayden/sticker.json","w","utf-8")
                                      json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                      client.sendReplyMessage(msg_id,msg.to, "Silahkan kirim stickernya...") 
                                  else:
                                      client.sendReplyMessage(msg_id,msg.to, "Sticker itu sudah dalam list") 
                            elif cmd.startswith("gantikel "):
                                  sep = text.split(" ")
                                  name = text.replace(sep[0] + " ","")
                                  name = name.lower()
                                  if name in stickers:
                                      settings["Addsticker"]["status"] = True
                                      settings["Addsticker"]["name"] = str(name.lower())
                                      stickers[str(name.lower())] = ""
                                      f = codecs.open("jsons/hayden/sticker.json","w","utf-8")
                                      json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                      client.sendReplyMessage(msg_id,msg.to, "Silahkan kirim pengganti stickernya...") 
                                  else:
                                      client.sendReplyMessage(msg_id,msg.to, "Sticker gagal diganti") 
                                
                            elif cmd.startswith("deltikel "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in stickers:
                                    del stickers[str(name.lower())]
                                    f = codecs.open("jsons/hayden/sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendReplyMessage(msg_id,msg.to, "Berhasil menghapus sticker {}".format( str(name.lower())))
                                else:
                                    client.sendReplyMessage(msg_id,msg.to, "Sticker itu tidak ada dalam list") 
                                                                  
                            elif cmd.startswith("listtikel"):
                                   no = 0
                                   ret_ = "╭─────────────\n│Sticker List:\n├─────────────"
                                   for sticker in stickers:
                                       no += 1
                                       ret_ += "\n│" + str(no) + " " + sticker.title()
                                   ret_ += "\n├─────────────\n│Total sticker List: {}\n╰─────────────".format(str(len(stickers)))
                                   client.sendReplyMessage(msg_id,to, ret_)
#=========== [ Setting Limit spam ] ============#                              
                            elif cmd.startswith("limittikel "):
                                  proses = text.split(" ")
                                  strnum = text.replace(proses[0] + " ","")
                                  num =  int(strnum)
                                  settings["limitTikel"] = num
                                  client.sendMessage(msg.to,"Spam sticker change {}".format(str(strnum)))
                            elif cmd.startswith("limitfoto "):
                                  proses = text.split(" ")
                                  strnum = text.replace(proses[0] + " ","")
                                  num =  int(strnum)
                                  settings["limitFoto"] = num
                                  client.sendMessage(msg.to,"Spam image change {}".format(str(strnum)))
                            elif cmd.startswith("limitvideo "):
                                  proses = text.split(" ")
                                  strnum = text.replace(proses[0] + " ","")
                                  num =  int(strnum)
                                  settings["limitVideo"] = num
                                  client.sendMessage(msg.to,"Spam video change {}".format(str(strnum)))
                            elif cmd.startswith("limitaudio "):
                                  proses = text.split(" ")
                                  strnum = text.replace(proses[0] + " ","")
                                  num =  int(strnum)
                                  settings["limitAudio"] = num
                                  client.sendMessage(msg.to,"Spam audio change {}".format(str(strnum)))
                            elif cmd.startswith("limittag "):
                                  proses = text.split(" ")
                                  strnum = text.replace(proses[0] + " ","")
                                  num =  int(strnum)
                                  settings["limitTag"] = num
                                  client.sendMessage(msg.to,"Spam tag change {}".format(str(strnum)))
                            elif cmd.startswith("limitgift "):
                                  proses = text.split(" ")
                                  strnum = text.replace(proses[0] + " ","")
                                  num =  int(strnum)
                                  settings["limitGift"] = num
                                  client.sendMessage(msg.to,"Spam gift change {}".format(str(strnum)))
                            elif cmd.startswith("limitchat "):
                                  proses = text.split(" ")
                                  strnum = text.replace(proses[0] + " ","")
                                  num =  int(strnum)
                                  settings["limitChat"] = num
                                  client.sendMessage(msg.to,"Spam chat change {}".format(str(strnum)))
                            elif cmd.startswith("limitcall "):
                                  proses = text.split(" ")
                                  strnum = text.replace(proses[0] + " ","")
                                  num =  int(strnum)
                                  settings["limitCall"] = num
                                  client.sendMessage(msg.to,"Spam call change {}".format(str(strnum)))
                            elif cmd.startswith("limitmessage "):
                                  proses = text.split(" ")
                                  strnum = text.replace(proses[0] + " ","")
                                  num =  int(strnum)
                                  settings["limitMessage"] = num
                                  client.sendMessage(msg.to,"Spam message change {}".format(str(strnum)))
#=========== [ Spam Perorangan By tag ] ============#                              
                            elif cmd.startswith("/call"):
                                  if msg.toType == 2:
                                      sep = text.replace("/call","")
                                      key = eval(msg.contentMetadata["MENTION"])
                                      target = key["MENTIONEES"][0]["M"]
                                      gege = sep.split(" ")
                                      num = int(gege[1])
                                      client.sendMessage(to, "Berhasil menyepam: "+client.getContact(target).displayName+"\nJumlah spam panggilan {}".format(str(num)))
                                      for var in range(0,num):
                                          hayden = client.getContact(target)
                                          members = [hayden.mid]
                                          client.acquireGroupCallRoute(to)
                                          client.inviteIntoGroupCall(to, contactIds=members)      
                            elif cmd.startswith("/gift"):
                                  if msg.toType == 2:
                                      sep = text.replace("/gift","")
                                      key = eval(msg.contentMetadata["MENTION"])
                                      target = key["MENTIONEES"][0]["M"]
                                      gege = sep.split(" ")
                                      num = int(gege[1])
                                      client.sendMessage(to, "Berhasil menyepam: "+client.getContact(target).displayName+"\nJumlah spam gift {}".format(str(num)))
                                      for var in range(0,num):
                                          hayden = client.getContact(target)
                                          members = [hayden.mid]
                                          client.sendMessage(target, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)    
                            elif cmd.startswith("/chat"):
                                  if msg.toType == 2:
                                      sep = text.replace("/chat","")
                                      key = eval(msg.contentMetadata["MENTION"])
                                      target = key["MENTIONEES"][0]["M"]
                                      gege = sep.split(" ")
                                      num = int(gege[1])
                                      client.sendMessage(to, "Berhasil menyepam: "+client.getContact(target).displayName+"\nJumlah spam chat {}".format(str(num)))
                                      for var in range(0,num):
                                          hayden = client.getContact(target)
                                          members = [hayden.mid]
                                          client.sendMessage(target, str(settings["spam1"]))  
                            elif cmd.startswith("/tikel"):
                                  if msg.toType == 2:
                                      sep = text.replace("/tikel","")
                                      key = eval(msg.contentMetadata["MENTION"])
                                      target = key["MENTIONEES"][0]["M"]
                                      gege = sep.split(" ")
                                      num = int(gege[1])
                                      client.sendMessage(to, "Berhasil menyepam: "+client.getContact(target).displayName+"\nJumlah spam sticker {}".format(str(num)))
                                      for var in range(0,num):
                                          hayden = client.getContact(target)
                                          members = [hayden.mid]
                                          sid = str(settings["Addstickerspam"]["sid"])
                                          spkg = str(settings["Addstickerspam"]["spkg"])
                                          client.sendSticker(target, spkg, sid)
                            elif cmd.startswith("/foto"):
                                  if msg.toType == 2:
                                      sep = text.replace("/foto","")
                                      key = eval(msg.contentMetadata["MENTION"])
                                      target = key["MENTIONEES"][0]["M"]
                                      gege = sep.split(" ")
                                      num = int(gege[1])
                                      client.sendMessage(to, "Berhasil menyepam: "+client.getContact(target).displayName+"\nJumlah spam image {}".format(str(num)))
                                      for var in range(0,num):
                                          hayden = client.getContact(target)
                                          members = [hayden.mid]
                                          gmb = str(settings["Addfotospam"]["img"])
                                          client.sendImage(target, gmb)
                            elif cmd.startswith("/tag"):
                                  if msg.toType == 2:
                                      sep = text.replace("/tag","")
                                      key = eval(msg.contentMetadata["MENTION"])
                                      target = key["MENTIONEES"][0]["M"]
                                      zx = ""
                                      zxc = " "
                                      zx2 = []
                                      pesan2 = "@a"" "
                                      xlen = str(len(zxc))
                                      xlen2 = str(len(zxc)+len(pesan2)-1)
                                      zx = {'S':xlen, 'E':xlen2, 'M':target}
                                      zx2.append(zx)
                                      zxc += pesan2
                                      msg.contentType = 0
                                      msg.text = zxc
                                      msg.contentMetadata = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                      gege = sep.split(" ")
                                      num = int(gege[1])
                                      client.sendMessage(to, "Berhasil menyepam: "+client.getContact(target).displayName+"\nJumlah spam tag: " + str(num))
                                      for var in range(0,num):
                                          hayden = client.getContact(target)
                                          members = [hayden.mid]
                                          client.sendMessage(target, text=zxc, contentMetadata = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
#=========== [ Spam Kesemua By jumlah ] ============#                            
                            elif cmd.startswith("gfoto"):
                                  if msg.toType == 2:
                                      sep = text.split(" ")
                                      strnum = text.replace(sep[0] + " ","")
                                      num = int(strnum)
                                      for var in range(0,num):
                                          group = client.getGroup(to)
                                          members = [mem.mid for mem in group.members]
                                          gmb = str(settings["Addfotospam"]["img"])
                                          client.sendImage(to, gmb)
                                     # client.sendMessage(to, "「Spam Foto group」\nBerhasil {} spam foto".format(str(num)))
                                          #client.acquireGroupCallRoute(to)
                                          #client.inviteIntoGroupCall(to, contactIds=members)
                            elif cmd.startswith("gtikel"):
                                  if msg.toType == 2:
                                      sep = text.split(" ")
                                      strnum = text.replace(sep[0] + " ","")
                                      num = int(strnum)
                                      for var in range(0,num):
                                          group = client.getGroup(to)
                                          members = [mem.mid for mem in group.members]
                                          sid = str(settings["Addstickerspam"]["sid"])
                                          spkg = str(settings["Addstickerspam"]["spkg"])
                                          client.sendSticker(to, spkg, sid)
                            elif cmd.startswith("gcall"):
                                  if msg.toType == 2:
                                      sep = text.split(" ")
                                      strnum = text.replace(sep[0] + " ","")
                                      num = int(strnum)
                                      client.sendMessage(to, "Berhasil mengundang {} panggilan group".format(str(num)))
                                      for var in range(0,num):
                                          group = client.getGroup(to)
                                          members = [mem.mid for mem in group.members]
                                          client.acquireGroupCallRoute(to)
                                          client.inviteIntoGroupCall(to, contactIds=members)
                            elif cmd.startswith("ggift"):
                                  if msg.toType == 2:
                                      sep = text.split(" ")
                                      strnum = text.replace(sep[0] + " ","")
                                      num = int(strnum)
                                      for var in range(0,num):
                                          group = client.getGroup(to)
                                          members = [mem.mid for mem in group.members]
                                          client.sendMessage(to, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                            elif cmd.startswith("gchat"):
                                  if msg.toType == 2:
                                      sep = text.split(" ")
                                      strnum = text.replace(sep[0] + " ","")
                                      num = int(strnum)
                                      for var in range(0,num):
                                          group = client.getGroup(to)
                                          members = [mem.mid for mem in group.members]
                                          client.sendMessage(to,  str(settings["spam1"]))
                            elif cmd.startswith("gtag"):
                                  if msg.toType == 2:
                                      sep = text.replace("stag","")
                                      key = eval(msg.contentMetadata["MENTION"])
                                      target = key["MENTIONEES"][0]["M"]
                                      zx = ""
                                      zxc = " "
                                      zx2 = []
                                      pesan2 = "@a"" "
                                      xlen = str(len(zxc))
                                      xlen2 = str(len(zxc)+len(pesan2)-1)
                                      zx = {'S':xlen, 'E':xlen2, 'M':target}
                                      zx2.append(zx)
                                      zxc += pesan2
                                      msg.contentType = 0
                                      msg.text = zxc
                                      msg.contentMetadata = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                      gege = sep.split(" ")
                                      num = int(gege[1])
                                      for var in range(0,num):
                                          hayden = client.getContact(target)
                                          members = [hayden.mid]
                                          client.sendMessage(to, text=zxc, contentMetadata = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                                                
                            elif cmd.startswith("unsends "):
                                sep = text.split(" ")
                                args = text.replace(sep[0] + " ","")
                                mes = int(sep[1])
                                M = client.getRecentMessagesV2(to, 1001)
                                MId = []
                                for ind,i in enumerate(M):
                                    if ind == 0:
                                        pass
                                    else:
                                        if i._from == client.profile.mid:
                                            MId.append(i.id)
                                            if len(MId) == mes:
                                               break
                                def unsMes(id):
                                   client.unsendMessage(id)
                                for i in MId:
                                    thread1 = threading.Thread(target=unsMes, args=(i,))
                                    thread1.daemon = True
                                    thread1.start()
                                    thread1.join()
                                client.unsendMessage(msg_id)    
                                #client.sendMessage(to, "「UNSEND」\nSuccess unsend {} message.".format(len(MId)))
    #-------------- copy profile----------
                            elif "Say " in msg.text:
                                txt = msg.text.split(" ")
                                jmlh = int(txt[2])
                                teks = msg.text.replace("Say "+str(txt[1])+" "+str(jmlh)+ " ","")
                                tulisan = jmlh * (teks+"\n")
                 #@reno.a.w
                                if txt[1] == "on":
                                    if jmlh <= 100000:
                                        for x in range(jmlh):
                                            client.sendMessage(msg.to, teks)
                                    else:
                                        client.sendMessage(msg.to, "Kelebihan batas:v")
                                elif txt[1] == "off":
                                    if jmlh <= 100000:
                                        client.sendMessage(msg.to, tulisan)
                                    else:
                                        client.sendMessage(msg.to, "Kelebihan batas :v")
                                if txt[1] == "ok":
                                    if jmlh <= 100000:
                                        for x in range(jmlh):
                                            client.sendMessage(msg.to, tulisan)
                                    else:
                                        client.sendMessage(msg.to, "Kelebihan batas :v")
#=========== [ Spam Kesemua memakai batas limit ] ============#                              
                            elif cmd.startswith("ltag "):
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    msg.contentMetadata = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    jmlh = int(settings["limitTag"])
                                    if jmlh <= 10000000000:
                                        for x in range(jmlh):
                                            try:
                                                client.sendMessage(to, text=zxc, contentMetadata = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                            except Exception as e:
                                                client.sendMessage(msg.to,str(e))
                                    else:
                                        client.sendMessage(msg.to,"Jumlah melebihi 10000000000")
                            elif cmd.startswith("lcall"):
                              if msg.toType == 2:
                               	group = client.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(settings["limitCall"])
                                client.sendMessage(to, "Berhasil spam panggilan {}".format((settings["limitCall"])))
                                if jmlh <= 10000000000:
                                  for x in range(jmlh):
                                    try:
                                        client.acquireGroupCallRoute(to)
                                        client.inviteIntoGroupCall(to, contactIds=members)
                                    except Exception as e:
                                         client.sendMessage(msg.to,str(e))
                                else:
                                  client.sendMessage(msg.to,"Jumlah melebihi 10000000000")
                            elif cmd.startswith("lgift"):
                              if msg.toType == 2:
                               	group = client.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(settings["limitGift"])
                                #client.sendMessage(to, "Berhasil spam panggilan {}".format((settings["limitCall"])))
                                if jmlh <= 10000000000:
                                  for x in range(jmlh):
                                    try:
                                        client.sendMessage(to, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                    except Exception as e:
                                        client.sendMessage(msg.to,str(e))
                                else:
                                  client.sendMessage(msg.to,"Jumlah melebihi 10000000000")
                            elif cmd.startswith("lchat"):
                              if msg.toType == 2:
                               	group = client.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(settings["limitChat"])
                                #client.sendMessage(to, "Berhasil spam panggilan {}".format((settings["limitCall"])))
                                if jmlh <= 10000000000:
                                  for x in range(jmlh):
                                    try:
                                        client.sendMessage(to, str(settings["spam1"]))
                                    except Exception as e:
                                        client.sendMessage(msg.to,str(e))
                                else:
                                  client.sendMessage(msg.to,"Jumlah melebihi 10000000000")
#=========== [ Spam By Mid ] ============#                                                         
                            elif "Stikel " in msg.text:
                                  korban = text.replace("Stikel ","")
                                  korban2 = korban.split()
                                  midd = korban2[0]
                                  jumlah = int(korban2[1])
                                  client.sendMessage(msg.to,"「 Spam Sticker 」\nJumlah spam sticker: " + str(jumlah)+" Berhasil menyepam: "+client.getContact(midd).displayName)
                                  if jumlah <= 10000:
                                      for var in range(0,jumlah):
                                            #hk = client.getContact(midd)
                                            #members = [hk.mid]                                     
                                            sid = str(settings["Addstickerspam"]["sid"])
                                            spkg = str(settings["Addstickerspam"]["spkg"])
                                            client.sendSticker(midd, spkg, sid)
                                      
                            elif "Sfoto " in msg.text:
                                  korban = text.replace("Sfoto ","")
                                  korban2 = korban.split()
                                  midd = korban2[0]
                                  jumlah = int(korban2[1])
                                  client.sendMessage(msg.to,"「 Spam Foto 」\nJumlah spam foto: " + str(jumlah)+" Berhasil menyepam: "+client.getContact(midd).displayName)
                                  if jumlah <= 10000:
                                      for var in range(0,jumlah):
                                            #hk = client.getContact(midd)
                                            #members = [hk.mid]                                     
                                            gmb = str(settings["Addfotospam"]["img"])
                                            client.sendImage(midd, gmb)
                                      
                            elif "Sgift " in msg.text:
                                  korban = text.replace("Sgift ","")
                                  korban2 = korban.split()
                                  midd = korban2[0]
                                  jumlah = int(korban2[1])
                                  client.sendMessage(msg.to,"「 Spam Gift 」\nJumlah spam gift: " + str(jumlah)+" Berhasil menyepam: "+client.getContact(midd).displayName)
                                  if jumlah <= 10000:
                                      for var in range(0,jumlah):
                                            #hk = client.getContact(midd)
                                            #members = [hk.mid]                                     
                                            client.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      
                            elif "Schat " in msg.text:
                                  korban = text.replace("Schat ","")
                                  korban2 = korban.split()
                                  midd = korban2[0]
                                  jumlah = int(korban2[1])
                                  client.sendMessage(msg.to,"「 Spam Chat 」\nJumlah spam chat: " + str(jumlah)+" Berhasil menyepam: "+client.getContact(midd).displayName)
                                  if jumlah <= 10000:
                                      for var in range(0,jumlah):
                                            #hk = client.getContact(midd)
                                            #members = [hk.mid]                                     
                                            client.sendMessage(midd, str(settings["spam1"]))
                                        
                            elif "Sgrup " in msg.text:
                                  korban = msg.text.replace("Sgrup ","")
                                  korban2 = korban.split()
                                  midd = korban2[0] 
                                  jumlah = int(korban2[1])
                                  client.sendMessage(msg.to,"「 Spam Group 」\nJumlah spam group: " + str(jumlah)+"\nBerhasil menyepam: "+ client.getContact(midd).displayName)
                                  #client.inviteIntoGroup(midd)
                               #   if jumlah <= 10000:
                                #      for var in range(0,jumlah):
                                 #           G = client.getContact(midd)
                                  #          client.findAndAddContactsByMid(G.mid)
                                   #         client.createGroup(settings["spamgrup"],[midd])                                          
                                    #        client.inviteIntoGroup(midd)
                                  if jumlah <= 10000:
                                      for var in range(0,jumlah):
                                            G = client.getContact(midd)
                                            client.findAndAddContactsByMid(G.mid)
                                            client.createGroup(settings["spamgrup"],[midd])
                                            client.inviteIntoGroup(midd)
                                  else:
                                      client.sendMessage(msg.to, "Kebanyakan gblk! ")            
                                  print ("T E R S P A M.")
                                  #else:
                                   #   client.sendMessage(msg.to, "Kebanyakan gblk! ")            
                                  #print ("T E R S P A M.")
                            elif cmd.startswith("spamgroup"):
                                #d = text.replace("spamgroup","")
                                a = text.split("|")
                                b = str(a[1])
                                c = str(a[2])
                                e = int(a[3])
                                groups = client.groups
                                g = client.getContact(b)
                                client.findAndAddContactsByMid(g.mid)
                                if e <= 1000:
                                   for var in range(0,e):
                                       client.createGroup(c, [b])
                                   for i in groups:
                                       gr = client.getGroup(i)
                                       if gr.name == c:
                                        client.inviteIntoGroup(gr.id, [b])
                                        
                            elif cmd.startswith("spaminvmid"):
                                dan = text.split("|")
                                nam = dan[1]
                                jlh = int(dan[2])
                                tar = dan[3]
                                grr = client.groups
                                client.findAndAddContactsByMid(tar)
                                if jlh <= 101:
                                    for var in range(0,jlh):
                                        gcr = client.createGroup(nam, [tar])
                                        Thread(target=client.inviteIntoGroup,args=(gcr.id, [tar]),).start()
                                        time.sleep(2)
                                        client.leaveGroup(gcr.id)
                                    client.sendMention(to, "Succesfully Spam Invite @! to Group {}".format(gcr.name), [tar])

                            elif cmd.startswith("spaminvite"):
                                key = eval(msg.contentMetadata["MENTION"])
                                tar = key["MENTIONEES"][0]["M"]
                                dan = text.split("|")
                                nam = dan[1]
                                jlh = int(dan[2])
                                grr = client.groups
                                client.findAndAddContactsByMid(tar)
                                if jlh <= 101:
                                    for var in range(0,jlh):
                                        gcr = client.createGroup(nam, [tar])
                                        client.inviteIntoGroup(gcr.id, [tar])
                                        time.sleep(2)
                                        client.leaveGroup(gcr.id)
                                    client.sendMention(to, "Succesfully Spam Invite @! to Group {}".format(gcr.name), [tar])
                                
#=========== [ Spam Broadcast ] ============#                              
                            elif cmd.startswith("vgrup"):
                                sep = text.split(" ")
                                bctxt = text.replace(sep [0] + " ","")
                                bc = (" broadcast by hayden")
                                cb = (bctxt + bc)
                                url = "https://rest.farzain.com/api/tts.php?id="+cb+"&apikey=Jvp8TLDuosjxuQn7eGDmVzx5g&type=json"
                                #tts = gTTS(cb, lang='id', slow=False)
                                #tts.save('tts.mp3')
                                n = client.getGroupIdsJoined()
                                for manusia in n:
                                    client.sendAudioWithURL(manusia, str(url))
                                client.sendMessage(msg.to, "Berhasil broadcast ke {} group".format(str(len(groups))))

                            elif cmd.startswith("vcgrup"):
                                sep = text.split(" ")
                                bctxt = text.replace(sep [0] + " ","")
                                bc = (" broadcast by hayden")
                                cb = (bctxt + bc)
                                url = "https://rest.farzain.com/api/tts.php?id="+cb+"&apikey=Jvp8TLDuosjxuQn7eGDmVzx5g&type=json"
                                n = client.getGroupIdsJoined()
                                for manusia in n:
                                    ct = str(settings["bcmid"])
                                    client.sendContact(manusia, ct)
                                    client.sendAudioWithURL(manusia, str(url))
                                client.sendMessage(msg.to, "Berhasil broadcast ke {} group".format(str(len(groups))))
                                
                            elif cmd.startswith("vfgrup"):
                                sep = text.split(" ")
                                bctxt = text.replace(sep [0] + " ","")
                                bc = (" broadcast by hayden")
                                cb = (bctxt + bc)
                                url = "https://rest.farzain.com/api/tts.php?id="+cb+"&apikey=Jvp8TLDuosjxuQn7eGDmVzx5g&type=json"
                                n = client.getGroupIdsJoined()
                                for manusia in n:
                                    gmb = str(settings["Addfotobc"]["img"])
                                    client.sendImage(manusia, gmb)
                                    client.sendAudioWithURL(manusia, str(url))
                                client.sendMessage(msg.to, "Berhasil broadcast ke {} group".format(str(len(groups))))

                            elif cmd.startswith("vtgrup"):
                                sep = text.split(" ")
                                bctxt = text.replace(sep [0] + " ","")
                                bc = (" broadcast by hayden")
                                cb = (bctxt + bc)
                                url = "https://rest.farzain.com/api/tts.php?id="+cb+"&apikey=Jvp8TLDuosjxuQn7eGDmVzx5g&type=json"
                                n = client.getGroupIdsJoined()
                                for manusia in n:
                                    sid = str(settings["Addstickerbc"]["sid"])
                                    spkg = str(settings["Addstickerbc"]["spkg"])
                                    client.sendSticker(manusia, spkg, sid)
                                    client.sendAudioWithURL(manusia, str(url))
                                client.sendMessage(msg.to, "Berhasil broadcast ke {} group".format(str(len(groups))))

                            elif cmd.startswith("vftgrup"):
                                sep = text.split(" ")
                                bctxt = text.replace(sep [0] + " ","")
                                bc = (" broadcast by hayden")
                                cb = (bctxt + bc)
                                url = "https://rest.farzain.com/api/tts.php?id="+cb+"&apikey=Jvp8TLDuosjxuQn7eGDmVzx5g&type=json"
                                n = client.getGroupIdsJoined()
                                for manusia in n:
                                    sid = str(settings["Addstickerbc"]["sid"])
                                    spkg = str(settings["Addstickerbc"]["spkg"])
                                    gmb = str(settings["Addfotobc"]["img"])
                                    client.sendImage(manusia, gmb)
                                    client.sendSticker(manusia, spkg, sid)
                                    client.sendAudioWithURL(manusia, str(url))
                                client.sendMessage(msg.to, "Berhasil broadcast ke {} group".format(str(len(groups))))

                            elif cmd.startswith("vteman"):
                                sep = text.split(" ")
                                bctxt = text.replace(sep [0] + " ","")
                                bc = (" broadcast by hayden")
                                cb = (bctxt + bc)
                                url = "https://rest.farzain.com/api/tts.php?id="+cb+"&apikey=Jvp8TLDuosjxuQn7eGDmVzx5g&type=json"
                                n = client.getAllContactIdsJoined()
                                for manusia in n:
                                    client.sendAudioWithURL(manusia, str(url))
                                client.sendMessage(msg.to, "Berhasil broadcast ke {} teman".format(str(len(groups))))
                                                                    
                            elif cmd.startswith("bgrup"):
                                sep = text.split(" ")
                                txt = text.replace(sep [0] + " ","")
                                groups = client.getGroupIdsJoined()
                                for group in groups:
                                    time.sleep(0.3)
                                    client.sendMessage(group, "{}".format(str(txt)))
                                client.sendMessage(msg.to, "Berhasil broadcast ke {} group".format(str(len(groups))))
                                
                            elif cmd.startswith("bcgrup"):
                                sep = text.split(" ")
                                txt = text.replace(sep [0] + " ","")
                                groups = client.getGroupIdsJoined()
                                for group in groups:
                                    ct = str(settings["bcmid"])
                                    client.sendContact(group, ct)
                                    client.sendMessage(group, "{}".format(str(txt)))
                                client.sendMessage(msg.to, "Berhasil broadcast ke {} group".format(str(len(groups))))
                                
                            elif cmd.startswith("bfgrup"):
                                sep = text.split(" ")
                                txt = text.replace(sep [0] + " ","")
                                groups = client.getGroupIdsJoined()
                                for group in groups:
                                    gmb= str(settings["Addfotobc"]["img"])
                                    client.sendImage(group, gmb)
                                    client.sendMessage(group, "{}".format(str(txt)))
                                client.sendMessage(msg.to, "Berhasil broadcast ke {} group".format(str(len(groups))))
                                
                            elif cmd.startswith("btgrup"):
                                sep = text.split(" ")
                                txt = text.replace(sep [0] + " ","")
                                groups = client.getGroupIdsJoined()
                                for group in groups:
                                    sid = str(settings["Addstickerbc"]["sid"])
                                    spkg = str(settings["Addstickerbc"]["spkg"])
                                    client.sendMessage(group, "{}".format(str(txt)))
                                    client.sendSticker(group, spkg, sid)
                                client.sendMessage(msg.to, "Berhasil broadcast ke {} group".format(str(len(groups))))
                                
                            elif cmd.startswith("bftgrup"):
                                sep = text.split(" ")
                                txt = text.replace(sep [0] + " ","")
                                groups = client.getGroupIdsJoined()
                                for group in groups:
                                    gmb = str(settings["Addfotobc"]["img"])
                                    sid = str(settings["Addstickerbc"]["sid"])
                                    spkg = str(settings["Addstickerbc"]["spkg"])
                                    client.sendImage(group, gmb)
                                    client.sendMessage(group, "{}".format(str(txt)))
                                    client.sendSticker(group, spkg, sid)
                                client.sendMessage(msg.to, "Berhasil broadcast ke {} group".format(str(len(groups))))
                                
                            elif cmd.startswith("bteman"):
                                sep = text.split(" ")                         
                                txt =  msg.text.replace(sep [0] + " ","")
                                friends = client.getAllContactIds()
                                for friend in friends:
                                    time.sleep(0.7)
                                    client.sendMessage(friend, "{}".format(str(txt)))
                                client.sendMessage(msg.to, "Berhasil broadcast ke {} teman".format(str(len(friends))))
#=========== [ Setting Set] ============#                                                              
                            elif cmd.startswith("tikelspam"):
                                 settings["Addstickerspam"]["status"] = True
                                 client.sendMessage(msg.to, "kirim stickernya")                               
                            elif cmd.startswith("cektikelspam"):
                                  sid = str(settings["Addstickerspam"]["sid"])
                                  spkg = str(settings["Addstickerspam"]["spkg"])
                                  client.sendSticker(to, spkg, sid)
                            elif cmd.startswith("tikelsider"):
                                 settings["Addstickersider"]["status"] = True
                                 client.sendMessage(msg.to, "kirim stickernya")
                            elif cmd.startswith("cektikelsider"):
                                  sid = str(settings["Addstickersider"]["sid"])
                                  spkg = str(settings["Addstickersider"]["spkg"])
                                  client.sendSticker(to, spkg, sid)
                            elif cmd == "tikeltag":
                                 settings["Addstickertag"]["status"] = True
                                 client.sendMessage(msg.to, "kirim stickernya")
                            elif cmd == "cektikeltag":
                                  sid = str(settings["Addstickertag"]["sid"])
                                  spkg = str(settings["Addstickertag"]["spkg"])
                                  client.sendSticker(to, spkg, sid)
                            elif cmd == "tikelmention":
                                 settings["Addstickermention"]["status"] = True
                                 client.sendMessage(msg.to, "kirim stickernya")
                            elif cmd == "tikelmention on":
                                 tagmention["group"] = True
                                 client.sendMessage(msg.to, "metion sticker on")
                            elif cmd == "tikelmention off":
                                 tagmention["group"] = False
                                 client.sendMessage(msg.to, "metion sticker off")
                            elif cmd == "cektikelmention":
                                  sid = str(settings["Addstickermention"]["sid"])
                                  spkg = str(settings["Addstickermention"]["spkg"])
                                  client.sendSticker(to, spkg, sid)
                            elif cmd == "deltikelkick":
                                del skick['ROM'][to]
                                client.sendMessage(to,"List tikelkick bersih")
                            elif cmd == "tikelkick":
                                 settings["Addstickerkick"]["status"] = True
                                 client.sendMessage(msg.to, "kirim stickernya")
                            elif cmd == "tikelkick on":
                                 testkick["group"] = True
                                 client.sendMessage(msg.to, "kick sticker on")
                            elif cmd == "tikelkick off":
                                 testkick["group"] = False
                                 client.sendMessage(msg.to, "kick sticker off")
                            elif cmd.startswith("cektikelkick"):
                                  sid = str(settings["Addstickerkick"]["sid"])
                                  spkg = str(settings["Addstickerkick"]["spkg"])
                                  client.sendSticker(to, spkg, sid)
                            elif cmd.startswith("tikelbc"):
                                 settings["Addstickerbc"]["status"] = True
                                 client.sendMessage(msg.to, "kirim stickernya")
                            elif cmd.startswith("cektikelbc"):
                                  sid = str(settings["Addstickerbc"]["sid"])
                                  spkg = str(settings["Addstickerbc"]["spkg"])
                                  client.sendSticker(to, spkg, sid)
                  
                            elif cmd.startswith("fotospam"):
                                 settings["Addfotospam"]["status"] = True
                                 client.sendMessage(msg.to, "kirim fotonya")
                            elif cmd.startswith("cekfotospam"):
                                  gmb = str(settings["Addfotospam"]["img"])
                                  client.sendImage(to, gmb)                                  
                            elif cmd.startswith("fotobc"):
                                 settings["Addfotobc"]["status"] = True
                                 client.sendMessage(msg.to, "kirim fotonya")                                  
                            elif cmd.startswith("cekfotobc"):
                                  gmb = str(settings["Addfotobc"]["img"])
                                  client.sendImage(to, gmb)               
                                  
                            elif cmd ==  "cekmidbc":
                                  ct = str(settings["bcmid"])
                                  client.sendMessage(msg.to," "+ str(settings["bcmid"]))
                                  client.sendContact(msg.to, ct)                                
                            elif cmd ==  "cekrespon":
                                  ret = "Detail semua respon"
                                  ret += "\n\nSpam chat:\n{}\n".format(str(settings["spam1"]))
                                  ret += "\nMid broadcast:\n{}\n".format(str(settings["bcmid"]))
                                  ret += "\nRespon tag:\n{}\n".format(str(settings["Respontag"]))
                                  ret += "\nRespon sider:\n{}\n".format(str(settings["mention"]))
                                  ret += "\nRespon welcome:\n{}\n".format(str(settings["welcome"]))
                                  ret += "\nRespon leave:\n{}\n".format(str(settings["leave"]))
                                  ret += "\nNama spam grup:\n{}\n".format(str(settings["spamgrup"]))
                                  ret += "\nRespon like:\n{}".format(str(settings["comment"]))
                                  client.sendMessage(to, str(ret))                                
                            elif cmd.startswith("setmidbc "):
                                  sep = text.split(" ")
                                  cos = text.replace(sep[0] + " ","")
                                  settings["bcmid"] = cos
                                  client.sendReplyMessage(msg_id,msg.to,"Berhasil menggati mid contact\n「"+settings["bcmid"]+"」")
                            elif cmd.startswith("setnamagrupspam "):
                                  sep = text.split(" ")
                                  cos = text.replace(sep[0] + " ","")
                                  settings["spamgrup"] = cos
                                  client.sendReplyMessage(msg_id,msg.to,"Berhasil menggati nama grup spam\n「"+settings["spamgrup"]+"」")
                            elif cmd.startswith("setchatspam "):
                                  sep = text.split(" ")
                                  cos = text.replace(sep[0] + " ","")
                                  settings["spam1"] = cos
                                  client.sendReplyMessage(msg_id,msg.to,"Berhasil menggati kata Spam Chat\n「"+settings["spam1"]+"」")
                            elif cmd.startswith("setrestag "):
                                  sep = text.split(" ")
                                  cos = text.replace(sep[0] + " ","")
                                  settings["Respontag"] = cos
                                  client.sendReplyMessage(msg_id,msg.to,"Berhasil menggati kata respon tag\n「"+settings["Respontag"]+"」")
                            elif cmd.startswith("setwelcome "):
                                  sep = text.split(" ")
                                  cos = text.replace(sep[0] + " ","")
                                  settings["welcome"] = cos
                                  client.sendReplyMessage(msg_id,msg.to,"Berhasil menggati sambutan welcome\n「"+settings["welcome"]+"」")
                            elif cmd.startswith("setleave "):
                                  sep = text.split(" ")
                                  cos = text.replace(sep[0] + " ","")
                                  settings["leave"] = cos
                                  client.sendReplyMessage(msg_id,msg.to,"Berhasil menggati sambutan leave\n「"+settings["leave"]+"」")
                            elif cmd.startswith("setsider "):
                                  sep = text.split(" ")
                                  cos = text.replace(sep[0] + " ","")
                                  settings["mention"] = cos
                                  client.sendReplyMessage(msg_id,msg.to,"Berhasil menggati respon sider\n「"+settings["mention"]+"」")
                            elif cmd.startswith("setlike "):
                                  sep = text.split(" ")
                                  cos = text.replace(sep[0] + " ","")
                                  settings["comment"] = cos
                                  client.sendReplyMessage(msg_id,msg.to,"Berhasil menggati respon like\n「"+settings["comment"]+"」")
#==============================================================================#
# COMMAND REMOTE GROUP #
#===========================|===================================================#
                            elif cmd.startswith("infogrup "):
                                  separate = text.split(" ")
                                  number = text.replace(separate[0] + " ","")
                                  groups = client.getGroupIdsJoined()
                                  ret_ = ""
                                  try:
                                      group = groups[int(number)-1]
                                      G = client.getGroup(group)
                                      try:
                                          gCreator = G.creator.displayName
                                      except:
                                          gCreator = "Tidak ditemukan"
                                      if G.invitee is None:
                                          gPending = "0"
                                      else:
                                          gPending = str(len(G.invitee))
                                      if G.preventedJoinByTicket == True:
                                          gQr = "Tertutup"
                                          gTicket = "Tidak ada"
                                      else:
                                          gQr = "Terbuka"
                                          gTicket = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(G.id)))
                                      timeCreated = []
                                      timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                      ret_ += "「 Group Info 」"
                                      ret_ += "\n➸ Nama Group : {}".format(G.name)
                                      ret_ += "\n➸ ID Group : {}".format(G.id)
                                      ret_ += "\n➸ Pembuat : {}".format(gCreator)
                                      ret_ += "\n➸ Waktu Dibuat : {}".format(str(timeCreated))
                                      ret_ += "\n➸ Jumlah Member : {}".format(str(len(G.members)))
                                      ret_ += "\n➸ Jumlah Pending : {}".format(gPending)
                                      ret_ += "\n➸ Group Qr : {}".format(gQr)
                                      ret_ += "\n➸ Group Ticket : {}".format(gTicket)
                                      ret_ += "\n➸ Picture Url : http://dl.profile.line-cdn.net/{}".format(G.pictureStatus)
                                      ret_ += ""
                                      client.sendMessage(to, str(ret_))
                                      client.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                                  except:
                                      pass

                            elif cmd.startswith("opengrup "):
                                  separate = text.split(" ")
                                  number = text.replace(separate[0] + " ","")
                                  groups = client.getGroupIdsJoined()
                                  ret_ = ""
                                  try:
                                      group = groups[int(number)-1]
                                      G = client.getGroup(group)
                                      G.preventedJoinByTicket = False
                                      client.updateGroup(G)
                                      try:
                                          gCreator = G.creator.mid
                                          dia = client.getContact(gCreator)
                                          zx = ""
                                          zxc = ""
                                          zx2 = []
                                          xpesan = '「 Sukses Open Qr 」\n• Creator :  '
                                          diaa = str(dia.displayName)
                                          pesan = ''
                                          pesan2 = pesan+"@a\n"
                                          xlen = str(len(zxc)+len(xpesan))
                                          xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                          zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                          zx2.append(zx)
                                          zxc += pesan2
                                      except:
                                          gCreator = "Tidak ditemukan"
                                      if G.invitee is None:
                                          gPending = "0"
                                      else:
                                          gPending = str(len(G.invitee))
                                      if G.preventedJoinByTicket == True:
                                          gQr = "Tertutup"
                                          gTicket = "Tidak ada"
                                      else:
                                          gQr = "Terbuka"
                                          gTicket = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(G.id)))
                                      timeCreated = []
                                      timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                      ret_ += xpesan+zxc
                                      ret_ += "• Nama : {}".format(G.name)
                                      ret_ += "\n• Group Qr : {}".format(gQr)
                                      ret_ += "\n• Pendingan : {}".format(gPending)
                                      ret_ += "\n• Group Ticket : {}".format(gTicket)
                                      ret_ += ""
                                      client.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  except:
                                      pass

                            elif cmd.startswith("closegrup "):
                                  separate = text.split(" ")
                                  number = text.replace(separate[0] + " ","")
                                  groups = client.getGroupIdsJoined()
                                  ret_ = ""
                                  try:
                                      group = groups[int(number)-1]
                                      G = client.getGroup(group)
                                      G.preventedJoinByTicket = True
                                      client.updateGroup(G)
                                      try:
                                          gCreator = G.creator.mid
                                          dia = client.getContact(gCreator)
                                          zx = ""
                                          zxc = ""
                                          zx2 = []
                                          xpesan = '「 Sukses Close Qr 」\n• Creator :  '
                                          diaa = str(dia.displayName)
                                          pesan = ''
                                          pesan2 = pesan+"@a\n"
                                          xlen = str(len(zxc)+len(xpesan))
                                          xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                          zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                          zx2.append(zx)
                                          zxc += pesan2
                                      except:
                                          gCreator = "Tidak ditemukan"
                                      if G.invitee is None:
                                          gPending = "0"
                                      else:
                                          gPending = str(len(G.invitee))
                                      if G.preventedJoinByTicket == True:
                                          gQr = "Tertutup"
                                          gTicket = "Tidak ada"
                                      else:
                                          gQr = "Terbuka"
                                          gTicket = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(G.id)))
                                      timeCreated = []
                                      timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                      ret_ += xpesan+zxc
                                      ret_ += "• Nama : {}".format(G.name)
                                      ret_ += "\n• Group Qr : {}".format(gQr)
                                      ret_ += "\n• Pendingan : {}".format(gPending)
                                      ret_ += "\n• Group Ticket : {}".format(gTicket)
                                      ret_ += ""
                                      client.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  except:
                                      pass                                    
                               
                            elif cmd.startswith("infopending "):
                                #if msg.toType == 2:
                                    sep = text.split(" ")
                                    number = text.replace(sep[0] + " ","")
                                    groups = client.getGroupIdsJoined()
                                    ret_ = "[ Detail Pending ]"
                                    no = 0
                                    try:
                                        group = groups[int(number)-1]
                                        G = client.getGroup(group)
                                        if G.invitee is None or G.invitee == []:
                                            client.sendMessage(to, "Tidak ada pendingan")
                                            return
                                        else:
                                            for pen in G.invitee:
                                                ret_ += "\n\n{}. {}".format(str(no), str(pen.displayName))
                                                no += 1
                                                ret_ += "\n{} ".format(str(pen.mid))
                                                ret_ += "\n{} ".format(str(pen.statusMessage))
                                            client.sendMessage(to, str(ret_))
                                    except:
                                        pass
                            elif cmd.startswith("infomember "):
                                  separate = msg.text.split(" ")
                                  number = msg.text.replace(separate[0] + " ","")
                                  groups = client.getGroupIdsJoined()
                                  ret_ = ""
                                  try:
                                      group = groups[int(number)-1]
                                      G = client.getGroup(group)
                                      no = 0
                                      ret_ = ""
                                      for mem in G.members:
                                          no += 1
                                          ret_ += "\n " "➸ "+ str(no) + ". " + mem.displayName
                                      client.sendMessage(to,"➸ Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                                  except: 
                                      pass 
                            elif cmd.startswith("leavegrup "):
                                  separate = msg.text.split(" ")
                                  number = msg.text.replace(separate[0] + " ","")
                                  groups = client.getGroupIdsJoined()
                                  ret_ = ""
                                  try:
                                      group = groups[int(number)-1]
                                      G = client.getGroup(group)
                                      try:
                                          ginfo = client.getGroup(group)
                                          gCreator = ginfo.creator.mid
                                          recky = client.getContact(gCreator)
                                          zx = ""
                                          zxc = ""
                                          zx2 = []
                                          xpesan = 'Terimaksih invitannya '
                                          reck = str(recky.displayName)
                                          pesan = ''
                                          pesan2 = pesan+"@x \n"
                                          xlen = str(len(zxc)+len(xpesan))
                                          xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                          zx = {'S':xlen, 'E':xlen2, 'M':recky.mid}
                                          zx2.append(zx)
                                          zxc += pesan2
                                          text = xpesan+zxc + "Lain kali mampir lagi" 
                                          client.sendMessage(group, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                          client.sendImageWithURL(group,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=u48c350911cde6604da051d9da06c5db7&oid=faadb1b4f3991376bdccbd5700545da6")
                                          client.leaveGroup(group)
                                      except:
                                          client.sendMessage(msg.to, "Grup itu tidak ada")
                                      if G.invitee is None:
                                          gPending = "0"
                                      else:
                                          gPending = str(len(G.invitee))
                                      timeCreated = []
                                      timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                      ginfo = client.getGroup(group)
                                      gCreator = ginfo.creator.mid
                                      reck = client.getContact(gCreator)
                                      zx = ""
                                      zxc = ""
                                      zx2 = []
                                      xpesan = '「 Sukses Leave Group 」\n• Creator :  '
                                      recky = str(reck.displayName)
                                      pesan = ''
                                      pesan2 = pesan+"@x\n"
                                      xlen = str(len(zxc)+len(xpesan))
                                      xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                      zx = {'S':xlen, 'E':xlen2, 'M':reck.mid}
                                      zx2.append(zx)
                                      zxc += pesan2
                                      ret_ += xpesan +zxc
                                      ret_ += "• Nama grup : {}".format(G.name)
                                      ret_ += "\n• Pendingan : {}".format(gPending)
                                      ret_ += "\n• Jumlah Member : {}".format(str(len(G.members)))
                                      client.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  except Exception as e:
                                      client.sendMessage(to, str(e))

                            elif cmd.startswith("mentiongrup "):
                                  separate = msg.text.split(" ")
                                  number = msg.text.replace(separate[0] + " ","")
                                  groups = client.getGroupIdsJoined()
                                  ret_ = ""
                                  try:
                                      group = groups[int(number)-1]
                                      G = client.getGroup(group)
                                      try:
                                          ginfo = client.getGroup(group)
                                          nama = [contact.mid for contact in ginfo.members]
                                          k = len(nama)//20
                                          for a in range(k+20):
                                              txt = u''
                                              s=0
                                              b=[]                                           
                                              for i in ginfo.members[a*20 : (a+1)*20]:
                                                  b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                                  s += 7
                                                  txt += u'@Zero \n'
                                              client.sendMessage(group, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                              client.sendMessage(group, "Total {} Mention".format(str(len(nama))))
                                      except:
                                          pass#    client.sendMessage(msg.to, "Grup itu tidak ada")
                                      if G.invitee is None:
                                          gPending = "0"
                                      else:
                                          gPending = str(len(G.invitee))
                                      timeCreated = []
                                      timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                      ginfo = client.getGroup(group)
                                      gCreator = ginfo.creator.mid
                                      reck = client.getContact(gCreator)
                                      zx = ""
                                      zxc = ""
                                      zx2 = []
                                      xpesan = '「 Sukses Mention Group 」\n• Creator :  '
                                      recky = str(reck.displayName)
                                      pesan = ''
                                      pesan2 = pesan+"@x\n"
                                      xlen = str(len(zxc)+len(xpesan))
                                      xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                      zx = {'S':xlen, 'E':xlen2, 'M':reck.mid}
                                      zx2.append(zx)
                                      zxc += pesan2
                                      ret_ += xpesan +zxc
                                      ret_ += "• Nama grup : {}".format(G.name)
                                      ret_ += "\n• Pendingan : {}".format(gPending)
                                      ret_ += "\n• Jumlah Member : {}".format(str(len(G.members)))
                                      client.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  except Exception as e:
                                      client.sendMessage(to, str(e))
                                      
                            elif cmd.startswith("detectupon "):
                                  separate = text.split(" ")
                                  number = text.replace(separate[0] + " ","")
                                  groups = client.getGroupIdsJoined()
                                  try:
                                      groupid = groups[int(number)-1]
                                      gm = client.getGroup(groupid)
                                      detectprofile["id"] = ""+str(gm.id)
                                      #print(detectprofile["id"])
                                      lmid=[m.mid for m in gm.members]
                                      data=[]
                                      for i in lmid:
                                        a=client.getContact(i)
                                        mb=a.mid
                                        nb=a.displayName
                                        bb=a.statusMessage
                                        cb = client.getProfileCoverURL(i)
                                        pb="https://obs.line-scdn.net/"+str(a.pictureStatus)
                                        data.append({""+str(mb):{"name":nb,"bio":bb,"foto":pb,"cover":cb}})
                                      result={""+str(groupid):data}
                                      f = codecs.open("jsons/hayden/detect2.json","w","utf-8")
                                      json.dump(result, f, sort_keys=True, indent=4, ensure_ascii=False)
                                      if groupid in detectprofile["detectprofile"]:                                      
                                         client.sendMessage(to, "Mode dup on in grup " + str(gm.name))
                                      else:
                                        detectprofile["detectprofile"].append(groupid)
                                        client.sendMessage(to, "ready on in grup " + str(gm.name))
                                  except:
                                      pass
                            elif cmd.startswith("detectupoff "):
                                  separate = text.split(" ")
                                  number = text.replace(separate[0] + " ","")
                                  groups = client.getGroupIdsJoined()
                                  try:
                                      groupid = groups[int(number)-1]
                                      detectprofile["id"] = ""
                                      result = {"data":"kosong"}
                                      f = codecs.open("jsons/hayden/detect2.json","w","utf-8")
                                      json.dump(result, f, sort_keys=True, indent=4, ensure_ascii=False)
                                      if groupid not in detectprofile["detectprofile"]:                                      
                                         client.sendMessage(to, "Mode dup off")
                                      else:
                                        detectprofile["detectprofile"].remove(groupid)
                                        client.sendMessage(to, "ready off")
                                  except:
                                      pass
                                      
                            elif cmd.startswith("chatgrup "):
                                  hk = msg.text.split(" ")
                                  spl = msg.text.replace(hk[0] + " ","")
                                  dan = spl.split("|")
                                  groups = client.getGroupIdsJoined()
                                  try:
                                      listGroup = groups[int(dan[0])-1]
                                      group = client.getGroup(listGroup)
                                      client.sendMessage(group.id, dan[1])
                                      client.sendMessage(to, "╭──「 Chat Group 」\n│ Success Chat to Group:\n│ {}\n╰──────────".format(group.name))#, Name, ticket, pict)
                                  except Exception as e:
                                    client.sendMessage(msg.to, str(e))
                                  #except:
                                   #   pass
                                    
                            elif cmd.startswith("mentionfake "):
                                #if msg.toType == 2:
                                    sep = text.split(" ")
                                    number = text.replace(sep[0] + " ","")
                                    groups = client.getGroupIdsJoined()
                                    no = 0
                                    try:
                                        group = groups[int(number)-1]
                                        G = client.getGroup(group)
                                        mem = [mem.mid for mem in G.members]
                                        if len(mem) >= 300:
                                          pass
                                        else:
                                          sid = str(settings["Addstickertag"]["sid"])   
                                          spkg = str(settings["Addstickertag"]["spkg"])
                                          client.fake_mention1(G.id, sid,spkg,mem)
                                          client.sendMessage(to,"sukses")
                                    except:
                                        pass
                            elif cmd.startswith("leavenamegrup "):
                                  hk = msg.text.split(" ")
                                  spl = msg.text.replace(hk[0] + " ","")
                                  for i in cl.getGroupIdsJoined():
                                      h = cl.getGroup(i).name
                                      if h == spl:
                                          print("leavegroup " + cl.getGroup(i).name)
                                          time.sleep(0.9)
                                          cl.leaveGroup(i)
                                  client.sendMessage(to,"Sukses keluar group: "+h)
#==============================================================================#
#==============================================================================#
#==============================================================================#
#==============================================================================#
#==============================================================================#
#==============================================================================#
#==============================================================================#
#==============================================================================#                                                                                                                                                                                                                                                                                                                                                                
                            elif cmd == "speed":
                                start = time.time()
                                time.sleep(0.001)
                                print(start)
                                #client.sendReplyMessage(msg_id,to, "Benchmarking...")
                                elapsed_time = time.time() - start
                                client.sendMessage(to, "Speed Bot\n{}".format(str(elapsed_time)))
                            elif cmd == "runtime":
                                #tz = pytz.timezone("Asia/Jakarta")
                                #timeNow = datetime.now(tz=tz)
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                #runtime = "{}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                runtime = format_timespan(runtime)
                                client.sendReplyMessage(msg_id,to, "Bot sudah berjalan selama {}".format(str(runtime)))
                            elif cmd == "restart":
                                client.sendReplyMessage(msg_id,to, "Berhasil merestart Bot")
                                restartBot()
                            elif cmd == 'remove':
                                try:
                                    client.removeAllMessages(op.param2)
                                    client.sendMessage(msg.to, "Sudah terhapus semua...")
                                except:
                                    pass
                            elif cmd == 'errorlog':
                                try:
                                    with open('logError.txt', 'r') as er:
                                        error = er.read()
                                    client.sendReplyMessage(msg_id,to, str(error))
                                except:
                                    pass
                            elif cmd == 'reseterror':
                                with open('logError.txt', 'w') as er:
                                    er.write("")
                                client.sendReplyMessage(msg_id,to, "Sukses reset errorlog")
# Pembatas Script #
                            elif cmd == "like on":
                                settings["likeOn"] = True
                                client.sendReplyMessage(msg_id,to, "Berhasil mengaktifkan auto like")
                            elif cmd == "like off":
                                settings["likeOn"] = False
                                client.sendReplyMessage(msg_id,to, "Berhasil menonaktifkan auto like")
                            elif cmd == "block on":
                                settings["autoBlock"] = True
                                client.sendReplyMessage(msg_id,to, "Berhasil mengaktifkan auto block")
                            elif cmd == "block off":
                                settings["autoBlock"] = False
                                client.sendReplyMessage(msg_id,to, "Berhasil menonaktifkan auto block")
                            elif cmd == "add on":
                                settings["autoAdd"] = True
                                client.sendReplyMessage(msg_id,to, "Berhasil mengaktifkan auto add")
                            elif cmd == "add off":
                                settings["autoAdd"] = False
                                client.sendReplyMessage(msg_id,to, "Berhasil menonaktifkan auto add")
                            elif cmd == "join on":
                                settings["autoJoin"] = True
                                client.sendReplyMessage(msg_id,to, "Berhasil mengaktifkan auto join")
                            elif cmd == "join off":
                                settings["autoJoin"] = False
                                client.sendReplyMessage(msg_id,to, "Berhasil menonaktifkan auto join")
                            elif cmd == "leave on":
                                settings["autoLeave"] = True
                                client.sendReplyMessage(msg_id,to, "Berhasil mengaktifkan auto leave")
                            elif cmd == "leave off":
                                settings["autoLeave"] = False
                                client.sendReplyMessage(msg_id,to, "Berhasil menonaktifkan auto leave")
                            elif cmd == "rescall on":
                                settings["responGc"] = True
                                client.sendReplyMessage(msg_id,to, "Mengaktifkan auto respon panggilan")
                            elif cmd == "rescall off":
                                settings["responGc"] = False
                                client.sendReplyMessage(msg_id,to, "Menonaktifkan auto respon panggilan")
                            elif cmd == "resfo on":
                                settings["detectMentionfo"] = True
                                client.sendReplyMessage(msg_id,to, "Mengaktifkan auto respon foto")
                            elif cmd == "resfo off":
                                settings["detectMentionfo"] = False
                                client.sendReplyMessage(msg_id,to, "Menonaktifkan auto respon foto")
                            elif cmd == "restik on":
                                settings["detectMentiontik"] = True
                                client.sendReplyMessage(msg_id,to, "Mengaktifkan auto respon tikel")
                            elif cmd == "restik off":
                                settings["detectMentiontik"] = False
                                client.sendReplyMessage(msg_id,to, "Menonaktifkan auto respon tikel")
                            elif cmd == "reskick on":
                                settings["detectMentionkik"] = True
                                client.sendReplyMessage(msg_id,to, "Mengaktifkan auto respon kick")
                            elif cmd == "reskick off":
                                settings["detectMentionkik"] = False
                                client.sendReplyMessage(msg_id,to, "Menonaktifkan auto respon kick")
                            elif cmd == "restag on":
                                settings["detectMentiontag"] = True
                                client.sendReplyMessage(msg_id,to, "Mengaktifkan auto respon tag")
                            elif cmd == "restag off":
                                settings["detectMentiontag"] = False
                                client.sendReplyMessage(msg_id,to, "Menonaktifkan auto respon tag")
                            elif cmd == "respm on":
                                settings["autoRespon"] = True
                                client.sendReplyMessage(msg_id,to, "Berhasil mengaktifkan auto respon pm")
                            elif cmd == "respm off":
                                settings["autoRespon"] = False
                                client.sendReplyMessage(msg_id,to, "Berhasil menonaktifkan auto respon pm")
                            elif cmd == "read on":
                                settings["autoRead"] = True
                                client.sendReplyMessage(msg_id,to, "Berhasil mengaktifkan auto read")
                            elif cmd == "read off":
                                settings["autoRead"] = False
                                client.sendReplyMessage(msg_id,to, "Berhasil menonaktifkan auto read")
                            elif cmd == "jointicket on":
                                settings["autoJoinTicket"] = True
                                client.sendReplyMessage(msg_id,to, "Berhasil mengaktifkan auto join by ticket")
                            elif cmd == "jointicket off":
                                settings["autoJoinTicket"] = False
                                client.sendReplyMessage(msg_id,to, "Berhasil menonaktifkan auto join by ticket")
                            elif cmd == "contact on":
                                settings["checkContact"] = True
                                client.sendReplyMessage(msg_id,to, "Berhasil mengaktifkan check details contact")
                            elif cmd == "contact off":
                                settings["checkContact"] = False
                                client.sendReplyMessage(msg_id,to, "Berhasil menonaktifkan check details contact")
                            elif cmd == "post on":
                                settings["checkPost"] = True
                                client.sendReplyMessage(msg_id,to, "Berhasil mengaktifkan check details post")
                            elif cmd == "post off":
                                settings["checkPost"] = False
                                client.sendReplyMessage(msg_id,to, "Berhasil menonaktifkan check details post")
                            elif cmd == "sticker on":
                                settings["checkSticker"] = True
                                client.sendReplyMessage(msg_id,to, "Berhasil mengaktifkan check details sticker")
                            elif cmd == "sticker off":
                                settings["checkSticker"] = False
                                client.sendReplyMessage(msg_id,to, "Berhasil menonaktifkan check details sticker")
                            elif cmd == "unsend on":
                                settings["cekUnsend"] = True
                                client.sendReplyMessage(msg_id,to, "Berhasil mengaktifkan check details unsend")
                            elif cmd == "unsend off":
                                settings["cekUnsend"] = False
                                client.sendReplyMessage(msg_id,to, "Berhasil menonaktifkan check details unsend")
                            elif cmd == "status":
                                try:
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    ret_ = "╔═══════════\n║ Setting\n╠═══════════"
                                    if settings["autoAdd"] == True: ret_ += "\n╠ 🔓 Add"
                                    else: ret_ += "\n╠ 🔒 Add"
                                    if settings["autoBlock"] == True: ret_ += "\n╠ 🔓 Block"
                                    else: ret_ += "\n╠ 🔒 Block"
                                    if settings["autoJoin"] == True: ret_ += "\n╠ 🔓 Join"
                                    else: ret_ += "\n╠ 🔒 Join"
                                    if settings["autoLeave"] == True: ret_ += "\n╠ 🔓 Leave"
                                    else: ret_ += "\n╠ 🔒 Leave"
                                    if settings["autoJoinTicket"] == True: ret_ += "\n╠ 🔓 JoinTicket"
                                    else: ret_ += "\n╠ 🔒 JoinTicket"
                                    if settings["autoRead"] == True: ret_ += "\n╠ 🔓 Read"
                                    else: ret_ += "\n╠ 🔒 Read"
                                    if settings["likeOn"] == True: ret_ += "\n╠ 🔓 Like"
                                    else: ret_ += "\n╠ 🔒 Like"
                                    if settings["responGc"] == True: ret_ += "\n╠ 🔓 Rescall"
                                    else: ret_ += "\n╠ 🔒 Rescall"
                                    if settings["autoRespon"] == True: ret_ += "\n╠ 🔓 Respm"
                                    else: ret_ += "\n╠ 🔒 Respm"
                                    if settings["detectMentionfo"] == True: ret_ += "\n╠ 🔓 Resfo"
                                    else: ret_ += "\n╠ 🔒 Resfo"
                                    if settings["detectMentiontik"] == True: ret_ += "\n╠ 🔓 Restik"
                                    else: ret_ += "\n╠ 🔒 Restik"
                                    if settings["detectMentionkik"] == True: ret_ += "\n╠ 🔓 Reskick"
                                    else: ret_ += "\n╠ 🔒 Reskick"
                                    if settings["detectMentiontag"] == True: ret_ += "\n╠ 🔓 Restag"
                                    else: ret_ += "\n╠ 🔒 Restag"
                                    if settings["checkContact"] == True: ret_ += "\n╠ 🔓 Contact"
                                    else: ret_ += "\n╠ 🔒 Contact"
                                    if settings["checkPost"] == True: ret_ += "\n╠ 🔓 Post"
                                    else: ret_ += "\n╠ 🔒 Post"
                                    if settings["checkSticker"] == True: ret_ += "\n╠ 🔓 Sticker"
                                    else: ret_ += "\n╠ 🔒 Sticker"
                                    if settings["Sambutan"] == True: ret_ += "\n╠ 🔓 Sambut"
                                    else: ret_ += "\n╠ 🔒 Sambut"
                                    if settings["cekUnsend"] == True: ret_ += "\n╠ 🔓 Unsend"
                                    else: ret_ += "\n╠ 🔒 Unsend"
                                    ret_ += "\n╠═══════════\n║ Day : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n║ Time [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n╚═══════════"
                                    client.sendReplyMessage(msg_id,to, str(ret_))
                                except Exception as e:
                                    client.sendMessage(msg.to, str(e))
# Pembatas Script #
                            elif cmd.startswith("cn:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = client.getProfile()
                                    profile.displayName = string
                                    client.updateProfile(profile)
                                    nama = "Sukses Mengganti nama\nMenjadi : {}".format(string)
                                    #sendTextTemplate1(to, nama)
                                    client.sendReplyMessage(msg_id,to,"Berhasil mengganti display name menjadi {}".format(str(string)))
                            elif cmd.startswith("cb:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = client.getProfile()
                                    profile.statusMessage = string
                                    client.updateProfile(profile)
                                    bio = "Sukses Mengganti status Menjadi\n{}".format(string)
                                    #sendTextTemplate1(to, bio)
                                    client.sendReplyMessage(msg_id,to,"Berhasil mengganti status message menjadi{}".format(str(string)))

                            elif cmd == "me":
                                client.sendContact(to, sender)
                                Musik1(to, sender)
                            elif cmd == "mid":
                                client.sendReplyMessage(msg_id,to, "{}".format(sender))
                            elif cmd == "name":
                                contact = client.getContact(sender)
                                client.sendReplyMessage(msg_id,to, "{}".format(contact.displayName))
                            elif cmd == "bio":
                                contact = client.getContact(sender)
                                client.sendReplyMessage(msg_id,to, "{}".format(contact.statusMessage))
                            elif cmd == "pict":
                                contact = client.getContact(sender)
                                client.sendImageWithURL(to,"https://obs.line-scdn.net/{}".format(contact.pictureStatus))
                            elif cmd == "cover":
                                contact = client.getContact(sender)
                                home = client.getProfileCoverDetail(sender)
                                if "videoCoverObsInfo" in home['result']:
                                  vc = "https://obs.line-scdn.net/r/myhome/vc/"+home['result']['videoCoverObsInfo']['objectId']
                                  c = "https://obs.line-scdn.net/r/myhome/c/"+home['result']['videoCoverObsInfo']['objectId']
                                  sendIL(to,c)
                                  sendVLP(to,vc,c)
                                else:
                                  c = "https://obs.line-scdn.net/r/myhome/c/"+home['result']['videoCoverObsInfo']['objectId']
                                  sendIL(to,c)
                            elif cmd == "video":
                                    h = client.getContact(clientMid)
                                    if h.videoProfile == None:
                                    	return client.sendMessage(to,"You Not Have Video Profile.")
                                    client.sendVideoWithURL(to,"https://obs.line-scdn.net/" + h.pictureStatus + "/vp")
                            elif cmd == 'detail':
                                a = client.getContact(sender)
                                userid = "https://line.me/ti/p/~" + client.profile.userid
                                namamu = a.displayName
                                biomu = a.statusMessage
                                midmu = a.mid
                                sendMention(to,'',[sender])
                                client.sendMessage(to,None,contentMetadata={'vCard': 'BEGIN:VCARD\r\nVERSION:3.0\r\nPRODID:ANDROID 8.13.3 Android OS 4.4.4\r\nFN:\\'+client.getContact(sender).displayName+'\nTEL;TYPE=mobile:'+client.getContact(sender).statusMessage+'\r\nN:?;\\,\r\nEND:VCARD\r\n', 'displayName': client.getContact(sender).displayName},contentType=13)
                                client.sendContact(to,midmu)
                                Musik1(to,midmu)
                                cdet(to,midmu)
                                pdet(to,midmu)
                                                                    
                            elif cmd.startswith("timeline "):
                                  hk = msg.text.split(" ")
                                  spl = msg.text.replace(hk[0] + " ","")
                                  a=client.createPost("{}".format(spl))
                                  client.sendMessage(to,"Sukses create timeline")
                            elif cmd == "tagtimeline" and sender == clientMid:
                                TimelineCreate(to,msg,cmd)
                                
                            elif cmd == "clearfriend":
                                n = len(client.getAllContactIds())
                                try:
                                    client.clearContacts()
                                except: 
                                    pass
                                t = len(client.getAllContactIds())
                                client.sendReplyMessage(msg_id,msg.to,"Type: Friendlist\n • Detail: Clear Contact\n • Before: %s Friendlist\n • After: %s Friendlist\n • Total removed: %s Friendlist\n • Status: Succes.."%(n,t,(n-t)))
                            elif cmd.startswith("delfriend "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                       if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.deleteContact(ls)
                                    client.sendReplyMessage(msg_id,to, "Success Del " + str(contact.displayName) + " to Friendlist")
                            elif cmd.startswith("addfriend "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                       if mention["M"] not in lists:
                                          lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.findAndAddContactsByMid(ls)
                                    client.sendReplyMessage(msg_id,to, "Success Add " + str(contact.displayName) + " to Friendlist")
                            elif cmd == "friendlist":
                                contactlist = client.getAllContactIds()
                                kontak = client.getContacts(contactlist)
                                num=1
                                msgs="「 Friend List 」\n"
                                for ids in kontak:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\nTotal Friend : %i" % len(kontak)
                                msgs+= "\nUsage : {}Friendinfo「 number 」".format(setKey)
                                client.sendReplyMessage(msg_id,to, msgs)
                            elif cmd.startswith("unfriend "):
                                separate = msg.text.split(" ")
                                number = msg.text.replace(separate[0] + " ","")
                                contactlist = client.getAllContactIds()
                                try:
                                    contact = contactlist[int(number)-1]
                                    friend = client.getContact(contact)
                                    client.deleteContact(contact)
                                    client.sendReplyMessage(msg_id,to, "Success menghapus teman " + str(friend.displayName) + " to Friendlist")
                                except Exception as e:
                                    client.sendMessage(msg.to, str(e))
                                    
                            elif cmd.startswith("friendinfo "):
                                number = removeCmd("friendinfo", text)
                                contactlist = client.getAllContactIds()
                                try:
                                    contact = contactlist[int(number)-1]
                                    friend = client.getContact(contact)
                                    cu = client.getProfileCoverURL(contact)
                                    path = str(cu)
                                    image = "https://obs.line-scdn.net/" + friend.pictureStatus
                                    try:
                                        client.sendReplyMessage(msg_id,to, "「 Friend Info 」\n" + "\nNama : " + friend.displayName + "\nBio : " + friend.statusMessage + "\nMid : " + friend.mid)
                                        client.sendImageWithURL(to,image)
                                        client.sendImageWithURL(to,path)
                                        client.sendContact(to, friend.mid)
                                    except:
                                        pass
                                except Exception as error:
                                    client.sendMessage(to, "「 Result Error 」\n" + str(error))
                            elif cmd.startswith("chatfriend"):
                                  hk = msg.text.split(" ")
                                  spl = msg.text.replace(hk[0] + " ","")
                                  dan = text.split("|")
                                  frs = client.getAllContactIds()
                                  try:
                                      listFriend = frs[int(dan[1])-1]
                                      friend = client.getContact(listFriend)
                                      client.sendMessage(friend.mid, dan[2])
                                      client.sendMessage(to, "╭──「 Chat Friend 」\n│ Success Friend to Group:\n│ {}\n╰──────────".format(friend.displayName))#, Name, ticket, pict)
                                  except:
                                      pass
                            elif cmd.startswith("addblock "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                       if mention["M"] not in lists:
                                          lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.blockContact(ls)
                                    client.sendReplyMessage(msg_id,to, "Success Block " + str(contact.displayName) + " to Blocklist")
                            elif cmd == "blocklist":
                                contactlist = client.getBlockedContactIds()
                                kontak = client.getContacts(contactlist)
                                num=1
                                msgs="「 Block List 」\n"
                                for ids in kontak:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\nTotal Block : %i" % len(kontak)
                                msgs+= "\nUsage : {}Blockinfo「 number 」".format(setKey)
                                client.sendReplyMessage(msg_id,to, msgs)
                            elif cmd.startswith("unblock "):
                                separate = msg.text.split(" ")
                                number = msg.text.replace(separate[0] + " ","")
                                #number = removeCmd("blockinfo", text)
                                contactlist = client.getBlockedContactIds()
                                try:
                                    contact = contactlist[int(number)-1]
                                    friend = client.getContact(contact)
                                    client.unblockContact(contact)
                                    client.sendReplyMessage(msg_id,to,"Blokiran sudah dibuka: "+ str(friend.displayName))
                                except Exception as error:
                                    client.sendMessage(to, "「 Result Error 」\n" + str(error))
                            elif cmd.startswith("blockinfo "):
                                number = removeCmd("blockinfo", text)
                                contactlist = client.getBlockedContactIds()
                                try:
                                    contact = contactlist[int(number)-1]
                                    friend = client.getContact(contact)
                                    cu = client.getProfileCoverURL(contact)
                                    path = str(cu)
                                    image = "https://obs.line-scdn.net/" + friend.pictureStatus
                                    try:
                                        client.sendReplyMessage(msg_id,to,"「 Block Info 」\n\n" + "Name : " + friend.displayName + "\nStatus : " + friend.statusMessage + "\nMid : " + friend.mid)
                                        client.sendImageWithURL(to,image)
                                        client.sendImageWithURL(to,path)
                                        client.sendContact(to, friend.mid)
                                    except:
                                        pass
                                except Exception as error:
                                    client.sendMessage(to, "「 Result Error 」\n" + str(error))
                            elif cmd.startswith("favoriteinfo "):
                                text = removeCmd("favoriteinfo", text)
                                separate = text.split(" ")
                                number = text.replace(separate[0] + " ", text)
                                contactlist = client.getFavoriteMids()
                                try:
                                    contact = contactlist[int(number)-1]
                                    friend = client.getContact(contact)
                                    cu = client.getProfileCoverURL(contact)
                                    path = str(cu)
                                    image = "https://obs.line-scdn.net/" + friend.pictureStatus
                                    try:
                                        client.sendReplyMessage(msg_id,to,"「 Favorite Info」\n\n" + "Name : " + friend.displayName + "\nStatus : " + friend.statusMessage + "\nMid : " + friend.mid)
                                        client.sendImageWithURL(to,image)
                                        client.sendImageWithURL(to,path)
                                        client.sendContact(to, friend.mid)
                                    except:
                                        pass
                                except Exception as error:
                                    client.sendMessage(to, "Result Error\n" + str(error))
                                
                            elif cmd == "favoritelist":
                                contactlist = client.getFavoriteMids()
                                kontak = client.getContacts(contactlist)
                                num=1
                                msgs="「 Favorite List 」\n"
                                for ids in kontak:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\n「 Total Favoritelist : %i 」" % len(kontak)
                                msgs+= "\nUsage : {}FavoriteInfo「 number 」".format(setKey)
                                client.sendReplyMessage(msg_id,to, msgs)
                                    
                            elif cmd.startswith("scontact "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        mi_d = contact.mid
                                        client.sendContact(msg.to, mi_d)
                            elif cmd.startswith("smid "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendReplyMessage(msg_id,to, "{}".format(str(contact.mid)))
                            elif cmd.startswith("sname "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendReplyMessage(msg_id,to, "{}".format(str(contact.displayName)))
                            elif cmd.startswith("sbio "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendReplyMessage(msg_id,to, "{}".format(str(contact.statusMessage)))
                                        
                            elif cmd.startswith("spict"):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        path = "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                                        client.sendImageWithURL(to, str(path))
                            elif cmd.startswith("svideo "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        path = "https://obs.line-scdn.net/{}/vp".format(contact.pictureStatus)
                                        client.sendVideoWithURL(to, str(path))
                            elif cmd.startswith("smusic "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        midd = contact.mid
                                        Musik1(to.midd)
                            elif cmd.startswith("scover "):
                                if client != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            home = client.getProfileCoverDetail(ls)
                                            if "videoCoverObsInfo" in home['result']:
                                              cv = "https://obs.line-apps.com/r/myhome/vc/"+home['result']['videoCoverObsInfo']['objectId']
                                              c = "https://obs.line-apps.com/r/myhome/c/"+home['result']['coverObsInfo']['objectId']
                                              sendIL(to,c)
                                              sendVLP(to,cv,c)
                                            else:
                                              c = "https://obs.line-apps.com/r/myhome/c/"+home['result']['coverObsInfo']['objectId']
                                              sendIL(to,c)
                            elif cmd.startswith("srename "):
                                separate = msg.text.split(" ")
                                sam = msg.text.replace(separate[0]+" ","")                                
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    sam1 = sam.split("|")
                                    kata1 = str(sam1[0])
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        midd = contact.mid
                                        client.renameContact(midd,kata1)
                                        client.sendMessage(to,"Sukses rename : {} menjadi {}".format(str(contact.displayName),str(kata1)))
                            elif cmd.startswith("sdetail "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        a = client.getContact(ls)
                                        userid = "https://line.me/ti/p/~" + client.profile.userid
                                        namamu = a.displayName
                                        biomu = a.statusMessage
                                        midmu = a.mid
                                        fotomu = "https://obs.line-scdn.net/{}".format(a.pictureStatus)
                                        covermu = client.getProfileCoverURL(ls)
                                        sendMention(to,'',[ls])
                                        client.sendMessage(to,None,contentMetadata={'vCard': 'BEGIN:VCARD\r\nVERSION:3.0\r\nPRODID:ANDROID 8.13.3 Android OS 4.4.4\r\nFN:\\'+client.getContact(ls).displayName+'\nTEL;TYPE=mobile:'+client.getContact(ls).statusMessage+'\r\nN:?;\\,\r\nEND:VCARD\r\n', 'displayName': client.getContact(ls).displayName},contentType=13)
                                        client.sendContact(to,midmu)
                                        Musik1(to,midmu)
                                        client.sendMessage(to,'Nama : '+namamu+'\nBio : '+biomu+'\nMid : '+midmu+'\nLink foto : '+fotomu+'\nLink cover : '+covermu)
                                        client.sendImageWithURL(to,fotomu)
                                        client.sendImageWithURL(to,covermu)
                            elif cmd == "tagbyone":
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    nama = [contact.mid for contact in group.members]
                                    for i in nama:
                                        ps = "{}".format(i)
                                        tagdia(msg.to, "@!",ps,[i])
                                else:
                                    gr = client.getGroup(to)
                                    mbr = [mem.mid for mem in gr.members]
                                    for c in mbr:
                                        anu = client.getContact(c)
                                        text = "{}".format(anu.displayName)
                                        icon = "https://obs.line-scdn.net/{}".format(anu.pictureStatus)
                                        name = "{}".format(anu.displayName)
                                        sendMessageCustom(to, text, icon, name)
                            elif cmd == "cme":
                                 client.sendContact(to,receiver)
                            elif cmd == "cmid":
                                  contact = client.getContact(receiver)#sender
                                  midd = contact.mid
                                  client.sendMessage(to,midd)
                            elif cmd == "cbio":
                                  contact = client.getContact(receiver)
                                  client.sendMessage(to,"{}".format(contact.statusMessage))                                                                
                            elif cmd == "cname":
                                  contact = client.getContact(receiver)
                                  client.sendMessage(to,"{}".format(contact.displayName))                                                                
                            elif cmd == "cpict":
                                  contact = client.getContact(receiver)
                                  client.sendImageWithURL(to,"https://obs.line-scdn.net/{}".format(contact.pictureStatus))                                                                
                            elif cmd.startswith("ccover "):
                                            separate = msg.text.split(" ")
                                            sam = msg.text.replace(separate[0]+" ","")                                
                                            home = client.getProfileCoverDetail(str(sam))
                                            if "videoCoverObsInfo" in home['result']:
                                              cv = "https://obs.line-apps.com/r/myhome/vc/"+home['result']['videoCoverObsInfo']['objectId']
                                              c = "https://obs.line-apps.com/r/myhome/c/"+home['result']['coverObsInfo']['objectId']
                                              sendIL(to,c)
                                              sendVLP(to,cv,c)
                                            else:
                                              c = "https://obs.line-apps.com/r/myhome/c/"+home['result']['coverObsInfo']['objectId']
                                              sendIL(to,c)
                            elif cmd.startswith("ctag"):
                                  sep = text.replace("ctag","")
                                  gege = sep.split(" ")
                                  num = int(gege[1])
                                  contact = client.getContact(receiver)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  ry = str(contact.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x \n"
                                  xlen = str(len(zxc))
                                  xlen2 = str(len(zxc)+len(pesan2))
                                  zx = {'S':xlen, 'E':xlen2, 'M':contact.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = zxc + ""
                                  for var in range(0,num):
                                    client.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)                                  
                            elif cmd == "cmusik":
                                  Musik1(to,receiver)
                            elif cmd == 'cdetail':
                                a = client.getContact(receiver)
                                userid = "https://line.me/ti/p/~" + client.profile.userid
                                namamu = a.displayName
                                biomu = a.statusMessage
                                midmu = a.mid
                                fotomu = ("https://obs.line-scdn.net/{}".format(a.pictureStatus))
                                covermu = client.getProfileCoverURL(receiver)
                                sendMention(to,'',[receiver])
                                client.sendMessage(to,None,contentMetadata={'vCard': 'BEGIN:VCARD\r\nVERSION:3.0\r\nPRODID:ANDROID 8.13.3 Android OS 4.4.4\r\nFN:\\'+client.getContact(receiver).displayName+'\nTEL;TYPE=mobile:'+client.getContact(receiver).statusMessage+'\r\nN:?;\\,\r\nEND:VCARD\r\n', 'displayName': client.getContact(receiver).displayName},contentType=13)
                                client.sendContact(to,midmu)
                                Musik1(to,midmu)
                                client.sendMessage(to,'Nama : '+namamu+'\nBio : '+biomu+'\nMid : '+midmu+'\nLink foto : '+fotomu+'\nLink cover : '+covermu)
                                client.sendImageWithURL(to,fotomu)
                                client.sendImageWithURL(to,covermu)
                            elif cmd == "convert":
                                cvt = "Cv-ca 「 Video keke Audio 」"
                                cvt += "\nCv-cf 「 Video keke File 」"
                                cvt += "\nCa-cv 「 Audio keke Video 」"
                                cvt += "\nCa-cf 「 Audio keke File 」"
                                cvt += "\nCf-cv 「 File keke Video 」"
                                cvt += "\nCv-ca 「 File keke Audio 」"
                                client.sendMessage(to, str(cvt))
                                
                            elif cmd == "cv-ca":
                                simple["convertAudio"][msg._from] = True
                                client.sendMessage(msg.to,"Send Videonya...")
                                
                            elif cmd == "cv-cf":
                                simple["convertVideoFile"][msg._from] = True
                                client.sendMessage(msg.to,"Send Videonya...")
                                
                            elif cmd == "ca-cv":
                                simple["convertVideo"][msg._from] = True
                                client.sendMessage(msg.to,"Send Audionya...")
                                
                            elif cmd == "ca-cf":
                                simple["convertAudioFile"][msg._from] = True
                                client.sendMessage(msg.to,"Send Audionya...")
                                
                            elif cmd == "cf-cv":
                                simple["convertFileVideo"][msg._from] = True
                                client.sendMessage(msg.to,"Send File Videonya...")
                                
                            elif cmd == "cf-ca":
                                simple["convertFileAudio"][msg._from] = True
                                client.sendMessage(msg.to,"Send File Audionya...")
                                
                            elif cmd == "cpp":
                                settings["changePictureProfile"] = True
                                client.sendReplyMessage(msg_id,to, "Silahkan kirim gambarnya")
                                            
                            elif cmd.startswith("cpc "):
                                separate = text.split(" ")
                                url = text.replace(separate[0] + " ","")
                                urls="image.jpg"
                                client.downloadFileURL(url,saveAs=urls)
                                client.updateProfileCover(urls)
                                client.sendMessage(to,"sukses")
                                
                            elif cmd == "cgp":
                                if msg.toType == 2:
                                    if to not in settings["changeGroupPicture"]:
                                        settings["changeGroupPicture"].append(to)
                                    client.sendReplyMessage(msg_id,to, "Silahkan kirim gambarnya")
                                
                            elif cmd == "cvp":
                                simple["ChangeVideoProfilevid"][msg._from] = True
                                client.sendMessage(msg.to,"Send Videonya...")
                                    
                            elif cmd.startswith("cvp2 "):
                                link = removeCmd("cvp2", text)
                                contact = client.getContact(sender)
                                client.sendMessage(to,"Sedang Mendownload Data ~")
                                pic = "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                                subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
                                pict = client.downloadFileURL(pic)
                                vids = "TeamAnuBot.mp4"
                                time.sleep(3)
                                changeVideoAndPictureProfile(pict, vids)
                                client.sendMessage(to, "Succes ~")
                                  
                                
                            elif cmd.startswith("cvc2 "):
                                link = removeCmd("cvc2", text)
                                cId = client.getProfileCoverId(sender)
                                client.sendMessage(to,"Sedang Mendownload Data ~")
                                vids = "HkBot.mp4"
                                client.downloadFileURL(link, saveAs=vids)
                                client.updateProfileCoverVideo(vids)
                                client.sendMessage(to, "Succes ~")
                                
                            elif cmd.startswith("cpc2 "):
                                link = removeCmd("cpc2", text)
                                cId = client.getProfileCoverId(sender)
                                client.sendMessage(to,"Sedang Mendownload Data ~")
                                vids = "Hk.jpg"
                                client.downloadFileURL(link, saveAs=vids)
                                client.updateProfileCoverPicture(vids)
                                client.sendMessage(to, "Succes ~")
                                
                            elif cmd.startswith("cvpc1 "):
                                sep = text.split(" ")
                                kata = text.replace(sep[0] + " ","")
                                cari = kata.split("|")
                                kata1 = cari[0]
                                kata2 = cari[1]
                                client.sendMessage(to,"Sedang Mendownload Data ~")
                                pict="Hk.jpg"
                                client.downloadFileURL(kata1, saveAs=pict)
                                vids = "HkBot.mp4"
                                client.downloadFileURL(kata2, saveAs=vids)
                                client.updateProfileCoverPictureAndVideo(pict,vids)
                                client.sendMessage(to, "Succes ~")
                                
                            elif cmd.startswith("cvpc2 "):
                                sep = text.split(" ")
                                kata = text.replace(sep[0] + " ","")
                                cari = kata.split("/")                                    
                                kata1 = cari[-1]
                                if 'tiktok' in kata:
                                  client.sendMessage(to,"Sedang Mendownload Data ~")
                                  from cloudscraper import create_scraper
                                  cf = create_scraper(delay=10)
                                  ss=cf.get("https://ssstik.io").text
                                  b=re.findall('hx-post=\"(.*?)\"',ss)[0]
                                  post = BeautifulSoup(cf.post("https://ssstik.io"+b, data={"id": kata,"locale": "en","tt": 0,"ts": 0}).text,'lxml')
                                  link=post.find('a',{'class':'pure-button pure-button-primary is-center u-bl dl-button download_link without_watermark_direct'}).get('href')
                                  img=ezgifvideotogif(link)
                                  pict="Hk.jpg"
                                  client.downloadFileURL(img, saveAs=pict)
                                  vids = "HkBot.mp4"
                                  client.downloadFileURL(link, saveAs=vids)
                                  client.updateProfileCoverPictureAndVideo(pict,vids)
                                  client.sendMessage(to, "Succes ~")
                                else:
                                  cari = kata.split("/")                                    
                                  kata1 = cari[-1]
                                  client.sendMessage(to,"Sedang Mendownload Data ~")
                                  pict="Hk.jpg"
                                  client.downloadFileURL("https://i.ytimg.com/vi/{}/hqdefault.jpg".format(kata1), saveAs=pict)
                                  a=pafy.new(kata).getbest().url
                                  #subprocess.getoutput('youtube-dl --format mp4 --output HkBot.mp4 {}'.format(kata))
                                  vids = "HkBot.mp4"
                                  client.downloadFileURL(a, saveAs=vids)
                                  client.updateProfileCoverPictureAndVideo(pict,vids)
                                  client.sendMessage(to, "Succes ~")
                                
                            elif cmd.startswith("clone "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        x = clclientient.getContact(sender)
                                        f = x.mid
                                        g = x.displayName
                                        h = x.statusMessage
                                        i = "https://obs.line-scdn.net/{}".format(x.pictureStatus)
                                        imag = client.downloadFileURL(i, saveAs='tmp/foto.bin')
                                        j = client.getProfileDetail(f)['result']['objectId']
                                        databackup = {"nama":g,"status":h,"picture":imag,"cover":j}
                                        simpan = codecs.open("tmp/cbackup.json","w","utf-8")
                                        json.dump(databackup, simpan, sort_keys=True, indent=4, ensure_ascii=False)
                                        a = client.getContact(ls)
                                        b = a.mid
                                        c = a.displayName
                                        d = a.statusMessage
                                        e = "https://obs.line-scdn.net/{}".format(a.pictureStatus)
                                        img = client.downloadFileURL(e, saveAs='tmp/copy.jpg')
                                        clientProfile = client.getProfile()
                                        clientProfile.statusMessage,clientProfile.displayName = d,c
                                        coverId = client.getProfileDetail(b)['result']['objectId']
                                        client.updateProfileCoverById(coverId)
                                        client.updateProfile(clientProfile)
                                        client.updateProfilePicture(img)
                                        client.deleteFile(img)
                                        client.sendContact(to, b)
                            elif cmd == "restore":
                              f = codecs.open("tmp/cbackup.json","r","utf-8")
                              databackup = json.load(f)
                              a = databackup['nama']
                              b = databackup['status']
                              c = databackup['picture']
                              d = databackup['cover']
                              clientProfile = client.getProfile()
                              clientProfile.statusMessage,clientProfile.displayName = b,a
                              client.updateProfile(clientProfile)
                              client.updateProfileCoverById(d)
                              client.updateProfilePicture(c)
                              client.sendContact(to, sender)
                              with open("tmp/cbackup.json","w") as error:
                                  error.write("{}")
                                
# Pembatas Script #
                            elif cmd.startswith("cium "):
                                targets = []  
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                      try:
                                          client.kickoutFromGroup(to,[target])
                                      except:
                                          client.sendMessage(msg.to, "Limit kick")
                                
                            elif cmd.startswith("invitemid "):
                                separate = text.split(" ")
                                midd = text.replace(separate[0] + " ","")
                                client.findAndAddContactsByMid(midd)   
                                client.inviteIntoGroup(to,[midd])
                            elif cmd.startswith("invite "):
                                targets = []  
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                      try:
                                          #G = client.getContact(op.param1)
                                          client.findAndAddContactsByMid(target)   
                                          client.inviteIntoGroup(to,[target])
                                      except:
                                          client.sendMessage(msg.to, "Limit invite")
                            elif cmd == "cancel":
                                    if msg.toType == 2:
                                        group = client.getGroup(to)
                                        if group.invitee is None or group.invitee == []:
                                            client.sendMessage(to,"Not Pendings Invitation In Group "+group.name+".")
                                        else:
                                            invitee = [contact.mid for contact in group.invitee]
                                            for inv in invitee:
                                                time.sleep(1.5)
                                                client.cancelGroupInvitation(to, [inv])
                                            client.sendMessage(to,"Clear {} Pending.".format(str(len(invitee))))

                            elif cmd == "rejectall":
                              int1 = len(client.getGroupIdsInvited())
                              if int1 == 0:
                                  print("No groups inviting")
                              else:
                                  for groups in client.getGroupIdsInvited():
                                     #print("Reject " + cl.getGroup(groups).name)
                                      time.sleep(0.7)
                                      client.rejectGroupInvitation(groups)
                                  client.sendMessage(to,"You reject : " + str(int1) + " groups invitation")
                                  
                            elif "Pancal @" in msg.text:
                                  _name = text.replace("Pancal @","")
                                  _nametarget = _name.rstrip(" ")
                                  gs = client.getGroup(to)
                                  targets = []
                                  for g in gs.members:
                                      if _nametarget in g.displayName:
                                          targets.append(g.mid)
                                  if targets == []:
                                      client.sendMessage(to,"target tidak ada")
                                  else:
                                      for target in targets:
                                            try:
                                               client.kickoutFromGroup(to,[target])
                                            except Exception as error:
                                                  print (error)     
# Pembatas Script #                                
                            elif cmd == 'gid':
                                gid = client.getGroup(to)
                                client.sendReplyMessage(msg_id,to, "[ID Groupnya : ]\n" + gid.id)
                            elif cmd == 'gpict':
                                group = client.getGroup(to)
                                path = ("https://obs.line-scdn.net/{}".format(group.pictureStatus))
                                client.sendImageWithURL(to, path)
                            elif "Gn: " in msg.text:
                                if msg.toType == 2:
                                    X = client.getGroup(msg.to)
                                    X.name = msg.text.replace("Gn: ","")
                                    client.updateGroup(X)
                                else:
                                    client.sendMessage(msg.to,"It can't be used besides the group.")
                            elif cmd == 'gname':
                                gid = client.getGroup(to)
                                client.sendReplyMessage(msg_id,to, "[Nama Groupnya : ]\n" + gid.name)
                            elif cmd == "gcreator":
                              if msg.toType == 2:
                                  try:
                                      group = client.getGroup(to)
                                      GS = group.creator.mid
                                      client.sendContact(to, GS)
                                  except:
                                      pass
                            elif cmd == 'url':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        ticket = client.reissueGroupTicket(to)
                                        client.sendReplyMessage(msg_id,to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                                    else:
                                        client.sendReplyMessage(msg_id,to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                            elif cmd == 'buka':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        client.sendReplyMessage(msg_id,to, "Grup qr sudah terbuka")
                                    else:
                                        group.preventedJoinByTicket = False
                                        client.updateGroup(group)
                                        client.sendReplyMessage(msg_id,to, "Berhasil membuka grup qr")
                            elif cmd == 'tutup':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == True:
                                        client.sendReplyMessage(msg_id,to, "Grup qr sudah tertutup")
                                    else:
                                        group.preventedJoinByTicket = True
                                        client.updateGroup(group)
                                        client.sendReplyMessage(msg_id,to, "Berhasil menutup grup qr")
                            elif cmd == 'gmember':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    ret_ = "╔══[ Member List ]"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                                    client.sendReplyMessage(msg_id,to, str(ret_))
                            elif cmd == 'glist':
                                    groups = client.getGroupIdsJoined()
                                    #groups = client.groups
                                    ret_ = "╔══[ Group List ]"
                                    no = 0 + 1
                                    for gid in groups:
                                        group = client.getGroup(gid)
                                        ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                        no += 1
                                    ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                                    client.sendReplyMessage(msg_id,to, str(ret_))
                            elif cmd == "gpending":
                                  group = client.getGroup(to)
                                  ret_ = "「 List Pending 」\n"
                                  no = 0 + 1
                                  if group.invitee is None or group.invitee == []:
                                      client.sendReplyMessage(msg_id,to, "Tidak ada pendingan")
                                      return
                                  else:
                                      for pen in group.invitee:
                                          ret_ += "\n{}. {}".format(str(no), str(pen.displayName))
                                          no += 1
                                      ret_ += "\n\n「 Total Groups : {} 」".format(str(len(group.invitee)))
                                      client.sendReplyMessage(msg_id,to, str(ret_))
                            elif cmd == "ginfo":
                              if msg.toType == 2: 
                                group = client.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(group.id)))
                                timeCreated = time.strftime("%d-%m-%Y", time.localtime(int(group.createdTime) / 1000))
                                path = "https://obs.line-scdn.net/{}".format(group.pictureStatus)
                                ret_ = "[ Group Information ]"
                                ret_ += "\n Name Group : {}".format(group.name)
                                ret_ += "\n ID Group : {}".format(group.id)
                                ret_ += "\n Creator Group : {}".format(gCreator)
                                ret_ += "\n Group Created : {}".format(str(timeCreated))
                                ret_ += "\n Jumlah Member : {}".format(str(len(group.members)))
                                ret_ += "\n Jumlah Pending : {}".format(gPending)
                                ret_ += "\n Group QR : {}".format(gQr)
                                ret_ += "\n Group URL : {}".format(gTicket)
                                ret_ += "\n[ Success ]"
                                client.sendMessage(to, str(ret_))
                                client.sendImageWithURL(to, path)                             
                            #    
                            elif cmd.startswith("gcreate "):
                                #text = removeCmd("creategroup", text)
                                  sep = text.split(" ")
                                  name = text.replace(sep[0] + " ","")
                                  client.createGroup(name, [clientMid])
                                  gids = client.getGroupIdsByName(name)
                                  for gid in gids:
                                      try:
                                          x = client.getGroup(gid)
                                          x.preventedJoinByTicket = False
                                          client.updateGroup(x)
                                      except Exception as e:
                                          client.sendMessage(to, str(e))
                                  client.sendReplyMessage(msg_id,to, "Create Group {}\n\nQR : http://line.me/R/ti/g/{}".format(str(name), str(client.reissueGroupTicket(x.id))))
                                  
                            elif cmd.startswith("cekgrup ") and sender == clientMid: # udah     @ gc yg sama
                              if 'MENTION' in msg.contentMetadata.keys() != None:
                                names = re.findall(r'@(\w+)', text)
                                #print(names)
                                #print(text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                #print(mention)
                                mentionees = mention['MENTIONEES']
                                #print(mentionees)
                                G = client.getGroupIdsJoined()
                                cgroup = client.getGroups(G)
                                groups = client.groups
                                ngroup = ""
                                ngroup += "╔══[ Found In Group ]"
                                no = 0 + 1
                                num = 0
                                for mention in mentionees:
                                    for x in range(len(cgroup)):
                                        gMembMids = [contact.mid for contact in cgroup[x].members]
                                        #print(gMembMids)
                                        if mention['M'] in gMembMids:
                                            #print(mention['M'])
                                            ngroup += "\n╠ {}. {} | {}".format(str(no), str(cgroup[x].name), str(len(cgroup[x].members)))
                                            no += 1
                                            num += 1
                                    ngroup += "\n╚══[ Total {} Groups ]".format(str(num))
                                    sendFooter(to, str(ngroup))
                                if ngroup == "":
                                    sendFooter(to, "NOT FOUND")                                    
                            elif cmd == "tagnote" and sender == clientMid:
                                NoteCreate(to,msg,cmd)
                            elif cmd.startswith("createnote ") and sender == clientMid:
                                NoteCreate(to,msg,cmd)
                            elif cmd.startswith("getnote "):
                                sep = text.split(" ")
                                kata = text.replace(sep[0] + " ","")
                                tim=time.time()                                
                                idgrup=client.getGroup(to).id
                                data=client.getGroupPost(idgrup)
                                lists=[i['post']['contents'] for i in data['result']['feeds']]
                                listsdata=lists[int(kata)-1]
                                c=[i['post'] for i in data['result']['feeds']]
                                d=c[int(kata)]['userInfo']['userValid']
                                lik=c[int(kata)]['postInfo']['likeCount']
                                com=c[int(kata)]['postInfo']['commentCount']
                                cre=c[int(kata)]['postInfo']['createdTime']//1000
                                timcre=tim-cre
                                if d == True:
                                  nik=c[int(kata)]['userInfo']['nickname']
                                else:
                                  nik="Tidak Diketahui"
                                ret="note {}".format(kata)
                                ret+="\nname: {}".format(nik)
                                ret+="\nlike: {}".format(lik)
                                ret+="\ncomment: {}".format(com)
                                #ret+="\ncreate: {}".format(format_timespan(int(timcre)))
                                sendFooter(to,ret)
                                if 'text' in listsdata:
                                  sendFooter(to,listsdata["text"])
                                if 'media' in listsdata:
                                  if 'VIDEO' in listsdata['media'][0]['type']:
                                      vid="https://obs-us.line-apps.com/myhome/h/download.nhn?oid="+listsdata["media"][0]['objectId']
                                      pic="https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&oid="+listsdata["media"][0]['objectId']
                                      sendVLP(to,vid,pic)
                                  else:
                                      sendIL(to,"https://obs-us.line-apps.com/myhome/h/download.nhn?oid="+listsdata["media"][0]['objectId'])
                                if 'stickers' in listsdata:
                                  stid="https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker.png".format(listsdata["stickers"][0]["id"])
                                  sendIL(to,stid)

                            elif cmd == "getalbum":
                                lalbum=client.getGroupAlbum(to)
                                item=lalbum['result']['items']
                                ret="List album"
                                no=0
                                for litem in item:
                                  if "recentPhotos" in litem:
                                    no+=1
                                    ret+="\n"+str(no)+"."+str(litem['title'])+" ~ "+str(len(litem["recentPhotos"]))+" photo"
                                ret+="\n\nTotal album ada {}".format(len(item))
                                Print(to,ret)
                            elif cmd.startswith("createalbum "):
                                sep = text.split(" ")
                                nam = text.replace(sep[0] + " ","")
                                calbum=client.createGroupAlbum(to,nam)
                                ret='Owner: '+str(client.getContact(calbum['result']['items'][0]['owner']['mid']).displayName)
                                ret+='\nLimitpost: '+str(calbum['result']['items'][0]['photoCountLimit'])
                                ret+='\nStatus: '+str(calbum['result']['items'][0]['status'])
                                ret+='\nTitle: '+str(calbum['result']['items'][0]['title'])
                                Print(to,ret)
                                
                            elif cmd.startswith("deletealbum "):
                                sep = text.split(" ")
                                nam = text.replace(sep[0] + " ","")
                                lalbum=client.getGroupAlbum(to)
                                item=lalbum['result']['items']
                                for litem in item:
                                  if nam in litem['title']:
                                    idi=litem['id']
                                    dele=client.deleteGroupAlbum(to,idi)
                                    Print(to,dele['message'])   
                                    
                            elif cmd.startswith("changealbum "):
                                sep = text.split(" ")
                                nam = text.replace(sep[0] + " ","")
                                snam=nam.split('|')
                                lalbum=client.getGroupAlbum(to)
                                item=lalbum['result']['items']
                                for litem in item:
                                  if snam[0] in litem['title']:
                                    idi=litem['id']
                                    cha=client.changeGroupAlbumName(to,idi,snam[1])
                                    Print(to,cha['message']) 
                                    
                            elif cmd.startswith("addtoalbum "):
                                sep = text.split(" ")
                                nam = text.replace(sep[0] + " ","")
                                snam=nam.split('|')                                
                                lalbum=client.getGroupAlbum(to)
                                item=lalbum['result']['items']
                                for litem in item:
                                  if snam[0] in litem['title']:
                                    img = client.downloadFileURL(snam[1], saveAs='LineAPI/tmp/hkupload.jpg')
                                    idi=litem['id']
                                    #fil=open(img, 'rb').read()
                                    dele=client.addImageToAlbum(to,idi,"LineAPI/tmp/hkupload.jpg")
                                    Print(to,dele)   
                                    
                            elif cmd.startswith("imagealbum "):
                                sep = text.split(" ")
                                nam = text.replace(sep[0] + " ","")
                                snam=nam.split('|')                                
                                lalbum=client.getGroupAlbum(to)
                                item=lalbum['result']['items']
                                for litem in item:
                                  if snam[0] in litem['title']:
                                    ialbum=litem['id']
                                    oalbum=litem["recentPhotos"][int(snam[1])-1]["oid"]
                                    imgalbum ="LineAPI/tmp/tes.bin"
                                    ambil=client.getImageGroupAlbum(to,ialbum,oalbum,returnAs='bin',saveAs=imgalbum)
                                    client.sendImage(to,imgalbum)   
                            elif cmd.startswith("imageallalbum "):
                                sep = text.split(" ")
                                nam = text.replace(sep[0] + " ","")
                                lalbum=client.getGroupAlbum(to)
                                item=lalbum['result']['items']
                                for litem in item:
                                  if nam in litem['title']:
                                    for jum in range(0,int(len(litem["recentPhotos"]))+1):
                                      ialbum=litem['id']
                                      oalbum=litem["recentPhotos"][int(jum)]["oid"]
                                      imgalbum ="LineAPI/tmp/tes.bin"
                                      ambil=client.getImageGroupAlbum(to,ialbum,oalbum,returnAs='bin',saveAs=imgalbum)
                                      client.sendImage(to,imgalbum)   
# Pembatas Script #
                            elif cmd == "deltagme":
                                del tagme['ROM'][to]
                                client.sendMessage(to, "「DEL MENTIONME」\nBerhasil menghapus data Mention di group \n{}".format(client.getGroup(to).name))
                            elif cmd == "tagme":
                                if to in tagme['ROM']:
                                    moneys = {}
                                    msgas = ''
                                    for a in tagme['ROM'][to].items():
                                        moneys[a[0]] = [a[1]['msg.id'],a[1]['waktu']] if a[1] is not None else idnya
                                    sort = sorted(moneys)
                                    sort.reverse()
                                    sort = sort[0:]
                                    msgas = '[Mention Me]'
                                    h = []
                                    no = 0
                                    for m in sort:
                                        has = ''
                                        nol = -1
                                        for kucing in moneys[m][0]:
                                            nol+=1
                                            has+= '\nline://nv/chatMsg?chatId={}&messageId={} \n{}'.format(to,kucing,humanize.naturaltime(datetime.fromtimestamp(moneys[m][1][nol]/1000)))
                                        h.append(m)
                                        no+=1
                                        if m == sort[0]:
                                            msgas+= '\n{}. @!{}x{}'.format(no,len(moneys[m][0]),has)
                                        else:
                                            msgas+= '\n\n{}. @!{}x{}'.format(no,len(moneys[m][0]),has)
                                    sendMention(to, msgas, h)
                                else:
                                    msgas = 'Sorry @!In {} nothink get a mention'.format(client.getGroup(to).name)
                                    sendMention(to, msgas, [sender])
                                    
                            elif cmd.startswith("mentionname "):
                              try:
                                  sep = text.split(" ")
                                  nam = text.replace(sep[0] + " ","")#a
                                  group = client.getGroup(msg.to)
                                  nama = [contact.mid for contact in group.members]
                                  #nama1 = [contact.dispayName for contact in group.members]
                                  k = len(nama)//20
                                  if k >= 20:
                                    k = 20
                                  for a in range(k+1):
                                      txt = u''
                                      s=0
                                      b=[]
                                      data=[]
                                      for i in group.members[a*20 : (a+1)*20]:
                                        if nam in i.displayName:
                                          data.append({"nama":i.displayName})
                                          b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                          s += 7
                                          txt += u'@Zero \n'
                                          bawah = '╭───────────────\n│Mention by huruf {} '.format(str(nam))
                                          bawah += '\n│Total {} Mention \n╰───────────────'.format(str(len(data)))
                                      client.sendMessage(to, text=txt + str(bawah), contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                              except:
                                  pass
                            elif cmd == "mentionpending":
                              try:
                                  group = client.getGroup(msg.to)
                                  if group.invitee is None or group.invitee == []:
                                      client.sendReplyMessage(msg_id,to, "Tidak ada pendingan")
                                      return
                                  else:
                                      nama = [contact.mid for contact in group.invitee]
                                      k = len(nama)//100
                                      for a in range(k+20):
                                        txt = u''
                                        s=0
                                        b=[]
                                        for i in group.invitee[a*20 : (a+1)*20]:
                                          b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                          s += 7
                                          txt += u'@Zero \n'
                                          bawah = '╭───────────────\n│Mentionall {} '.format(str(group.name))
                                          bawah += '\n│Total {} Pendingan\n╰───────────────'.format(str(len(nama)))
                                        client.sendMessage(to, text=txt + str(bawah), contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                              except:
                                  pass
                                
                            elif cmd == "mention":
                              try:
                                  group = client.getGroup(msg.to)
                                  nama = [contact.mid for contact in group.members]
                                  k = len(nama)//100
                                  for a in range(k+20):
                                      txt = u''
                                      s=0
                                      b=[]
                                      for i in group.members[a*20 : (a+1)*20]:
                                          b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                          s += 7
                                          txt += u'@Zero \n'
                                          bawah = '╭───────────────\n│Mentionall {} '.format(str(group.name))
                                          bawah += '\n│Total {} Members\n╰───────────────'.format(str(len(nama)))
                                      client.sendMessage(to, text=txt + str(bawah), contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b}),'EMTVER':'4'}, contentType=0)
                              except:
                                  pass
                            elif cmd == "sticon":
                              try:
                                  group = client.getGroup(msg.to)
                                  nama = [contact.mid for contact in group.members]
                                  k = len(nama)//140
                                  name="hayden"
                                  num=len(name)+1
                                  pid="5ac1bfd5040ab15980c9b435"
                                  sid=['001', '002', '003', '004', '005', '006', '007', '008', '009','010', '011', '012', '013', '014', '015', '016', '017', '018', '019', '020', '021', '022', '023', '024', '025', '026', '027', '028', '029', '030', '031', '032', '033', '034', '035', '036', '037', '038', '039', '040', '041', '042', '043', '044', '045', '046', '047', '048', '049', '050', '051', '052', '053', '054', '055', '056', '057', '058', '059', '060', '061', '062', '063', '064', '065', '066', '067', '068', '069', '070', '071', '072', '073', '074', '075', '076', '077', '078', '079', '080', '081', '082', '083', '084', '085', '086', '087', '088', '089', '090', '091', '092', '093', '094', '095', '096', '097', '098', '099','100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199', '200', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '220', '221', '222', '223', '224', '225', '226', '227', '228', '229', '230', '231', '232', '233', '234', '235', '236', '237', '238', '239', '240', '241', '242', '243', '244', '245', '246', '247', '248', '249', '250']
                                  sver="1"
                                  for a in range(k+20):
                                      txt = u''
                                      s=0
                                      b=[]
                                      c=[]
                                      for i in group.members[a*20 : (a+1)*20]:
                                          b.append({"S":str(s), "E" :str(s+num), "productId":pid,"sticonId":random.choice(sid),"version":sver})
                                          c.append({"S":str(s), "E" :str(s+num), "M":i.mid})
                                          s += num + 1
                                          txt += u'@{}\n'.format(name)
                                      data={u'REPLACE': json.dumps({'sticon':{'resources':b}}),'STICON_OWNERSHIP': '["5ac1bfd5040ab15980c9b435"]','MENTION': json.dumps({'MENTIONEES':c})}
                                      client.sendMessage(to, text=txt, contentMetadata=data, contentType=0)
                              except:# Exception as error:
                                 pass#Print(to,error)
                            elif cmd == "hi":
                                mem = [mem.mid for mem in client.getGroup(to).members]
                                if len(mem) >=500:
                                    pass
                                else:
                                    #md ="u4440dd10ae295d0e3a4e8fde8470e929"
                                    client.fake_mention2(to, clientMid,mem)                            
                            elif cmd == "faketik":
                                mem = [mem.mid for mem in client.getGroup(to).members]
                                if len(mem) >=500:
                                    pass
                                else:
                                    sid = str(settings["Addstickerbc"]["sid"])
                                    spkg = str(settings["Addstickerbc"]["spkg"])
                                    client.fake_mention1(to, sid,spkg,mem)           
                            elif cmd == "men":
                              try:
                                  group = client.getGroup(msg.to)
                                  nama = [contact.mid for contact in group.members]
                                  k = len(nama)//140
                                  for a in range(k+1):
                                      txt = u''
                                      s=0
                                      b=[]
                                      for i in group.members[a*140 : (a+1)*140]:
                                          b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                          s += 7
                                          txt += u'@Zero \n'
                                          sid = str(settings["Addstickerbc"]["sid"])
                                          spkg = str(settings["Addstickerbc"]["spkg"])
                                      men={u'MENTION': json.dumps({'MENTIONEES':b}),'STKID': '{}'.format(sid),'STKPKGID':'{}'.format(spkg),'STKVER': '1',}
                                      client.sendMessage(to, text=txt, contentMetadata=men, contentType=7)
                              except:
                                  pass
                                    
                            elif cmd == 'sider on':
                                try:
                                    del cctv['point'][receiver]
                                    del cctv['sidermem'][receiver]
                                    #del cctv['cyduk'][receiver]
                                except:
                                    pass
                                cctv['point'][receiver] = msg.id
                                cctv['sidermem'][receiver] = ""
                                cctv['cyduk'] = True
                                client.sendMessage(msg.to, "Auto sider on")
                            elif cmd == 'sider off':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'] = False
                                    client.sendMessage(receiver, 'Auto sider off')
                                                                        
                            elif cmd.startswith("sambut on"):
                              if settings["Sambutan"] == True:
                                 if settings["lang"] == "JP":
                                     client.sendMessage(msg.to,"Sudah Onヽ(´▽｀)/")
                              else:
                                  settings["Sambutan"] = True
                                  if settings["lang"] == "JP":
                                      client.sendMessage(msg.to,"Sambutan Di Aktifkanヾ(*´∀｀*)ﾉ")

                            elif cmd.startswith("sambut off"):
                              if settings["Sambutan"] == False:
                                 if settings["lang"] == "JP":
                                     client.sendMessage(msg.to,"Sudah Off(p′︵‵。)")
                              else: 
                                  settings["Sambutan"] = False
                                  if settings["lang"] == "JP":
                                      client.sendMessage(msg.to,"Sambutan Di Nonaktifkan(　＾∇＾)")
                            
                            elif cmd.startswith("cam "):
                                  hk = msg.text.split(" ")
                                  spl = msg.text.replace(hk[0] + " ","")
                                  if spl == 'on':
                                      if msg.to in welcome:
                                           msgs = "Welcome Msg allways on"
                                      else:
                                           welcome.append(msg.to)
                                           ginfo = client.getGroup(msg.to)
                                           msgs = "Welcome Msg mode on\nGroup : " +str(ginfo.name)
                                           client.sendMessage(msg.to, msgs)
                                  elif spl == 'off':
                                        if msg.to in welcome:
                                             welcome.remove(msg.to)
                                             ginfo = client.getGroup(msg.to)
                                             msgs = "Welcome Msg mode off\nGroup : " +str(ginfo.name)
                                        else:
                                             msgs = "Welcome Msg allready off"
                                        client.sendMessage(msg.to, msgs)
                                
                            elif cmd.startswith("bye "):
                                  hk = msg.text.split(" ")
                                  spl = msg.text.replace(hk[0] + " ","")
                                  if spl == 'on':
                                      if msg.to in leave:
                                           msgs = "Leave Msg allways on"
                                      else:
                                           leave.append(msg.to)
                                           ginfo = client.getGroup(msg.to)
                                           msgs = "Leave Msg mode on\nGroup : " +str(ginfo.name)
                                           client.sendMessage(msg.to, msgs)
                                  elif spl == 'off':
                                        if msg.to in leave:
                                             leave.remove(msg.to)
                                             ginfo = client.getGroup(msg.to)
                                             msgs = "Leave Msg mode off\nGroup : " +str(ginfo.name)
                                        else:
                                             msgs = "Leave Msg allready off"
                                        client.sendMessage(msg.to, msgs)
                                

                            elif cmd.startswith("micadd"):
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        settings["mimic"]["target"][target] = True
                                        client.sendMessage(msg.to,"Target ditambahkan!")
                                        break
                                    except:
                                        client.sendMessage(msg.to,"Gagal menambahkan target")
                                        break
                            elif cmd.startswith("micdel"):
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        del settings["mimic"]["target"][target]
                                        client.sendMessage(msg.to,"Target dihapuskan!")
                                        break
                                    except:
                                        client.sendMessage(msg.to,"Gagal menghapus target")
                                        break
                                    
                            elif cmd == "miclist":
                                if settings["mimic"]["target"] == {}:
                                    client.sendMessage(msg.to,"Tidak Ada Target")
                                else:
                                    mc = "╔══[ Mimic List ]"
                                    for mi_d in settings["mimic"]["target"]:
                                        mc += "\n╠ "+client.getContact(mi_d).displayName
                                    mc += "\n╚══[ Finish ]"
                                    client.sendMessage(msg.to,mc)
                                
                            elif cmd.startswith("mimic"):
                                sep = text.split(" ")
                                mic = text.replace(sep[0] + " ","")
                                if mic == "on":
                                    if settings["mimic"]["status"] == False:
                                        settings["mimic"]["status"] = True
                                        client.sendMessage(msg.to,"Reply Message on")
                                elif mic == "off":
                                    if settings["mimic"]["status"] == True:
                                        settings["mimic"]["status"] = False
                                        client.sendMessage(msg.to,"Reply Message off")
# Pembatas Script #                                                                         
# Pembatas Script #
                    elif msg.contentType == 1:
                        if settings["changePictureProfile"] == True:
                            path = client.downloadObjectMsg(msg_id)
                            settings["changePictureProfile"] = False
                            client.updateProfilePicture(path)
                            client.sendReplyMessage(msg_id,to, "Berhasil mengubah foto profile")
                        if settings["changePicturejs"] == True:
                            path = js.downloadObjectMsg(msg_id)
                            settings["changePicturejs"] = False
                            js.updateProfilePicture(path)
                            js.sendReplyMessage(msg_id,to, "Berhasil mengubah foto profile")
                        if msg.toType == 2:
                            if to in settings["changeGroupPicture"]:
                                path = client.downloadObjectMsg(msg_id)
                                settings["changeGroupPicture"].remove(to)
                                client.updateGroupPicture(to, path)
                                client.sendReplyMessage(msg_id,to, "Berhasil mengubah foto group")
                    elif msg.contentType == 13:
                        if settings["checkContact"] == True:
                            try:
                                contact = client.getContact(msg.contentMetadata["mid"])
                                if client != None:
                                    cover = client.getProfileCoverURL(msg.contentMetadata["mid"])
                                else:
                                    cover = "Tidak dapat masuk di line channel"
                                path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                try:
                                    client.sendImageWithURL(to, str(path))
                                except:
                                    pass
                                ret_ = "╔══[ Details Contact ]"
                                ret_ += "\n╠ Nama : {}".format(str(contact.displayName))
                                ret_ += "\n╠ MID : {}".format(str(msg.contentMetadata["mid"]))
                                ret_ += "\n╠ Bio : {}".format(str(contact.statusMessage))
                                ret_ += "\n╠ Gambar Profile : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                ret_ += "\n╠ Gambar Cover : {}".format(str(cover))
                                ret_ += "\n╚══[ Finish ]"
                                client.sendMessage(to, str(ret_))
                            except:
                                client.sendMessage(to, "Kontak tidak valid")
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                
        if op.type == 25 or op.type == 26 :
            try:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if settings["autoRead"] == True:
                        client.sendChatChecked(to, msg_id)
                    if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                        text = msg.text
                        if text is not None:
                            client.sendReplyMessage(msg_id,msg.to,text)
                    if msg.contentType == 0:
                        if text is None:
                            return
                        if "/ti/g/" in msg.text.lower():
                            if settings["autoJoinTicket"] == True:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    group = client.findGroupByTicket(ticket_id)
                                    client.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    client.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
                        if 'MENTION' in msg.contentMetadata.keys() != None:
                          names = re.findall(r'@(\w+)', text)
                          mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                          mentionees = mention['MENTIONEES']
                          for mention in mentionees:
                            if clientMid in mention["M"]:
                              #if client.getProfile().mid in mention["M"]:
                                if to not in tagme['ROM']:
                                  tagme['ROM'][to] = {}
                                if sender not in tagme['ROM'][to]:
                                  tagme['ROM'][to][sender] = {}
                                if 'msg.id' not in tagme['ROM'][to][sender]:
                                   tagme['ROM'][to][sender]['msg.id'] = []
                                if 'waktu' not in tagme['ROM'][to][sender]:
                                   tagme['ROM'][to][sender]['waktu'] = []
                                tagme['ROM'][to][sender]['msg.id'].append(msg.id)
                                tagme['ROM'][to][sender]['waktu'].append(msg.createdTime)
                                    
                        if 'MENTION' in msg.contentMetadata.keys() != None:
                          if settings["autoRespon"] == True:
                            contact = client.getContact(sender)
                            image = "https://obs.line-scdn.net/" + contact.pictureStatus
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if clientMid in mention["M"]:
                                        client.sendImageWithURL(sender, image)
                                        sendMention(sender, "Ini kak @!,yang suka tag digruop", [sender])
                                        break                                        
                        if 'MENTION' in msg.contentMetadata.keys() != None:
                          if settings["detectMentiontag"] == True:
                            contact = client.getContact(sender)
                            names = contact.displayName
                            icon = 'https://obs.line-scdn.net/' + contact.pictureStatus
                            hayden = {'MSG_SENDER_NAME': names,
                                      'MSG_SENDER_ICON': icon
                            }
                            name = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if mention ['M'] in clientMid:
                                    client.sendReplyMessage(msg_id,to, settings["Respontag"],hayden)                                                              
                                    break
                        if 'MENTION' in msg.contentMetadata.keys() != None:
                          if settings["detectMentionfo"] == True:
                            contact = client.getContact(sender)
                            names = contact.displayName
                            midd = contact.mid
                            icon = 'https://obs.line-scdn.net/' + contact.pictureStatus
                            hayden = {'mid': midd,
                                      'MSG_SENDER_NAME': names,
                                      'MSG_SENDER_ICON': icon
                            }
                            name = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if mention ['M'] in clientMid:
                                    client.sendReplyImageWithURL(msg_id,to, icon,contentMetadata=hayden)
                                    client.sendReplyMessage(msg_id,to, settings["Respontag"],hayden)
                                    break
                        if 'MENTION' in msg.contentMetadata.keys() != None:
                          if settings["detectMentiontik"] == True:
                            contact = client.getContact(sender)
                            name = contact.displayName
                            icon = 'https://obs.line-scdn.net/' + contact.pictureStatus
                            sid = str(settings["Addstickertag"]["sid"])
                            spkg = str(settings["Addstickertag"]["spkg"])
                            hayden1 = {'MSG_SENDER_NAME': name,
                                      'MSG_SENDER_ICON': icon,
                            }
                            hayden = {'MSG_SENDER_NAME': name,
                                      'MSG_SENDER_ICON': icon,
                                      'STKPKGID': spkg,
                                      'STKID': sid
                            }
                            name = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if mention ['M'] in clientMid:
                                    client.sendReplyMessage(msg_id,to, settings["Respontag"],hayden1)
                                    client.sendReplyMessage(msg_id,to, None, contentMetadata=hayden, contentType=7)
                                    break
                        if 'MENTION' in msg.contentMetadata.keys() != None:
                          if settings["detectMentionkik"] == True:
                            contact = client.getContact(sender)
                            name = contact.displayName
                            midd = contact.mid
                            icon = 'https://obs.line-scdn.net/' + contact.pictureStatus
                            sid = str(settings["Addstickertag"]["sid"])
                            spkg = str(settings["Addstickertag"]["spkg"])
                            hayden1 = {'MSG_SENDER_NAME': name,
                                      'MSG_SENDER_ICON': icon,
                            }
                            hayden = {'MSG_SENDER_NAME': name,
                                      'MSG_SENDER_ICON': icon,
                                      'STKPKGID': spkg,
                                      'STKID': sid
                            }
                            name = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if mention ['M'] in clientMid:
                                    client.sendReplyMessage(msg_id,to, settings["Respontag"],hayden1)
                                    client.kickoutFromGroup(to,[midd])
                                    break
            except:# Exception as error:
                pass#logError(error)
                #traceback.print_tb(error.__traceback__)
 #          print ("MEMBER JOIN TO GROUP")
  #         if settings["Sambutan"] == True:
   #          if op.param2 in clientMid:
    #             return
     #        ginfo = client.getGroup(op.param1)
      #       contact = client.getContact(op.param2)
       #      image = "https://obs.line-scdn.net/" + contact.pictureStatus
        #     client.sendImageWithURL(op.param1,image)
         #    client.sendMessage(op.param1,"╔══[ Respon sambutan ]\n╠ Salken kakak " + client.getContact(op.param2).displayName + "\n╠ Selamat datang di " + str(ginfo.name) + "\n╠ Jangan lupa cek note\n╠ Jangan baper yaa\n╠ Nggak boleh nakal\n╠ Semoga betah dirumah baru\n╚══[ By: ƬΣΛM HK BӨƬ ]")
#        if op.type == 17:
 #          print ("MEMBER LEAVE TO GROUP")
  #         if settings["Sambutan"] == True:
   #          if op.param2 in clientMid:
    #             return
     #        ginfo = client.getGroup(op.param1)
      #       contact = client.getContact(op.param2)
       #      image = "https://obs.line-scdn.net/" + contact.pictureStatus
        #     client.sendImageWithURL(op.param1,image)
         #    client.sendMessage(op.param1,"╔══[ Respon keluar ]\n╠ Terimah kasih kak " + client.getContact(op.param2).displayName + "\n╠ Sudah singgah di " + str(ginfo.name) +  "\n╠ Jangan lupa bahagia diluar\n╚══[ By: ƬΣΛM HK BӨƬ ]")
                            
        if op.type == 55:
           if cctv['cyduk'] == True:
            try:
                if op.param1 in cctv['point']:
                    Name = client.getContact(op.param2).mid
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        contact = client.getContact(op.param2)
                        mids=contact.mid
                        fcctv(op.param1,mids)
#                        picts="https://obs.line-scdn.net/{}".format(client.getContact(op.param2).pictureStatus)
#                        client.sendImageWithURL(op.param1,ftts)
  #                      mentionMembers(op.param1,[mids])
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)        

while True:
    saveSc()
    try:
        ops = clientPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                clientBot(op)
                clientPoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
#while True:
 #   try:
  #      ops = clientPoll.singleTrace(count=50)
   #     if ops is not None:
    #        for op in ops:
     #           clientPoll.setRevision(op.revision)
      #          thread = threading.Thread(target=clientBot, args=(op,))
       #         thread.daemon = False
        #        thread.start()
         #       thread.join()
    #except Exception as e:
     #   logError(e)
        
