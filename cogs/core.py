import discord, requests
from datetime import datetime
from discord.ext import commands

class Core(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        
    @commands.command(aliases=['s'])
    async def steam(self, ctx, id : str):
        with requests.Session() as s:
            steam_key = "YOUR STEAM WEB API KEY"
            r=s.get(f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={steam_key}&steamids={id}&format=json")
            dict= {"response":{"players":[{"steamid":"Unavailable","communityvisibilitystate":0,"realname": "Unavailable","profilestate":0,"personaname":"Unavailable","profileurl":"Unavailable","avatarmedium":"https://cdn.discordapp.com/attachments/855448636880191499/878268636467429487/6.png","avatarhash":"Unavailable","personastate":0,"primaryclanid":"Unavailable","timecreated":0,"loccountrycode": "Unavailable","locstatecode": "Unavailable","loccityid": "Unavailable","personastateflags":0, "lastlogoff": 0}]}}

            for v in r.json()["response"]["players"][0].items():
                dict["response"]["players"][0][list(v)[0]] = list(v)[1]

            embed=discord.Embed(title=f"Profile: {dict['response']['players'][0]['personaname']} ({dict['response']['players'][0]['steamid']})", description=f"Avatar Hash: **{dict['response']['players'][0]['avatarhash']}**\nProfile URL: **{dict['response']['players'][0]['profileurl']}**", color=65535)
            embed.add_field(name=" ‎\nReal Name", value=f"🔹 **{dict['response']['players'][0]['realname']}**")
            embed.add_field(name=" ‎\nAccount Created", value=f"🔹 **{datetime.utcfromtimestamp(int(dict['response']['players'][0]['timecreated'])).strftime('%Y-%m-%d %H:%M:%S')}**")
            embed.add_field(name='\u200b', value='\u200b')
            embed.add_field(name="‏‏‎ ‎\nVisibility State", value=f"🔹 **{dict['response']['players'][0]['communityvisibilitystate']}**")
            embed.add_field(name=" ‎\nProfile State", value=f"🔹 **{dict['response']['players'][0]['profilestate']}**")
            embed.add_field(name='\u200b', value='\u200b')
            embed.add_field(name=" ‎\nLast Online", value=f"🔹 **{datetime.utcfromtimestamp(int(dict['response']['players'][0]['lastlogoff'])).strftime('%Y-%m-%d %H:%M:%S')}**")
            embed.add_field(name=" ‎\nPrimary Clan ID", value=f"🔹 **{dict['response']['players'][0]['primaryclanid']}**")
            embed.add_field(name='\u200b', value='\u200b')
            embed.add_field(name=" ‎\nCountry Code", value=f"🔹 **{dict['response']['players'][0]['loccountrycode']}**")
            embed.add_field(name=" ‎\nState Code", value=f"🔹 **{dict['response']['players'][0]['locstatecode']}**")
            embed.add_field(name='\u200b', value='\u200b')
            embed.add_field(name=" ‎\nCity Code", value=f"🔹 **{dict['response']['players'][0]['loccityid']}**")
            embed.set_thumbnail(url=f"{dict['response']['players'][0]['avatarmedium']}")
            await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Core(client))
