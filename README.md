# houdini-notifier
HDA to get notified when a process in done.

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
