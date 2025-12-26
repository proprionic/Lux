import { cloudLogin, loginDevice } from "tp-link-tapo-connect";
import dotenv from 'dotenv';

dotenv.config();

console.log("Running.")


const email = process.env.TAPO_EMAIL;
const psw = process.env.TAPO_PASS;
const deviceIp = process.env.DEVICE_IP;
console.log(".env loaded.")
const cloudApi = await cloudLogin(email, psw);

console.log("Logged in.")

const res = await cloudApi.listDevicesByType("SMART.TAPOBULB");

const localDevices = [];

for (const d of res) {
    console.log("Logging into:", d.alias);
    const device = await loginDevice(email, psw, d);
    localDevices.push(device);
}

// Print info for all devices
for (let i = 0; i < localDevices.length; i++) {
    const d = localDevices[i];
    const info = await d.getDeviceInfo(); // ✅ must call it
    console.log(`${i + 1}) ${info.alias} (${info.deviceType})`);
}
