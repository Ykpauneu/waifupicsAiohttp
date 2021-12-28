from distutils.core import setup
setup(
    name='waifupicsAiohttp',
    author='Ykpauneu',
    author_email="mestodan230@gmail.com",
    url="https://github.com/Ykpauneu/waifupicsAiohttp",
    download_url="https://github.com/Ykpauneu/waifupicsAiohttp/archive/refs/tags/1.0.0.tar.gz",
    version="1.0.0",
    packages=["waifupicsAiohttp"],
    license="GNU v3",
    description="Python module that uses Waifu.pics API via aiohttp",
    install_requires=['aiohttp', 'asyncio']
)
