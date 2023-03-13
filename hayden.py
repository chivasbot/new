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
from deep_translator import GoogleTranslator
from subprocess import Popen, PIPE
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
from os.path import getmtime
#from tiktok_downloader import snaptik,ssstik,tikmate,mdown
#from TikTokApi import TikTokApi 
import pyqrcode
import png
import hashlib, pyshorteners, pyimgflip, time, subprocess, youtube_dl, threading, string, requests,urllib, urllib3, urllib.parse, random, sys, json, codecs, re, os, requests, ast, pytz, atexit, traceback, base64, pafy, livejson, timeago, math, humanize, argparse
_session = requests.session()

requests.packages.urllib3.disable_warnings()
listApp = [
    "IOSIPAD\t8.12.2\tHelloWorld\t8.22.7", 
    "CHROMEOS\t2.1.5\tHelloWorld\t11.2.5", 
    "DESKTOPWIN\t5.9.2\tHelloWorld\t11.2.5", 
    "DESKTOPMAC\t5.9.2\tHelloWorld\t11.2.5", 
    "WIN10\t5.5.5\tHelloWorld\t11.2.5"
]
client=LINE("FhEBf2dj0uyWUlvFA587.1SywK/hZsLABL4LneAuNzW.z0KR0z/f3cFA8xuqgj8YgqfFF/OBJVMIzL5mBa30QO4=")
#client = LINE("epuput4@gmail.com", passwd="setiaq15")
#client = LINE("FgYVb9R7H854goMt7SY9.redDek4Pxq46tO+EHhdPkq.HO3PSO43r7DPYg3wfwiUOBqf8+QYTPg2lf6luZUyaT0=")
#client = LINE("riskyhermanto319@gmail.com", passwd="setiaq15")
#client = LINE("haydenprakoso@gmail.com", passwd="setiaq15")
#client = LINE("F8BGTg4jWoJe70KWYs12.DJWq0pTtByYtm5DfoGJwyG.D86N9skPSHRMtI6BZP5oGNzo3bYOmjVM0xyJj8uZi7M=")
client.log("Auth Token : " + str(client.authToken))
  
clientMid = client.profile.mid
clientStart = time.time()
clientPoll = OEPoll(client)
mid = client.getProfile().mid
Creator=["udbd94d6715ce71f30587deff0dcb7788"]
settings={
  "autoJoin": True,  
  "keyCommand":"",
  "setKey":False,
  "react":False,
  "mention":""
}

NOT_COOLING_TEXT = ['sp']
SEND_MESSAGE_COOLING = {}
COOLING_TIME = 5

def danbooru(to,text):
    r=BeautifulSoup(requests.get("https://danbooru.donmai.us/posts?page={}".format(text)).text,"html5lib")
    a=r.findAll("a",{"class":"post-preview-link"})
    data=[]
    for i in range(10):
      nama="{}.jpg".format(i)
      b="https://danbooru.donmai.us"+str(a[i].get("href"))
      c=BeautifulSoup(requests.get(b).text,"html5lib")
      d=c.findAll("li",{"id":"post-info-size"})[0].find("a")["href"]
      client.downloadFileURL(d, saveAs=nama)
      data.append(nama)
    client.uploadMultipleImageToTalk(data,to)

def ims(to,txt,txt1):
    url="https://id.images.search.yahoo.com/search/images;_ylt=Awr1SXQMms1iHycNHvvMQwx.;_ylc=X1MDMjExNDczMzAwNARfcgMyBGZyAwRncHJpZANjUTFPQktpblJST1J4OXRaVGVRMVJBBG5fc3VnZwM1BG9yaWdpbgNpZC5pbWFnZXMuc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAwRxc3RybAM2BHF1ZXJ5A2JvcnV0bwR0X3N0bXADMTY1NzY0MTQ4OQ--?fr2=sb-top-id.images.search&p={}&ei=UTF-8&fr=sfp&bucket=&exclusive_bucket=".format(txt)
    b=BeautifulSoup(requests.get(url).text,"html5lib").findAll("img",{"class":"process"})
    data=[]
    for i in b:
      im=i.get("data-src")
      data.append({"image":im})
    result={"data":data}
    nama=[]
    for jum in range(0,int(txt1)):
      nam="{}.jpg".format(str(jum))
      i=[isi["image"] for isi in result["data"]]
      client.downloadFileURL(i[jum],saveAs="{}.jpg".format(str(jum)))
      print("{}.jpg".format(str(jum)))
      nama.append(nam)
    client.uploadMultipleImageToTalk(nama,to)

