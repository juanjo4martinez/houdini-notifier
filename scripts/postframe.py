import os

import hou
import requests


# User that will receive the message.
user_id = os.environ["DISCORD_USER_ID"]

# Direct message channel ID.
dm_channel_id = os.environ["DM_CHANNEL_ID"]

# Header containing bot credentials.
headers = {
    "Authorization": os.environ["DISCORD_TOKEN"]
}


# Direct Messages API Endpoint.
dm_url = f"https://discordapp.com/api/channels/{dm_channel_id}/messages"


def draw_progress_bar(current_percent):
    """Generate a progress bar depending on the completed percentage.

    :param current_percent: Percentage of work that is complete
    :type current_percent: int

    :return: String representing a progress bar
    :rtype: str
    """
    if 0 <= current_percent <= 9:
        return "▱▱▱▱▱▱▱▱▱▱"
    if 10 <= current_percent <= 19:
        return "▰▱▱▱▱▱▱▱▱▱"
    if 20 <= current_percent <= 29:
        return "▰▰▱▱▱▱▱▱▱▱"
    if 30 <= current_percent <= 39:
        return "▰▰▰▱▱▱▱▱▱▱"
    if 40 <= current_percent <= 49:
        return "▰▰▰▰▱▱▱▱▱▱"
    if 50 <= current_percent <= 59:
        return "▰▰▰▰▰▱▱▱▱▱"
    if 60 <= current_percent <= 69:
        return "▰▰▰▰▰▰▱▱▱▱"
    if 70 <= current_percent <= 79:
        return "▰▰▰▰▰▰▰▱▱▱"
    if 80 <= current_percent <= 89:
        return "▰▰▰▰▰▰▰▰▱▱"
    if 90 <= current_percent < 99:
        return "▰▰▰▰▰▰▰▰▰▱"
    if 99 <= current_percent:
        return "▰▰▰▰▰▰▰▰▰▰"


# Get the start and end frames from the node.
start_frame = hou.pwd().evalParm("f1")
end_frame = hou.pwd().evalParm("f2")

# Calculate the total amount of frames to be processed.
total_frames = end_frame - start_frame + 1

# Read the current frame number and calculate the percentage.
current_frame = hou.frame()
current_percent = round((current_frame * 100) / end_frame, 2)


# Message to be sent.
payload = {
    "content": (
        f"{draw_progress_bar(current_percent)}  "
        f"{current_percent}% ({int(current_frame)}/{int(end_frame)})"
    )
}


# On the first frame...
if int(current_frame) == start_frame:
    # Send request to post the message in the DM channel.
    response = requests.post(dm_url, json=payload, headers=headers)

    # Retrieve the message ID and store it as an environment variable.
    progress_message_id = response.json()["id"]
    os.environ["PROGRESS_MESSAGE_ID"] = progress_message_id

# On following frames...
else:
    # Retrieve the message ID from the environment variable.
    progress_message_id = os.environ["PROGRESS_MESSAGE_ID"]

    # Single Message API Endpoint.
    message_url = f"https://discordapp.com/api/channels/{dm_channel_id}/messages/{progress_message_id}"

    # Send request to update the message (i.e: the progress bar) on steps of 25.
    # The lower the number, the more precise the progress bar will be.
    # However, values lower than 25 might cause the bot to be rate limited.
    if current_percent % 25 == 0:
        response = requests.patch(message_url, json=payload, headers=headers)


# Store the current frame as an environment variable.
# This will help us later when detecting errors.
os.environ["LAST_CACHED_FRAME"] = str(int(hou.frame()))
