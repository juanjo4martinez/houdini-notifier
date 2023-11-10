import os

import hou
import requests


# User that will receive the message.
user_id = os.environ["DISCORD_USER_ID"]

# Direct message channel ID.
dm_channel_id = os.environ["DM_CHANNEL_ID"]

# Retrieve the first message ID (see "Pre-Render" script).
first_message_id = os.environ["FIRST_MESSAGE_ID"]

# Retrieve the progress bar message ID (see "Post-Frame" script).
progress_message_id = os.environ["PROGRESS_MESSAGE_ID"]

# Header containing bot credentials.
headers = {
    "Authorization": os.environ["DISCORD_TOKEN"]
}


# Direct Messages API Endpoint.
dm_url = f"https://discordapp.com/api/channels/{dm_channel_id}/messages"

# Single Message API Endpoint.
message_url = f"https://discordapp.com/api/channels/{dm_channel_id}/messages/{progress_message_id}"


# Compare the last cached frame against the last frame in the File Cache node.
if int(os.environ["LAST_CACHED_FRAME"]) != int(hou.pwd().evalParm("f2")):
    # If they don't match, not all frames were exported so it failed.
    payload = {
        "content": (
            f":red_circle: Failed on frame "
            f"{int(os.environ['LAST_CACHED_FRAME'])+1}\n"
            "_ _"
        ),
        # "message_reference": {
        #     "channel_id": dm_channel_id,
        #     "message_id": first_message_id,
        # }
    }

    # Send request to post a message in the DM channel.
    response_dm = requests.post(dm_url, json=payload, headers=headers)

else:
    # If they match, all frames were exported so it worked.
    payload = {
        "content": (
            ":green_circle:  Done  \n"
            "_ _"
        ),
        # "message_reference": {
        #     "channel_id": dm_channel_id,
        #     "message_id": first_message_id,
        # }
    }

    # Send request to post a message in the DM channel.
    response_dm = requests.post(dm_url, json=payload, headers=headers)