def relike(idmsg):
    m = "react"
    i=int(idmsg)
    r=random.choice([1,2, 3, 4, 5, 6])
    p = [
            [12, 1, [
                [8, 1, 0],
                [10, 2, i],
                [12, 3, [
                    [8, 1, r]
                ]]
            ]]
    ]
    a=client.generateDummyProtocol(m,p,4)
    client.postPackDataAndGetUnpackRespData("/S5", a, 5)
def bulat(to,i):
    w, h = 200,200
    l=1*i
    shape = [(l,l),(w-l,h-l)]
    l1=2*i
    shape1 = [(l1,l1),(w-l1,h-l1)]
    l2=3*i
    shape2 = [(l2,l2),(w-l2,h-l2)]
    l3=4*i
    shape3 = [(l3,l3),(w-l3,h-l3)]
    l4=5*i
    shape4 = [(l4,l4),(w-l4,h-l4)]
    l5=6*i
    shape5 = [(l5,l5),(w-l5,h-l5)]
    l6=7*i
    shape6 = [(l6,l6),(w-l6,h-l6)]
    l7=8*i
    shape7 = [(l7,l7),(w-l7,h-l7)]
    img = Image.new("RGBA", (w, h))
    img1 = ImageDraw.Draw(img)   
    img1.ellipse(shape, outline ="green")
    img1.ellipse(shape1, outline ="red")
    img1.ellipse(shape2, outline ="blue")
    img1.ellipse(shape3, outline ="yellow")
    img1.ellipse(shape4, outline ="pink")
    img1.ellipse(shape5, outline ="white")
    img1.ellipse(shape6, outline ="gold")
    img1.ellipse(shape7, outline ="grey")
    img.save("0.png")
    client.sendImage(to,"0.png")

def kotak(to,i):
  images = []
  for i1 in range(1, 90):
    w, h = 400,400
    w1, h1 = 500,500
    l=3*i
    shape = [(l,l),(w-l,h-l)]
    l1=4*i
    shape1 = [(l1,l1),(w-l1,h-l1)]
    l2=5*i
    shape2 = [(l2,l2),(w-l2,h-l2)]
    l3=6*i
    shape3 = [(l3,l3),(w-l3,h-l3)]
    l4=7*i
    shape4 = [(l4,l4),(w-l4,h-l4)]
    l5=8*i
    shape5 = [(l5,l5),(w-l5,h-l5)]
    l6=9*i
    shape6 = [(l6,l6),(w-l6,h-l6)]
    l7=10*i
    shape7 = [(l7,l7),(w-l7,h-l7)]
    img = Image.new("RGBA", (w, h))
    img1 = ImageDraw.Draw(img)   
    img1.rectangle(shape, outline ="green")
    img1.rectangle(shape1, outline ="red")
    img1.rectangle(shape2, outline ="blue")
    img1.rectangle(shape3, outline ="yellow")
    img1.rectangle(shape4, outline ="pink")
    img1.rectangle(shape5, outline ="white")
    img1.rectangle(shape6, outline ="gold")
    img1.rectangle(shape7, outline ="grey")
    img.save("0.png")
    a="0.png"
    b="1.png"
    c="2.png"
    d="3.png"
    e="4.png"
    f="5.png"
    g="6.png"
    a1=Image.open(a)
    a2=a1.rotate(15)
    a2.save(b)
    a3=a1.rotate(30)
    a3.save(c)
    a4=a1.rotate(45)
    a4.save(d)
    a5=a1.rotate(60)
    a5.save(e)
    a6=a1.rotate(75)
    a6.save(f)
    b1=Image.open(b)
    b2=Image.open(c)
    b3=Image.open(d)
    b4=Image.open(e)
    b5=Image.open(f)
    a1.paste(b1,b1)
    a1.paste(b2,b2)
    a1.paste(b3,b3)
    a1.paste(b4,b4)
    a1.paste(b5,b5)
    a1.save(g)
    a7 = Image.new("RGB", (w1, h1))
    a8=Image.open(g).rotate(i1)
    a7.paste(a8,(50,50),a8)
    images.append(a7)
  images[0].save('out.gif',save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)
  client.sendGIF(to,"out.gif")    
def Members(to, mid,mids):
    try:
        arrData = ""
        arr = []
        for i in mids:
            textx = "{}@{} ".format(str(mid),client.getContact(i).displayName)
