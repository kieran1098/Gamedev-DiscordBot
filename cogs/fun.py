import discord
import random
import requests
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        try:
            response = requests.get("https://some-random-api.ml/meme")
            data = response.json()
            if "image" in data:
                meme_url = data["image"]
                embed = discord.Embed(title="Meme", color=discord.Color.blue())
                embed.set_image(url=meme_url)
                await ctx.send(embed=embed)
            else:
                await ctx.send("Sorry, I couldn't fetch a meme at the moment.")
        except Exception as e:
            await ctx.send("Sorry, I encountered an error while fetching the meme.")

# Add this cog to the bot


async def setup(bot):
    await bot.add_cog(Fun(bot))
