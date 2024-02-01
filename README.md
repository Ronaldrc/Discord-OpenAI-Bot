# Discord-OpenAI-Bot
## Description
A discord bot that uses slash commands to generate chat and images using official ChatGPT models.
Popular models include ChatGPT-4 and Dalle-3, which can generate text or images, respectively.
<p align="center">
  <img src= "https://github.com/Ronaldrc/Discord-OpenAI-Bot/assets/107775094/863604b5-de07-41c4-872f-073faa3ed0ae"/>
</p>

<p align="center">
   <img src= "https://github.com/Ronaldrc/Discord-OpenAI-Bot/assets/107775094/7b75342e-90ff-4f55-93d0-8f138770242f"/>
</p>

To use this script, you must modify **THREE** lines of code for: 
- OpenAI API token
- Discord Bot token

Instructions for creating the OpenAI token, creating the discord bot, downloading and running the python script, and final pointers will be discussed in further detail.

Note: ***Usage of the OpenAI's API may incur costs.*** 
Please refer to OpenAI's pricing policy before continuing any further.

## Creating an OpenAI Token
1. Head over to [OpenAI](https://platform.openai.com/) and create an account. Then, login using the credentials you have just created.
2. Once signed in, hover your mouse over the lefthand dropdown and click on `API keys`.
3. Press `Create new secret key` and type any name of your choice. I named mine "Discord Bot".
<p align="center">
   <img src= "https://github.com/Ronaldrc/Discord-OpenAI-Bot/assets/107775094/48ef5ea9-d5e9-4cea-83ae-a6c566e456b9"/>
</p>

4. ***Important***:
Be sure to copy down the secret key for later use.
**Do NOT** share it with others.

## Creating a Discord Bot
The discord bot must be created in the developer portal.
1. Head over to https://www.discord.com/developers and create an account.
2. Sign into the developer portal.
3. Create a `New Application`
4. Name the application and click `Create`
5. Click on the newly created bot and copy down 3 pieces of information
   - `Token`
   - `Application ID`
   - `Public Key`

## Downloading the Python Script
The only file required for running the bot is `main.py`. Simply download the raw file from GitHub and store it on your local machine.

## Modifying the Script
As mentioned in the beginning, the user must change **THREE** lines of code to get their own discord bot up and running.

Delete this line of code from `main.py`.

```python
load_dotenv()
```

Next, find these two lines of code. We will modify them, soon.
```python
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DISCORD_BOT_KEY = os.getenv("DISCORD_BOT_KEY")
```

Replace `os.getenv("OPENAI_API_KEY")` and `os.getenv("DISCORD_BOT_KEY")` with their respective keys.

The final code should look something like this.
```python
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY_GOES_HERE"
DISCORD_BOT_KEY = "YOUR_DISCORD_BOT_KEY_GOES_HERE"
```

## Running the Script / Launching the Bot
To run the script, the user must have `Python` installed.
Windows users can install Python from `Microsoft Store` or [Python Org](https://www.python.org/).

## Additional Tips
1. Changing chat or image models
OpenAI offers many models for generating text or images. Check out [OpenAI Models](https://platform.openai.com/docs/models/overview).
To change your model, find and modify these two lines of code from `main.py`.
```python
CHAT_MODEL = "gpt-3.5-turbo-1106"
IMAGE_MODEL = "dall-e-3"
```
Now, replace `gpt-3.5-turbo-1106` and/or `dall-e-3` with the model name.
For example, if I wanted to use GPT-4 Turbo, I would modify one line so it looks like this.
```python
CHAT_MODEL = "gpt-4-0125-preview"
```
And happy coding!