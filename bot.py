import requests
import json
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

bot = commands.Bot(command_prefix="/")
slash = SlashCommand(bot)

@slash.slash(name="album")
async def album(ctx: SlashContext):
    url = "https://1001albumsgenerator.com/api/v1/groups/bruzzy"
    resp = requests.get(url)
    if(resp.ok):
        # Loading the response data into a dict variable
        # json.loads takes in only binary or string variables so using content to fetch binary content
        # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
        jData = json.loads(resp.content)
        await ctx.send(jData["currentAlbum"]["name"] + " - " + jData["currentAlbum"]["artist"] + " https://open.spotify.com/album/"+jData["currentAlbum"]["spotifyId"])
    else:
        # If response code is not ok (200), print the resulting http error code with description
        resp.raise_for_status()

bot.run('TOKEN')
