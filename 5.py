# -*- coding: utf-8 -*-
import linepy
from linepy import *
from akad.ttypes import *
from datetime import datetime
from datetime import timedelta, date
import pytz
import pafy
import time
import asyncio
import random
import multiprocessing
import timeit
import sys
import json
import ctypes
import codecs
import tweepy
import threading
import glob
import re
import ast
import six
import os
import subprocess
import wikipedia
import atexit
import goslate
import urllib
import urllib.parse
import urllib.error
import urllib.request
import urllib3
import string
import tempfile
import shutil
import unicodedata
from humanfriendly import format_timespan, format_size, format_number, format_length
from akad.ttypes import ChatRoomAnnouncement
from akad.ttypes import Location
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import ContentType as Type
from multiprocessing import Pool, Process
from thrift import transport, protocol, server
from thrift.TRecursive import *
from thrift.TSerialization import *
from thrift.TMultiplexedProcessor import *
from thrift.unverting import *
import html5lib
import requests
import json
import urllib3
import ffmpy
from random import randint
from bs4 import BeautifulSoup
from gtts import gTTS
from wikiapi import WikiApi
from googletrans import Translator
from pafy import pafy
import youtube_dl
from time import sleep
import pyimgflip

botStart = time.time()
msg_dict = {}
msg_dict1 = {}

cl = LINE("EMAIL", "PASSWORD")
cl.log("Auth Token : " + str(cl.authToken))

ki = LINE("EMAIL", "PASSWORD")
ki.log("Auth Token : " + str(ki.authToken))

kk = LINE("EMAIL", "PASSWORD")
kk.log("Auth Token : " + str(kk.authToken))

kc = LINE("EMAIL", "PASSWORD")
kc.log("Auth Token : " + str(kc.authToken))

sw = LINE("EMAIL", "PASSWORD")
sw.log("Auth Token : " + str(sw.authToken))

poll = OEPoll(cl)
call = cl

mid = cl.profile.mid
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Zmid = sw.getProfile().mid

print("𐀀 BOT-1 = " + mid)
print("𐀀 BOT-2 = " + Amid)
print("𐀀 BOT-3 = " + Bmid)
print("𐀀 BOT-4 = " + Cmid)
print("𐀀 BOT-5 = " + Zmid)
print("\n\n𐀀 HELLTERHEAD IS READY❗\n\n")

creator = [""]
owner = [""]
admin = [""]
staff = [""]
DRE = [cl, ki, kk, kc, sw]
ghost = [sw]
Bots = [mid, Amid, Bmid, Cmid, Zmid]
squad = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []
warmode = []
welcome = []
leave = []
left = []
msg_dict = {}
msg_dict1 = {}

responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = sw.getProfile().displayName

settings = {
    "Picture": False,
    "group": {},
    "changeCover": False,
    "changeVideo": False,
    "groupPicture": False,
    "changePicture": False,
    "autoJoinTicket": False,
    # "restartPoint": True,
    "userMention": {},
    "timeRestart": {},
    "server": {},
    "simiSimi": {},
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
    ],
}

wait = {
    "Limit": 1,
    "owner": {},
    "admin": {},
    "addadmin": False,
    "delladmin": False,
    "staff": {},
    "addstaff": False,
    "dellstaff": False,
    "bots": {},
    "addbots": False,
    "dellbots": False,
    "blacklist": {},
    "wblacklist": False,
    "dblacklist": False,
    "Talkblacklist": {},
    "Talkwblacklist": False,
    "Talkdblacklist": False,
    "talkban": False,
    "contact": False,
    "invite": False,
    "ghost": True,
    "protectqr": True,
    "protectkick": True,
    "protectcancel": True,
    "protectinvite": True,
    "protectantijs": True,
    "protectjoin": False,
    "warmode": False,
    "lang": "JP",
    "autoJoin": True,
    "autoAdd": False,
    "autoBlock": False,
    "autoRead": False,
    "Timeline": False,
    "autoLeave": True,
    "detectMention": False,
    "mentionKick": False,
    "welcome": False,
    "leave": False,
    "likeOn": False,
    "stickerOn": False,
    "Addsticker": {"name": "", "status": False},
    "stk": {},
    "selfbot": True,
    "Images": {},
    "Img": {},
    "Videos": {},
    "Addimage": {"name": "", "status": False},
    "Addaudio": {"name": "", "status": False},
    "Addvideo": {"name": "", "status": False},
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": "",
    },
    "mention": "reading...",
    "Respontag": "Yes, me!",
    "welcome": "welcome",
    "leave": "thanks for join, see you next time",
    "comment": "𐀀 HELLTERHEAD\nもばんづ\nJust other people.\nIllustrator / Graphic Designer\nEast Java - ID\n\nline.me/ti/p/~mo-banzu",
    "message": "Thanks for invite, let's be friend",
}
read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "ROM": {},
}

cctv = {"cyduk": {}, "point": {}, "sidermem": {}}

with open("creator.json", "r") as fp:
    creator = json.load(fp)
with open("owner.json", "r") as fp:
    owner = json.load(fp)

Setbot = codecs.open("setting.json", "r", "utf-8")
imagesOpen = codecs.open("image.json", "r", "utf-8")
videosOpen = codecs.open("video.json", "r", "utf-8")
stickersOpen = codecs.open("sticker.json", "r", "utf-8")
audiosOpen = codecs.open("audio.json", "r", "utf-8")
Setmain = json.load(Setbot)
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def waktu(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    days, hours = divmod(hours, 24)
    return "%00d Hari %00d Jam %00d Menit %00d Detik" % (
        days, hours, mins, secs)


def runtime(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    days, hours = divmod(hours, 24)
    return "%00d Hari %00d Jam %00d Menit %00d Detik" % (
        days, hours, mins, secs)


def sendAudioWithURL(self, to_, url):
    path = self.downloadFileWithURL(url)
    try:
        self.sendAudio(to_, path)
    except Exception as e:
        raise Exception(e)


def sendAudioWithUrl(self, to_, url):
    path = "%s/pythonLine-%1.data" % (tempfile.gettempdir(), randint(0, 9))
    r = requests.get(url, stream=True, verify=False)
    if r.status_code == 200:
        with open(path, "w") as f:
            shutil.copyfileobj(r.raw, f)
    else:
        raise Exception("Download audio failure.")
    try:
        self.sendAudio(to_, path)
    except Exception as e:
        raise e


def mentionMembers(to, mid):
    try:
        arrData = ""
        ginfo = cl.getGroup(to)
        textx = "「 Daftar Member 」\n\n"
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {"S": slen, "E": elen, "M": i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "• {}. ".format(str(no))
            else:
                textx += "\n「 Total {} Member 」".format(str(len(mid)))
        cl.sendMessage(
            to, textx, {
                "MENTION": str(
                    '{"MENTIONEES":' + json.dumps(arr) + "}")}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "User ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x "
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {"S": slen, "E": elen, "M": i}
            arr.append(arrData)
            textx += mention + wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num = num + 1
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except BaseException:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(
            to, textx, {
                "MENTION": str(
                    '{"MENTIONEES":' + json.dumps(arr) + "}")}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Hi ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x "
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {"S": slen, "E": elen, "M": i}
            arr.append(arrData)
            textx += mention + wait["welcome"] + " to " + str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num = num + 1
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except BaseException:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(
            to, textx, {
                "MENTION": str(
                    '{"MENTIONEES":' + json.dumps(arr) + "}")}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Bye ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x "
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {"S": slen, "E": elen, "M": i}
            arr.append(arrData)
            textx += mention + wait["leave"]
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num = num + 1
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except BaseException:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(
            to, textx, {
                "MENTION": str(
                    '{"MENTIONEES":' + json.dumps(arr) + "}")}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " % (str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {"S": slen, "E": elen, "M": mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(
            to, text, {
                "MENTION": str(
                    '{"MENTIONEES":' + json.dumps(arr) + "}")}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"], "")
    else:
        cmd = "command"
    return cmd


# message.createdTime -> 00:00:00


def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[: len(str(unixtime)) - 3]))


def dt_to_str(dt):
    return dt.strftime("%H:%M:%S")


# delete log if pass more than 24 hours


def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (
            datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])
        ) > datetime.timedelta(1):
            del msg_dict1[msg_id]


def atend1():
    print("Saving")
    with open("Log_data.json", "w", encoding="utf8") as f:
        json.dump(
            msg_dict1,
            f,
            ensure_ascii=False,
            indent=4,
            separators=(
                ",",
                ": "))
    print("SAVED")


def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[: len(str(unixtime)) - 3]))


def dt_to_str(dt):
    return dt.strftime("%H:%M:%S")


def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (
            datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])
        ) > datetime.timedelta(1):
            del msg_dict[msg_id]


def atend():
    print("Saving")
    with open("Log_data.json", "w", encoding="utf8") as f:
        json.dump(
            msg_dict,
            f,
            ensure_ascii=False,
            indent=4,
            separators=(
                ",",
                ": "))
    print("SAVED")


def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = (
        "\nHELP MENU 🔻\n"
        + "• Menu:command\n"
        + "• Menu:protect\n"
        + "• Menu:banned\n"
        + "• Menu:update\n"
        + "• Menu:group\n"
        + "• Menu:squad\n"
        + "• Menu:status\n"
        + "• Menu:message\n"
        + "• Menu:kicker\n\n"
        + "By : DRE❗\n"
        + "line.me/ti/p/~mo-banzu"
    )

    return helpMessage


def help1():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = (
        "\nMENU COMMAND 🔻\n"
        + "• Help\n"
        + "• Me\n"
        + "• Mid\n"
        + "• Mid [@]\n"
        + "• Tagall\n"
        + "• ?Remove chat\n"
        + "• !Remove chat\n"
        + "• Status\n"
        + "• About\n"
        + "• Runtime\n"
        + "• Respontime\n"
        + "• Creator / Owner\n"
        + "• Speed / Sp\n"
        + "• ?Bye\n"
        + "• !Restart\n"
        + "• .Promo\n"
        + "• Sider [on|off]\n"
        + "• Hlth [on|off]\n\n"
        + "By : DRE❗\n"
        + "line.me/ti/p/~mo-banzu"
    )

    return helpMessage1


def help2():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = (
        "\nMENU PROTECT 🔻\n"
        + "• Revive\n"
        + "• !In\n"
        + "• !Out\n"
        + "• Antijs:stay\n"
        + "• Ghost:in\n"
        + "• Ghost:out\n"
        + "• Hlth\n"
        + "• Hlth:in\n"
        + "• Hlth:out\n"
        + "• Protectkick [on|off]\n"
        + "• Protectjoin [on|off]\n"
        + "• Protectinvite [on|off]\n"
        + "• Protectqr [on|off]\n"
        + "• Ghost [on|off]\n"
        + "• Antijs [on|off]\n"
        + "• Protectall [on|off]\n"
        + "• Listprotect\n"
        + "• Absen\n"
        + "• Respon\n"
        + "• Reject\n\n"
        + "By : DRE❗\n"
        + "line.me/ti/p/~mo-banzu"
    )

    return helpMessage2


def help3():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage3 = (
        "\nMENU BANNED 🔻\n"
        + "• Blacklist / Blc\n"
        + "• Clearban / Clb\n"
        + "• Ban [@]\n"
        + "• Unban [@]\n"
        + "• Ban:on [contact]\n"
        + "• Unban:on [contact]\n"
        + "• Banlist\n"
        + "• Talkban [@]\n"
        + "• Untalkban [@]\n"
        + "• Talkban:on [contact]\n"
        + "• Untalkban:on [contact]\n"
        + "• Talkbanlist\n\n"
        + "By : DRE❗\n"
        + "line.me/ti/p/~mo-banzu"
    )

    return helpMessage3


def help4():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage4 = (
        "\nMENU UPDATE 🔻\n"
        + "• Name: [text]\n"
        + "• Bot[number]name: [text]\n"
        + "• Cpp [image]\n"
        + "• Cvp [video]\n"
        + "• Bot[number]pict [image]\n"
        + "• Broadcast: [text] / Bc: [text]\n"
        + "• Setkey: [text]\n"
        + "• Key\n"
        + "• Resetkey\n\n"
        + "By : DRE❗\n"
        + "line.me/ti/p/~mo-banzu"
    )

    return helpMessage4


def help5():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage5 = (
        "\nMENU GROUP 🔻\n"
        + "• Ginfo\n"
        + "• Ginfo: [number]\n"
        + "• Infomem: [number]\n"
        + "• Open\n"
        + "• Open: [number]\n"
        + "• Close\n"
        + "• Close: [number]\n"
        + "• Gurl\n"
        + "• Grouplist\n"
        + "• Grouplist[number]\n\n"
        + "By : DRE❗\n"
        + "line.me/ti/p/~mo-banzu"
    )

    return helpMessage5


def help6():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage6 = (
        "\nMENU SQUAD 🔻\n"
        + "• Adminadd [@] / Admindel [@]\n"
        + "• Staffadd [@] / Staffdel [@]\n"
        + "• Botadd [@] / Botdel [@]\n"
        + "• Admin:on [contact]\n"
        + "• Staff:on [contact]\n"
        + "• Bot:on [contact]\n"
        + "• Admin:repeat [contact]\n"
        + "• Staff:repeat [contact]\n"
        + "• Bot:repeat [contact]\n"
        + "• Listadmin\n"
        + "• Liststaff\n"
        + "• Listbot\n"
        + "• Contact admin / C:admin\n"
        + "• Contact staff / C:staff\n"
        + "• Contact bot / C:bot\n"
        + "• !Abort\n\n"
        + "By : DRE❗\n"
        + "line.me/ti/p/~mo-banzu"
    )

    return helpMessage6


def help7():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage7 = (
        "\nMENU STATUS 🔻\n"
        + "• Invite [on|off]\n"
        + "• Sticker [on|off]\n"
        + "• Sider [on|off]\n"
        + "• Respon [on|off]\n"
        + "• Timeline [on|off]\n"
        + "• Contact [on|off]\n"
        + "• Autojoin [on|off]\n"
        + "• Autoadd [on|off]\n"
        + "• Welcome [on|off]\n"
        + "• Leave [on|off]\n"
        + "• Autoleave [on|off]\n"
        + "• Warmode [on|off]\n"
        + "• Jointicket [on|off]\n\n"
        + "By : DRE❗\n"
        + "line.me/ti/p/~mo-banzu"
    )

    return helpMessage7


def help8():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage8 = (
        "\nMENU MESSAGE 🔻\n"
        + "• Check sider\n"
        + "• Check message\n"
        + "• Check respon\n"
        + "• Check leave\n"
        + "• Check welcome\n"
        + "• Set sider: [text]\n"
        + "• Set message: [text]\n"
        + "• Set respon: [text]\n"
        + "• Set leave: [text]\n"
        + "• Set welcome: [text]\n\n"
        + "By : DRE❗\n"
        + "line.me/ti/p/~mo-banzu"
    )

    return helpMessage8


def help9():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage9 = (
        "\nMENU KICKER 🔻\n"
        + "• Kick! [@]\n"
        + "• Kill! [@]\n"
        + "• !Kick [pro]\n"
        + "• !Bye [self]\n"
        + "• !Kibar\n\n"
        + "By : DRE❗\n"
        + "line.me/ti/p/~mo-banzu"
    )

    return helpMessage9


