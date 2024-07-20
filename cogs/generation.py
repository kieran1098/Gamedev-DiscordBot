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


class generation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command(name='idea')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def random_word(self, ctx):
        # Open the file and read all lines
        with open('words.txt', 'r', encoding='utf-8') as file:
            words = file.readlines()

        # Choose a random word from the list
        random_word = random.choice(words).strip()

        # Create an embed
        embed = discord.Embed(title="Random Word",
                              description=random_word, color=discord.Color.blue())

        # Send the embed to the Discord channel
        await ctx.send(embed=embed)

    unsplash_access_key = "kMlrzA2yeCY8W1oglGl0WoSKtif97Cpff5RcdtUuyUQ"

    @bot.command(name='generateimage', aliases=['image', 'randomimage'])
    async def generate_image(self, ctx):
        try:
            # Fetch a random image from Unsplash
            image_url = self.get_random_image()

            if image_url:
                # Create an embed with the image
                embed = discord.Embed(title="Random Image",
                                      color=discord.Color.blue())
                embed.set_image(url=image_url)

                # Send the embed to the Discord channel
                await ctx.send(embed=embed)
            else:
                await ctx.send("Failed to fetch a random image.")
        except Exception as e:
            print(f"An error occurred: {e}")
            await ctx.send("An error occurred while fetching the random image.")

    def get_random_image(self):
        try:
            # Use the Unsplash API to get a random image
            unsplash_url = "https://api.unsplash.com/photos/random"
            headers = {
                "Authorization": f"Client-ID {self.unsplash_access_key}"
            }

            response = requests.get(unsplash_url, headers=headers)
            if response.status_code == 200:
                image_data = response.json()
                image_url = image_data['urls']['regular']
                return image_url
            else:
                print(f"Failed to fetch a random image. Status code: {
                      response.status_code}")
                return None
        except Exception as e:
            print(f"An error occurred while fetching a random image: {e}")
            return None

    @bot.command(name='RandomPalette', aliases=['randompalette'])
    async def randompalette(self, ctx):
        # Generate a random color palette with 5 colors
        palette = [discord.Color(random.randint(0, 0xFFFFFF))
                   for _ in range(5)]

        # Create an image to represent each color
        image_size = 50
        images = []
        for color in palette:
            image = Image.new('RGB', (image_size, image_size), color.to_rgb())
            images.append(image)

        # Combine images horizontally into a single image
        combined_image = Image.new(
            'RGB', (image_size * len(palette), image_size))
        x_offset = 0
        for image in images:
            combined_image.paste(image, (x_offset, 0))
            x_offset += image_size

        # Save the combined image
        combined_image_path = 'palette.png'
        combined_image.save(combined_image_path)

        # Create an embed to display the color palette
        embed = discord.Embed(
            title="Random Color Palette",
            description="Here is a random color palette:",
            color=discord.Color.blurple()
        )

        # Add the combined image as an attachment
        file = discord.File(combined_image_path, filename='palette.png')
        embed.set_image(url='attachment://palette.png')

        # Send the embed to the Discord channel
        await ctx.send(embed=embed, file=file)


async def setup(bot):
    await bot.add_cog(generation(bot))
