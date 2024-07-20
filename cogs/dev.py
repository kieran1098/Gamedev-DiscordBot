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


class development(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command(name='TextureBrick', aliases=['texturebrick'])
    async def sendrandombrick(self, ctx):
        # Get a list of all image files in the folder
        image_folder = "dev/Bricks"  # Change this to your image folder
        image_files = [file for file in os.listdir(
            image_folder) if file.endswith(('.png', '.jpg', '.jpeg'))]

        # Check if there are any image files in the folder
        if not image_files:
            await ctx.send("No images found in the folder.")
            return

        # Select a random image file
        random_image = random.choice(image_files)
        image_path = os.path.join(image_folder, random_image)

        # Create an embed with the random image
        embed = discord.Embed(title="Random seamless Brick",
                              color=discord.Color.blue())
        embed.set_image(url=f"attachment://{random_image}")

        # Send the embed with the random image as an attachment
        with open(image_path, "rb") as file:
            image_file = discord.File(file, filename=random_image)
            await ctx.send(embed=embed, file=image_file)

    @bot.command(name='TextureWood', aliases=['texturewood'])
    async def sendrandomwood(self, ctx):
        # Get a list of all image files in the folder
        image_folder = "dev/Woods"  # Change this to your image folder
        image_files = [file for file in os.listdir(
            image_folder) if file.endswith(('.png', '.jpg', '.jpeg'))]

        # Check if there are any image files in the folder
        if not image_files:
            await ctx.send("No images found in the folder.")
            return

        # Select a random image file
        random_image = random.choice(image_files)
        image_path = os.path.join(image_folder, random_image)

        # Create an embed with the random image
        embed = discord.Embed(title="Random seamless Wood",
                              color=discord.Color.blue())
        embed.set_image(url=f"attachment://{random_image}")

        # Send the embed with the random image as an attachment
        with open(image_path, "rb") as file:
            image_file = discord.File(file, filename=random_image)
            await ctx.send(embed=embed, file=image_file)

    @bot.command(name='TextureConcrete', aliases=['textureconcrete'])
    async def sendrandomconcrete(self, ctx):
        # Get a list of all image files in the folder
        image_folder = "dev/Concrete"  # Change this to your image folder
        image_files = [file for file in os.listdir(
            image_folder) if file.endswith(('.png', '.jpg', '.jpeg'))]

        # Check if there are any image files in the folder
        if not image_files:
            await ctx.send("No images found in the folder.")
            return

        # Select a random image file
        random_image = random.choice(image_files)
        image_path = os.path.join(image_folder, random_image)

        # Create an embed with the random image
        embed = discord.Embed(title="Random seamless concrete",
                              color=discord.Color.blue())
        embed.set_image(url=f"attachment://{random_image}")

        # Send the embed with the random image as an attachment
        with open(image_path, "rb") as file:
            image_file = discord.File(file, filename=random_image)
            await ctx.send(embed=embed, file=image_file)

    @bot.command(name='TextureMetal', aliases=['texturemetal'])
    async def sendrandommetal(self, ctx):
        # Get a list of all image files in the folder
        image_folder = "dev/metals"  # Change this to your image folder
        image_files = [file for file in os.listdir(
            image_folder) if file.endswith(('.png', '.jpg', '.jpeg'))]

        # Check if there are any image files in the folder
        if not image_files:
            await ctx.send("No images found in the folder.")
            return

        # Select a random image file
        random_image = random.choice(image_files)
        image_path = os.path.join(image_folder, random_image)

        # Create an embed with the random image
        embed = discord.Embed(title="Random seamless metal",
                              color=discord.Color.blue())
        embed.set_image(url=f"attachment://{random_image}")

        # Send the embed with the random image as an attachment
        with open(image_path, "rb") as file:
            image_file = discord.File(file, filename=random_image)
            await ctx.send(embed=embed, file=image_file)

    @bot.command(name='TextureFabric', aliases=['texturefabric'])
    async def sendrandomfabric(self, ctx):
        # Get a list of all image files in the folder
        image_folder = "dev/fabrics"  # Change this to your image folder
        image_files = [file for file in os.listdir(
            image_folder) if file.endswith(('.png', '.jpg', '.jpeg'))]

        # Check if there are any image files in the folder
        if not image_files:
            await ctx.send("No images found in the folder.")
            return

        # Select a random image file
        random_image = random.choice(image_files)
        image_path = os.path.join(image_folder, random_image)

        # Create an embed with the random image
        embed = discord.Embed(title="Random seamless fabric",
                              color=discord.Color.blue())
        embed.set_image(url=f"attachment://{random_image}")

        # Send the embed with the random image as an attachment
        with open(image_path, "rb") as file:
            image_file = discord.File(file, filename=random_image)
            await ctx.send(embed=embed, file=image_file)


async def setup(bot):
    await bot.add_cog(development(bot))
