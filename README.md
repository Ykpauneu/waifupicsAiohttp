# waifupicsAiohttp
Python module that uses Waifu.pics API via aiohttp

# Install:
```
pip install waifupicsAiohttp
```

# Requirements
- asyncio
- aiohttp

# Types and categories:
| Type | Category |
| ------ | ------ |
| "sfw" | 'waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 'cry', 'hug', 'awoo', 'kiss', 'lick', 'pat', 'smug', 'bonk', 'yeet', 'blush', 'smile', 'wave', 'highfive', 'handhold', 'nom', 'bite', 'glomp', 'slap', 'cringe', 'dance', 'poke', 'wink', 'happy', 'kick', 'kiss' |
| "nsfw" | 'nsfw_waifu', 'nsfw_neko', 'trap', 'blowjob' |

# Example:
```python
from waifupicsAiohttp import Request
import asyncio

async def main():
    res = await Request().get_image(type, category)
    print(res)
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
