import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "G8AZAAL")
ALIVE_NAME = getenv("ALIVE_NAME", "U_Y_H")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "J_G_A")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "U_Y_H")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/8a86b05d8d6d9702f21a0.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "400"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/jankarikiduniya/Dr-Music-Video-Streaming")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/e0327ca6d4354bfbeff07.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/b00aa8d8b65dc8c232fdf.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/e0327ca6d4354bfbeff07.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/e0327ca6d4354bfbeff07.jpg")

# Don't Change It Bro ❣️ 😂


MY_SERVER = getenv("MY_SERVER", "J_G_A")
REPO_OWNER = getenv("REPO_OWNER", "g8azal/Dj-Music")
MY_HEART = getenv("MY_HEART", "J_G_A")
BOT_UPDATE = getenv("BOT_UPDATE", "U_Y_H")
MY_BRO = getenv("MY_BRO", "U_Y_H")