#            Print(to,textx)
#            Print(to,len(textx))
            b=str(textx.encode('unicode-escape').decode("utf-8"))
            c="{}".format(b.replace("0","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","").replace("\\U",""))
 #           Print(to,len(c))  
            spl=len(c)-len(textx)
  #          Print(to,spl)  
            
            if 0 == spl:
              mention = "{}".format(client.getContact(i).displayName)
              slen = str(len(c) - len(mention))
              elen = str(int(slen) + len(mention)+1)
              arrData = {'S':slen, 'E':elen, 'M':i}
#              Print(to,arrData)            
              arr.append(arrData)
            elif 1 == spl:
              mention = "{}".format(client.getContact(i).displayName)
              slen = str(len(c) - len(mention)+spl)
              elen = str(int(slen) + len(mention)+1)
              arrData = {'S':slen, 'E':elen, 'M':i}
 #             Print(to,arrData)            
              arr.append(arrData)
            elif 2 == spl:
              mention = "{}".format(client.getContact(i).displayName)
              slen = str(len(c) - len(mention)+spl)
              elen = str(int(slen) + len(mention)+1)
              arrData = {'S':slen, 'E':elen, 'M':i}
  #            Print(to,arrData)            
              arr.append(arrData)
            elif 3 == spl:
              mention = "{}".format(client.getContact(i).displayName)
              slen = str(len(c) - len(mention)+1)
              elen = str(int(slen)+ len(mention)+1)
              arrData = {'S':slen, 'E':elen, 'M':i}
#              Print(to,arrData)            
              arr.append(arrData)
        textx += ""
        
        client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        client.sendMessage(to, "[ INFO ] Error :\n" + str(error))
    
    
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

def sendL(to, isi):
    data = {
        "type": "text",
        "text": isi,
        "sentBy": {
            "label": "{}".format(client.getContact(clientMid).displayName),
            "iconUrl": "https://obs.line-scdn.net/{}".format(client.getContact(clientMid).pictureStatus),
        }
    }
    client.postTemplate(to, data)
def sendIL(to, isi):
    data = {
    "type": "image",
    "originalContentUrl": isi,
    "duration": 60000,
    "previewImageUrl": isi,
    "sentBy": {
      "label": "{}".format(client.getContact(clientMid).displayName),
      "iconUrl": "https://obs.line-scdn.net/{}".format(client.getContact(clientMid).pictureStatus),
      }
    }
    client.postTemplate(to, data)
def sendAL(to, isi):
    data = {
    "type": "audio",
    "originalContentUrl": isi,
    "duration": 60000
    }
    client.postTemplate(to, data)
def sendVL(to, isi):
    data = {
    "type": "video",
    "originalContentUrl": isi,
    "duration": 60000,
    "previewImageUrl": "https://i.ytimg.com/vi/jxBfCwr-2v4/maxresdefault.jpg"
    }
    client.postTemplate(to, data)
def sendVLP(to, isi,img):
    data = {
    "type": "video",
    "originalContentUrl": isi,
    "duration": 60000,
    "previewImageUrl": img
    }
    client.postTemplate(to, data)
def B64e(to, url):
    import base64
    return client.sendMessage(to, base64.b64encode(url.encode()).decode('utf-8'))
def B64e2(to, url):
    import base64
    return Print(to, base64.b64encode(url.encode()))

def B64d(to, url):
    import base64
    return client.sendMessage(to, base64.b64decode(url.encode()).decode('utf-8'))
    
def commander(text):
    pesan = text.lower()
    if settings["setKey"] == False:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
  