def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"]:
                    if (
                        op.param2 not in Bots
                        and op.param2 not in owner
                        and op.param2 not in admin
                        and op.param2 not in staff
                    ):
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(
                            op.param1, "Don't invite without my author!")
                        cl.sendMessage(op.param1, "line.me/ti/p/~mo-banzu")
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)

                return

        if op.type == 26 or op.type == 25:
            print("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if wait["autoRead"]:
                    cl.sendChatChecked(to, msg_id)
                    ki.sendChatChecked(to, msg_id)
                    kk.sendChatChecked(to, msg_id)
                    kc.sendChatChecked(to, msg_id)
                    sw.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True

        if op.type == 11:
            if op.param1 in warmode:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if (
                            op.param2 not in Bots
                            and op.param2 not in owner
                            and op.param2 not in admin
                            and op.param2 not in staff
                        ):
                            wait["blacklist"][op.param2] = True
                            try:
                                ki.kickoutFromGroup(op.param1, [op.param2])
                            except BaseException:
                                try:
                                    kk.kickoutFromGroup(op.param1, [op.param2])
                                except BaseException:
                                    try:
                                        kc.kickoutFromGroup(
                                            op.param1, [op.param2])
                                    except BaseException:
                                        try:
                                            sw.kickoutFromGroup(
                                                op.param1, [op.param2])
                                        except BaseException:
                                            pass

                            warmode.remove(op.param1)
                except BaseException:
                    pass

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if (
                    op.param2 not in Bots
                    and op.param2 not in owner
                    and op.param2 not in admin
                    and op.param2 not in staff
                ):
                    try:
                        ki.kickoutFromGroup(op.param1, [op.param2])
                    except BaseException:
                        try:
                            kk.kickoutFromGroup(op.param1, [op.param2])
                        except BaseException:
                            try:
                                kc.kickoutFromGroup(op.param1, [op.param2])
                            except BaseException:
                                try:
                                    sw.kickoutFromGroup(op.param1, [op.param2])
                                except BaseException:
                                    try:
                                        cl.reissueGroupTicket(op.param1)
                                        X = cl.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        Ticket = cl.reissueGroupTicket(
                                            op.param1)
                                        sw.acceptGroupInvitationByTicket(
                                            op.param1, Ticket
                                        )
                                        sw.kickoutFromGroup(
                                            op.param1, [op.param2])
                                    except BaseException:
                                        pass
                    cl.reissueGroupTicket(op.param1)
                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    cl.updateGroup(X)
                    warmode.append(op.param1)
                else:
                    pass

        if op.type == 11:
            if wait["protectqr"]:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if (
                            op.param2 not in Bots
                            and op.param2 not in owner
                            and op.param2 not in admin
                            and op.param2 not in staff
                        ):
                            wait["blacklist"][op.param2] = True
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            random.choice(DRE).kickoutFromGroup(
                                op.param1, [op.param2])
                            cl.updateGroup(X)
                            cl.sendMessage(
                                op.param1,
                                None,
                                contentMetadata={"mid": op.param2},
                                contentType=13,
                            )
                            cl.sendMessage(
                                op.param1,
                                "Don't open link QR group without permission!",
                            )
                except BaseException:
                    try:
                        if ki.getGroup(
                                op.param1).preventedJoinByTicket == False:
                            if (
                                op.param2 not in Bots
                                and op.param2 not in owner
                                and op.param2 not in admin
                                and op.param2 not in staff
                            ):
                                wait["blacklist"][op.param2] = True
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                random.choice(DRE).kickoutFromGroup(
                                    op.param1, [op.param2]
                                )
                                ki.updateGroup(X)
                                ki.sendMessage(
                                    op.param1,
                                    None,
                                    contentMetadata={"mid": op.param2},
                                    contentType=13,
                                )
                                ki.sendMessage(
                                    op.param1, "Don't open link QR group without permission!", )
                    except BaseException:
                        try:
                            if kk.getGroup(
                                    op.param1).preventedJoinByTicket == False:
                                if (
                                    op.param2 not in Bots
                                    and op.param2 not in owner
                                    and op.param2 not in admin
                                    and op.param2 not in staff
                                ):
                                    wait["blacklist"][op.param2] = True
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    random.choice(DRE).kickoutFromGroup(
                                        op.param1, [op.param2]
                                    )
                                    kk.updateGroup(X)
                                    kk.sendMessage(
                                        op.param1,
                                        None,
                                        contentMetadata={"mid": op.param2},
                                        contentType=13,
                                    )
                                    kk.sendMessage(
                                        op.param1, "Don't open link QR group without permission!", )
                        except BaseException:
                            try:
                                if (kc.getGroup(
                                        op.param1).preventedJoinByTicket == False):
                                    if (
                                        op.param2 not in Bots
                                        and op.param2 not in owner
                                        and op.param2 not in admin
                                        and op.param2 not in staff
                                    ):
                                        wait["blacklist"][op.param2] = True
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        random.choice(DRE).kickoutFromGroup(
                                            op.param1, [op.param2]
                                        )
                                        kc.updateGroup(X)
                                        kc.sendMessage(
                                            op.param1,
                                            None,
                                            contentMetadata={"mid": op.param2},
                                            contentType=13,
                                        )
                                        kc.sendMessage(
                                            op.param1, "Don't open link QR group without permission!", )
                            except BaseException:
                                pass

            if op.type == 13:
                if mid in op.param3:
                    if wait["autoLeave"]:
                        if (
                            op.param2 not in Bots
                            and op.param2 not in owner
                            and op.param2 not in admin
                            and op.param2 not in staff
                        ):
                            cl.acceptGroupInvitation(op.param1)
                            ginfo = cl.getGroup(op.param1)
                            cl.leaveGroup(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            ginfo = cl.getGroup(op.param1)

            if op.type == 13:
                if mid in op.param3:
                    if wait["autoJoin"]:
                        if (
                            op.param2 not in Bots
                            and op.param2 not in owner
                            and op.param2 not in admin
                            and op.param2 not in staff
                        ):
                            cl.acceptGroupInvitation(op.param1)
                            ginfo = cl.getGroup(op.param1)
                            cl.sendMessage(
                                op.param1, "Don't invite without my author!")
                            cl.sendMessage(op.param1, "line.me/ti/p/~mo-banzu")
                            cl.leaveGroup(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            ginfo = cl.getGroup(op.param1)
            if Amid in op.param3:
                if wait["autoJoin"]:
                    if (
                        op.param2 not in Bots
                        and op.param2 not in owner
                        and op.param2 not in admin
                        and op.param2 not in staff
                    ):
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(
                            op.param1, "Don't invite without my commander!")
                        ki.sendMessage(op.param1, "line.me/ti/p/~mo-banzu")
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
            if Bmid in op.param3:
                if wait["autoJoin"]:
                    if (
                        op.param2 not in Bots
                        and op.param2 not in owner
                        and op.param2 not in admin
                        and op.param2 not in staff
                    ):
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.sendMessage(
                            op.param1, "Don't invite without my commander!")
                        kk.sendMessage(op.param1, "line.me/ti/p/~mo-banzu")
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
            if Cmid in op.param3:
                if wait["autoJoin"]:
                    if (
                        op.param2 not in Bots
                        and op.param2 not in owner
                        and op.param2 not in admin
                        and op.param2 not in staff
                    ):
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(
                            op.param1, "Don't invite without my commander!")
                        kc.sendMessage(op.param1, "line.me/ti/p/~mo-banzu")
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)

        if op.type == 13:
            if wait["protectinvite"]:
                if (
                    op.param2 not in Bots
                    and op.param2 not in owner
                    and op.param2 not in admin
                    and op.param2 not in staff
                ):
                    try:
                        wait["blacklist"][op.param2] = True
                        G = cl.getGroup(op.param1)
                        random.choice(DRE).cancelGroupInvitation(
                            op.param1, [op.param3])
                        random.choice(DRE).kickoutFromGroup(
                            op.param1, [op.param2])
                        random.choice(DRE).inviteIntoGroup(op.param1, [Zmid])
                        cl.sendMessage(
                            op.param1, "Don't invite without permission!")
                    except BaseException:
                        try:
                            wait["blacklist"][op.param2] = True
                            G = ki.getGroup(op.param1)
                            random.choice(DRE).cancelGroupInvitation(
                                op.param1, [op.param3]
                            )
                            random.choice(DRE).kickoutFromGroup(
                                op.param1, [op.param2])
                            random.choice(DRE).inviteIntoGroup(
                                op.param1, [Zmid])
                            ki.sendMessage(
                                op.param1, "Don't invite without permission!"
                            )
                        except BaseException:
                            try:
                                wait["blacklist"][op.param2] = True
                                G = kk.getGroup(op.param1)
                                random.choice(DRE).cancelGroupInvitation(
                                    op.param1, [op.param3]
                                )
                                random.choice(DRE).kickoutFromGroup(
                                    op.param1, [op.param2]
                                )
                                random.choice(DRE).inviteIntoGroup(
                                    op.param1, [Zmid])
                                kk.sendMessage(
                                    op.param1, "Don't invite without permission!")
                            except BaseException:
                                try:
                                    wait["blacklist"][op.param2] = True
                                    G = kc.getGroup(op.param1)
                                    random.choice(DRE).cancelGroupInvitation(
                                        op.param1, [op.param3]
                                    )
                                    random.choice(DRE).kickoutFromGroup(
                                        op.param1, [op.param2]
                                    )
                                    random.choice(DRE).inviteIntoGroup(
                                        op.param1, [Zmid]
                                    )
                                    kc.sendMessage(
                                        op.param1, "Don't invite without permission!", )
                                except BaseException:
                                    pass

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(DRE).kickoutFromGroup(op.param1, [op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = "http://dl.profile.line.naver.jp" + contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in leave:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = "http://dl.profile.line.naver.jp" + contact
                leaveMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if (
                    op.param2 not in Bots
                    and op.param2 not in owner
                    and op.param2 not in admin
                    and op.param2 not in staff
                ):
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            random.choice(DRE).kickoutFromGroup(
                                op.param1, [op.param2])
                            cl.sendMessage(
                                op.param1, "Sorry anyone can't join, protect join is actived", )
                    except BaseException:
                        pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"]:
                cl.findAndAddContactsByMid(op.param1)
                sendMention(op.param1, "Hi ", "thanks for invite me!")
                cl.sendText(op.param1, wait["message"])
                cl.sendContact(op.param1, "u20452d2a7b27a3536e1172e4c8d0a8b4")

        if op.type == 19:
            if wait["protectkick"]:
                if (
                    op.param2 not in Bots
                    and op.param2 not in owner
                    and op.param2 not in admin
                    and op.param2 not in staff
                ):
                    wait["blacklist"][op.param2] = True
                    random.choice(DRE).kickoutFromGroup(op.param1, [op.param2])
                    cl.sendMessage(op.param1, "Don't kick without permission!")
                else:
                    pass

        if op.type == 19:
            if op.param1 in ghost:
                try:
                    if (
                        op.param2 not in Bots
                        and op.param2 not in owner
                        and op.param2 not in admin
                        and op.param2 not in staff
                    ):
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        sw.acceptGroupInvitationByTicket(op.param1, Ticket)
                        sw.kickoutFromGroup(op.param1, [op.param2])
                        sw.sendMessage(
                            op.param1,
                            None,
                            contentMetadata={"mid": op.param2},
                            contentType=13,
                        )
                        sw.leaveGroup(op.param1)
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
                        cl.inviteIntoGroup(op.param1, [Zmid])
                        wait["blacklist"][op.param2] = True
                except BaseException:
                    try:
                        if (
                            op.param2 not in Bots
                            and op.param2 not in owner
                            and op.param2 not in admin
                            and op.param2 not in staff
                        ):
                            G = ki.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            ki.updateGroup(G)
                            invsend = 0
                            Ticket = ki.reissueGroupTicket(op.param1)
                            sw.acceptGroupInvitationByTicket(op.param1, Ticket)
                            sw.kickoutFromGroup(op.param1, [op.param2])
                            sw.sendMessage(
                                op.param1,
                                None,
                                contentMetadata={"mid": op.param2},
                                contentType=13,
                            )
                            sw.leaveGroup(op.param1)
                            X = ki.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            ki.updateGroup(X)
                            ki.inviteIntoGroup(op.param1, [Zmid])
                            wait["blacklist"][op.param2] = True
                    except BaseException:
                        try:
                            if (
                                op.param2 not in Bots
                                and op.param2 not in owner
                                and op.param2 not in admin
                                and op.param2 not in staff
                            ):
                                G = kk.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                kk.updateGroup(G)
                                invsend = 0
                                Ticket = kk.reissueGroupTicket(op.param1)
                                sw.acceptGroupInvitationByTicket(
                                    op.param1, Ticket)
                                sw.kickoutFromGroup(op.param1, [op.param2])
                                sw.sendMessage(
                                    op.param1,
                                    None,
                                    contentMetadata={"mid": op.param2},
                                    contentType=13,
                                )
                                sw.leaveGroup(op.param1)
                                X = kk.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                kk.updateGroup(X)
                                kk.inviteIntoGroup(op.param1, [Zmid])
                                wait["blacklist"][op.param2] = True
                        except BaseException:
                            try:
                                if (
                                    op.param2 not in Bots
                                    and op.param2 not in owner
                                    and op.param2 not in admin
                                    and op.param2 not in staff
                                ):
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kc.updateGroup(G)
                                    invsend = 0
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                    sw.acceptGroupInvitationByTicket(
                                        op.param1, Ticket)
                                    sw.kickoutFromGroup(op.param1, [op.param2])
                                    sw.sendMessage(
                                        op.param1,
                                        None,
                                        contentMetadata={"mid": op.param2},
                                        contentType=13,
                                    )
                                    sw.leaveGroup(op.param1)
                                    X = kc.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kc.updateGroup(X)
                                    kc.inviteIntoGroup(op.param1, [Zmid])
                                    wait["blacklist"][op.param2] = True
                            except BaseException:
                                pass

        if op.type == 19:
            if wait["ghost"]:
                try:
                    if (
                        op.param2 not in Bots
                        and op.param2 not in owner
                        and op.param2 not in admin
                        and op.param2 not in staff
                    ):
                        G = random.choice(DRE).getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        random.choice(DRE).updateGroup(G)
                        Ticket = random.choice(
                            DRE).reissueGroupTicket(op.param1)
                        sw.acceptGroupInvitationByTicket(op.param1, Ticket)
                        sw.kickoutFromGroup(op.param1, [op.param2])
                        sw.sendMessage(
                            op.param1,
                            None,
                            contentMetadata={"mid": op.param2},
                            contentType=13,
                        )
                        sw.leaveGroup(op.param1)
                        X = random.choice(DRE).getGroup(op.param1)
                        random.choice(DRE).updateGroup(X)
                        X.preventedJoinByTicket = True
                        random.choice(DRE).inviteIntoGroup(op.param1, [Zmid])
                        wait["blacklist"][op.param2] = True
                except BaseException:
                    pass

        if op.type == 19:
            if wait["protectantijs"]:
                try:
                    if (
                        op.param2 not in Bots
                        and op.param2 not in owner
                        and op.param2 not in admin
                        and op.param2 not in staff
                    ):
                        sw.acceptGroupInvitation(op.param1)
                        sw.findAndAddContactsByMid(op.param3)
                        sw.kickoutFromGroup(op.param1, [op.param2])
                        wait["blacklist"][op.param2] = True
                        X = sw.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        sw.updateGroup(X)
                        Ticket = sw.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                        sw.leaveGroup(op.param1)
                        random.choice(DRE).inviteIntoGroup(op.param1, [Zmid])
                        X = random.choice(DRE).getGroup(op.param1)
                        X.preventJoinByTicket = False
                        random.choice(DRE).updateGroup(X)
                except BaseException:
                    pass

        if op.type == 19:
            try:
                if wait["protectantijs"]:
                    if op.param3 in mid:
                        if (
                            op.param2 not in Bots
                            and op.param2 not in owner
                            and op.param2 not in admin
                            and op.param2 not in staff
                        ):
                            G = cl.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            Ticket = cl.reissueGroupTicket(op.param1)
                            cl.acceptGroupInvitationByTicket(op.param1, Ticket)
                            ki.acceptGroupInvitationByTicket(op.param1, Ticket)
                            kk.acceptGroupInvitationByTicket(op.param1, Ticket)
                            kc.acceptGroupInvitationByTicket(op.param1, Ticket)
                            sw.acceptGroupInvitationByTicket(op.param1, Ticket)
                            sw.kickoutFromGroup(op.param1, [op.param2])
                            sw.inviteIntoGroup(
                                op.param1, [mid, Amid, Bmid, Cmid, admin]
                            )
                            sw.leaveGroup(op.param1)
                            random.choice(DRE).inviteIntoGroup(
                                op.param1, [Zmid])
                            X = random.choice(DRE).getGroup(op.param1)
                            random.choice(DRE).updateGroup(X)
                            X.preventedJoinByTicket = True
                            wait["blacklist"][op.param2] = True
                        else:
                            pass

                if op.param3 in Zmid:
                    if (
                        op.param2 not in Bots
                        and op.param2 not in owner
                        and op.param2 not in admin
                        and op.param2 not in staff
                    ):
                        random.choice(DRE).kickoutFromGroup(
                            op.param1, [op.param2])
                        random.choice(DRE).findAndAddContactsByMid(op.param3)
                        random.choice(DRE).inviteIntoGroup(op.param1, [Zmid])
                    else:
                        random.choice(DRE).kickoutFromGroup(
                            op.param1, [op.param2])
                        random.choice(DRE).findAndAddContactsByMid(op.param3)
                        random.choice(DRE).inviteIntoGroup(op.param1, [Zmid])

                if (
                    op.param2 not in Bots
                    and op.param2 not in owner
                    and op.param2 not in admin
                    and op.param2 not in staff
                ):
                    if op.param3 in admin:
                        if wait["backup"]:
                            wait["blacklist"][op.param2] = True
                            random.choice(DRE).kickoutFromGroup(
                                op.param1, [op.param2])
                            random.choice(
                                DRE).findAndAddContactsByMid(op.param3)
                            random.choice(DRE).inviteIntoGroup(
                                op.param1, [op.param3])
                else:
                    pass

                if op.param3 in Amid:
                    if (
                        op.param2 not in Bots
                        and op.param2 not in owner
                        and op.param2 not in admin
                        and op.param2 not in staff
                    ):
                        random.choice(DRE).kickoutFromGroup(
                            op.param1, [op.param2])
                        random.choice(DRE).findAndAddContactsByMid(op.param3)
                        random.choice(DRE).inviteIntoGroup(op.param1, [Amid])
                    else:
                        random.choice(DRE).kickoutFromGroup(
                            op.param1, [op.param2])
                        random.choice(DRE).findAndAddContactsByMid(op.param3)
                        random.choice(DRE).inviteIntoGroup(op.param1, [Amid])

                if (
                    op.param2 not in Bots
                    and op.param2 not in owner
                    and op.param2 not in admin
                    and op.param2 not in staff
                ):
                    if op.param3 in admin:
                        if wait["backup"]:
                            wait["blacklist"][op.param2] = True
                            random.choice(DRE).kickoutFromGroup(
                                op.param1, [op.param2])
                            random.choice(
                                DRE).findAndAddContactsByMid(op.param3)
                            random.choice(DRE).inviteIntoGroup(
                                op.param1, [op.param3])
                else:
                    pass

                if op.param3 in Bmid:
                    if (
                        op.param2 not in Bots
                        and op.param2 not in owner
                        and op.param2 not in admin
                        and op.param2 not in staff
                    ):
                        random.choice(DRE).kickoutFromGroup(
                            op.param1, [op.param2])
                        random.choice(DRE).findAndAddContactsByMid(op.param3)
                        random.choice(DRE).inviteIntoGroup(op.param1, [Bmid])
                    else:
                        random.choice(DRE).kickoutFromGroup(
                            op.param1, [op.param2])
                        random.choice(DRE).findAndAddContactsByMid(op.param3)
                        random.choice(DRE).inviteIntoGroup(op.param1, [Bmid])

                if (
                    op.param2 not in Bots
                    and op.param2 not in owner
                    and op.param2 not in admin
                    and op.param2 not in staff
                ):
                    if op.param3 in admin:
                        if wait["backup"]:
                            wait["blacklist"][op.param2] = True
                            random.choice(DRE).kickoutFromGroup(
                                op.param1, [op.param2])
                            random.choice(
                                DRE).findAndAddContactsByMid(op.param3)
                            random.choice(DRE).inviteIntoGroup(
                                op.param1, [op.param3])
                else:
                    pass

                if op.param3 in Cmid:
                    if (
                        op.param2 not in Bots
                        and op.param2 not in owner
                        and op.param2 not in admin
                        and op.param2 not in staff
                    ):
                        random.choice(DRE).kickoutFromGroup(
                            op.param1, [op.param2])
                        random.choice(DRE).findAndAddContactsByMid(op.param3)
                        random.choice(DRE).inviteIntoGroup(op.param1, [Cmid])
                    else:
                        random.choice(DRE).kickoutFromGroup(
                            op.param1, [op.param2])
                        random.choice(DRE).findAndAddContactsByMid(op.param3)
                        random.choice(DRE).inviteIntoGroup(op.param1, [Cmid])

                if (
                    op.param2 not in Bots
                    and op.param2 not in owner
                    and op.param2 not in admin
                    and op.param2 not in staff
                ):
                    if op.param3 in admin:
                        if wait["backup"]:
                            wait["blacklist"][op.param2] = True
                            random.choice(DRE).kickoutFromGroup(
                                op.param1, [op.param2])
                            random.choice(
                                DRE).findAndAddContactsByMid(op.param3)
                            random.choice(DRE).inviteIntoGroup(
                                op.param1, [op.param3])
                else:
                    pass
            except BaseException:
                pass

        if op.type == 32:
            if wait["protectcancel"]:
                if (
                    op.param2 not in Bots
                    and op.param2 not in owner
                    and op.param2 not in admin
                    and op.param2 not in staff
                ):
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            random.choice(DRE).kickoutFromGroup(
                                op.param1, [op.param2])
                            random.choice(DRE).inviteIntoGroup(
                                op.param1, [Zmid])
                            cl.sendMessage(
                                op.param1, "Don't cancel pending member without permission!", )
                    except BaseException:
                        pass
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1, [op.param2])
                        ki.inviteIntoGroup(op.param1, [mid, Bmid, Cmid])
                        cl.acceptGroupInvitation(op.param1)
                        kk.acceptGrouoInvitation(op.param1)
                        kc.acceptGroupInvitation(op.param1)
                        random.choice(DRE).inviteIntoGroup(op.param1, [Zmid])
                    except BaseException:
                        try:
                            kk.kickoutFromGroup(op.param1, [op.param2])
                            kk.inviteIntoGroup(op.param1, [mid, Amid, Cmid])
                            cl.acceptGroupInvitation(op.param1)
                            ki.acceptGroupInvitation(op.param1)
                            kc.acceptGroupInvitation(op.param1)
                            random.choice(DRE).inviteIntoGroup(
                                op.param1, [Zmid])
                        except BaseException:
                            try:
                                kc.kickoutFromGroup(op.param1, [op.param2])
                                kc.inviteIntoGroup(
                                    op.param1, [mid, Amid, Bmid])
                                cl.acceptGroupInvitation(op.param1)
                                ki.acceptGroupInvitation(op.param1)
                                kk.acceptGroupInvitation(op.param1)
                                random.choice(DRE).inviteIntoGroup(
                                    op.param1, [Zmid])
                            except BaseException:
                                try:
                                    G = random.choice(DRE).getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(DRE).kickoutFromGroup(
                                        op.param1, [op.param2]
                                    )
                                    random.choice(DRE).updateGroup(G)
                                    Ticket = random.choice(
                                        DRE).reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(
                                        op.param1, Ticket)
                                    ki.acceptGroupInvitationByTicket(
                                        op.param1, Ticket)
                                    kk.acceptGroupInvitationByTicket(
                                        op.param1, Ticket)
                                    kc.acceptGroupInvitationByTicket(
                                        op.param1, Ticket)
                                    G = random.choice(DRE).getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    random.chaoice(DRE).updateGroup(G)
                                    Ticket = random.choice(
                                        DRE).reissueGroupTicket(op.param1)
                                except BaseException:
                                    pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1, [op.param2])
                        kk.inviteIntoGroup(op.param1, [Amid, mid, Cmid])
                        ki.acceptGroupInvitation(op.param1)
                        cl.acceptGroupInvitation(op.param1)
                        kc.acceptGroupInvitation(op.param1)
                        random.choice(DRE).inviteIntoGroup(op.param1, [Zmid])
                    except BaseException:
                        try:
                            kc.kickoutFromGroup(op.param1, [op.param2])
                            kc.inviteIntoGroup(op.param1, [Amid, mid, Bmid])
                            ki.acceptGroupInvitation(op.param1)
                            cl.acceptGroupInvitation(op.param1)
                            kk.acceptGroupInvitation(op.param1)
                            random.choice(DRE).inviteIntoGroup(
                                op.param1, [Zmid])
                        except BaseException:
                            try:
                                cl.kickoutFromGroup(op.param1, [op.param2])
                                cl.inviteIntoGroup(
                                    op.param1, [Amid, Bmid, Cmid])
                                ki.acceptGroupInvitation(op.param1)
                                kk.acceptGroupInvitation(op.param1)
                                kc.acceptGroupInvitation(op.param1)
                                random.choice(DRE).inviteIntoGroup(
                                    op.param1, [Zmid])
                            except BaseException:
                                try:
                                    G = random.choice(DRE).getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(DRE).kickoutFromGroup(
                                        op.param1, [op.param2]
                                    )
                                    random.choice(DRE).updateGroup(G)
                                    Ticket = random.choice(
                                        DRE).reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(
                                        op.param1, Ticket)
                                    ki.acceptGroupInvitationByTicket(
                                        op.param1, Ticket)
                                    kk.acceptGroupInvitationByTicket(
                                        op.param1, Ticket)
                                    kc.acceptGroupInvitationByTicket(
                                        op.param1, Ticket)
                                    G = kLrandom.choice(
                                        DRE).getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    random.choice(DRE).updateGroup(G)
                                    Ticket = random.choice(
                                        DRE).reissueGroupTicket(op.param1)
                                except BaseException:
                                    pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1, [op.param2])
                        kc.inviteIntoGroup(op.param1, [Bmid, mid, Amid])
                        kk.acceptGroupInvitation(op.param1)
                        cl.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        random.choice(DRE).inviteIntoGroup(op.param1, [Zmid])
                    except BaseException:
                        try:
                            cl.kickoutFromGroup(op.param1, [op.param2])
                            cl.inviteIntoGroup(op.param1, [Bmid, Amid, Cmid])
                            kk.acceptGroupInvitation(op.param1)
                            ki.acceptGroupInvitation(op.param1)
                            kc.acceptGroupInvitation(op.param1)
                            random.choice(DRE).inviteIntoGroup(
                                op.param1, [Zmid])
                        except BaseException:
                            try:
                                ki.kickoutFromGroup(op.param1, [op.param2])
                                ki.inviteIntoGroup(
                                    op.param1, [Bmid, mid, Cmid])
                                kk.acceptGroupInvitation(op.param1)
                                cl.acceptGroupInvitation(op.param1)
                                kc.acceptGroupInvitation(op.param1)
                                random.choice(DRE).inviteIntoGroup(
                                    op.param1, [Zmid])
                            except BaseException:
                                try:
                                    G = random.choice(DRE).getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(DRE).kickoutFromGroup(
                                        op.param1, [op.param2]
                                    )
                                    random.choice(DRE).updateGroup(G)
                                    Ticket = random.choice(
                                        DRE).reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(
                                        op.param1, Ticket)
                                    ki.acceptGroupInvitationByTicket(
                                        op.param1, Ticket)
                                    kk.acceptGroupInvitationByTicket(
                                        op.param1, Ticket)
                                    kc.acceptGroupInvitationByTicket(
                                        op.param1, Ticket)
                                    G = random.choice(DRE).getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    random.choice(DRE).updateGroup(G)
                                    Ticket = random.choice(
                                        DRE).reissueGroupTicket(op.param1)
                                except BaseException:
                                    pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1, [op.param2])
                        cl.inviteIntoGroup(op.param1, [Cmid, Amid, Bmid])
                        kc.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        kk.acceptGroupInvitation(op.param1)
                        random.choice(DRE).inviteIntoGroup(op.param1, [Zmid])
                    except BaseException:
                        try:
                            ki.kickoutFromGroup(op.param1, [op.param2])
                            ki.inviteIntoGroup(op.param1, [Cmid, mid, Bmid])
                            kc.acceptGroupInvitation(op.param1)
                            cl.acceptGroupInvitation(op.param1)
                            kk.acceptGroupInvitation(op.param1)
                            random.choice(DRE).inviteIntoGroup(
                                op.param1, [Zmid])
                        except BaseException:
                            try:
                                kk.kickoutFromGroup(op.param1, [op.param2])
                                kk.inviteIntoGroup(
                                    op.param1, [Cmid, mid, Amid])
                                kc.acceptGroupInvitation(op.param1)
                                cl.acceptGroupInvitation(op.param1)
                                ki.acceptGroupInvitation(op.param1)
                                random.choice(DRE).inviteIntoGroup(
                                    op.param1, [Zmid])
                            except BaseException:
                                try:
                                    G = random.choice(DRE).getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(DRE).kickoutFromGroup(
                                        op.param1, [op.param2]
                                    )
                                    random.choice(DRE).updateGroup(G)
                                    Ticket = random.choice(
                                        DRE).reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(
                                        op.param1, Ticket)
                                    ki.acceptGroupInvitationByTicket(
                                        op.param1, Ticket)
                                    kk.acceptGroupInvitationByTicket(
                                        op.param1, Ticket)
                                    kc.acceptGroupInvitationByTicket(
                                        op.param1, Ticket)
                                    G = random.choice(DRE).getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    random.choice(DRE).updateGroup(G)
                                    Ticket = random.choice(
                                        DRE).reissueGroupTicket(op.param1)
                                except BaseException:
                                    pass
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1, [op.param2])
                        cl.findAndAddContactsByMid(op.param1, op.param3)
                        cl.inviteIntoGroup(op.param1, op.param3)
                    except BaseException:
                        try:
                            ki.kickoutFromGroup(op.param1, [op.param2])
                            ki.findAndAddContactsByMid(op.param1, op.param3)
                            ki.inviteIntoGroup(op.param1, op.param3)
                        except BaseException:
                            try:
                                kk.kickoutFromGroup(op.param1, [op.param2])
                                kk.findAndAddContactsByMid(
                                    op.param1, op.param3)
                                kk.inviteIntoGroup(op.param1, op.param3)
                            except BaseException:
                                try:
                                    kc.kickoutFromGroup(op.param1, [op.param2])
                                    kc.findAndAddContactsByMid(
                                        op.param1, op.param3)
                                    kc.inviteIntoGroup(op.param1, op.param3)
                                except BaseException:
                                    pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1, [op.param2])
                        cl.findAndAddContactsByMid(op.param1, op.param3)
                        cl.inviteIntoGroup(op.param1, op.param3)
                    except BaseException:
                        try:
                            ki.kickoutFromGroup(op.param1, [op.param2])
                            ki.findAndAddContactsByMid(op.param1, op.param3)
                            ki.inviteIntoGroup(op.param1, op.param3)
                        except BaseException:
                            try:
                                kk.kickoutFromGroup(op.param1, [op.param2])
                                kk.findAndAddContactsByMid(
                                    op.param1, op.param3)
                                kk.inviteIntoGroup(op.param1, op.param3)
                            except BaseException:
                                try:
                                    kc.kickoutFromGroup(op.param1, [op.param2])
                                    kc.findAndAddContactsByMid(
                                        op.param1, op.param3)
                                    kc.inviteIntoGroup(op.param1, op.param3)
                                except BaseException:
                                    pass
                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["RAreadPoint"]:
                    if op.param2 in Setmain["RAreadMember"][op.param1]:
                        pass
                    else:
                        Setmain["RAreadMember"][op.param1][op.param2] = True
                else:
                    pass
            except BaseException:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(DRE).kickoutFromGroup(op.param1, [op.param2])
            else:
                pass

        if op.type == 55:
            try:
                if op.param1 in Setmain["ARreadPoint"]:
                    if op.param2 in Setmain["ARreadMember"][op.param1]:
                        pass
                    else:
                        Setmain["ARreadMember"][op.param1][op.param2] = True
                else:
                    pass
            except BaseException:
                pass

            if cctv["cyduk"][op.param1]:
                if op.param1 in cctv["point"]:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv["sidermem"][op.param1]:
                        pass
                    else:
                        cctv["sidermem"][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        sider = cl.getContact(op.param2).picturePath
                        image = "http://dl.profile.line.naver.jp" + sider
                        cl.sendImageWithURL(op.param1, image)

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(DRE).kickoutFromGroup(op.param1, [op.param2])
            else:
                pass

        if op.type == 26:
            if wait["selfbot"]:
                msg = op.message
                if msg._from not in Bots:
                    if msg._from in wait["blacklist"]:
                        try:
                            random.choice(DRE).kickoutFromGroup(
                                msg.to, [msg._from])
                        except BaseException:
                            try:
                                random.choice(DRE).kickoutFromGroup(
                                    msg.to, [msg._from])
                            except BaseException:
                                random.choice(DRE).kickoutFromGroup(
                                    msg.to, [msg._from])
                if msg._from not in Bots:
                    if wait["talkban"]:
                        if msg._from in wait["Talkblacklist"]:
                            try:
                                random.choice(DRE).kickoutFromGroup(
                                    msg.to, [msg._from])
                            except BaseException:
                                try:
                                    random.choice(DRE).kickoutFromGroup(
                                        msg.to, [msg._from]
                                    )
                                except BaseException:
                                    random.choice(DRE).kickoutFromGroup(
                                        msg.to, [msg._from]
                                    )
                if "MENTION" in msg.contentMetadata.keys() is not None:
                    if wait["detectMention"]:
                        contact = cl.getContact(msg._from)
                        image = (
                            "http://dl.profile.line-cdn.net/" +
                            contact.pictureStatus)
                        name = re.findall(r"@(\w+)", msg.text)
                        mention = ast.literal_eval(
                            msg.contentMetadata["MENTION"])
                        mentionees = mention["MENTIONEES"]
                        for mention in mentionees:
                            if mention["M"] in Bots:
                                squads = cl.getContact(msg._from)
                                sendMention(
                                    msg.to, squads.mid, "", wait["Respontag"])
                                cl.sendMessage(
                                    msg.to,
                                    None,
                                    contentMetadata={
                                        "STKID": "25628787",
                                        "STKPKGID": "1818607",
                                        "STKVER": "1",
                                    },
                                    contentType=7,
                                )
                                cl.sendMessage(msg.to, wait["Respontag"])
                                cl.sendImageWithURL(msg.to, image)
                                rnd = ["Hallo!"]
                                p = random.choice(rnd)
                                lang = "id"
                                tts = gTTS(text=p, lang=lang)
                                tts.save("hasil.mp3")
                                cl.sendAudio(msg.to, "hasil.mp3")
                                cl.sendMessage(
                                    msg.to,
                                    None,
                                    contentMetadata={
                                        "STKID": "25628787",
                                        "STKPKGID": "1818607",
                                        "STKVER": "1",
                                    },
                                    contentType=7,
                                )
                                break
                if "MENTION" in msg.contentMetadata.keys() is not None:
                    if msg._from not in Bots:
                        if wait["detectMention"]:
                            name = re.findall(r"@(\w+)", msg.text)
                            mention = ast.literal_eval(
                                msg.contentMetadata["MENTION"])
                            mentionees = mention["MENTIONEES"]
                            for mention in mentionees:
                                if mention["M"] in admin:
                                    squads = cl.getContact(msg._from)
                                    sendMention(
                                        msg.to, squads.mid, "", wait["Respontag"])
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={
                                            "PRDID": "a0768339-c2d3-4189-9653-2909e9bb6f58",
                                            "PRDTYPE": "THEME",
                                            "MSGTPL": "6",
                                        },
                                        contentType=9,
                                    )
                                    break
                if "MENTION" in msg.contentMetadata.keys() is not None:
                    if msg._from not in Bots:
                        if wait["mentionKick"]:
                            name = re.findall(r"@(\w+)", msg.text)
                            mention = ast.literal_eval(
                                msg.contentMetadata["MENTION"])
                            mentionees = mention["MENTIONEES"]
                            for mention in mentionees:
                                if mention["M"] in admin:
                                    cl.sendMessage(msg.to, "Don't tag me!")
                                    cl.kickoutFromGroup(msg.to, [msg._from])
                                    break
                if msg.contentType == 7:
                    if wait["sticker"]:
                        msg.contentType = 0
                        cl.sendMessage(
                            msg.to,
                            "「ID Sticker」\n• STKID : "
                            + msg.contentMetadata["STKID"]
                            + "\n• STKPKGID : "
                            + msg.contentMetadata["STKPKGID"]
                            + "\n• STKVER : "
                            + msg.contentMetadata["STKVER"]
                            + "\n\n「Link Sticker」"
                            + "\nline://shop/detail/"
                            + msg.contentMetadata["STKPKGID"],
                        )
                if msg.contentType == 13:
                    if wait["contact"]:
                        msg.contentType = 0
                        cl.sendMessage(msg.to, msg.contentMetadata["mid"])
                        if "displayName" in msg.contentMetadata:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            path = cl.getContact(
                                msg.contentMetadata["mid"]).picturePath
                            image = "http://dl.profile.line.naver.jp" + path
                            cl.sendMessage(
                                msg.to,
                                "• Nama : " +
                                msg.contentMetadata["displayName"] +
                                "\n• MID : " +
                                msg.contentMetadata["mid"] +
                                "\n• Status Message : " +
                                contact.statusMessage +
                                "\n• Picture URL : http://dl.profile.line-cdn.net/" +
                                contact.pictureStatus,
                            )
                            cl.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 7:
                    if wait["sticker"]:
                        msg.contentType = 0
                        cl.sendMessage(
                            msg.to,
                            "• STKID : "
                            + msg.contentMetadata["STKID"]
                            + "\n• STKPKGID : "
                            + msg.contentMetadata["STKPKGID"]
                            + "\n• STKVER : "
                            + msg.contentMetadata["STKVER"]
                            + "\n\n「Link Sticker」"
                            + "\nline://shop/detail/"
                            + msg.contentMetadata["STKPKGID"],
                        )
                if msg.contentType == 13:
                    if wait["contact"]:
                        msg.contentType = 0
                        cl.sendMessage(msg.to, msg.contentMetadata["mid"])
                        if "displayName" in msg.contentMetadata:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            path = cl.getContact(
                                msg.contentMetadata["mid"]).picturePath
                            image = "http://dl.profile.line.naver.jp" + path
                            cl.sendMessage(
                                msg.to,
                                "• Nama : " +
                                msg.contentMetadata["displayName"] +
                                "\n• MID : " +
                                msg.contentMetadata["mid"] +
                                "\n• Status Message : " +
                                contact.statusMessage +
                                "\n• Picture URL : http://dl.profile.line-cdn.net/" +
                                contact.pictureStatus,
                            )
                            cl.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
                if msg.toType == 0:
                    to = msg._from
                elif msg.toType == 2:
                    to = msg.to
                if msg.contentType == 16:
                    if wait["Timeline"]:
                        ret_ = "「 Detail Post 」"
                        if msg.contentMetadata["serviceType"] == "GB":
                            contact = cl.getContact(sender)
                            auth = "\n• Penulis : {}".format(
                                str(contact.displayName))
                        else:
                            auth = "\n• Penulis : {}".format(
                                str(msg.contentMetadata["serviceName"])
                            )
                        ret_ += auth
                        if "stickerId" in msg.contentMetadata:
                            stck = "\n• Sticker : https://line.me/R/shop/detail/{}".format(
                                str(msg.contentMetadata["packageId"]))
                            ret_ += stck
                        if "mediaOid" in msg.contentMetadata:
                            object_ = msg.contentMetadata["mediaOid"].replace(
                                "svc=myhome|sid=h|", ""
                            )
                            if msg.contentMetadata["mediaType"] == "V":
                                if msg.contentMetadata["serviceType"] == "GB":
                                    ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(
                                        str(msg.contentMetadata["mediaOid"]))
                                    murl = "\n• Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(
                                        str(msg.contentMetadata["mediaOid"]))
                                else:
                                    ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(
                                        str(object_))
                                    murl = "\n• Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(
                                        str(object_))
                                ret_ += murl
                            else:
                                if msg.contentMetadata["serviceType"] == "GB":
                                    ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(
                                        str(msg.contentMetadata["mediaOid"]))
                                else:
                                    ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(
                                        str(object_))
                            ret_ += ourl
                        if "text" in msg.contentMetadata:
                            text = "\n• Text : {}".format(
                                str(msg.contentMetadata["text"])
                            )
                            purl = "\n• Post URL : {}".format(
                                str(msg.contentMetadata["postEndUrl"]).replace(
                                    "line://", "https://line.me/R/"
                                )
                            )
                            ret_ += purl
                            ret_ += text
                        cl.sendMessage(to, str(ret_))
                        cl.like(url[25:58], url[66:], likeType=1005)
                        cl.comment(url[25:58], url[66:], wait["message"])
                if msg.contentType == 0:
                    msg_dict[msg.id] = {
                        "text": msg.text,
                        "from": msg._from,
                        "createdTime": msg.createdTime,
                    }
                if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {
                        "text": "Memuat gambar...",
                        "data": path,
                        "from": msg._from,
                        "createdTime": msg.createdTime,
                    }
                if msg.contentType == 7:
                    stk_id = msg.contentMetadata["STKID"]
                    stk_ver = msg.contentMetadata["STKVER"]
                    pkg_id = msg.contentMetadata["STKPKGID"]
                    ret_ = "\n\n「 Sticker Info 」"
                    ret_ += "\n• Sticker ID : {}".format(stk_id)
                    ret_ += "\n• Sticker Version : {}".format(stk_ver)
                    ret_ += "\n• Sticker Package : {}".format(pkg_id)
                    ret_ += "\n• Sticker URL : line://shop/detail/{}".format(
                        pkg_id)
                    query = int(stk_id)
                    if isinstance(query, int):
                        data = (
                            "https://stickershop.line-scdn.net/stickershop/v1/sticker/" +
                            str(query) +
                            "/ANDROID/sticker.png")
                        path = cl.downloadFileURL(data)
                        msg_dict1[msg.id] = {
                            "text": str(ret_),
                            "data": path,
                            "from": msg._from,
                            "createdTime": msg.createdTime,
                        }
                if msg.contentType == 7:
                    if wait["stickerOn"]:
                        stk_id = msg.contentMetadata["STKID"]
                        stk_ver = msg.contentMetadata["STKVER"]
                        pkg_id = msg.contentMetadata["STKPKGID"]
                        with requests.session() as s:
                            s.headers["user-agent"] = "Mozilla/5.0"
                            r = s.get(
                                "https://store.line.me/stickershop/product/{}/id".format(
                                    urllib.parse.quote(pkg_id)
                                )
                            )
                            soup = BeautifulSoup(r.content, "html5lib")
                            data = soup.select("[class~=mdBtn01Txt]")[0].text
                            if data == "Lihat Produk Lain":
                                ret_ = "「 Sticker Info 」"
                                ret_ += "\n• Sticker ID : {}".format(stk_id)
                                ret_ += "\n• Sticker Package : {}".format(
                                    pkg_id)
                                ret_ += "\n• Sticker Version : {}".format(
                                    stk_ver)
                                ret_ += "\n• Sticker URL : line://shop/detail/{}".format(
                                    pkg_id)
                                cl.sendMessage(msg.to, str(ret_))
                                query = int(stk_id)
                                if isinstance(query, int):
                                    data = (
                                        "https://stickershop.line-scdn.net/stickershop/v1/sticker/" +
                                        str(query) +
                                        "/ANDROID/sticker.png")
                                    path = cl.downloadFileURL(data)
                                    cl.sendImage(msg.to, path)
                            else:
                                ret_ = "「 Sticker Info 」"
                                ret_ += (
                                    "\n• Price : "
                                    + soup.findAll(
                                        "p", attrs={"class": "mdCMN08Price"}
                                    )[0].text
                                )
                                ret_ += ("\n• Author : " +
                                         soup.select("a[href*=/stickershop/author]")[0].text)
                                ret_ += "\n• Sticker ID : {}".format(
                                    str(stk_id))
                                ret_ += "\n• Sticker Package : {}".format(
                                    str(pkg_id))
                                ret_ += "\n• Sticker Version : {}".format(
                                    str(stk_ver))
                                ret_ += "\n• Sticker URL : line://shop/detail/{}".format(
                                    str(pkg_id))
                                ret_ += ("\n• Description :\n" + soup.findAll("p",
                                                                              attrs={"class": "mdCMN08Desc"})[0].text)
                                cl.sendMessage(msg.to, str(ret_))
                                query = int(stk_id)
                                if isinstance(query, int):
                                    data = (
                                        "https://stickershop.line-scdn.net/stickershop/v1/sticker/" +
                                        str(query) +
                                        "/ANDROID/sticker.png")
                                    path = cl.downloadFileURL(data)
                                    cl.sendImage(msg.to, path)
                if msg.contentType == 13:
                    if wait["contact"]:
                        msg.contentType = 0
                        cl.sendMessage(msg.to, msg.contentMetadata["mid"])
                        if "displayName" in msg.contentMetadata:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            path = cl.getContact(
                                msg.contentMetadata["mid"]).picturePath
                            image = "http://dl.profile.line.naver.jp" + path
                            cl.sendMessage(
                                msg.to,
                                "「 Contact Info 」\n• Nama : " +
                                msg.contentMetadata["displayName"] +
                                "\n• MID : " +
                                msg.contentMetadata["mid"] +
                                "\n• Status Message : " +
                                contact.statusMessage +
                                "\n• Picture URL : http://dl.profile.line-cdn.net/" +
                                contact.pictureStatus,
                            )
                            cl.sendImageWithURL(msg.to, image)
                if msg.contentType == 13:
                    if msg._from in admin:
                        if wait["invite"]:
                            msg.contentType = 0
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            invite = msg.contentMetadata["mid"]
                            groups = cl.getGroup(msg.to)
                            pending = groups.invitee
                            targets = []
                            for s in groups.members:
                                if invite in wait["blacklist"]:
                                    cl.sendMessage(
                                        msg.to, "Ter-blacklist! Hapus blacklist lalu invite lagi", )
                                    break
                                else:
                                    targets.append(invite)
                            if targets == []:
                                pass
                            else:
                                for target in targets:
                                    try:
                                        cl.findAndAddContactsByMid(target)
                                        cl.inviteIntoGroup(msg.to, [target])
                                        ryan = cl.getContact(target)
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = "「 Sukses Invite 」\nNama : "
                                        ret_ = "Ketik 'Invite off' jika sudah selesai"
                                        ry = str(ryan.displayName)
                                        pesan = ""
                                        pesan2 = pesan + "@x\n"
                                        xlen = str(len(zxc) + len(xpesan))
                                        xlen2 = str(
                                            len(zxc) + len(pesan2) + len(xpesan) - 1)
                                        zx = {
                                            "S": xlen, "E": xlen2, "M": ryan.mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                        text = xpesan + zxc + ret_ + ""
                                        cl.sendMessage(
                                            msg.to,
                                            text,
                                            contentMetadata={
                                                "MENTION": str(
                                                    '{"MENTIONEES":' +
                                                    json.dumps(zx2).replace(
                                                        " ",
                                                        "") +
                                                    "}")},
                                            contentType=0,
                                        )
                                        wait["invite"] = False
                                        break
                                    except BaseException:
                                        cl.sendText(
                                            msg.to, "Anda terkena limit")
                                        wait["invite"] = False
                                        break

                # ADD BOTS
                if msg.contentType == 13:
                    if msg._from in admin:
                        if wait["addbots"]:
                            if msg.contentMetadata["mid"] in Bots:
                                cl.sendMessage(
                                    msg.to, "Contact itu sudah jadi bot")
                                wait["addbots"] = True
                            else:
                                Bots.append(msg.contentMetadata["mid"])
                                wait["addbots"] = True
                                cl.sendMessage(
                                    msg.to, "Berhasil menambahkan ke bot")
                    if wait["dellbots"]:
                        if msg.contentMetadata["mid"] in Bots:
                            Bots.remove(msg.contentMetadata["mid"])
                            cl.sendMessage(
                                msg.to, "Berhasil menghapus dari bot")
                        else:
                            wait["dellbots"] = True
                            cl.sendMessage(msg.to, "Contact itu bukan bot")

                # ADD STAFF
                if msg.contentType == 13:
                    if msg._from in admin:
                        if wait["addstaff"]:
                            if msg.contentMetadata["mid"] in staff:
                                cl.sendMessage(
                                    msg.to, "Contact itu sudah jadi staff")
                                wait["addstaff"] = True
                            else:
                                staff.append(msg.contentMetadata["mid"])
                                wait["addstaff"] = True
                                cl.sendMessage(
                                    msg.to, "Berhasil menambahkan ke staff")
                    if wait["dellstaff"]:
                        if msg.contentMetadata["mid"] in staff:
                            staff.remove(msg.contentMetadata["mid"])
                            cl.sendMessage(
                                msg.to, "Berhasil menghapus dari staff")
                            wait["dellstaff"] = True
                        else:
                            wait["dellstaff"] = True
                            cl.sendMessage(msg.to, "Contact itu bukan staff")

                # ADD ADMIN
                if msg.contentType == 13:
                    if msg._from in admin:
                        if wait["addadmin"]:
                            if msg.contentMetadata["mid"] in admin:
                                cl.sendMessage(
                                    msg.to, "Contact itu sudah jadi admin")
                                wait["addadmin"] = True
                            else:
                                admin.append(msg.contentMetadata["mid"])
                                wait["addadmin"] = True
                                cl.sendMessage(
                                    msg.to, "Berhasil menambahkan ke admin")
                    if wait["delladmin"]:
                        if msg.contentMetadata["mid"] in admin:
                            admin.remove(msg.contentMetadata["mid"])
                            cl.sendMessage(
                                msg.to, "Berhasil menghapus dari admin")
                        else:
                            wait["delladmin"] = True
                            cl.sendMessage(msg.to, "Contact itu bukan admin")

                # ADD BLACKLIST
                if msg.contentType == 13:
                    if msg._from in admin:
                        if wait["wblacklist"]:
                            if msg.contentMetadata["mid"] in wait["blacklist"]:
                                cl.sendMessage(
                                    msg.to, "Contact itu sudah ada di blacklist")
                                wait["wblacklist"] = True
                            else:
                                wait["blacklist"][msg.contentMetadata["mid"]] = True
                                wait["wblacklist"] = True
                                cl.sendMessage(
                                    msg.to, "Berhasil menambahkan ke blacklist"
                                )
                    if wait["dblacklist"]:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            del wait["blacklist"][msg.contentMetadata["mid"]]
                            cl.sendMessage(
                                msg.to, "Berhasil menghapus dari blacklist")
                        else:
                            wait["dblacklist"] = True
                            cl.sendMessage(
                                msg.to, "Contact itu tidak ada di blacklist")

                # ADD TALKBAN
                if msg.contentType == 13:
                    if msg._from in admin:
                        if wait["Talkwblacklist"]:
                            if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                                cl.sendMessage(
                                    msg.to, "Contact itu sudah ada di Talkban"
                                )
                                wait["Talkwblacklist"] = True
                            else:
                                wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                                wait["Talkwblacklist"] = True
                                cl.sendMessage(
                                    msg.to, "Berhasil menambahkan ke Talkban"
                                )
                    if wait["Talkdblacklist"]:
                        if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                            del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                            cl.sendMessage(
                                msg.to, "Berhasil menghapus dari Talkban")
                        else:
                            wait["Talkdblacklist"] = True
                            cl.sendMessage(
                                msg.to, "Contact itu tidak ada di Talkban")

                # MEDIA
                if msg.contentType == 1:
                    if msg._from in admin:
                        if wait["Addimage"]["status"]:
                            path = cl.downloadObjectMsg(msg.id)
                            images[wait["Addimage"]["name"]] = str(path)
                            f = codecs.open("image.json", "w", "utf-8")
                            json.dump(images, f, sort_keys=True,
                                      indent=4, ensure_ascii=False)
                            cl.sendMessage(
                                msg.to,
                                "Berhasil menambahkan gambar {}".format(
                                    str(wait["Addimage"]["name"])
                                ),
                            )
                            wait["Addimage"]["status"] = False
                            wait["Addimage"]["name"] = ""
                if msg.contentType == 2:
                    if msg._from in admin:
                        if wait["Addvideo"]["status"]:
                            path = cl.downloadObjectMsg(msg.id)
                            videos[wait["Addvideo"]["name"]] = str(path)
                            f = codecs.open("video.json", "w", "utf-8")
                            json.dump(videos, f, sort_keys=True,
                                      indent=4, ensure_ascii=False)
                            cl.sendMessage(
                                msg.to,
                                "Berhasil menambahkan video {}".format(
                                    str(wait["Addvideo"]["name"])
                                ),
                            )
                            wait["Addvideo"]["status"] = False
                            wait["Addvideo"]["name"] = ""
                if msg.contentType == 7:
                    if msg._from in admin:
                        if wait["Addsticker"]["status"]:
                            stickers[wait["Addsticker"]["name"]] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"],
                            }
                            f = codecs.open("sticker.json", "w", "utf-8")
                            json.dump(
                                stickers,
                                f,
                                sort_keys=True,
                                indent=4,
                                ensure_ascii=False,
                            )
                            cl.sendMessage(
                                msg.to,
                                "Berhasil menambahkan sticker {}".format(
                                    str(wait["Addsticker"]["name"])
                                ),
                            )
                            wait["Addsticker"]["status"] = False
                            wait["Addsticker"]["name"] = ""
                if msg.contentType == 3:
                    if msg._from in admin:
                        if wait["Addaudio"]["status"]:
                            path = cl.downloadObjectMsg(msg.id)
                            audios[wait["Addaudio"]["name"]] = str(path)
                            f = codecs.open("audio.json", "w", "utf-8")
                            json.dump(audios, f, sort_keys=True,
                                      indent=4, ensure_ascii=False)
                            cl.sendMessage(
                                msg.to,
                                "Berhasil menambahkan mp3 {}".format(
                                    str(wait["Addaudio"]["name"])
                                ),
                            )
                            wait["Addaudio"]["status"] = False
                            wait["Addaudio"]["name"] = ""

                if msg.contentType == 1:
                    if msg._from in admin:
                        if mid in Setmain["ARfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to, "Foto berhasil dirubah")
                        if Amid in Setmain["ARfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to, "Foto berhasil dirubah")
                        if Bmid in Setmain["ARfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Bmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to, "Foto berhasil dirubah")
                        if Cmid in Setmain["ARfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to, "Foto berhasil dirubah")
                        if Zmid in Setmain["ARfoto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Zmid]
                            sw.updateProfilePicture(path)
                            sw.sendMessage(msg.to, "Foto berhasil dirubah")

                if msg.contentType == 1:
                    if msg._from in admin:
                        if setting["changePicture"]:
                            path1 = cl.downloadObjectMsg(msg_id)
                            path2 = ki.downloadObjectMsg(msg_id)
                            path3 = kk.downloadObjectMsg(msg_id)
                            path4 = kc.downloadObjectMsg(msg_id)
                            path5 = sw.downloadObjectMsg(msg_id)
                            setting["changePicture"] = False
                            cl.updateProfilePicture(path1)
                            cl.sendMessage(msg.to, "Foto berhasil dirubah")
                            ki.updateProfilePicture(path2)
                            ki.sendMessage(msg.to, "Foto berhasil dirubah")
                            kk.updateProfilePicture(path3)
                            kk.sendMessage(msg.to, "Foto berhasil dirubah")
                            kc.updateProfilePicture(path4)
                            kc.sendMessage(msg.to, "Foto berhasil dirubah")
                            sw.updateProfilePicture(path5)
                            sw.sendMessage(msg.to, "Foto berhasil dirubah")
                if msg.contentType == 2:
                    if msg._from in admin:
                        if mid in Setmain["ARvideo"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["ARvideo"][mid]
                            cl.updateProfileVideoPicture(path)
                            cl.sendMessage(
                                msg.to, "Foto berhasil dirubah jadi video")

                if msg.contentType == 0:
                    if wait["autoRead"]:
                        cl.sendChatChecked(to, msg_id)
                        ki.sendChatChecked(to, msg_id)
                        kk.sendChatChecked(to, msg_id)
                        kc.sendChatChecked(to, msg_id)
                        sw.sendChatChecked(to, msg_id)
                    if text is None:
                        return
                    else:
                        for sticker in stickers:
                            if msg._from in admin:
                                if text.lower() == sticker:
                                    sid = stickers[text.lower()]["STKID"]
                                    spkg = stickers[text.lower()]["STKPKGID"]
                                    cl.sendSticker(to, spkg, sid)
                        for image in images:
                            if msg._from in admin:
                                if text.lower() == image:
                                    cl.sendImage(msg.to, images[image])
                        for audio in audios:
                            if msg._from in admin:
                                if text.lower() == audio:
                                    cl.sendAudio(msg.to, audios[audio])
                        for video in videos:
                            if msg._from in admin:
                                if text.lower() == video:
                                    cl.sendVideo(msg.to, videos[video])
                        cmd = command(text)
                        if cmd == "hlth on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                cl.sendText(msg.to, "「 ON 」\nBot diaktifkan")

                        elif cmd == "hlth off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendText(
                                    msg.to, "「 OFF 」\nBot dinonaktifkan")

                        # HELP MENU
                        elif cmd == "help":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    helpMessage = help()
                                    ryan = cl.getContact(mid)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = "「 HELLTERHEAD 」\nUser : "
                                    ret_ = str(helpMessage)
                                    ry = str(ryan.displayName)
                                    pesan = ""
                                    pesan2 = pesan + "@x \n\n"
                                    xlen = str(len(zxc) + len(xpesan))
                                    xlen2 = str(
                                        len(zxc) + len(pesan2) + len(xpesan) - 1)
                                    zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(
                                        to,
                                        text,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":' +
                                                json.dumps(zx2).replace(
                                                    " ",
                                                    "") +
                                                "}")},
                                        contentType=0,
                                    )

                        elif cmd == "menu:command":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    helpMessage1 = help1()
                                    ryan = cl.getContact(mid)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = "「 HELLTERHEAD 」\nUser : "
                                    ret_ = str(helpMessage1)
                                    ry = str(ryan.displayName)
                                    pesan = ""
                                    pesan2 = pesan + "@x \n\n"
                                    xlen = str(len(zxc) + len(xpesan))
                                    xlen2 = str(
                                        len(zxc) + len(pesan2) + len(xpesan) - 1)
                                    zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(
                                        to,
                                        text,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":' +
                                                json.dumps(zx2).replace(
                                                    " ",
                                                    "") +
                                                "}")},
                                        contentType=0,
                                    )

                        elif cmd == "menu:protect":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    helpMessage2 = help2()
                                    ryan = cl.getContact(mid)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = "「 HELLTERHEAD 」\nUser : "
                                    ret_ = str(helpMessage2)
                                    ry = str(ryan.displayName)
                                    pesan = ""
                                    pesan2 = pesan + "@x \n\n"
                                    xlen = str(len(zxc) + len(xpesan))
                                    xlen2 = str(
                                        len(zxc) + len(pesan2) + len(xpesan) - 1)
                                    zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(
                                        to,
                                        text,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":' +
                                                json.dumps(zx2).replace(
                                                    " ",
                                                    "") +
                                                "}")},
                                        contentType=0,
                                    )

                        elif cmd == "menu:banned":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    helpMessage3 = help3()
                                    ryan = cl.getContact(mid)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = "「 HELLTERHEAD 」\nUser : "
                                    ret_ = str(helpMessage3)
                                    ry = str(ryan.displayName)
                                    pesan = ""
                                    pesan2 = pesan + "@x \n\n"
                                    xlen = str(len(zxc) + len(xpesan))
                                    xlen2 = str(
                                        len(zxc) + len(pesan2) + len(xpesan) - 1)
                                    zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(
                                        to,
                                        text,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":' +
                                                json.dumps(zx2).replace(
                                                    " ",
                                                    "") +
                                                "}")},
                                        contentType=0,
                                    )

                        elif cmd == "menu:update":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    helpMessage4 = help4()
                                    ryan = cl.getContact(mid)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = "「 HELLTERHEAD 」\nUser : "
                                    ret_ = str(helpMessage4)
                                    ry = str(ryan.displayName)
                                    pesan = ""
                                    pesan2 = pesan + "@x \n\n"
                                    xlen = str(len(zxc) + len(xpesan))
                                    xlen2 = str(
                                        len(zxc) + len(pesan2) + len(xpesan) - 1)
                                    zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(
                                        to,
                                        text,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":' +
                                                json.dumps(zx2).replace(
                                                    " ",
                                                    "") +
                                                "}")},
                                        contentType=0,
                                    )

                        elif cmd == "menu:group":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    helpMessage5 = help5()
                                    ryan = cl.getContact(mid)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = "「 HELLTERHEAD 」\nUser : "
                                    ret_ = str(helpMessage5)
                                    ry = str(ryan.displayName)
                                    pesan = ""
                                    pesan2 = pesan + "@x \n\n"
                                    xlen = str(len(zxc) + len(xpesan))
                                    xlen2 = str(
                                        len(zxc) + len(pesan2) + len(xpesan) - 1)
                                    zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(
                                        to,
                                        text,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":' +
                                                json.dumps(zx2).replace(
                                                    " ",
                                                    "") +
                                                "}")},
                                        contentType=0,
                                    )

                        elif cmd == "menu:squad":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    helpMessage6 = help6()
                                    ryan = cl.getContact(mid)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = "「 HELLTERHEAD 」\nUser : "
                                    ret_ = str(helpMessage6)
                                    ry = str(ryan.displayName)
                                    pesan = ""
                                    pesan2 = pesan + "@x \n\n"
                                    xlen = str(len(zxc) + len(xpesan))
                                    xlen2 = str(
                                        len(zxc) + len(pesan2) + len(xpesan) - 1)
                                    zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(
                                        to,
                                        text,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":' +
                                                json.dumps(zx2).replace(
                                                    " ",
                                                    "") +
                                                "}")},
                                        contentType=0,
                                    )

                        elif cmd == "menu:status":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    helpMessage7 = help7()
                                    ryan = cl.getContact(mid)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = "「 HELLTERHEAD 」\nUser : "
                                    ret_ = str(helpMessage7)
                                    ry = str(ryan.displayName)
                                    pesan = ""
                                    pesan2 = pesan + "@x \n\n"
                                    xlen = str(len(zxc) + len(xpesan))
                                    xlen2 = str(
                                        len(zxc) + len(pesan2) + len(xpesan) - 1)
                                    zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(
                                        to,
                                        text,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":' +
                                                json.dumps(zx2).replace(
                                                    " ",
                                                    "") +
                                                "}")},
                                        contentType=0,
                                    )

                        elif cmd == "menu:message":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    helpMessage8 = help8()
                                    ryan = cl.getContact(mid)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = "「 HELLTERHEAD 」\nUser : "
                                    ret_ = str(helpMessage8)
                                    ry = str(ryan.displayName)
                                    pesan = ""
                                    pesan2 = pesan + "@x \n\n"
                                    xlen = str(len(zxc) + len(xpesan))
                                    xlen2 = str(
                                        len(zxc) + len(pesan2) + len(xpesan) - 1)
                                    zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(
                                        to,
                                        text,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":' +
                                                json.dumps(zx2).replace(
                                                    " ",
                                                    "") +
                                                "}")},
                                        contentType=0,
                                    )

                        elif cmd == "menu:kicker":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    helpMessage9 = help9()
                                    ryan = cl.getContact(mid)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = "「 HELLTERHEAD 」\nUser : "
                                    ret_ = str(helpMessage9)
                                    ry = str(ryan.displayName)
                                    pesan = ""
                                    pesan2 = pesan + "@x \n\n"
                                    xlen = str(len(zxc) + len(xpesan))
                                    xlen2 = str(
                                        len(zxc) + len(pesan2) + len(xpesan) - 1)
                                    zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(
                                        to,
                                        text,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":' +
                                                json.dumps(zx2).replace(
                                                    " ",
                                                    "") +
                                                "}")},
                                        contentType=0,
                                    )

                        # STATUS
                        elif cmd == "status":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    md = "\n「 STATUS」\n"
                                    if wait["stickerOn"]:
                                        md += "• Sticker [ON] ☑️\n"
                                    else:
                                        md += "• Sticker [OFF] ❎\n"
                                    if wait["contact"]:
                                        md += "• Contact [ON] ☑️\n"
                                    else:
                                        md += "• Contact [OFF] ❎\n"
                                    if wait["detectMention"]:
                                        md += "• Respon [ON] ☑️\n"
                                    else:
                                        md += "• Respon [OFF] ❎\n"
                                    if wait["Timeline"]:
                                        md += "• Timeline [ON] ☑️\n"
                                    else:
                                        md += "• Timeline [OFF] ❎\n"
                                    if wait["warmode"]:
                                        md += "• Warmode [ON] ☑️\n"
                                    else:
                                        md += "• Warmode [OFF] ❎\n"
                                    if wait["autoJoin"]:
                                        md += "• Autojoin [ON] ☑️\n"
                                    else:
                                        md += "• Autojoin [OFF] ❎\n"
                                    if wait["autoAdd"]:
                                        md += "• Autoadd [ON] ☑️\n"
                                    else:
                                        md += "• Autoadd [OFF] ❎\n"
                                    if wait["autoRead"]:
                                        md += "• Autoread [ON] ☑️\n"
                                    else:
                                        md += "• Autoread [OFF] ❎\n"
                                    if settings["autoJoinTicket"]:
                                        md += "• Jointicket [ON] ☑️\n"
                                    else:
                                        md += "• Jointicket [OFF] ❎\n"
                                    if msg.to in welcome:
                                        md += "• Welcome [ON] ☑️\n"
                                    else:
                                        md += "• Welcome [OFF] ❎\n"
                                    if msg.to in leave:
                                        md += "• Leave [ON] ☑️\n"
                                    else:
                                        md += "• Leave [OFF] ❎\n"
                                    if wait["autoLeave"]:
                                        md += "• Autoleave [ON] ☑️\n"
                                    else:
                                        md += "• Autoleave [OFF] ❎\n"
                                    if msg.to in protectqr:
                                        md += "• Protectqr [ON] ☑️\n"
                                    else:
                                        md += "• Protectqr [OFF] ❎\n"
                                    if msg.to in protectjoin:
                                        md += "• Protectjoin [ON] ☑️\n"
                                    else:
                                        md += "• Protectjoin [OFF] ❎\n"
                                    if msg.to in protectinvite:
                                        md += "• Protectinvite [ON] ☑️\n"
                                    else:
                                        md += "• Protectinvite [OFF] ❎\n"
                                    if msg.to in protectkick:
                                        md += "• Protectkick [ON] ☑️\n"
                                    else:
                                        md += "• Protectkick [OFF] ❎\n"
                                    if msg.to in protectcancel:
                                        md += "• Protectcancel [ON] ☑️\n"
                                    else:
                                        md += "• Protectcancel [OFF] ❎\n"
                                    if msg.to in protectantijs:
                                        md += "• Antijs [ON] ☑️\n"
                                    else:
                                        md += "• Antijs [OFF] ❎\n"
                                    if msg.to in ghost:
                                        md += "• Ghost [ON] ☑️\n"
                                    else:
                                        md += "• Ghost [OFF] ❎\n"
                                    ginfo = cl.getGroup(msg.to)
                                    ryan = cl.getContact(mid)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = "「 HELLTERHAD 」\n• User : "
                                    ret_ = "• Group : {}\n".format(
                                        str(ginfo.name))
                                    ret_ += str(md)
                                    ry = str(ryan.displayName)
                                    pesan = ""
                                    pesan2 = pesan + "@x \n\n"
                                    xlen = str(len(zxc) + len(xpesan))
                                    xlen2 = str(
                                        len(zxc) + len(pesan2) + len(xpesan) - 1)
                                    zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = (
                                        xpesan +
                                        zxc +
                                        ret_ +
                                        "\n• Jam [ " +
                                        datetime.strftime(
                                            timeNow,
                                            "%H:%M:%S") +
                                        " ]" +
                                        "\n• Tanggal : " +
                                        datetime.strftime(
                                            timeNow,
                                            "%Y-%m-%d"))
                                    cl.sendMessage(
                                        to,
                                        text,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":' +
                                                json.dumps(zx2).replace(
                                                    " ",
                                                    "") +
                                                "}")},
                                        contentType=0,
                                    )

                        # CREATOR
                        elif cmd == "creator" or text.lower() == "owner":
                            if msg._from in admin:
                                cl.sendText(
                                    msg.to, "「 𐀀 HELLTERHEAD 」\nBy : DRE❗\nline.me/ti/p/~mo-banzu", )
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(mid)
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": mid},
                                        contentType=13,
                                    )

                        # ABOUT
                        elif cmd.startswith("about"):
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    try:
                                        arr = []
                                        today = datetime.today()
                                        thn = 1995
                                        bln = 12
                                        hr = 23
                                        future = datetime(thn, bln, hr)
                                        days = str(future - today)
                                        comma = days.find(",")
                                        days = days[:comma]
                                        contact = cl.getContact(mid)
                                        favoritelist = cl.getFavoriteMids()
                                        grouplist = cl.getGroupIdsJoined()
                                        contactlist = cl.getAllContactIds()
                                        blockedlist = cl.getBlockedContactIds()
                                        eltime = time.time() - mulai
                                        bot = runtime(eltime)
                                        start = time.time()
                                        elapsed_time = time.time() - start
                                        ryan = cl.getContact(mid)
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = "「 About 」\n• User : "
                                        ret_ = "• Group : {} Group".format(
                                            str(len(grouplist))
                                        )
                                        ret_ += "\n• Friend : {} Friend".format(
                                            str(len(contactlist)))
                                        ret_ += "\n• Blocked : {} Blocked".format(
                                            str(len(blockedlist)))
                                        ret_ += "\n• Favorite : {} Favorite".format(
                                            str(len(favoritelist)))
                                        ret_ += "\n• Version : [ Bot Protect v5 ]"
                                        ret_ += "\n• Expired : {} - {} - {}".format(
                                            str(hr), str(bln), str(thn))
                                        ret_ += "\n• In Days : {} Again".format(
                                            days)
                                        ret_ += "\n• Speed : {} Second".format(
                                            str(elapsed_time)
                                        )
                                        ret_ += "\n• Runtime : {}".format(
                                            str(bot))
                                        ret_ += "\n\nBy : DRE❗"
                                        ret_ += "\nline.me/ti/p/~mo-banzu"
                                        ry = str(ryan.displayName)
                                        pesan = ""
                                        pesan2 = pesan + "@x \n"
                                        xlen = str(len(zxc) + len(xpesan))
                                        xlen2 = str(
                                            len(zxc) + len(pesan2) + len(xpesan) - 1)
                                        zx = {
                                            "S": xlen, "E": xlen2, "M": ryan.mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                        text = xpesan + zxc + ret_ + ""
                                        cl.sendMessage(
                                            to,
                                            text,
                                            contentMetadata={
                                                "MENTION": str(
                                                    '{"MENTIONEES":' +
                                                    json.dumps(zx2).replace(
                                                        " ",
                                                        "") +
                                                    "}")},
                                            contentType=0,
                                        )
                                    except Exception as e:
                                        cl.sendMessage(msg.to, str(e))

                        # PROFILE
                        elif cmd == "me" or text.lower() == "me":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    msg.contentType = 13
                                    msg.contentMetadata = {"mid": msg._from}
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": msg._from},
                                        contentType=13,
                                    )
                                    cl.getContact(msg.contentMetadata["mid"])

                        elif text.lower() == "mid":
                            cl.sendMessage(msg.to, msg._from)

                        elif cmd.startswith("mid "):
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    mi = cl.getContact(key1)
                                    cl.sendMessage(
                                        msg.to,
                                        "Nama : "
                                        + str(mi.displayName)
                                        + "\nMID : "
                                        + key1,
                                    )
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": key1},
                                        contentType=13,
                                    )

                        elif cmd.startswith(".promo"):
                            cl.sendMessage(
                                msg.to,
                                "╭─── 𐀀 HELLTERHEAD Corp.\n╽╭── VPS 🔻\n││• 1 vCPU - 2 GB RAM - 20 GB SSD\n││• 2 vCPU - 4 GB RAM - 30 GB SSD\n││• 4 vCPU - 8 GB RAM - 50 GB SSD\n│╰──────\n╽╭── PROTECT 🔻\n││• 1 Commander\n││• 4 Assist\n││• 3 Anti JS\n│╰──────\n╽╭── BOT 🔻\n││• SelfBot Classic\n││• SelfBot Template\n││• Kicker JS\n│╰──────\n│• All subject to availability.\n│• Anytime can maintenance for system\n│ development.\n│• Custom VPS according to budget.\n│• Contact person:\n│ line.me/ti/p/~mo-banzu\n╰──────── DRE❗",
                            )

                        elif "/ti/g/" in msg.text.lower() == "gsearch":
                            if msg._from in admin:
                                if settings["autoJoinTicket"]:
                                    link_re = re.compile(
                                        r"(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?"
                                    )
                                    links = link_re.findall(text)
                                    n_links = []
                                    for l in links:
                                        if l not in n_links:
                                            n_links.append(l)
                                    for ticket_id in n_links:
                                        group = cl.findGroupByTicket(ticket_id)
                                        cl.acceptGroupInvitationByTicket(
                                            group.id, ticket_id
                                        )
                                        cl.sendMessage(
                                            msg.to, "Masuk : %s" % str(group.name)
                                        )

                        # REJECT
                        elif cmd == "reject":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    ginvited = cl.getGroupIdsInvited()
                                    if ginvited != [] and ginvited is not None:
                                        for gid in ginvited:
                                            cl.rejectGroupInvitation(gid)
                                            ki.rejectGroupInvitation(gid)
                                            kk.rejectGroupInvitation(gid)
                                            kc.rejectGroupInvitation(gid)
                                            sw.rejectGroupInvitation(gid)
                                        cl.sendMessage(
                                            to,
                                            "Berhasil tolak sebanyak {} undangan grup".format(
                                                str(len(ginvited))
                                            ),
                                        )
                                    else:
                                        cl.sendMessage(
                                            to, "Tidak ada undangan yang tertunda")

                        # BROADCAST
                        elif cmd.startswith("bc: "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                bc = text.replace(sep[0] + " ", "")
                                saya = cl.getGroupIdsJoined()
                                for group in saya:
                                    ryan = cl.getContact(mid)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = "「 Broadcast 」\nBroadcast by "
                                    ret_ = "{}".format(str(bc))
                                    ry = str(ryan.displayName)
                                    pesan = ""
                                    pesan2 = pesan + "@x\n"
                                    xlen = str(len(zxc) + len(xpesan))
                                    xlen2 = str(
                                        len(zxc) + len(pesan2) + len(xpesan) - 1)
                                    zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(
                                        group,
                                        text,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":' +
                                                json.dumps(zx2).replace(
                                                    " ",
                                                    "") +
                                                "}")},
                                        contentType=0,
                                    )

                        # KEY
                        elif text.lower() == "key":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    cl.sendMessage(
                                        msg.to,
                                        "「 Status Setkey 」\nSetkey saat ini「 "
                                        + str(Setmain["keyCommand"])
                                        + " 」",
                                    )

                        elif cmd.startswith("setkey "):
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    sep = text.split(" ")
                                    key = text.replace(sep[0] + " ", "")
                                    if key in ["", " ", "\n", None]:
                                        cl.sendMessage(
                                            msg.to, "Gagal mengganti key")
                                    else:
                                        Setmain["keyCommand"] = str(
                                            key).lower()
                                        cl.sendMessage(
                                            msg.to, "「 Change Setkey 」\nSetkey diganti jadi「{}」".format(
                                                str(key).lower()), )

                        elif text.lower() == "resetkey":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    Setmain["keyCommand"] = ""
                                    cl.sendMessage(
                                        msg.to, "「 Resetkey 」\nSetkey mu telah direset")

                        # RESTART
                        elif cmd == "!restart":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    cl.sendMessage(msg.to, "Restarting...")
                                    python3 = sys.executable
                                    os.execl(python3, python3, *sys.argv)

                        # RUNTIME
                        elif cmd == "runtime":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    eltime = time.time() - mulai
                                    bot = runtime(eltime)
                                    ryan = cl.getContact(mid)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = "「 Runtime 」\n• User : "
                                    ret_ = "• {}".format(str(bot))
                                    ry = str(ryan.displayName)
                                    pesan = ""
                                    pesan2 = pesan + "@x \n"
                                    xlen = str(len(zxc) + len(xpesan))
                                    xlen2 = str(
                                        len(zxc) + len(pesan2) + len(xpesan) - 1)
                                    zx = {"S": xlen, "E": xlen2, "M": ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(
                                        to,
                                        text,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":' +
                                                json.dumps(zx2).replace(
                                                    " ",
                                                    "") +
                                                "}")},
                                        contentType=0,
                                    )

                        # GROUP INFO
                        elif cmd == "ginfo":
                            if msg._from in admin:
                                try:
                                    G = cl.getGroup(msg.to)
                                    if G.invitee is None:
                                        gPending = "0"
                                    else:
                                        gPending = str(len(G.invitee))
                                    if G.preventedJoinByTicket:
                                        gQr = "Tertutup"
                                        gTicket = "Tidak ada"
                                    else:
                                        gQr = "Terbuka"
                                        gTicket = "https://line.me/R/ti/g/{}".format(
                                            str(cl.reissueGroupTicket(G.id)))
                                    timeCreated = []
                                    timeCreated.append(
                                        time.strftime(
                                            "%d-%m-%Y [ %H:%M:%S ]",
                                            time.localtime(int(G.createdTime) / 1000),
                                        )
                                    )
                                    cl.sendMessage(
                                        msg.to,
                                        "「 Group Info 」\n• Name Group : {}".format(
                                            G.name) +
                                        "\n• ID Group : {}".format(
                                            G.id) +
                                        "\n• Pembuat : {}".format(
                                            G.creator.displayName) +
                                        "\n• Waktu Dibuat : {}".format(
                                            str(timeCreated)) +
                                        "\n• Jumlah Member : {}".format(
                                            str(
                                                len(
                                                    G.members))) +
                                        "\n• Jumlah Pending : {}".format(gPending) +
                                        "\n• Group QR : {}".format(gQr) +
                                        "\n• Group Ticket : {}".format(gTicket),
                                    )
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": G.creator.mid},
                                        contentType=13,
                                    )
                                    cl.sendImageWithURL(
                                        msg.to,
                                        "http://dl.profile.line-cdn.net/"
                                        + G.pictureStatus,
                                    )
                                except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("ginfo: "):
                            if msg._from in admin:
                                separate = text.split(" ")
                                number = text.replace(separate[0] + " ", "")
                                groups = cl.getGroupIdsJoined()
                                ret_ = ""
                                try:
                                    group = groups[int(number) - 1]
                                    G = cl.getGroup(group)
                                    try:
                                        gCreator = G.creator.displayName
                                    except BaseException:
                                        gCreator = "Tidak ditemukan"
                                    if G.invitee is None:
                                        gPending = "0"
                                    else:
                                        gPending = str(len(G.invitee))
                                    if G.preventedJoinByTicket:
                                        gQr = "Tertutup"
                                        gTicket = "Tidak ada"
                                    else:
                                        gQr = "Terbuka"
                                        gTicket = "https://line.me/R/ti/g/{}".format(
                                            str(cl.reissueGroupTicket(G.id)))
                                    timeCreated = []
                                    timeCreated.append(
                                        time.strftime(
                                            "%d-%m-%Y [ %H:%M:%S ]",
                                            time.localtime(int(G.createdTime) / 1000),
                                        )
                                    )
                                    ret_ += "「 Group Info 」"
                                    ret_ += "\n• Nama Grup : {}".format(G.name)
                                    ret_ += "\n• ID Grup : {}".format(G.id)
                                    ret_ += "\n• Pembuat : {}".format(gCreator)
                                    ret_ += "\n• Waktu Dibuat : {}".format(
                                        str(timeCreated)
                                    )
                                    ret_ += "\n• Jumlah Member : {}".format(
                                        str(len(G.members))
                                    )
                                    ret_ += "\n• Jumlah Pending : {}".format(
                                        gPending)
                                    ret_ += "\n• Group QR : {}".format(gQr)
                                    ret_ += "\n• Group Ticket : {}".format(
                                        gTicket)
                                    ret_ += "\n• Picture URL : http://dl.profile.line-cdn.net/{}".format(
                                        G.pictureStatus)
                                    ret_ += ""
                                    cl.sendMessage(to, str(ret_))
                                    cl.sendImageWithURL(
                                        msg.to,
                                        "http://dl.profile.line-cdn.net/"
                                        + G.pictureStatus,
                                    )
                                except BaseException:
                                    pass

                        elif cmd.startswith("leave: "):
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                number = msg.text.replace(
                                    separate[0] + " ", "")
                                groups = cl.getGroupIdsJoined()
                                group = groups[int(number) - 1]
                                for i in group:
                                    ginfo = cl.getGroup(i)
                                    if ginfo == group:
                                        ki.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        cl.sendMessage(
                                            msg.to,
                                            "Berhasil keluar dari grup "
                                            + str(ginfo.name),
                                        )

                        # CODE QR
                        elif cmd.startswith("open: "):
                            if msg._from in admin:
                                separate = text.split(" ")
                                number = text.replace(separate[0] + " ", "")
                                groups = cl.getGroupIdsJoined()
                                ret_ = ""
                                try:
                                    group = groups[int(number) - 1]
                                    G = cl.getGroup(group)
                                    G.preventedJoinByTicket = False
                                    cl.updateGroup(G)
                                    try:
                                        gCreator = G.creator.mid
                                        dia = cl.getContact(gCreator)
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = "「 Sukses Open QR 」\n• Creator :  "
                                        diaa = str(dia.displayName)
                                        pesan = ""
                                        pesan2 = pesan + "@a\n"
                                        xlen = str(len(zxc) + len(xpesan))
                                        xlen2 = str(
                                            len(zxc) + len(pesan2) + len(xpesan) - 1)
                                        zx = {
                                            "S": xlen, "E": xlen2, "M": dia.mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    except BaseException:
                                        gCreator = "Tidak ditemukan"
                                    if G.invitee is None:
                                        gPending = "0"
                                    else:
                                        gPending = str(len(G.invitee))
                                    if G.preventedJoinByTicket:
                                        gQr = "Tertutup"
                                        gTicket = "Tidak ada"
                                    else:
                                        gQr = "Terbuka"
                                        gTicket = "https://line.me/R/ti/g/{}".format(
                                            str(cl.reissueGroupTicket(G.id)))
                                    timeCreated = []
                                    timeCreated.append(
                                        time.strftime(
                                            "%d-%m-%Y [ %H:%M:%S ]",
                                            time.localtime(int(G.createdTime) / 1000),
                                        )
                                    )
                                    ret_ += xpesan + zxc
                                    ret_ += "• Nama : {}".format(G.name)
                                    ret_ += "\n• Group QR : {}".format(gQr)
                                    ret_ += "\n• Pending : {}".format(gPending)
                                    ret_ += "\n• Group Ticket : {}".format(
                                        gTicket)
                                    ret_ += ""
                                    cl.sendMessage(
                                        receiver,
                                        ret_,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":' +
                                                json.dumps(zx2).replace(
                                                    " ",
                                                    "") +
                                                "}")},
                                        contentType=0,
                                    )
                                except BaseException:
                                    pass

                        elif cmd.startswith("close: "):
                            if msg._from in admin:
                                separate = text.split(" ")
                                number = text.replace(separate[0] + " ", "")
                                groups = cl.getGroupIdsJoined()
                                ret_ = ""
                                try:
                                    group = groups[int(number) - 1]
                                    G = cl.getGroup(group)
                                    G.preventedJoinByTicket = True
                                    cl.updateGroup(G)
                                    try:
                                        gCreator = G.creator.mid
                                        dia = cl.getContact(gCreator)
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = "「 Sukses Close QR 」\n• Creator :  "
                                        diaa = str(dia.displayName)
                                        pesan = ""
                                        pesan2 = pesan + "@a\n"
                                        xlen = str(len(zxc) + len(xpesan))
                                        xlen2 = str(
                                            len(zxc) + len(pesan2) + len(xpesan) - 1)
                                        zx = {
                                            "S": xlen, "E": xlen2, "M": dia.mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    except BaseException:
                                        gCreator = "Tidak ditemukan"
                                    if G.invitee is None:
                                        gPending = "0"
                                    else:
                                        gPending = str(len(G.invitee))
                                    if G.preventedJoinByTicket:
                                        gQr = "Tertutup"
                                        gTicket = "Tidak ada"
                                    else:
                                        gQr = "Terbuka"
                                        gTicket = "https://line.me/R/ti/g/{}".format(
                                            str(cl.reissueGroupTicket(G.id)))
                                    timeCreated = []
                                    timeCreated.append(
                                        time.strftime(
                                            "%d-%m-%Y [ %H:%M:%S ]",
                                            time.localtime(int(G.createdTime) / 1000),
                                        )
                                    )
                                    ret_ += xpesan + zxc
                                    ret_ += "• Nama : {}".format(G.name)
                                    ret_ += "\n• Group QR : {}".format(gQr)
                                    ret_ += "\n• Pending : {}".format(gPending)
                                    ret_ += "\n• Group Ticket : {}".format(
                                        gTicket)
                                    ret_ += ""
                                    cl.sendMessage(
                                        receiver,
                                        ret_,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":' +
                                                json.dumps(zx2).replace(
                                                    " ",
                                                    "") +
                                                "}")},
                                        contentType=0,
                                    )
                                except BaseException:
                                    pass

                        elif cmd.startswith("infomem "):
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                number = msg.text.replace(
                                    separate[0] + " ", "")
                                groups = cl.getGroupIdsJoined()
                                ret_ = ""
                                try:
                                    group = groups[int(number) - 1]
                                    G = cl.getGroup(group)
                                    no = 0
                                    ret_ = ""
                                    for mem in G.members:
                                        no += 1
                                        ret_ += ("\n " "• " + str(no) +
                                                 ". " + mem.displayName)
                                    cl.sendMessage(to, "• Group Name: " +
                                                   str(G.name) +
                                                   "\n\n[ List Member ]\n" +
                                                   ret_ +
                                                   "\n\n[ Total %i Member ]" %
                                                   len(G.members), )
                                except BaseException:
                                    pass

                        # QR GROUP
                        elif cmd.startswith("protectqr:on "):
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                number = msg.text.replace(
                                    separate[0] + " ", "")
                                groups = cl.getGroupIdsJoined()
                                ret_ = ""
                                try:
                                    group = groups[int(number) - 1]
                                    G = cl.getGroup(group)
                                    try:
                                        protectqr[G] = True
                                        f = codecs.open(
                                            "protectqr.json", "w", "utf-8")
                                        json.dump(
                                            protectqr,
                                            f,
                                            sort_keys=True,
                                            indent=4,
                                            ensure_ascii=False,
                                        )
                                        gCreator = G.creator.mid
                                        dia = cl.getContact(gCreator)
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = (
                                            "「 Protect QR Diaktifkan 」\n• Creator :  "
                                        )
                                        diaa = str(dia.displayName)
                                        pesan = ""
                                        pesan2 = pesan + "@a\n"
                                        xlen = str(len(zxc) + len(xpesan))
                                        xlen2 = str(
                                            len(zxc) + len(pesan2) + len(xpesan) - 1)
                                        zx = {
                                            "S": xlen, "E": xlen2, "M": dia.mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    except BaseException:
                                        cl.sendText(
                                            msg.to, "Grup itu tidak ada")
                                        gCreator = "Tidak ditemukan"
                                    if G.invitee is None:
                                        gPending = "0"
                                    else:
                                        gPending = str(len(G.invitee))
                                    timeCreated = []
                                    timeCreated.append(
                                        time.strftime(
                                            "%d-%m-%Y [ %H:%M:%S ]",
                                            time.localtime(int(G.createdTime) / 1000),
                                        )
                                    )
                                    ret_ += xpesan + zxc
                                    ret_ += "• Nama Grup : {}".format(G.name)
                                    ret_ += "\n• Pending : {}".format(gPending)
                                    ret_ += "\n• Jumlah Member : {}".format(
                                        str(len(G.members))
                                    )
                                    cl.sendMessage(
                                        receiver,
                                        ret_,
                                        contentMetadata={
                                            "MENTION": str(
                                                '{"MENTIONEES":' +
                                                json.dumps(zx2).replace(
                                                    " ",
                                                    "") +
                                                "}")},
                                        contentType=0,
                                    )
                                except Exception as e:
                                    cl.sendMessage(to, str(e))

                        elif cmd == "open":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    if msg.toType == 2:
                                        X = cl.getGroup(msg.to)
                                        X.preventedJoinByTicket = False
                                        cl.updateGroup(X)
                                        cl.sendMessage(msg.to, "URL Opened")

                        elif cmd == "close":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    if msg.toType == 2:
                                        X = cl.getGroup(msg.to)
                                        X.preventedJoinByTicket = True
                                        cl.updateGroup(X)
                                        cl.sendMessage(msg.to, "URL Closed")

                        elif cmd == "gurl":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    if msg.toType == 2:
                                        x = cl.getGroup(msg.to)
                                        if x.preventedJoinByTicket:
                                            x.preventedJoinByTicket = False
                                            cl.updateGroup(x)
                                        gurl = cl.reissueGroupTicket(msg.to)
                                        cl.sendMessage(
                                            msg.to,
                                            "• Group :"
                                            + str(x.name)
                                            + "\n• URL Group : http://line.me/R/ti/g/"
                                            + gurl,
                                        )

                        # PROFILE UPDATE
                        elif cmd == "cpp":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    Setmain["ARfoto"][mid] = True
                                    cl.sendText(msg.to, "Kirim fotonya")

                        elif cmd == "cvp":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    Setmain["ARvideo"][mid] = True
                                    cl.sendText(msg.to, "Kirim videonya")

                        elif cmd.startswith("name: "):
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                string = msg.text.replace(
                                    separate[0] + " ", "")
                                if len(string) <= 10000000000:
                                    profile = cl.getProfile()
                                    profile.displayName = string
                                    cl.updateProfile(profile)
                                    cl.sendMessage(
                                        msg.to, "Nama diganti jadi " + string + "")

                        # MENTION
                        elif msg.text in ["Tagall"]:
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    group = cl.getGroup(msg.to)
                                nama = [
                                    contact.mid for contact in group.members]
                                k = len(nama) // 20
                                for a in range(k + 1):
                                    txt = u""
                                    s = 0
                                    b = []
                                    for i in group.members[a *
                                                           20: (a + 1) * 20]:
                                        b.append(
                                            {"S": str(s), "E": str(s + 6), "M": i.mid}
                                        )
                                        s += 7
                                        txt += u"@Zero \n"
                                    cl.sendMessage(
                                        msg.to,
                                        text=txt,
                                        contentMetadata={
                                            u"MENTION": json.dumps({"MENTIONEES": b})
                                        },
                                        contentType=0,
                                    )

                        # KICK ALL
                        elif "!bye" in msg.text:
                            if msg._from in admin:
                                if msg.toType == 2:
                                    print("BOOM❗")
                                    _name = msg.text.replace("!bye", "")
                                    gs = cl.getGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                                    cl.sendMessage(
                                        msg.to, "「 𐀀 HELLTERHEAD WAS HERE! 」\n\n\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n\n\n\n"
                                        " █▌▓▒▒░░░░░░░░░░░░░░░░░░░░░░░▒▓█\n"
                                        " █▓▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█▌\n"
                                        "█▓▒▒░░░░░░░ 𐀀 HELLTERHEAD ░░░░░░▒▓█\n"
                                        "█▐▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▓\n"
                                        "█▓█▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▓█\n"
                                        "█▓▓█▒░░░▒█▄▒▒░░░░░░░░▒▒░▄█▒░░░▒█▓▓█\n"
                                        " █▓█▒░▒▒▒░░▀▀█▄▄░░░░▄▄█▀▀░░▒▒▒░▒▒▐██\n"
                                        " █▓▌▒▒▓▓▓▓▄▄▄▒▒▒▀█░░░█▀▒▒▒▄▄▄▓▓▒▒▐▓█\n"
                                        " ██▌▒▓███▓████▓▒▐▌░▐▌▒▓████▓███▓▒▐██\n"
                                        " ██▒▒▓███▓▓▓███▓▄░░▄▓████▓▓▓███▓▒▒██\n"
                                        " █▓▒▒▓█████████▓▒░░▒▓█████████▓▒▒▓█\n"
                                        "  █▓▒░▒▓██████▓▓▄▀░▀ ▄▓▓██████▓▒▒▓█\n"
                                        "   █▓▒░▒▒▓▓▓▄▄▄▀▒░░░░▒▀▄▄▄▓▓▓▒▒░▓█\n"
                                        "     █▓▒░▒▒▒░░░░░░▒▒▒░░░░░░▒▒▒░▒▓█\n"
                                        "      █▓▓▒▒░░██░░▒▓█▓▒░░██░░▒▒▓▓█\n"
                                        "      ▀██▓▓▒░░▀░▒▓███▓▒░▀░░▒▓▓██\n"
                                        "       ░▀▓▓▒░░░▓█▓▒▒▓█▓▒░░▒▒▓█▀\n"
                                        "       ░░█▓▓▒░░▒▒▒░▒▒▒░░▒▓▓██\n\n\n\n"
                                        "RATA GAK RATA TETAP PLAY❗\n"
                                        "SILAHKAN KALAU BISA TANGKIS, ADA KATA TERAKHIR?\n"
                                        "SELAMAT MENIKMATI PERTUNJUKAN\n\n\n"
                                        "HASTA LA VISTA, BABY❗\n"
                                        "HASTA LA VISTA, BABY❗\n"
                                        "HASTA LA VISTA, BABY❗\n"
                                        "HASTA LA VISTA, BABY❗\n"
                                        "HASTA LA VISTA, BABY❗\n\n\n"
                                        "By : DRE❗\n"
                                        "line.me/ti/p/~mo-banzu\n"
                                        "line.me/ti/p/~@722tmgxp", )
                                    targets = []
                                    for g in gs.members:
                                        if _name in g.displayName:
                                            targets.append(g.mid)
                                    if targets == []:
                                        cl.sendText(msg.to, "Not found!")
                                    else:
                                        for target in targets:
                                            if target not in admin and staff and Bots:
                                                try:
                                                    klist = [cl]
                                                    kicker = random.choice(
                                                        klist)
                                                    kicker.kickoutFromGroup(
                                                        msg.to, [target]
                                                    )
                                                    print(msg.to, [g.mid])
                                                except Exception as e:
                                                    break

                        # ABSEN
                        elif cmd == "absen":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    msg.contentType = 13
                                    msg.contentMetadata = {"mid": mid}
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": mid},
                                        contentType=13,
                                    )
                                    cl.getContact(msg.contentMetadata["mid"])
                                    msg.contentType = 13
                                    msg.contentMetadata = {"mid": Amid}
                                    ki.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": Amid},
                                        contentType=13,
                                    )
                                    ki.getContact(msg.contentMetadata["mid"])
                                    msg.contentType = 13
                                    msg.contentMetadata = {"mid": Bmid}
                                    kk.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": Bmid},
                                        contentType=13,
                                    )
                                    kk.getContact(msg.contentMetadata["mid"])
                                    msg.contentType = 13
                                    msg.contentMetadata = {"mid": Cmid}
                                    kc.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": Cmid},
                                        contentType=13,
                                    )
                                    kc.getContact(msg.contentMetadata["mid"])
                                    msg.contentType = 13
                                    msg.contentMetadata = {"mid": Zmid}
                                    sw.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": Zmid},
                                        contentType=13,
                                    )
                                    sw.getContact(msg.contentMetadata["mid"])

                        # REMOVE CHAT
                        elif text.lower() == "!removechat":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    try:
                                        ki.removeAllMessages(op.param2)
                                        kk.removeAllMessages(op.param2)
                                        kc.removeAllMessages(op.param2)
                                        sw.removeAllMessages(op.param2)
                                        ki.sendText(
                                            msg.to, "Chat dibersihkan...")
                                        kk.sendText(
                                            msg.to, "Chat dibersihkan...")
                                        kc.sendText(
                                            msg.to, "Chat dibersihkan...")
                                        sw.sendText(
                                            msg.to, "Chat dibersihkan...")
                                    except BaseException:
                                        pass

                        elif text.lower() == "?removechat":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    try:
                                        cl.removeAllMessages(op.param2)
                                        cl.sendText(
                                            msg.to, "Chat dibersihkan...")
                                    except BaseException:
                                        pass

                        # KICKER
                        elif "!kick" in msg.text:
                            if msg._from in admin:
                                if msg.toType == 2:
                                    print("BOOM❗")
                                    _name = msg.text.replace("!kick", "")
                                    gs = cl.getGroup(msg.to)
                                    gs = ki.getGroup(msg.to)
                                    gs = kk.getGroup(msg.to)
                                    gs = kc.getGroup(msg.to)
                                    gs = sw.getGroup(msg.to)
                                    random.choice(DRE).sendMessage(
                                        msg.to, "「 𐀀 HELLTERHEAD WAS HERE! 」\n\n\n"
                                        " █▌▓▒▒░░░░░░░░░░░░░░░░░░░░░░░▒▓█\n"
                                        " █▓▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█▌\n"
                                        "█▓▒▒░░░░░░░ 𐀀 HELLTERHEAD ░░░░░░▒▓█\n"
                                        "█▐▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▓\n"
                                        "█▓█▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▓█\n"
                                        "█▓▓█▒░░░▒█▄▒▒░░░░░░░░▒▒░▄█▒░░░▒█▓▓█\n"
                                        " █▓█▒░▒▒▒░░▀▀█▄▄░░░░▄▄█▀▀░░▒▒▒░▒▒▐██\n"
                                        " █▓▌▒▒▓▓▓▓▄▄▄▒▒▒▀█░░░█▀▒▒▒▄▄▄▓▓▒▒▐▓█\n"
                                        " ██▌▒▓███▓████▓▒▐▌░▐▌▒▓████▓███▓▒▐██\n"
                                        " ██▒▒▓███▓▓▓███▓▄░░▄▓████▓▓▓███▓▒▒██\n"
                                        " █▓▒▒▓█████████▓▒░░▒▓█████████▓▒▒▓█\n"
                                        "  █▓▒░▒▓██████▓▓▄▀░▀ ▄▓▓██████▓▒▒▓█\n"
                                        "   █▓▒░▒▒▓▓▓▄▄▄▀▒░░░░▒▀▄▄▄▓▓▓▒▒░▓█\n"
                                        "     █▓▒░▒▒▒░░░░░░▒▒▒░░░░░░▒▒▒░▒▓█\n"
                                        "      █▓▓▒▒░░██░░▒▓█▓▒░░██░░▒▒▓▓█\n"
                                        "      ▀██▓▓▒░░▀░▒▓███▓▒░▀░░▒▓▓██\n"
                                        "       ░▀▓▓▒░░░▓█▓▒▒▓█▓▒░░▒▒▓█▀\n"
                                        "       ░░█▓▓▒░░▒▒▒░▒▒▒░░▒▓▓██\n\n\n"
                                        "By : DRE❗\n"
                                        "line.me/ti/p/~mo-banzu", )
                                    random.choice(DRE).sendMessage(
                                        msg.to, "「 𐀀 HELLTERHEAD WAS HERE! 」\n\n\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n\n"
                                        "RATA GAK RATA TETAP PLAY❗\n"
                                        "SILAHKAN KALAU BISA TANGKIS, ADA KATA TERAKHIR?\n"
                                        "SELAMAT MENIKMATI PERTUNJUKAN\n\n\n"
                                        "HASTA LA VISTA, BABY❗\n"
                                        "HASTA LA VISTA, BABY❗\n"
                                        "HASTA LA VISTA, BABY❗\n"
                                        "HASTA LA VISTA, BABY❗\n"
                                        "HASTA LA VISTA, BABY❗\n\n"
                                        "By : DRE❗\n"
                                        "line.me/ti/p/~mo-banzu\n"
                                        "line.me/ti/p/~@722tmgxp", )
                                    targets = []
                                    for g in gs.members:
                                        if _name in g.displayName:
                                            targets.append(g.mid)
                                    if targets == []:
                                        cl.sendText(msg.to, "Not found!")
                                    else:
                                        for target in targets:
                                            if target not in admin and staff and Bots:
                                                try:
                                                    klist = [
                                                        cl, ki, kk, kc, sw]
                                                    kicker = random.choice(
                                                        klist)
                                                    kicker.kickoutFromGroup(
                                                        msg.to, [target]
                                                    )
                                                    print(msg.to, [g.mid])
                                                except Exception as e:
                                                    break

                        elif cmd == "hellterhead!" or cmd == "hlth!":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    start = time.time()
                                    cl.sendMessage(msg.to, "[ 𐀀 HELLTERHEAD ]")
                                    elapsed_time = time.time()
                                    ki.sendMessage(
                                        msg.to, "READY❗".format(
                                            str(elapsed_time)))
                                    kk.sendMessage(
                                        msg.to, "READY❗".format(
                                            str(elapsed_time)))
                                    kc.sendMessage(
                                        msg.to, "READY❗".format(
                                            str(elapsed_time)))
                                    sw.sendMessage(msg.to, "DONE❗")
                                    cl.sendMessage(
                                        msg.to, "line.me/ti/p/~mo-banzu")

                        elif cmd == "hlth:in":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                sw.leaveGroup(msg.to)
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(
                                    msg.to, Ticket)
                                kk.acceptGroupInvitationByTicket(
                                    msg.to, Ticket)
                                kc.acceptGroupInvitationByTicket(
                                    msg.to, Ticket)
                                sw.acceptGroupInvitationByTicket(
                                    msg.to, Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)
                                ki.sendMessage(
                                    msg.to, "𐀀 HELLTERHEAD IS READY❗")
                                kk.sendMessage(
                                    msg.to, "𐀀 HELLTERHEAD IS READY❗")
                                kc.sendMessage(
                                    msg.to, "𐀀 HELLTERHEAD IS READY❗")
                                sw.sendMessage(
                                    msg.to, "𐀀 HELLTERHEAD IS READY❗")

                        elif cmd == "hlth:out":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(
                                    msg.to, "𐀀 HELLTERHEAD Squad has been pushed back!")
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                sw.leaveGroup(msg.to)

                        elif cmd == "respon":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    ki.sendMessage(msg.to, responsename1)
                                    kk.sendMessage(msg.to, responsename2)
                                    kc.sendMessage(msg.to, responsename3)
                                    sw.sendMessage(msg.to, responsename4)

                        # BOT
                        elif cmd == "antijs:stay":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    try:
                                        ginfo = cl.getGroup(msg.to)
                                        cl.inviteIntoGroup(msg.to, [Zmid])
                                    except BaseException:
                                        pass

                        elif cmd == "!in":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    G = cl.getGroup(msg.to)
                                    ginfo = cl.getGroup(msg.to)
                                    G.preventedJoinByTicket = False
                                    cl.updateGroup(G)
                                    invsend = 0
                                    Ticket = cl.reissueGroupTicket(msg.to)
                                    ki.acceptGroupInvitationByTicket(
                                        msg.to, Ticket)
                                    kk.acceptGroupInvitationByTicket(
                                        msg.to, Ticket)
                                    kc.acceptGroupInvitationByTicket(
                                        msg.to, Ticket)
                                    G = random.choice(DRE).getGroup(msg.to)
                                    G.preventedJoinByTicket = True
                                    random.choice(DRE).updateGroup(G)

                        elif cmd == "!out":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    G = cl.getGroup(msg.to)
                                    ki.leaveGroup(msg.to)
                                    kk.leaveGroup(msg.to)
                                    kc.leaveGroup(msg.to)

                        # ASSIST
                        elif cmd == "assist1":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(
                                    msg.to, Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "assist2":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(
                                    msg.to, Ticket)
                                G = kk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)

                        elif cmd == "assist3":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGropup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(
                                    msg.to, Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)

                        # GHOST
                        elif cmd == "ghost:in":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(
                                    msg.to, Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "ghost:out":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sw.leaveGroup(msg.to)

                        # BOT ON OFF
                        elif "Antijs " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Antijs ", "")
                                if spl == "on":
                                    if msg.to in protectantijs:
                                        msgs = "Anti JS sudah aktif"
                                    else:
                                        protectantijs.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Anti JS Diaktifkan\nDi Group : " + \
                                            str(ginfo.name)
                                    cl.sendMessage(
                                        msg.to, "「Diaktifkan」\n" + msgs)
                                elif spl == "off":
                                    if msg.to in protectantijs:
                                        protectantijs.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = (
                                            "Anti JS Dinonaktifkan\nDi Group : "
                                            + str(ginfo.name)
                                        )
                                    else:
                                        msgs = "Anti JS sudah tidak aktif"
                                    cl.sendMessage(
                                        msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif "Ghost " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Ghost ", "")
                                if spl == "on":
                                    if msg.to in ghost:
                                        msgs = "Ghost sudah aktif"
                                    else:
                                        ghost.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Ghost Diaktifkan\nDi Group : " + \
                                            str(ginfo.name)
                                    cl.sendMessage(
                                        msg.to, "「Diaktifkan」\n" + msgs)
                                elif spl == "off":
                                    if msg.to in ghost:
                                        ghost.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Ghost Dinonaktifkan\nDi Group : " + \
                                            str(ginfo.name)
                                    else:
                                        msgs = "Ghost sudah tidak aktif"
                                    cl.sendMessage(
                                        msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif "Warmode " in msg.text:
                            if msg._from in admin or msg._from in owner:
                                spl = msg.text.replace("Warmode ", "")
                                if spl == "on":
                                    if msg.to in warmode:
                                        msgs = "Mode war berhasil diaktifkan!"
                                    else:
                                        warmode.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Mode War Diaktifkan\nDi Group : " + \
                                            str(ginfo.name)
                                    cl.sendMessage(
                                        msg.to, "「Diaktifkan」\n" + msgs)
                                elif spl == "off":
                                    if msg.to in warmode:
                                        warmode.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = (
                                            "Mode War Dinonaktifkan\nDi Group : "
                                            + str(ginfo.name)
                                        )
                                    else:
                                        msgs = "Mode War sudah tidak aktif"
                                    cl.sendMessage(
                                        msg.to, "「Dinonaktifkan」\n" + msgs)

                        # REVIVE
                        elif cmd == "revive":
                            if msg._from in admin:
                                try:
                                    cl.inviteIntoGroup(to, [""])
                                    has = "OK"
                                except BaseException:
                                    has = "NOT"
                                try:
                                    cl.kickoutFromGroup(to, [""])
                                    has1 = "OK"
                                except BaseException:
                                    has1 = "NOT"
                                if has == "OK":
                                    sil = "Healthy"
                                else:
                                    sil = "Sick"
                                if has1 == "OK":
                                    sil1 = "Healthy"
                                else:
                                    sil1 = "Sick"
                                cl.sendMessage(
                                    to, "「 Survives 」\n\n• Kick : {} \n• Invite : {}".format(
                                        sil1, sil), )
                                try:
                                    ki.inviteIntoGroup(to, [""])
                                    has = "OK"
                                except BaseException:
                                    has = "NOT"
                                try:
                                    ki.kickoutFromGroup(to, [""])
                                    has1 = "OK"
                                except BaseException:
                                    has1 = "NOT"
                                if has == "OK":
                                    sil = "Healthy"
                                else:
                                    sil = "Sick"
                                if has1 == "OK":
                                    sil1 = "Healthy"
                                else:
                                    sil1 = "Sick"
                                ki.sendMessage(
                                    to, "「 Survives 」\n\n• Kick : {} \n• Invite : {}".format(
                                        sil1, sil), )
                                try:
                                    kk.inviteIntoGroup(to, [""])
                                    has = "OK"
                                except BaseException:
                                    has = "NOT"
                                try:
                                    kk.kickoutFromGroup(to, [""])
                                    has1 = "OK"
                                except BaseException:
                                    has1 = "NOT"
                                if has == "OK":
                                    sil = "Healthy"
                                else:
                                    sil = "Sick"
                                if has1 == "OK":
                                    sil1 = "Healthy"
                                else:
                                    sil1 = "Sick"
                                kk.sendMessage(
                                    to, "「 Survives 」\n\n• Kick : {} \n• Invite : {}".format(
                                        sil1, sil), )
                                try:
                                    kc.inviteIntoGroup(to, [""])
                                    has = "OK"
                                except BaseException:
                                    has1 = "NOT"
                                try:
                                    kc.kickoutFromGroup(to, [""])
                                    has1 = "OK"
                                except BaseException:
                                    has == "OK"
                                if has == "OK":
                                    sil = "Healthy"
                                else:
                                    sil = "Sick"
                                if has1 == "OK":
                                    sil1 = "Healthy"
                                else:
                                    sil1 = "Sick"
                                kc.sendMessage(
                                    to, "「 Survives 」\n\n• Kick : {} \n• Invite : {}".format(
                                        sil1, sil), )
                                try:
                                    sw.inviteIntoGroup(to, [""])
                                    has = "OK"
                                except BaseException:
                                    has = "NOT"
                                try:
                                    sw.kickoutFromGroup(to, [""])
                                    has1 = "OK"
                                except BaseException:
                                    has1 = "NOT"
                                if has == "OK":
                                    sil = "Healthy"
                                else:
                                    sil = "Sick"
                                if has1 == "OK":
                                    sil1 = "Healthy"
                                else:
                                    sil1 = "Sick"
                                sw.sendMessage(
                                    to, "「 Survives 」\n\n• Kick : {} \n• Invite : {}".format(
                                        sil1, sil), )

                        # GROUP LIST
                        elif cmd == "grouplist":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    ma = ""
                                    a = 0
                                    gid = cl.getGroupIdsJoined()
                                    for i in gid:
                                        G = cl.getGroup(i)
                                        a = a + 1
                                        end = "\n"
                                        ma += "╠ " + str(a) + \
                                            ". " + G.name + "\n"
                                    cl.sendMessage(
                                        msg.to,
                                        "╔══[ GROUP LIST ]\n║\n"
                                        + ma
                                        + "║\n╚══[ Total "
                                        + str(len(gid))
                                        + " Groups ]",
                                    )

                        elif cmd == "grouplist1":
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                gid = ki.getGroupIdsJoined()
                                for i in gid:
                                    G = ki.getGroup(i)
                                    a = a + 1
                                    end = "\n"
                                    ma += "╠ " + str(a) + ". " + G.name + "\n"
                                ki.sendMessage(
                                    msg.to,
                                    "╔══[ GROUP LIST ]\n║\n"
                                    + ma
                                    + "║\n╚══[ Total "
                                    + str(len(gid))
                                    + " Groups ]",
                                )

                        elif cmd == "grouplist2":
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                gid = kk.getGroupIdsJoined()
                                for i in gid:
                                    G = kk.getGroup(i)
                                    a = a + 1
                                    end = "\n"
                                    ma += "╠ " + str(a) + ". " + G.name + "\n"
                                kk.sendMessage(
                                    msg.to,
                                    "╔══[ GROUP LIST ]\n║\n"
                                    + ma
                                    + "║\n╚══[ Total "
                                    + str(len(gid))
                                    + " Groups ]",
                                )

                        elif cmd == "grouplist3":
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                gid = kc.getGroupIdsJoined()
                                for i in gid:
                                    G = kc.getGroup(i)
                                    a = a + 1
                                    end = "\n"
                                    ma += "╠ " + str(a) + ". " + G.name + "\n"
                                kc.sendMessage(
                                    msg.to,
                                    "╔══[ GROUP LIST ]\n║\n"
                                    + ma
                                    + "║\n╚══[ Total "
                                    + str(len(gid))
                                    + " Groups ]",
                                )

                        elif cmd == "grouplist4":
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                gid = sw.getGroupIdsJoined()
                                for i in gid:
                                    G = sw.getGroup(i)
                                    a = a + 1
                                    end = "\n"
                                    ma += "╠ " + str(a) + ". " + G.name + "\n"
                                sw.sendMessage(
                                    msg.to,
                                    "╔══[ GROUP LIST ]\n║\n"
                                    + ma
                                    + "║\n╚══[ Total "
                                    + str(len(gid))
                                    + " Groups ]",
                                )

                        # LIST SQUAD
                        elif cmd == "listadmin":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    ma = ""
                                    mb = ""
                                    mc = ""
                                    a = 0
                                    b = 0
                                    c = 0
                                    for m_id in owner:
                                        a = a + 1
                                        end = "\n"
                                        ma += (
                                            str(a)
                                            + ". "
                                            + cl.getContact(m_id).displayName
                                            + "\n"
                                        )
                                    for m_id in admin:
                                        b = b + 1
                                        end = "\n"
                                        mb += (
                                            str(b)
                                            + ". "
                                            + cl.getContact(m_id).displayName
                                            + "\n"
                                        )
                                    for m_id in staff:
                                        c = c + 1
                                        end = "\n"
                                        mc += (
                                            str(c)
                                            + ". "
                                            + cl.getContact(m_id).displayName
                                            + "\n"
                                        )
                                    cl.sendMessage(
                                        msg.to,
                                        "「 Daftar User Admin 」\n\n" +
                                        mb +
                                        "\nTotal「%s」Admin" %
                                        (str(
                                            len(admin))),
                                    )

                        elif cmd == "liststaff":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    ma = ""
                                    mb = ""
                                    mc = ""
                                    a = 0
                                    b = 0
                                    c = 0
                                    for m_id in owner:
                                        a = a + 1
                                        end = "\n"
                                        ma += (
                                            str(a)
                                            + ". "
                                            + cl.getContact(m_id).displayName
                                            + "\n"
                                        )
                                    for m_id in admin:
                                        b = b + 1
                                        end = "\n"
                                        mb += (
                                            str(b)
                                            + ". "
                                            + cl.getContact(m_id).displayName
                                            + "\n"
                                        )
                                    for m_id in staff:
                                        c = c + 1
                                        end = "\n"
                                        mc += (
                                            str(c)
                                            + ". "
                                            + cl.getContact(m_id).displayName
                                            + "\n"
                                        )
                                    cl.sendMessage(
                                        msg.to,
                                        "「 Daftar User Staff 」\n\n" +
                                        mc +
                                        "\nTotal「%s」Staff" %
                                        (str(
                                            len(staff))),
                                    )

                        elif cmd == "listbot":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    ma = ""
                                    a = 0
                                    for m_id in Bots:
                                        a = a + 1
                                        end = "\n"
                                        ma += (
                                            str(a)
                                            + ". "
                                            + cl.getContact(m_id).displayName
                                            + "\n"
                                        )
                                    cl.sendMessage(
                                        msg.to,
                                        "「 Daftar User Bot 」\n\n"
                                        + ma
                                        + "\nTotal「%s」Bot" % (str(len(Bots))),
                                    )

                        # LIST PROTECT
                        elif cmd == "listprotect":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    ma = ""
                                    mb = ""
                                    mc = ""
                                    md = ""
                                    me = ""
                                    a = 0
                                    b = 0
                                    c = 0
                                    d = 0
                                    e = 0
                                    gid = protectqr
                                    for group in gid:
                                        a = a + 1
                                        end = "\n"
                                        ma += (
                                            str(a)
                                            + ". "
                                            + cl.getGroup(group).name
                                            + "\n"
                                        )
                                    gid = protectkick
                                    for group in gid:
                                        b = b + 1
                                        end = "\n"
                                        mb += (
                                            str(b)
                                            + ". "
                                            + cl.getGroup(group).name
                                            + "\n"
                                        )
                                    gid = protectcancel
                                    for group in gid:
                                        c = c + 1
                                        end = "\n"
                                        mc += (
                                            str(c)
                                            + ". "
                                            + cl.getGroup(group).name
                                            + "\n"
                                        )
                                    gid = protectjoin
                                    for group in gid:
                                        d = d + 1
                                        end = "\n"
                                        md += (
                                            str(d)
                                            + ". "
                                            + cl.getGroup(group).name
                                            + "\n"
                                        )
                                    gid = protectinvite
                                    for group in gid:
                                        e = e + 1
                                        end = "\n"
                                        me += (
                                            str(e)
                                            + ". "
                                            + cl.getGroup(group).name
                                            + "\n"
                                        )
                                    cl.sendMessage(
                                        msg.to,
                                        "「 𐀀 HELLTERHEAD 」\n\n• PROTECT QR :\n"
                                        + ma
                                        + "\n• PROTECT KICK :\n"
                                        + mb
                                        + "\n• PROTECT CANCEL :\n"
                                        + mc
                                        + "\n• PROTECT JOIN :\n"
                                        + md
                                        + "\n• PROTECT INVITE :\n"
                                        + me
                                        + "\n• Total「%s」Protection"
                                        % (
                                            str(
                                                len(protectqr)
                                                + len(protectkick)
                                                + len(protectcancel)
                                                + len(protectjoin)
                                                + len(protectinvite)
                                            )
                                        ),
                                    )

                        # GHOST KICKER
                        elif "Kill! " in msg.text:
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        if target not in Bots:
                                            try:
                                                G = cl.getGroup(msg.to)
                                                G.preventedJoinByTicket = False
                                                cl.updateGroup(G)
                                                invsend = 0
                                                Ticket = cl.reissueGroupTicket(
                                                    msg.to)
                                                sw.acceptGroupInvitationByTicket(
                                                    msg.to, Ticket)
                                                sw.kickoutFromGroup(
                                                    msg.to, [target])
                                                sw.leaveGroup(msg.to)
                                                X = cl.getGroup(msg.to)
                                                X.preventedJoinByTicket = True
                                                cl.updateGroup(X)
                                            except BaseException:
                                                pass

                        elif "Kick! " in msg.text:
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        if target not in Bots:
                                            try:
                                                random.choice(DRE).kickoutFromGroup(
                                                    msg.to, [target])
                                            except BaseException:
                                                pass

                        # BOT UPDATE
                        elif cmd == "bot1pict":
                            if msg._from in admin:
                                Setmain["ARfoto"][Amid] = True
                                ki.sendText(msg.to, "Kirim fotonya")

                        elif cmd == "bot2pict":
                            if msg._from in admin:
                                Setmain["ARfoto"][Bmid] = True
                                kk.sendText(msg.to, "Kirim fotonya")

                        elif cmd == "bot3pict":
                            if msg._from in admin:
                                Setmain["ARfoto"][Cmid] = True
                                kc.sendText(msg.to, "Kirim fotonya")

                        elif cmd == "bot4pict":
                            if msg._from in admin:
                                Setmain["ARfoto"][Zmid] = True
                                sw.sendText(msg.to, "Kirim fotonya")

                        elif cmd.startswith("bot1name: "):
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                string = msg.text.replace(
                                    separate[0] + " ", "")
                                if len(string) <= 10000000000:
                                    profile = ki.getProfile()
                                    profile.displayName = string
                                    ki.updateProfile(profile)
                                    ki.sendMessage(
                                        msg.to, "Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot2name: "):
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                string = msg.text.replace(
                                    separate[0] + " ", "")
                                if len(string) <= 10000000000:
                                    profile = kk.getProfile()
                                    profile.displayName = string
                                    kk.updateProfile(profile)
                                    kk.sendMessage(
                                        msg.to, "Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot3name: "):
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                string = msg.text.replace(
                                    separate[0] + " ", "")
                                if len(string) <= 10000000000:
                                    profile = kc.getProfile()
                                    profile.displayName = string
                                    kc.updateProfile(profile)
                                    kc.sendMessage(
                                        msg.to, "Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot4name: "):
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                string = msg.text.replace(
                                    separate[0] + " ", "")
                                if len(string) <= 10000000000:
                                    profile = sw.getProfile()
                                    profile.displayName = string
                                    sw.updateProfile(profile)
                                    sw.sendMessage(
                                        msg.to, "Nama diganti jadi " + string + "")

                        # SQUAD
                        elif cmd.startswith("adminadd "):
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            admin.append(target)
                                            cl.sendMessage(
                                                msg.to, "Berhasil menambahkan admin")
                                        except BaseException:
                                            pass

                        elif cmd.startswith("staffadd "):
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            staff.append(target)
                                            cl.sendMessage(
                                                msg.to, "Berhasil menambahkan staff")
                                        except BaseException:
                                            pass

                        elif cmd.startswith("botadd "):
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            Bots.append(target)
                                            cl.sendMessage(
                                                msg.to, "Berhasil menambahkan bot")
                                        except BaseException:
                                            pass

                        elif cmd.startswith("admindel "):
                            if msg._from in admin:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in squad:
                                        try:
                                            admin.remove(target)
                                            cl.sendMessage(
                                                msg.to, "Berhasil menghapus admin")
                                        except BaseException:
                                            pass

                        elif cmd.startswith("staffdel "):
                            if msg._from in admin:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in squad:
                                        try:
                                            staff.remove(target)
                                            cl.sendMessage(
                                                msg.to, "Berhasil menghapus staff")
                                        except BaseException:
                                            pass

                        elif cmd.startswith("botdel "):
                            if msg._from in admin:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in squad:
                                        try:
                                            Bots.remove(target)
                                            cl.sendMessage(
                                                msg.to, "Berhasil menghapus bot")
                                        except BaseException:
                                            pass

                        elif cmd == "admin:on" or text.lower() == "admin:on":
                            if msg._from in admin:
                                wait["addadmin"] = True
                                cl.sendText(msg.to, "Kirim kontaknya...")

                        elif cmd == "admin:repeat" or text.lower() == "admin:repeat":
                            if msg._from in admin:
                                wait["delladmin"] = True
                                cl.sendText(msg.to, "Kirim kontaknya...")

                        elif cmd == "staff:on" or text.lower() == "staff:on":
                            if msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendText(msg.to, "Kirim kontaknya...")

                        elif cmd == "staff:repeat" or text.lower() == "staff:repeat":
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendText(msg.to, "Kirim kontaknya...")

                        elif cmd == "bot:on" or text.lower() == "bot:on":
                            if msg._from in admin:
                                wait["addbots"] = True
                                cl.sendText(msg.to, "Kirim kontaknya...")

                        elif cmd == "bot:repeat" or text.lower() == "bot:repeat":
                            if msg._from in admin:
                                wait["dellbots"] = True
                                cl.sendText(msg.to, "Kirim kontaknya...")

                        elif cmd == "!abort" or text.lower() == "!abort":
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendText(msg.to, "Command aborted!")

                        elif cmd == "contact admin" or text.lower() == "c:admin":
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": i},
                                        contentType=13,
                                    )

                        elif cmd == "contact staff" or text.lower() == "c:staff":
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": i},
                                        contentType=13,
                                    )

                        elif cmd == "contact bot" or text.lower() == "c:bot":
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={"mid": i},
                                        contentType=13,
                                    )

                        elif cmd == "contact on" or text.lower() == "contact on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["contact"] = True
                                    cl.sendText(
                                        msg.to, "Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == "contact off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["contact"] = False
                                    cl.sendText(
                                        msg.to, "Deteksi contact dinonaktifkan")

                        # BANNED
                        elif cmd.startswith("talkban "):
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            wait["Talkblacklist"][target] = True
                                            cl.sendMessage(
                                                msg.to, "Berhasil menambahkan blacklist")
                                        except BaseException:
                                            pass

                        elif cmd.startswith("untalkban "):
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            del wait["Talkblacklist"][target]
                                            cl.sendMessage(
                                                msg.to, "Berhasil menghapus blacklist")
                                        except BaseException:
                                            pass

                        elif cmd == "talkban:on" or text.lower() == "talkban:on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["Talkwblacklist"] = True
                                    cl.sendText(msg.to, "Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == "untalkban:on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["Talkdblacklist"] = True
                                    cl.sendText(msg.to, "Kirim kontaknya...")

                        elif cmd.startswith("ban "):
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            wait["blacklist"][target] = True
                                            cl.sendMessage(
                                                msg.to, "Berhasil menambahkan blacklist")
                                        except BaseException:
                                            pass

                        elif cmd.startswith("unban "):
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            del wait["blacklist"][target]
                                            cl.sendMessage(
                                                msg.to, "Berhasil menghapus blacklist")
                                        except BaseException:
                                            pass

                        elif cmd == "ban:on" or text.lower() == "ban:on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["wblacklist"] = True
                                    cl.sendText(msg.to, "Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == "unban:on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["dblacklist"] = True
                                    cl.sendText(msg.to, "Kirim kontaknya...")

                        elif cmd == "talkbanlist" or text.lower() == "talkbanlist":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    if wait["Talkblacklist"] == {}:
                                        cl.sendMessage(
                                            msg.to, "Tidak ada talkban user")
                                    else:
                                        ma = ""
                                        a = 0
                                        for m_id in wait["Talkblacklist"]:
                                            a = a + 1
                                            end = "\n"
                                            ma += (str(a) +
                                                   ". " +
                                                   cl.getContact(m_id).displayName +
                                                   "\n")
                                        cl.sendMessage(
                                            msg.to,
                                            "「 𐀀 HELLTERHEAD 」\n• Talkban User\n\n" +
                                            ma +
                                            "\n• Total「%s」Talkban User" %
                                            (str(
                                                len(
                                                    wait["Talkblacklist"]))),
                                        )

                        elif cmd == "banlist" or text.lower() == "banlist":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    if wait["blacklist"] == {}:
                                        cl.sendMessage(
                                            msg.to, "Tidak ada banlist")
                                    else:
                                        ma = ""
                                        a = 0
                                        for m_id in wait["blacklist"]:
                                            a = a + 1
                                            end = "\n"
                                            ma += (str(a) +
                                                   ". " +
                                                   cl.getContact(m_id).displayName +
                                                   "\n")
                                        cl.sendMessage(
                                            msg.to,
                                            "• Blacklist User\n\n"
                                            + ma
                                            + "\n• Total「%s」Blacklist User"
                                            % (str(len(wait["blacklist"]))),
                                        )

                        elif cmd == "blacklist" or text.lower() == "blc":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    if wait["blacklist"] == {}:
                                        cl.sendMessage(
                                            msg.to, "Tidak ada blacklist")
                                    else:
                                        ma = ""
                                        for i in wait["blacklist"]:
                                            ma = cl.getContact(i)
                                            cl.sendMessage(
                                                msg.to,
                                                None,
                                                contentMetadata={"mid": i},
                                                contentType=13,
                                            )

                        elif cmd == "clearban" or text.lower() == "clb":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["blacklist"] = {}
                                    ragets = cl.getContacts(wait["blacklist"])
                                    mc = "「%i」User Blacklist" % len(ragets)
                                    cl.sendMessage(
                                        msg.to, "Sukses membersihkan" + mc)

                        # LEAVE
                        elif cmd == "?bye":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    G = cl.getGroup(msg.to)
                                    cl.sendText(msg.to, "Bye! " + str(G.name))
                                    cl.leaveGroup(msg.to)

                        # RESPON TIME
                        elif cmd == "respontime":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    get_profile_time_start = time.time()
                                    get_profile = cl.getProfile()
                                    get_profile_time = (
                                        time.time() - get_profile_time_start
                                    )
                                    get_group_time_start = time.time()
                                    get_group = cl.getGroupIdsJoined()
                                    get_group_time = time.time() - get_group_time_start
                                    get_contact_time_start = time.time()
                                    get_contact = cl.getContact(mid)
                                    get_contact_time = (
                                        time.time() - get_contact_time_start
                                    )
                                    cl.sendMessage(
                                        msg.to, "「 Response Time 」\n\n • Get Profile\n   %.10f\n • Get Contact\n   %.10f\n • Get Group\n   %.10f" %
                                        (get_profile_time / 3, get_contact_time / 3, get_group_time / 3, ), )

                        # SPEED
                        elif cmd == "speed" or cmd == "sp":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    start = time.time()
                                    sendMention(
                                        msg.to, sender, "「 Selfbot Speed 」\n• User ", "")
                                    elapsed_time = time.time() - start
                                    cl.sendMessage(
                                        msg.to, "{} Second".format(
                                            str(elapsed_time)))

                        # SIDER
                        elif cmd == "sider on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    try:
                                        tz = pytz.timezone("Asia/Jakarta")
                                        timeNow = datetime.now(tz=tz)
                                        cl.sendMessage(
                                            msg.to,
                                            "「 Status Sider 」\n\nBerhasil diaktifkan\n\n• Jam [ " +
                                            datetime.strftime(
                                                timeNow,
                                                "%H:%M:%S") +
                                            " ]" +
                                            "\n• Tanggal : " +
                                            datetime.strftime(
                                                timeNow,
                                                "%Y-%m-%d"),
                                        )
                                        del cctv["point"][msg.to]
                                        del cctv["sidermem"][msg.to]
                                        del cctv["cyduk"][msg.to]
                                    except BaseException:
                                        pass
                                    cctv["point"][msg.to] = msg.id
                                    cctv["sidermem"][msg.to] = ""
                                    cctv["cyduk"][msg.to] = True

                        elif cmd == "sider off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    if msg.to in cctv["point"]:
                                        tz = pytz.timezone("Asia/Jakarta")
                                        timeNow = datetime.now(tz=tz)
                                        cctv["cyduk"][msg.to] = False
                                        cl.sendMessage(
                                            msg.to,
                                            "「 Status Sider 」\n\nBerhasil dinonaktifkan\n\n• Jam [ " +
                                            datetime.strftime(
                                                timeNow,
                                                "%H:%M:%S") +
                                            " ]" +
                                            "\n• Tanggal : " +
                                            datetime.strftime(
                                                timeNow,
                                                "%Y-%m-%d"),
                                        )
                                    else:
                                        cl.sendMessage(
                                            msg.to, "Sudah tidak aktif")

                        # IMAGE
                        elif cmd.startswith("addimage "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ", "")
                                name = name.lower()
                                if name not in images:
                                    wait["Addimage"]["status"] = True
                                    wait["Addimage"]["name"] = str(
                                        name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("image.json", "w", "utf-8")
                                    json.dump(
                                        images,
                                        f,
                                        sort_keys=True,
                                        indent=4,
                                        ensure_ascii=False,
                                    )
                                    cl.sendText(msg.to, "Kirim fotonya")
                                else:
                                    cl.sendText(
                                        msg.to, "Foto itu sudah dalam list")

                        elif cmd.startswith("delimage "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ", "")
                                name = name.lower()
                                if name in images:
                                    cl.deleteFile(images[str(name.lower())])
                                    del images[str(name.lower())]
                                    f = codecs.open("image.json", "w", "utf-8")
                                    json.dump(
                                        images,
                                        f,
                                        sort_keys=True,
                                        indent=4,
                                        ensure_ascii=False,
                                    )
                                    cl.sendText(
                                        msg.to,
                                        "Berhasil menghapus image {}".format(
                                            str(name.lower())
                                        ),
                                    )
                                else:
                                    cl.sendText(
                                        msg.to, "Foto itu tidak ada dalam list")

                        elif text.lower() == "listimage":
                            if msg._from in admin:
                                no = 0
                                ret_ = "「 Daftar Image 」\n\n"
                                for image in images:
                                    no += 1
                                    ret_ += str(no) + ". " + \
                                        image.title() + "\n"
                                ret_ += "\nTotal「{}」Images".format(
                                    str(len(images)))
                                cl.sendText(to, ret_)

                        # VIDEO
                        elif cmd.startswith("addvideo "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ", "")
                                name = name.lower()
                                if name not in videos:
                                    wait["Addvideo"]["status"] = True
                                    wait["Addvideo"]["name"] = str(
                                        name.lower())
                                    videos[str(name.lower())] = ""
                                    f = codecs.open("video.json", "w", "utf-8")
                                    json.dump(
                                        videos,
                                        f,
                                        sort_keys=True,
                                        indent=4,
                                        ensure_ascii=False,
                                    )
                                    cl.sendText(msg.to, "Kirim videonya")
                                else:
                                    cl.sendText(
                                        msg.to, "Video itu sudah dalam list")

                        elif cmd.startswith("delvideo "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ", "")
                                name = name.lower()
                                if name in videos:
                                    cl.deleteFile(videos[str(name.lower())])
                                    del videos[str(name.lower())]
                                    f = codecs.open("video.json", "w", "utf-8")
                                    json.dump(
                                        videos,
                                        f,
                                        sort_keys=True,
                                        indent=4,
                                        ensure_ascii=False,
                                    )
                                    cl.sendText(
                                        msg.to,
                                        "Berhasil menghapus video {}".format(
                                            str(name.lower())
                                        ),
                                    )
                                else:
                                    cl.sendText(
                                        msg.to, "Video itu tidak ada dalam list")

                        elif text.lower() == "listvideo":
                            if msg._from in admin:
                                no = 0
                                ret_ = "「 Daftar Video 」\n\n"
                                for video in videos:
                                    no += 1
                                    ret_ += str(no) + ". " + \
                                        video.title() + "\n"
                                ret_ += "\nTotal「{}」Videos".format(
                                    str(len(videos)))
                                cl.sendText(to, ret_)

                        # MP3
                        elif cmd.startswith("addaudio "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ", "")
                                name = name.lower()
                                if name not in audios:
                                    wait["Addaudio"]["status"] = True
                                    wait["Addaudio"]["name"] = str(
                                        name.lower())
                                    audios[str(name.lower())] = ""
                                    f = codecs.open("audio.json", "w", "utf-8")
                                    json.dump(
                                        audios,
                                        f,
                                        sort_keys=True,
                                        indent=4,
                                        ensure_ascii=False,
                                    )
                                    cl.sendText(msg.to, "Kirim mp3 nya")
                                else:
                                    cl.sendText(
                                        msg.to, "Mp3 itu sudah dalam list")

                        elif cmd.startswith("delaudio "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ", "")
                                name = name.lower()
                                if name in audios:
                                    cl.deleteFile(audios[str(name.lower())])
                                    del audios[str(name.lower())]
                                    f = codecs.open("audio.json", "w", "utf-8")
                                    json.dump(
                                        audios,
                                        f,
                                        sort_keys=True,
                                        indent=4,
                                        ensure_ascii=False,
                                    )
                                    cl.sendText(
                                        msg.to,
                                        "Berhasil menghapus mp3 {}".format(
                                            str(name.lower())
                                        ),
                                    )
                                else:
                                    cl.sendText(
                                        msg.to, "Mp3 itu tidak ada dalam list")

                        elif cmd == "listaudio":
                            no = 0
                            ret_ = "「 Daftar Lagu 」\n\n"
                            for audio in audios:
                                no += 1
                                ret_ += str(no) + ". " + audio.title() + "\n"
                            ret_ += "\nTotal「{}」Lagu".format(str(len(audios)))
                            cl.sendText(to, ret_)

                        # STICKER
                        elif cmd.startswith("addsticker "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ", "")
                                name = name.lower()
                                if name not in stickers:
                                    wait["Addsticker"]["status"] = True
                                    wait["Addsticker"]["name"] = str(
                                        name.lower())
                                    stickers[str(name.lower())] = ""
                                    f = codecs.open(
                                        "sticker.json", "w", "utf-8")
                                    json.dump(
                                        stickers,
                                        f,
                                        sort_keys=True,
                                        indent=4,
                                        ensure_ascii=False,
                                    )
                                    cl.sendText(msg.to, "Kirim stickernya")
                                else:
                                    cl.sendText(
                                        msg.to, "Sticker itu sudah dalam list")

                        elif cmd.startswith("delsticker "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ", "")
                                name = name.lower()
                                if name in stickers:
                                    del stickers[str(name.lower())]
                                    f = codecs.open(
                                        "sticker.json", "w", "utf-8")
                                    json.dump(
                                        stickers,
                                        f,
                                        sort_keys=True,
                                        indent=4,
                                        ensure_ascii=False,
                                    )
                                    cl.sendText(
                                        msg.to,
                                        "Berhasil menghapus sticker {}".format(
                                            str(name.lower())
                                        ),
                                    )
                                else:
                                    cl.sendText(
                                        msg.to, "Sticker itu tidak ada dalam list")

                        elif text.lower() == "liststicker":
                            if msg._from in admin:
                                no = 0
                                ret_ = "「 Daftar Sticker 」\n\n"
                                for sticker in stickers:
                                    no += 1
                                    ret_ += str(no) + ". " + \
                                        sticker.title() + "\n"
                                ret_ += "\nTotal「{}」Stickers".format(
                                    str(len(stickers)))
                                cl.sendText(to, ret_)

                        # KIBAR KICKER
                        elif cmd == "!kibar":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    cl.sendContact(to, mid)
                                    cl.sendMessage(
                                        msg.to, "「 𐀀 HELLTERHEAD WAS HERE! 」\n\n\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n"
                                        " ☣ DANGER❗ ☣ DANGER❗ ☣ DANGER❗ ☣\n\n\n\n"
                                        " █▌▓▒▒░░░░░░░░░░░░░░░░░░░░░░░▒▓█\n"
                                        " █▓▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█▌\n"
                                        "█▓▒▒░░░░░░░ 𐀀 HELLTERHEAD ░░░░░░▒▓█\n"
                                        "█▐▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▓\n"
                                        "█▓█▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▓█\n"
                                        "█▓▓█▒░░░▒█▄▒▒░░░░░░░░▒▒░▄█▒░░░▒█▓▓█\n"
                                        " █▓█▒░▒▒▒░░▀▀█▄▄░░░░▄▄█▀▀░░▒▒▒░▒▒▐██\n"
                                        " █▓▌▒▒▓▓▓▓▄▄▄▒▒▒▀█░░░█▀▒▒▒▄▄▄▓▓▒▒▐▓█\n"
                                        " ██▌▒▓███▓████▓▒▐▌░▐▌▒▓████▓███▓▒▐██\n"
                                        " ██▒▒▓███▓▓▓███▓▄░░▄▓████▓▓▓███▓▒▒██\n"
                                        " █▓▒▒▓█████████▓▒░░▒▓█████████▓▒▒▓█\n"
                                        "  █▓▒░▒▓██████▓▓▄▀░▀ ▄▓▓██████▓▒▒▓█\n"
                                        "   █▓▒░▒▒▓▓▓▄▄▄▀▒░░░░▒▀▄▄▄▓▓▓▒▒░▓█\n"
                                        "     █▓▒░▒▒▒░░░░░░▒▒▒░░░░░░▒▒▒░▒▓█\n"
                                        "      █▓▓▒▒░░██░░▒▓█▓▒░░██░░▒▒▓▓█\n"
                                        "      ▀██▓▓▒░░▀░▒▓███▓▒░▀░░▒▓▓██\n"
                                        "       ░▀▓▓▒░░░▓█▓▒▒▓█▓▒░░▒▒▓█▀\n"
                                        "       ░░█▓▓▒░░▒▒▒░▒▒▒░░▒▓▓██\n\n\n\n"
                                        "RATA GAK RATA TETAP PLAY❗\n"
                                        "SILAHKAN KALAU BISA TANGKIS, ADA KATA TERAKHIR?\n"
                                        "SELAMAT MENIKMATI PERTUNJUKAN\n\n\n"
                                        "HASTA LA VISTA, BABY❗\n"
                                        "HASTA LA VISTA, BABY❗\n"
                                        "HASTA LA VISTA, BABY❗\n"
                                        "HASTA LA VISTA, BABY❗\n"
                                        "HASTA LA VISTA, BABY❗\n\n\n"
                                        "By : DRE❗\n"
                                        "line.me/ti/p/~mo-banzu\n"
                                        "line.me/ti/p/~@722tmgxp", )
                                    cl.sendMessage(
                                        msg.to,
                                        None,
                                        contentMetadata={
                                            "STKID": "15996978",
                                            "STKPKGID": "1416471",
                                            "STKVER": "1",
                                        },
                                        contentType=7,
                                    )

                        # HELLTERHEAD
                        elif cmd == "hellterhead" or cmd == "hlth":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    start = time.time()
                                    cl.sendMessage(msg.to, "PING!!!")
                                    elapsed_time = time.time() - start
                                    cl.sendMessage(
                                        msg.to, "READY❗ ".format(
                                            str(elapsed_time)))

                        # GREETING
                        elif "Welcome " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Welcome ", "")
                                if spl == "on":
                                    if msg.to in welcome:
                                        msgs = "Welcome Message sudah aktif"
                                    else:
                                        welcome.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ ON ]\nDi Group : " + \
                                            str(ginfo.name)
                                    cl.sendMessage(
                                        msg.to, "「 Status Welcome 」\n" + msgs
                                    )
                                elif spl == "off":
                                    if msg.to in welcome:
                                        welcome.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ OFF ]\nDi Group : " + \
                                            str(ginfo.name)
                                    else:
                                        msgs = "Welcome Message sudah tidak aktif"
                                    cl.sendMessage(
                                        msg.to, "「 Status Welcome 」\n" + msgs
                                    )

                        elif "Leave " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Leave ", "")
                                if spl == "on":
                                    if msg.to in leave:
                                        msgs = "Leave Message sudah aktif"
                                    else:
                                        leave.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ ON ]\nDi Group : " + \
                                            str(ginfo.name)
                                    cl.sendMessage(
                                        msg.to, "「 Status Leave 」\n" + msgs)
                                elif spl == "off":
                                    if msg.to in leave:
                                        leave.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ OFF ]\nDi Group : " + \
                                            str(ginfo.name)
                                    else:
                                        msgs = "Leave Message sudah tidak aktif"
                                    cl.sendMessage(
                                        msg.to, "「 Status Leave 」\n" + msgs)

                        # PROTECTION
                        elif "Protectqr " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Protectqr ", "")
                                if spl == "on":
                                    if msg.to in protectqr:
                                        msgs = "Protect Qr sudah aktif"
                                    else:
                                        protectqr.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ ON ]\nDi Group : " + \
                                            str(ginfo.name)
                                    cl.sendMessage(
                                        msg.to, "「 Status Protect Qr 」\n" + msgs)
                                elif spl == "off":
                                    if msg.to in protectqr:
                                        protectqr.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ OFF ]\nDi Group : " + \
                                            str(ginfo.name)
                                    else:
                                        msgs = "Protect Qr sudah tidak aktif"
                                    cl.sendMessage(
                                        msg.to, "「 Status Protect Qr 」\n" + msgs)

                        elif "Protectkick " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Protectkick ", "")
                                if spl == "on":
                                    if msg.to in protectkick:
                                        msgs = "Protect kick sudah aktif"
                                    else:
                                        protectkick.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ ON ]\nDi Group : " + \
                                            str(ginfo.name)
                                    cl.sendMessage(
                                        msg.to, "「 Status Protect kick 」\n" + msgs)
                                elif spl == "off":
                                    if msg.to in protectkick:
                                        protectkick.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ OFF ]\nDi Group : " + \
                                            str(ginfo.name)
                                    else:
                                        msgs = "Protect kick sudah tidak aktif"
                                    cl.sendMessage(
                                        msg.to, "「 Status Protect kick 」\n" + msgs)

                        elif "Protectjoin " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Protectjoin ", "")
                                if spl == "on":
                                    if msg.to in protectjoin:
                                        msgs = "Protect join sudah aktif"
                                    else:
                                        protectjoin.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ ON ]\nDi Group : " + \
                                            str(ginfo.name)
                                    cl.sendMessage(
                                        msg.to, "「 Status Protect Join 」\n" + msgs)
                                elif spl == "off":
                                    if msg.to in protectjoin:
                                        protectjoin.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ OFF ]\nDi Group : " + \
                                            str(ginfo.name)
                                    else:
                                        msgs = "Protect join sudah tidak aktif"
                                    cl.sendMessage(
                                        msg.to, "「 Status Protect Join 」\n" + msgs)

                        elif "Protectcancel " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Protectcancel ", "")
                                if spl == "on":
                                    if msg.to in protectcancel:
                                        msgs = "Protect cancel sudah aktif"
                                    else:
                                        protectcancel.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ ON ]\nDi Group : " + \
                                            str(ginfo.name)
                                    cl.sendMessage(
                                        msg.to, "「 Status Protect Cancel 」\n" + msgs)
                                elif spl == "off":
                                    if msg.to in protectcancel:
                                        protectcancel.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ OFF ]\nDi Group : " + \
                                            str(ginfo.name)
                                    else:
                                        msgs = "Protect cancel sudah tidak aktif"
                                    cl.sendMessage(
                                        msg.to, "「 Status Protect Cancel 」\n" + msgs)

                        elif "Protectinvite " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Protectinvite ", "")
                                if spl == "on":
                                    if msg.to in protectinvite:
                                        msgs = "Protect invite sudah aktif"
                                    else:
                                        protectinvite.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ ON ]\nDi Group : " + \
                                            str(ginfo.name)
                                    cl.sendMessage(
                                        msg.to, "「 Status Protect Invite 」\n" + msgs)
                                elif spl == "off":
                                    if msg.to in protectinvite:
                                        protectinvite.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ OFF ]\nDi Group : " + \
                                            str(ginfo.name)
                                    else:
                                        msgs = "Protect invite sudah tidak aktif"
                                    cl.sendMessage(
                                        msg.to, "「 Status Protect Invite 」\n" + msgs)

                        elif "Protectall " in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace("Protectall ", "")
                                if spl == "on":
                                    if msg.to in protectqr:
                                        msgs = "Protect QR : ON"
                                    else:
                                        protectqr.append(msg.to)
                                    if msg.to in protectkick:
                                        msgs = "Protect kick : ON"
                                    else:
                                        protectkick.append(msg.to)
                                    if msg.to in protectinvite:
                                        msgs = "Protect invite : ON"
                                    else:
                                        protectinvite.append(msg.to)
                                    if msg.to in protectcancel:
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ ON ]\nDi Group : " + \
                                            str(ginfo.name)
                                        msgs += "\nSemua protection diaktifkan"
                                    else:
                                        protectcancel.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ ON ]\nDi Group : " + \
                                            str(ginfo.name)
                                        msgs += "\nSemua protection diaktifkan"
                                    cl.sendMessage(
                                        msg.to, "「 Status Protection 」\n" + msgs)
                                elif spl == "off":
                                    if msg.to in protectqr:
                                        protectqr.remove(msg.to)
                                    else:
                                        msgs = "Protect QR : OFF"
                                    if msg.to in protectkick:
                                        protectkick.remove(msg.to)
                                    else:
                                        msgs = "Protect kick : OFF"
                                    if msg.to in protectinvite:
                                        protectinvite.remove(msg.to)
                                    else:
                                        msgs = "Protect invite : OFF"
                                    if msg.to in protectcancel:
                                        protectcancel.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ OFF ]\nDi Group : " + \
                                            str(ginfo.name)
                                        msgs += "\nSemua protection dinonaktifkan"
                                    else:
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Status : [ OFF ]\nDi Group : " + \
                                            str(ginfo.name)
                                        msgs += "\nSemua protection dinonaktifkan"
                                    cl.sendMessage(
                                        msg.to, "「 Status Protection 」\n" + msgs)

                        # COMMAND ON OFF
                        elif cmd == "timeline on" or text.lower() == "timeline on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["Timeline"] = True
                                    sendMention(
                                        msg.to,
                                        sender,
                                        "「 Status Timeline 」\n• User ",
                                        "\nDeteksi timeline diaktifkan",
                                    )

                        elif cmd == "timeline off" or text.lower() == "timeline off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["Timeline"] = False
                                    sendMention(
                                        msg.to,
                                        sender,
                                        "「 Status Timeline 」\n• User ",
                                        "\nDeteksi timeline dinonaktifkan",
                                    )

                        elif cmd == "invite on" or text.lower() == "invite on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["invite"] = True
                                    sendMention(
                                        msg.to,
                                        sender,
                                        "「 Status Invite 」\n• User ",
                                        "\nInvite via contact diaktifkan",
                                    )

                        elif cmd == "invite off" or text.lower() == "invite off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["invite"] = False
                                    sendMention(
                                        msg.to,
                                        sender,
                                        "「 Status Invite 」\n• User ",
                                        " \nInvite via contact dinonaktifkan",
                                    )

                        elif cmd == "notag on" or text.lower() == "notag on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["mentionKick"] = True
                                    cl.sendText(
                                        msg.to, "「 Status Notag 」\nNotag telah diaktifkan", )

                        elif cmd == "notag off" or text.lower() == "notag off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["mentionKick"] = False
                                    cl.sendText(
                                        msg.to, "「 Status Notag 」\nNotag telah dinonaktifkan", )

                        elif cmd == "contact on" or text.lower() == "contact on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["contact"] = True
                                    sendMention(
                                        msg.to,
                                        sender,
                                        "「 Status Contact 」\n• User ",
                                        "\nDeteksi contact diaktifkan",
                                    )

                        elif cmd == "contact off" or text.lower() == "contact off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["contact"] = False
                                    cl.sendText(
                                        msg.to,
                                        sender,
                                        "「 Status Contact 」\n• User ",
                                        "\nDeteksi contact dinonaktifkan",
                                    )

                        elif cmd == "respon on" or text.lower() == "respon on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["detectMention"] = True
                                    cl.sendText(
                                        msg.to, "「 Status Respon 」\nAuto respon diaktifkan", )

                        elif cmd == "respon off" or text.lower() == "respon off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["detectMention"] = False
                                    cl.sendText(
                                        msg.to, "「 Status Respon 」\nAuto respon dinonaktifkan", )

                        elif cmd == "autoread on" or text.lower() == "autoread on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["autoRead"] = True
                                    cl.sendText(
                                        msg.to, "「 Auto Read 」\nAuto read message diaktifkan", )

                        elif cmd == "autoread off" or text.lower() == "autoread off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["autoRead"] = False
                                    cl.sendText(
                                        msg.to, "「 Auto Read 」\nAuto read message dinonaktifkan", )

                        elif cmd == "autojoin on" or text.lower() == "autojoin on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["autoJoin"] = True
                                    cl.sendText(
                                        msg.to, "「 Status Autojoin 」\nAuto join telah diaktifkan", )

                        elif cmd == "autojoin off" or text.lower() == "autojoin off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["autoJoin"] = False
                                    cl.sendText(
                                        msg.to, "「 Status Autojoin 」\nAuto join telah dinonaktifkan", )

                        elif cmd == "autoleave on" or text.lower() == "autoleave on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["autoLeave"] = True
                                    cl.sendText(
                                        msg.to, "「 Status Autoleave 」\nAuto leave telah diaktifkan", )

                        elif cmd == "autoleave off" or text.lower() == "autoleave off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["autoLeave"] = False
                                    cl.sendText(
                                        msg.to, "「 Status Autoleave 」\nAuto leave telah dinonaktifkan", )

                        elif cmd == "autoblock on" or text.lower() == "autoblock on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["autoBlock"] = True
                                    cl.sendText(
                                        msg.to, "「 Status Autoblock 」\nAuto block telah diaktifkan", )

                        elif cmd == "autoblock off" or text.lower() == "autoblock off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["autoBlock"] = False
                                    cl.sendText(
                                        msg.to, "「 Status Autoblock 」\nAuto block telah dinonaktifkan", )

                        elif cmd == "autoadd on" or text.lower() == "autoadd on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["autoAdd"] = True
                                    cl.sendText(
                                        msg.to, "「 Status Autoadd 」\nAuto add telah diaktifkan", )

                        elif cmd == "autoadd off" or text.lower() == "autoadd off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["autoAdd"] = False
                                    cl.sendText(
                                        msg.to, "「 Status Autoadd 」\nAuto add telah dinonaktifkan", )

                        elif cmd == "sticker on" or text.lower() == "sticker on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["stickerOn"] = True
                                    sendMention(
                                        msg.to, sender, "「 Status Sticker Check 」\nSticker check diaktifkan", )

                        elif cmd == "sticker off" or text.lower() == "sticker off":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    wait["stickerOn"] = False
                                    cl.sendText(
                                        msg.to, "「 Status Sticker Check 」\nSticker check dinonaktifkan", )

                        elif cmd == "jointicket on" or text.lower() == "jointicket on":
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    settings["autoJoinTicket"] = True
                                    sendMention(
                                        msg.to, sender, "「 Status Jointicket 」\nJoin ticket telah diaktifkan", )

                        elif (
                            cmd == "jointicket off" or text.lower() == "jointicket off"
                        ):
                            if wait["selfbot"]:
                                if msg._from in admin:
                                    settings["autoJoinTicket"] = False
                                    cl.sendText(
                                        msg.to, sender, "「 Status Jointicket 」\nJoin ticket telah dinonaktifkan", )

                        # SETTING MESSAGE
                        elif cmd.startswith("set message: "):
                            if msg._from in admin:
                                spl = msg.text.replace("set message: ", "")
                                if spl in ["", " ", "\n", None]:
                                    cl.sendMessage(
                                        msg.to, "Gagal mengganti chat message"
                                    )
                                else:
                                    wait["message"] = spl
                                    cl.sendMessage(
                                        msg.to, "「 Berhasil Diganti 」\nChat message diganti jadi :\n\n{}".format(
                                            str(spl)), )

                        elif cmd.startswith("set welcome: "):
                            if msg._from in admin:
                                spl = msg.text.replace("set welcome: ", "")
                                if spl in ["", " ", "\n", None]:
                                    cl.sendMessage(
                                        msg.to, "Gagal mengganti welcome message")
                                else:
                                    wait["welcome"] = spl
                                    cl.sendMessage(
                                        msg.to, "「 Berhasil Diganti 」\nWelcome message diganti jadi :\n\n{}".format(
                                            str(spl)), )

                        elif cmd.startswith("set leave: "):
                            if msg._from in admin:
                                spl = msg.text.replace("set leave: ", "")
                                if spl in ["", " ", "\n", None]:
                                    cl.sendMessage(
                                        msg.to, "Gagal mengganti leave message"
                                    )
                                else:
                                    wait["leave"] = spl
                                    cl.sendMessage(
                                        msg.to, "「 Berhasil Diganti 」\nLeave message diganti jadi :\n\n{}".format(
                                            str(spl)), )

                        elif cmd.startswith("set respon: "):
                            if msg._from in admin:
                                spl = msg.text.replace("set respon: ", "")
                                if spl in ["", " ", "\n", None]:
                                    cl.sendMessage(
                                        msg.to, "Gagal mengganti respon message")
                                else:
                                    wait["Respontag"] = spl
                                    cl.sendMessage(
                                        msg.to, "「 Berhasil Diganti 」\nRespon message diganti jadi :\n\n{}".format(
                                            str(spl)), )

                        elif cmd.startswith("set sider: "):
                            if msg._from in admin:
                                spl = msg.text.replace("set sider: ", "")
                                if spl in ["", " ", "\n", None]:
                                    cl.sendMessage(
                                        msg.to, "Gagal mengganti sider message"
                                    )
                                else:
                                    wait["mention"] = spl
                                    cl.sendMessage(
                                        msg.to, "「 Berhasil Diganti 」\nSider message diganti jadi :\n\n{}".format(
                                            str(spl)), )

                        # CHECK MESSAGE
                        elif text.lower() == "check message":
                            if msg._from in admin:
                                cl.sendMessage(
                                    msg.to,
                                    "「 Status Message 」\nChat message :\n\n"
                                    + str(wait["message"]),
                                )

                        elif text.lower() == "check welcome":
                            if msg._from in admin:
                                cl.sendMessage(
                                    msg.to,
                                    "「 Status Welcome 」\nWelcome message :\n\n"
                                    + str(wait["welcome"]),
                                )

                        elif text.lower() == "check leave":
                            if msg._from in admin:
                                cl.sendMessage(
                                    msg.to,
                                    "「 Status Leave 」\nLeave message :\n\n"
                                    + str(wait["leave"]),
                                )

                        elif text.lower() == "check respon":
                            if msg._from in admin:
                                cl.sendMessage(
                                    msg.to,
                                    "「 Status Respon 」\nRespon message :\n\n"
                                    + str(wait["Respontag"]),
                                )

                        elif text.lower() == "check sider":
                            if msg._from in admin:
                                cl.sendMessage(
                                    msg.to,
                                    "「 Status Sider 」\nSider message :\n\n"
                                    + str(wait["mention"]),
                                )

                        # JOIN TICKET
                        elif "/ti/g/" in msg.text.lower():
                            if wait["selfbot"]:
                                if settings["autoJoinTicket"]:
                                    link_re = re.compile(
                                        r"(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?"
                                    )
                                    links = link_re.findall(text)
                                    n_links = []
                                    for l in links:
                                        if l not in n_links:
                                            n_links.append(l)
                                    for ticket_id in n_links:
                                        group = cl.findGroupByTicket(ticket_id)
                                        cl.acceptGroupInvitationByTicket(
                                            group.id, ticket_id
                                        )
                                        cl.sendMessage(
                                            msg.to, "Masuk : %s" % str(group.name)
                                        )
                                        group1 = ki.findGroupByTicket(
                                            ticket_id)
                                        ki.acceptGroupInvitationByTicket(
                                            group1.id, ticket_id
                                        )
                                        ki.sendMessage(
                                            msg.to, "Masuk : %s" % str(group.name)
                                        )
                                        group2 = kk.findGroupByTicket(
                                            ticket_id)
                                        kk.acceptGroupInvitationByTicket(
                                            group2.id, ticket_id
                                        )
                                        kk.sendMessage(
                                            msg.to, "Masuk : %s" % str(group.name)
                                        )
                                        group3 = kc.findGroupByTicket(
                                            ticket_id)
                                        kc.acceptGroupInvitationByTicket(
                                            group3.id, ticket_id
                                        )
                                        kc.sendMessage(
                                            msg.to, "Masuk : %s" % str(group.name)
                                        )

    except Exception as error:
        print(error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(
                    target=bot, args=(op,)
                )  # self.OpInterrupt[op.type], args=(op,)
                # thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
