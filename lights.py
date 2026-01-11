import asyncio
import os
from dotenv import load_dotenv

from tapo import ApiClient

load_dotenv()

async def handle_connection():
    tapo_username = os.getenv("TAPO_USERNAME")
    tapo_password = os.getenv("TAPO_PASSWORD")
    target = os.getenv("TARGET")

    client = ApiClient(tapo_username, tapo_password)
    device = await client.l510(target)
    print(f"Connected to device: {device}")

    return device

async def info():

    device = await handle_connection()

    dInfo = await device.get_device_info()

    return dInfo
    

async def on():
    device = await handle_connection()
    device.on()
    

async def off():
    device = await handle_connection()
    device.off()