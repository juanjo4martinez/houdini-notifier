# houdini-notifier
HDA to get notified when a process in done. This is currently a WIP, so more functionality is to be expected in the future.

- Download the `.hda` file and put it in your `otls` directory (on Windows, that's usually `\Documents\houdinixx.x\otls`).
- Launch Houdini and the HDA should appear in the TAB Menu under the name `Send Email` (only in the SOP context).

**Important:** In order to use this tool with a Gmail account, you have to first **generate an app password** following [these steps](https://support.google.com/accounts/answer/185833?hl=en). That app password is what you should enter in your credentials file or parameters, not the usual one!

The JSON credentials file should follow this template:

```
{
  "login": "me@domain.com",
  "password": "1234"
}
```

### Tracking jobs in Discord
Here are the steps to make it work:
- Create your own bot following [these steps](https://discordpy.readthedocs.io/en/stable/discord.html), or have access to an already existing one.
- Invite the bot to your server.
- Edit the `houdini.env` file and add your bot's token under a `DISCORD_TOKEN` variable, and your user ID under a `DISCORD_USER_ID` variable.
  
  For example:
  - DISCORD_TOKEN = "Bot 1234567890thisismytoken"
  - DISCORD_USER_ID = "718419653205950520"

- Restart Houdini, load your scene and find the `Scripts` tab of an output node in Houdini.
- Set the Pre-Render, Post-Frame and Post-Render scripts (you'll find them here in the `/scripts` folder).
- Execute the node and you should receive a direct message from the bot with info about the job.

This has only been tested with `File Cache` nodes. More info coming in next releases.
