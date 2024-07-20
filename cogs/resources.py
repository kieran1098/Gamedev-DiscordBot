import os
import sys
import discord
import random
from PIL import Image, ImageDraw, ImageFont
import textwrap
import requests
from discord.ext import commands
from discord.ext.commands import Bot
from discord import app_commands
from discord import Interaction
from discord import interactions
import interactions
import logging
import sqlite3


# Set the bot prefix
bot_prefix = "??"
command_prefix = "/"


# Define intents
intents = discord.Intents.all()
intents.messages = True
intents.members = True  # Enable the GUILD_MEMBERS intent
intents.guilds = True

# Create a bot instance with a command prefix and intents
bot = commands.Bot(command_prefix=bot_prefix,
                   intents=intents, help_command=None)


class resources(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command(name='TexturingTUTs')
    async def TexturingTUTslink(self, ctx):
        # Create an embed with the link
        embed = discord.Embed(title="TexturingTUTs link",
                              description="[Click here for the TexturingTUTs (substance painter)!](https://mega.nz/file/13kW1LQQ#Gomq5092qVlthSk5g4WCgK3i4XuG91--4jZi28_447s)", color=discord.Color.blue())

        # Send the embed to the Discord channel
        await ctx.send(embed=embed)

    @bot.command(name='ModelingTUTs')
    async def ModelingTUTslink(self, ctx):
        # Create an embed with the link
        embed = discord.Embed(title="ModelingTUTs link",
                              description="[Click here for the ModelingTUTs (Blender + Maya)!](https://mega.nz/file/w2FXABBZ#lqEmOs2CMuvOiE7ocklafGSfFs4cxJqxm8LrSuUKvow)", color=discord.Color.blue())

        # Send the embed to the Discord channel
        await ctx.send(embed=embed)

    @bot.command(name='SculptingTUTs')
    async def SculptingTUTslink(self, ctx):
        # Create an embed with the link
        embed = discord.Embed(title="SculptingTUTs link",
                              description="[Click here for the SculptingTUTs (Blender + zbrush)!](https://mega.nz/file/I6MThJrb#30yg3WCNGPl3hMo9vcwIe60_xd0JIHb3QYnr_1s7QyM)", color=discord.Color.blue())

        # Send the embed to the Discord channel
        await ctx.send(embed=embed)

    @bot.command(name='EngineTUTs')
    async def EngineTUTslink(self, ctx):
        # Create an embed with the link
        embed = discord.Embed(title="EngineTUTs link",
                              description="[Click here for the EngineTUTs (Unity + UE)!](https://mega.nz/file/crUhEYDB#6I_PJTGJzhdxDCnz6TsU_ZX05dVK4LBHXslrzIYs-O4)", color=discord.Color.blue())

        # Send the embed to the Discord channel
        await ctx.send(embed=embed)

    @bot.command(name='sound')
    async def sendrandomaudio(self, ctx):
        # Get a list of all audio files in the folder
        audio_folder = "audio"  # Change this to your audio folder
        audio_files = [file for file in os.listdir(
            audio_folder) if file.endswith(('.mp3', '.wav'))]

        # Check if there are any audio files in the folder
        if not audio_files:
            await ctx.send("No audio files found in the folder.")
            return

        # Select a random audio file
        random_audio = random.choice(audio_files)
        audio_path = os.path.join(audio_folder, random_audio)

        # Create an embed with the random audio file
        embed = discord.Embed(title=random_audio, color=discord.Color.blue())

        # Send the embed with the random audio file as an attachment
        with open(audio_path, "rb") as file:
            audio_file = discord.File(file, filename=random_audio)
            await ctx.send(embed=embed, file=audio_file)


async def setup(bot):
    await bot.add_cog(resources(bot))
