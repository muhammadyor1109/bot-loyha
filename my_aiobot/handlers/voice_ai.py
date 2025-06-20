from aiogram import Router, types
from pydub import AudioSegment
import speech_recognition as sr

router = Router()

@router.message(lambda m: m.voice)
async def voice_handler(message: types.Message, bot):
    file = await bot.get_file(message.voice.file_id)
    path = await bot.download_file(file.file_path)

    sound = AudioSegment.from_ogg(path.name)
    sound.export("voice.wav", format="wav")

    r = sr.Recognizer()
    with sr.AudioFile("voice.wav") as source:
        audio = r.record(source)

    text = r.recognize_google(audio, language='ru-RU')
    await message.answer(f"Ovoz matni: {text}")
