from requests import get, post, put, delete

male_voice = [
    'https://github.com/Jodode/ai_methods/raw/refs/heads/main/lab01/data/mp3/male_voice_message_1.mp3',
    'https://github.com/Jodode/ai_methods/raw/refs/heads/main/lab01/data/mp3/male_voice_message_2.mp3',
    'https://github.com/Jodode/ai_methods/raw/refs/heads/main/lab01/data/mp3/male_voice_message_3.mp3',
    'https://github.com/Jodode/ai_methods/raw/refs/heads/main/lab01/data/mp3/male_voice_message_4.mp3',
    'https://github.com/Jodode/ai_methods/raw/refs/heads/main/lab01/data/mp3/male_voice_message_5.mp3',
]
female_voice = [
    'https://github.com/Jodode/ai_methods/raw/refs/heads/main/lab01/data/mp3/female_voice_message_1.mp3',
    'https://github.com/Jodode/ai_methods/raw/refs/heads/main/lab01/data/mp3/female_voice_message_2.mp3',
    'https://github.com/Jodode/ai_methods/raw/refs/heads/main/lab01/data/mp3/female_voice_message_3.mp3',
    'https://github.com/Jodode/ai_methods/raw/refs/heads/main/lab01/data/mp3/female_voice_message_4.mp3',
    'https://github.com/Jodode/ai_methods/raw/refs/heads/main/lab01/data/mp3/female_voice_message_5.mp3',
 ]

def get_voice_data(url):
    url = "https://open-ai21.p.rapidapi.com/texttoimage2"

    payload = { "text": "dog" }
    headers = {
        "x-rapidapi-key": "c1ed10766amshcae26b62c408e44p1b56dejsn0318b221d1ff",
        "x-rapidapi-host": "open-ai21.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = post(url, json=payload, headers=headers)

    print(response.json())