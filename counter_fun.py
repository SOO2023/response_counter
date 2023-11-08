from emoji_remove import remove_emoji
import emoji
import re


def response_summary(response):

    def word_count(response):

        if len(response) == 0:
            return 0
        if emoji.emoji_list(response):
            response = remove_emoji(response)

        for word in response.split(' '):
            if len(word) == 1 and word.lower() not in ['a', 'i']:
                continue
            yield 1

    def sen_count(response):

        pattern = re.compile(r'(\.|\!|\?)+')
        response = pattern.sub(r'.', response)

        word_count = 0
        for char in response:
            if char in ['.', '?', '!']:
                word_count += 1
        return word_count

    number_chars_response = len(response.strip())

    number_words_response = word_count(response.strip())

    number_sen_response = sen_count(response.strip())

    number_emoji_response = emoji.emoji_count(response)

    return number_chars_response, sum(number_words_response), number_sen_response, number_emoji_response


if __name__ == '__main__':
    resp1 = "Stethoscopes use sound waves to amplify internal body sounds, like your heartbeat or breathing. The doctor places the stethoscope on your chest or back, and the sound waves travel through the tubing to their ears, allowing them to hear your heartbeat or breathing more clearly. It;s like a tiny microphone for your body! 😎🌦️🌡️💭"

    resp2 = "Stethoscopes work by amplifying sounds within the body - like your heartbeat! Doctors place the stethoscope on their ears and press the chestpiece against your skin to listen. The chestpiece contains a diaphragm that vibrates with sound waves, which travel through tubing to the doctor's ears. Neat, right? 😎"

    number_chars_response1, number_words_response1, number_sen_response1, number_emoji_response1 = response_summary(
        resp1)
    number_chars_response2, number_words_response2, number_sen_response2, number_emoji_response2 = response_summary(
        resp2)

    print(number_words_response2)
    print(number_emoji_response1, number_emoji_response2)

    # print(
    #     f"response 1 character count: {number_chars_response1}, response 2 character count: {number_chars_response2}")
    # print(
    #     f"response 1 word count: {number_words_response1}, response 2 word count: {number_words_response2}")
    # print(
    #     f"response 1 sentence count: {number_sen_response1}, response 2 sentence count: {number_sen_response2}")
    # print(
    #     f"response 1 avg character per sentence count: {number_chars_response1/number_sen_response1}, response 2 avg character per sentence count: {number_chars_response2/number_sen_response2}")
    # print(
    #     f"response 1 avg word per sentence count: {number_words_response1/number_sen_response1}, response 2 avg word per sentence count: {number_words_response2/number_sen_response2}")
