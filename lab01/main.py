from requests import get, post, put, delete

male_voice = [
    'data/mp3/male_voice_message_1.mp3',
    'data/mp3/male_voice_message_2.mp3',
    'data/mp3/male_voice_message_3.mp3',
    'data/mp3/male_voice_message_4.mp3',
    'data/mp3/male_voice_message_5.mp3',
]
female_voice = [
    'data/mp3/female_voice_message_1.mp3',
    'data/mp3/female_voice_message_2.mp3',
    'data/mp3/female_voice_message_3.mp3',
    'data/mp3/female_voice_message_4.mp3',
    'data/mp3/female_voice_message_5.mp3',
 ]

def get_voice_data(url):
    response = get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
