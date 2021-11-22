#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


from pyrogram import (
    Client,
    __version__
)

from config import (
    API_HASH,
    APP_ID,
    LOGGER,
    TG_BOT_SESSION,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS
)

from user import User



class Bot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            TG_BOT_SESSION,
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"""Konichiwa 💛 I'm Eriri 🤗
 
You Can Download Any Romance/Shoujo Manga Using Me 💛😜
💛My Owner is @tr0j3n 🖤
💛If You Have Got Any Problem 'bout Me Please Contact him or @Peaceful_Wolf_016 😈
💛Join @waifuNetBots To Get Help 💛
💛My Owner's And Dev's Harem & From Here You Can See My Sisters: @waifuNetwork!"""
        )
        self.USER, self.USER_ID = await User().start()
        await self.USER.send_message(
            chat_id=usr_bot_me.username,
            text="😬🤒🤒"
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("I'm Going To Sleep so Bye Bye 💛")
