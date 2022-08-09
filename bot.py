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
    if(resp.ok)
        jData = json.loads(resp.content)
        await ctx.send(jData["currentAlbum"]["name"] + " - " + jData["currentAlbum"]["artist"] + " https://open.spotify.com/album/"+jData["currentAlbum"]["spotifyId"])
    else:
        resp.raise_for_status()

bot.run('TOKEN')
