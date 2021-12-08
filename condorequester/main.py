import requests 
from requests import post, get, patch
import json
import time

def main(cookie):
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
    print(userId)
    gameId = requests.get("https://inventory.roblox.com/v2/users/" +
                          str(userId) + "/inventory/9?limit=10&sortOrder=Asc",
                          headers={
                              'x-csrf-token': token,
                              'User-Agent': 'Roblox'
                          },
                          cookies={
                              '.ROBLOSECURITY': cookie
                          }).json()["data"][0]["assetId"]
    print(gameId)
    myfiles = open("Baseplate.rbxlx", "rb").read()
    unvid = get(
        "https://api.roblox.com/universes/get-universe-containing-place?placeid="
        + str(gameId)).json()["UniverseId"]
    print(unvid)
    url = f"https://data.roblox.com/Data/Upload.ashx?assetid={str(gameId)}"

    url2 = f"https://develop.roblox.com/v2/universes/{str(unvid)}/configuration"

    maxplayers = 100
    avatartype = "MorphToR6"
    allowprivateservers = True

    gamedata = {
        "name": "hello",
        "description": "Hello",
        "universeAvatarType": avatartype,
        "universeAnimationType": "Standard",
        "maxPlayerCount": 100,
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

    print(gameData.status_code)
    upload = post(url,
                  headers={
                      'Content-Type': 'application/xml',
                      'User-Agent': 'Roblox',
                      'x-csrf-token': token
                  },
                  cookies={'.ROBLOSECURITY': cookie},
                  data=myfiles)
    if upload.status_code == 200:
        print('success')
        time.sleep(50)

if __name__ == "__main__":
    filename = 'cookies.txt'
    line_to_delete = 1
    initial_line = 1
    file_lines = {}

    with open(filename) as f:
        content = f.readlines() 

    for line in content:
        file_lines[initial_line] = line.strip()
        initial_line += 1

    f = open(filename, "w")
    for line_number, line_content in file_lines.items():
        if line_number != line_to_delete:
            f.write('{}\n'.format(line_content))
            main(line_content)
            print('Deleted line: {}'.format(line_to_delete))

    f.close()