import asyncio
import aiohttp

class Request():
    def __init__(self):
        self.possible_args = ['waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 'cry', 'hug', 'awoo', 'kiss', 'lick', 'pat', 'smug', 'bonk', 'yeet', 'blush', 'smile', 'wave', 'highfive', 'handhold', 'nom', 'bite', 'glomp', 'slap', 'cringe', 'dance', 'poke', 'wink', 'happy', 'kick', 'kiss', 'nsfw_waifu', 'nsfw_neko', 'trap', 'blowjob']
        self.possible_types = ['sfw', 'nsfw']

    async def get_image(self, type:str, category:str):
        if type is None:
            print("waifupicsAiohttp: error, type must not be None")
            return

        if category is None:
            print("waifupicsAiohttp:error, category must not be None")
            return

        if type not in self.possible_types:
            print("waifupicsAiohttp: error, avaible types: 'sfw', 'nsfw'")
            return
        if category not in self.possible_args:
            print("waifupicsAiohttp: error, category must be in possible_sfw or possible_nsfw")
            return

        if category == 'nsfw_waifu':
            category = "waifu"

        if category == 'nsfw_neko':
            category = "neko"

        try:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f"https://api.waifu.pics/{type}/{category}") as r:
                    res = await r.json()
                    return(res["url"])
        except:
            print("waifupicsAiohttp: error, API is not working..")
            return
