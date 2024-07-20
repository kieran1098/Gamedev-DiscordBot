import os
import io
import traceback
import sys
import subprocess
import discord
import random
import requests
from discord.ext import commands
from discord import Interaction
import pyflakes.api
import pyflakes.checker
from pyflakes import reporter as pyflakes_reporter
from pyflakes import messages as pyflakes_messages
import ast
import logging
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set the logging level to INFO

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


class tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    async def review(self, ctx, *, code):
        try:
            # Analyze the provided code
            issues = self.analyze_code(code)

            # Format the review response
            response = self.format_review_response(issues)

            # Send the response to the user
            await ctx.send(embed=response)
        except Exception as e:
            # If an error occurs, send an error message
            await ctx.send(f"An error occurred while processing the command: {e}")

    def analyze_code(self, code):
        print("Analyzing code...")
        print(code)  # Print out the input code
        issues = []
        try:
            # Use pyflakes to analyze the code and detect issues
            old_stdout = sys.stdout
            new_stdout = io.StringIO()
            sys.stdout = new_stdout
            tree = ast.parse(code)
            pyflakes.api.check(tree, 'example.py')
            sys.stdout = old_stdout
            output = new_stdout.getvalue()
            issues = [line.strip()
                      for line in output.split('\n') if line.strip()]
        except Exception as e:
            issues.append(f"An error occurred during code analysis: {e}")

        print("Code analysis complete.")
        return issues

    def format_review_response(self, issues):
        # Format the code review response based on the detected issues
        response_embed = discord.Embed(
            title="Code Review", color=discord.Color.blurple())

        if issues:
            for issue in issues:
                response_embed.add_field(
                    name=f"Issue", value=issue, inline=False)
        else:
            response_embed.add_field(
                name="No Issues Detected", value="Your code looks good!", inline=False)

        return response_embed

    @commands.command(name="events")
    async def Events(self, ctx):
        # Define the URL of the webpage to scrape (replace with your desired event website)
        url = "https://ingamejob.com/en/events"

        try:
            # Send a request to the webpage
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for any HTTP error

            # Parse the HTML content of the webpage
            soup = BeautifulSoup(response.content, "html.parser")

            # Find and extract event information from the webpage
            events = soup.find_all("div", class_="event")

            # Create an embed to display the events
            embed = discord.Embed(title="Upcoming Events",
                                  color=discord.Color.blue())

            # Add each event to the embed
            for event in events:
                # Try to extract event information, handling potential None values
                event_name = event.find("h2")
                event_date = event.find("span", class_="date")
                event_location = event.find("span", class_="location")

                # Check if any of the elements are None
                if event_name and event_date and event_location:
                    # Add the event to the embed
                    embed.add_field(
                        name=event_name.text.strip(),
                        value=f"Date: {event_date.text.strip()}\nLocation: {
                            event_location.text.strip()}",
                        inline=False
                    )

            # Check if any events were found
            if embed.fields:
                # Send the embed as a message
                await ctx.send(embed=embed)
            else:
                await ctx.send("No upcoming events found.")

        except requests.RequestException as e:
            await ctx.send(f"Failed to fetch events. Error: {e}")
        except Exception as e:
            await ctx.send(f"An unexpected error occurred: {e}")


async def setup(bot):
    await bot.add_cog(tools(bot))
