import json
import os

import hou
import requests


# User that will receive the message.
user_id = os.environ["DISCORD_USER_ID"]

# Set the user as recipient of the message.
data = {"recipient_id": user_id}

# Header containing bot credentials.
headers = {
    "Authorization": os.environ["DISCORD_TOKEN"]
}

# Send request to create a DM channel.
response_dm_channel = requests.post(
    "https://discord.com/api/users/@me/channels",
    json=data,
    headers=headers)

# Retrieve the channel ID and store it as an environment variable.
dm_channel_id = response_dm_channel.json()["id"]
os.environ["DM_CHANNEL_ID"] = dm_channel_id


# Direct Messages API Endpoint.
dm_url = f"https://discordapp.com/api/channels/{dm_channel_id}/messages"

# Message to be sent.
payload = {
    "content": (
        f"**{hou.pwd().parent().path()}**  ▸  {hou.hipFile.basename()}"
    )
}

# Send request to post the message in the DM channel.
response = requests.post(dm_url, json=payload, headers=headers)

# Retrieve the message ID and store it as an environment variable.
first_message_id = response.json()["id"]
os.environ["FIRST_MESSAGE_ID"] = first_message_id
