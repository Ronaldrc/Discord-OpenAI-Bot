# Copyright 2023 Ron Chim
# Description: This program launches a discord bot which utilizes the OpenAI API to generate text and images.

import discord
import aiohttp
import io
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import bot
from discord import app_commands
from openai import AsyncOpenAI

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

# Define client, tree, and bot
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
bot = commands.Bot(command_prefix='!', intents=intents)

# Get API key for ChatGPT from the .env file on my local machine
# Load .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DISCORD_BOT_KEY = os.getenv("DISCORD_BOT_KEY")

# 2 models for chatting or images - change as needed
CHAT_MODEL = "gpt-3.5-turbo-1106"
IMAGE_MODEL = "dall-e-3"

# Perform on bot startup
@bot.event
async def on_ready():
    print('All-in-one Brozzer bot is online! - POGGERS')
    try:
        # Sync all recently created slash commands 
        synced = await bot.tree.sync()
        print(f"synched {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands {e}")

# Slash command to access .csv file and announce the next bday
# @bot.tree.command(name="nextbday")

# Create slash commands
# Send cat image to cat-image channel when /cat is typed
cat_channel = bot.get_channel(1191649805747888178)      # cat-image channel
cat_url = "https://images.unsplash.com/photo-1608848461950-0fe51dfc41cb?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8fA%3D%3D"
@bot.tree.command(name="cat", description="Need cat")
async def cat(interaction: discord.Interaction):
    async with aiohttp.ClientSession() as session:      # create session
        async with session.get(cat_url) as resp:        # gets image from url
            image = await resp.read()       # read image from response
            with io.BytesIO(image) as file:       # converts to file-like object
                await interaction.response.send_message(file=discord.File(file, "need_cat.png"))  # send the file to discord channel

# Slash command to access ChatGPT API and get a text response
# Takes in an argument as a sentence
@bot.tree.command(name="chatgpt", description="Type a message to ChatGPT and get a response back")
@app_commands.describe(prompt = "type your message here")
async def say(interaction: discord.Interaction, prompt: str):
    await interaction.response.defer()      # since interaction is lost after 3 seconds
    openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)
    response = await openai_client.chat.completions.create(
                model = CHAT_MODEL,
                response_format={ "type": "json_object" },
                messages = [
                    {"role": "system", "content": "You are a helpful and creative assistant designed to only output JSON."},
                    {"role": "user", "content": prompt}
                ], 
                max_tokens=100,
                temperature=0.6
            )
    message_output = response.choices[0].message.content[1:-1]
    new_start = message_output.find(':') + 1
    message_output = message_output[new_start:]     # only print response from model, which was after first colon
    message_output = f"{interaction.user.mention} asked:\n\"{prompt}\"\n\nChatGPT says:\n{message_output}"
    await interaction.followup.send(message_output)

# Slash command to access Dalle-3 API and get an image response
# Takes in an argument as a sentence
@bot.tree.command(name="dalle3", description="Type what you want to see")
@app_commands.describe(prompt = "type your message here")
async def say(interaction: discord.Interaction, prompt: str):
    await interaction.response.defer()      # since interaction is lost after 3 seconds
    openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)
    response = await openai_client.images.generate(
                model = IMAGE_MODEL,
                prompt = prompt,
                size = "1024x1024",
                quality = "standard",
                n=1,
            )
    image_url = response.data[0].url
    print(image_url)
    async with aiohttp.ClientSession() as session:
        async with session.get(image_url) as resp:
            img = await resp.read()
            with io.BytesIO(img) as file:
                text = f"{interaction.user.mention} asked for \"{prompt}\"..."
                await interaction.followup.send(content=text, file=discord.File(file, "image.png"))

bot.run(DISCORD_BOT_KEY)