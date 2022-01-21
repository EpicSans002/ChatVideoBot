import BotAmino
from BotAmino import BotAmino, Parameters
import urllib
import os
import time
import sys

print("wait...")
client = BotAmino("jwevri9h@xojxe.com", "aaaa5555", deviceId = ("329F46F833E61F4635BB2519139256FC10DA6F359C6970CE01F54F4B9064674A0509B9733C650C4D56")



client.prefix = "/"  # set the prefix to /
client.wait = 4  # wait 4 sec before doing a new command

comid= 165549708


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
	
client.launch()
print("ready")