def clientBot(op):
    try:
        if op.type == 12:
          print(op)
        if op.type == 13:
          if clientMid in op.param3:
            if settings["autoJoin"] == True:
              #if op.param2 not in Creator:
                client.acceptGroupInvitation(op.param1)
               # client.leaveGroup(op.param1)
              #else:
               # client.acceptGroupInvitation(op.param1)                    
        if op.type == 26:
          msg=op.message
          if msg.contentType == 15:
            al=msg.location
            Print(msg.to,al)
          if settings["react"] == True:
            msg = op.message
            relike(msg.id)
        if op.type in [25,26]:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                cmd = commander(text)
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
                        if cmd == "cek":
                          if msg._from in Creator:
                            client.sendMessage(to,"oke")
                        elif cmd.startswith("!exec"):
                          if msg._from in Creator:
                                  sep = text.split("\n")
                                  hayden = text.replace(sep[0] + "\n","")
                                  try:
                                      exec(hayden)
                                  except Exception as e:
                                      client.sendMessage(receiver, str(e))
                        elif cmd == "react on":
                          if msg._from in Creator:
                                settings["react"] = True
                                client.sendMessage(to, "Mode on")                        
                        elif cmd == "react off":
                          if msg._from in Creator:
                                settings["react"] = False
                                client.sendMessage(to, "Mode off")
                        elif cmd.startswith("albumimage "):
                          if msg._from in Creator:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                nama1=cond[0]
                                nama2=cond[1]
                                nama3=cond[2]
                                a=client.createGroupAlbum(to,"{}".format(nama1))
                                ida=a["result"]["items"][0]["id"]
                                url="https://id.images.search.yahoo.com/search/images;_ylt=Awr1SXQMms1iHycNHvvMQwx.;_ylc=X1MDMjExNDczMzAwNARfcgMyBGZyAwRncHJpZANjUTFPQktpblJST1J4OXRaVGVRMVJBBG5fc3VnZwM1BG9yaWdpbgNpZC5pbWFnZXMuc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAwRxc3RybAM2BHF1ZXJ5A2JvcnV0bwR0X3N0bXADMTY1NzY0MTQ4OQ--?fr2=sb-top-id.images.search&p={}&ei=UTF-8&fr=sfp&bucket=&exclusive_bucket=".format(nama2)
                                b=BeautifulSoup(requests.get(url).text,"html5lib").findAll("img",{"class":"process"})
                                data=[]
                                for i in b:
                                  im=i.get("data-src")
                                  data.append({"image":im})
                                result={"data":data}
                                imgs=[]
                                for jum in range(0,int(nama3)):
                                  nam="{}.jpg".format(str(jum))
                                  iso=[isi["image"] for isi in result["data"]]
                                  client.downloadFileURL(iso[jum],saveAs="{}".format(str(nam)))
                                  oid=client.uploadObjAlbum(to,ida,nam)
                                  imgs.append({"oid":oid})
                                client.addImageMultyToAlbum(to,ida,imgs)
                        elif cmd.startswith("noteimage "):
                          if msg._from in Creator:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split('|')
                                nama1=cond[0]
                                nama2=cond[1]
                                nama3=cond[2]
                                url="https://id.images.search.yahoo.com/search/images;_ylt=Awr1SXQMms1iHycNHvvMQwx.;_ylc=X1MDMjExNDczMzAwNARfcgMyBGZyAwRncHJpZANjUTFPQktpblJST1J4OXRaVGVRMVJBBG5fc3VnZwM1BG9yaWdpbgNpZC5pbWFnZXMuc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAwRxc3RybAM2BHF1ZXJ5A2JvcnV0bwR0X3N0bXADMTY1NzY0MTQ4OQ--?fr2=sb-top-id.images.search&p={}&ei=UTF-8&fr=sfp&bucket=&exclusive_bucket=".format(nama1)
                                b=BeautifulSoup(requests.get(url).text,"html5lib").findAll("img",{"class":"process"})
                                data=[]
                                for i in b:
                                  im=i.get("data-src")
                                  data.append({"image":im})
                                result={"data":data}
                                imgs=[]
                                for jum in range(0,int(nama2)):
                                  nam="{}.jpg".format(str(jum))
                                  iso=[isi["image"] for isi in result["data"]]
                                  client.downloadFileURL(iso[jum],saveAs="{}".format(str(nam)))
                                  #oid=client.uploadObjAlbum(to,ida,nam)
                                  imgs.append(nam)
                                client.createGroupPostMultyImage(to,imgs,nama3)
                        elif cmd == "imagelink":
                          if msg._from in Creator:
                                a = client.getRecentMessagesV2(to, 1000)
                                for i in a:
                                  if i.id in msg.relatedMessageId:
                                    client.downloadObjectMsg(i.id,saveAs="Hk.jpg")
                                b=client.uploadObject("Hk.jpg")
                                client.sendMessage(to,"https://obs.line-scdn.net/"+b["x-obs-hash"])
                        elif cmd == "videolink":
                          if msg._from in Creator:
                                a = client.getRecentMessagesV2(to, 1000)
                                for i in a:
                                  if i.id in msg.relatedMessageId:
                                    client.downloadObjectMsg(i.id,saveAs="HkBot.mp4")
                                b=client.uploadObject("HkBot.mp4")
                                client.sendMessage(to,"https://obs.line-scdn.net/"+b["x-obs-hash"])
                                      
            except Exception as error:
              print(error)
    except Exception as error:
        print(error)
while True:
        try:
            ops = clientPoll.singleTrace(count=50)
            if ops is not None:
                for op in ops:
                    clientPoll.setRevision(op.revision)
                    clientBot(op)
        except Exception as e:
            print(e)
            traceback.print_tb(e.__traceback__)