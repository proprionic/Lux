from fastapi import FastAPI
from lights import handle_connection

app = FastAPI()
device = None

@app.on_event("startup")
async def startup():
    global device
    device = await handle_connection()

@app.post("/on")
async def turn_on():
    await device.on()
    return {"status": "on"}

@app.post("/off")
async def turn_off():
    await device.off()
    return {"status": "off"}

@app.get("/status")
async def status():
    info = await device.get_device_info()
    return {
        "on": info.device_on,
        "brightness": info.brightness,
    }
