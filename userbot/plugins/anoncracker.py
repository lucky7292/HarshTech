"""Emoji
Available Commands:
.anoncracker
Credits to @anon_cracker
"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd


@borg.on(admin_cmd("AnonCracker"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.5
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "pureindialover":
    await event.edit("@anon_cracker")
    animation_chars = [
            "@anon_cracker tera baap",
            "@anon_cracker is bot ka creator",
            "@anon_cracker bot ko jaan dene wala",
            "@anon_cracker owner of @Error69Club",
            "tujhe aur kya chaiye vo hai mere sath",
            "tera baap",
            "@anon_cracker"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
