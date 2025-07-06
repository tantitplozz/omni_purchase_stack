from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.utils import executor
import os
import requests
import json

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: Message):
    await message.reply("🤖 สวัสดี! ส่ง /buy เพื่อเริ่มซื้อ iPhone")

@dp.message_handler(commands=['buy'])
async def handle_buy(message: Message):
    await message.reply("🚀 กำลังเริ่มกระบวนการสั่งซื้อ iPhone... กรุณารอสักครู่")
    try:
        # Prepare the task data from the trigger template
        with open('../scripts/trigger_template.json', 'r', encoding='utf-8') as f:
            task_data = json.load(f)

        # Call the backend API
        api_url = "http://backend:8000/api/run_purchase"
        response = requests.post(api_url, json=task_data, timeout=300) # 5 minutes timeout
        response.raise_for_status()  # Raise an exception for bad status codes

        result = response.json()
        await message.reply(f"✅ การสั่งซื้อเสร็จสิ้น!\nผลลัพธ์: ```{json.dumps(result, indent=2)}```")

    except requests.exceptions.RequestException as e:
        await message.reply(f"❌ เกิดข้อผิดพลาดในการเชื่อมต่อกับ Backend: {e}")
    except (IOError, json.JSONDecodeError) as e:
        await message.reply(f"❌ เกิดข้อผิดพลาดในการอ่านไฟล์ task: {e}")
    except BaseException:
        await message.reply("❌ เกิดข้อผิดพลาดที่ไม่คาดคิด")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
