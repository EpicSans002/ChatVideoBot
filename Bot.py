import BotAmino
from BotAmino import BotAmino, Parameters
import urllib
import os
import time
import sys

print("wait...")
client = BotAmino("1fmlx94zixce@yoggm.com", "aaaa5555", deviceId = "3236DCDA9D56E3B5F51F00770B45DD2275A7615F721A2FC859617C39A80B7BE06DA73D7FC6DDDCF1E6")



client.prefix = "/"  # set the prefix to /
client.wait = 4  # wait 4 sec before doing a new command

comid= 165549708
chatid= 'b240367a-8a5a-4d93-aaa8-dd40fe42c711'

client.add_community(comid)
subclient = client.get_community(comid)
subclient.join_chatroom("http://aminoapps.com/p/k6wfjvy")

@client.command()
def help(data):
  help = ("Bot Help Menu                                     startvc      -to start Vc                    endvc        -to end Vc                startVideo   -to start video                    bg                - get background image")
  data.subClient.send_message(data.chatId, message=help)

@client.command()
def startvc(data):
	client.start_vc(comId=data.comId,chatId=data.chatId)

@client.command()
def endvc(data):
	client.end_vc(comId=data.comId,chatId=data.chatId)

@client.command()
def startVideo(data):
  client.start_video_chat(comId=data.comId,chatId=data.chatId)

@client.command()
def bg(data):
    image = data.subClient.get_chat_thread(data.chatId).backgroundImage
    if image is not None:
      filename = image.split("/")[-1]
      urllib.request.urlretrieve(image, filename)
      with open(filename, 'rb') as fp:
        data.subClient.send_message(chatId=data.chatId, file=fp, fileType="image")

@client.command()
def wallet(data):
     coins = data.subClient.get_wallet_amount()
     print(coins)

@client.command()
def Coins(data):
  

client.launch()
print("ready")


