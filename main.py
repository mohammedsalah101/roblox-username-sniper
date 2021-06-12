from discord_webhook import DiscordWebhook , DiscordEmbed
import random, string, requests, time
from discord.ext import commands
import keep_alive
keep_alive.keep_alive()
z= 3 
import discord
while z==3:
  f = open("words.txt",'r').read().splitlines()
  a = random.choice(f) + random.choice(f)
  lena = len(a)
  b = open('Usernames.txt','a+')
  r = requests.get(f"https://api.roblox.com/users/get-by-username?username={a}")
  if '{"success":false,"errorMessage":"User not found"}' in r.text:
    print(f"Available user: {a}")
    b.write(a + "\n")
    b.close()

    requests.post("webhook here"),json={"content":None,"thumbnail":"discord.com/attachments/814461663696781322/841230405049909288/Roblox_logo.png", "embeds":[{"title":"Rare Username Sniped!","color":255,"fields":[{"name":"Letters Count:","value":lena},{"name":"Username:","value":a}]}]}) 
    time.sleep(20)
  else: 
    print("EHH")
  time.sleep(1)
