import asyncio
import random

import edge_tts
from edge_tts import VoicesManager

TEXT = input("Okutulacak metni giriniz:")
GENDER = input('Seslendirmen Cinsiyeti (E/K):')
GENDER = 'Male' if GENDER.lower().strip() == 'e' else 'Female'
OUTPUT_FILE = input('Çıktı Dosyası Adı:')
OUTPUT_FILE = OUTPUT_FILE if OUTPUT_FILE.endswith('.mp3') else OUTPUT_FILE+'.mp3'
LANG = input('Dil Giriniz (Türkçe için "tr"):')


async def amain() -> None:
    voices = await VoicesManager.create()
    voice = voices.find(Gender=GENDER, Language=LANG)
    communicate = edge_tts.Communicate(TEXT, random.choice(voice)["Name"])
    await communicate.save(OUTPUT_FILE)


if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    try:
        loop.run_until_complete(amain())
    finally:
        loop.close()