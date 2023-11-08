import re


def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


if __name__ == '__main__':

    resp1 = "Stethoscopes use sound waves to amplify internal body sounds, like your heartbeat or breathing. The doctor places the stethoscope on your chest or back, and the sound waves travel through the tubing to their ears, allowing them to hear your heartbeat or breathing more clearly. It's like a tiny microphone for your body! 😎🌦️🌡️💭"

    new_resp = remove_emoji(resp1)

    print(new_resp)
