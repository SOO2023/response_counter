from flask import Flask, render_template, request
from waitress import serve
from counter_fun import response_summary

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/summary', methods=['GET', 'POST'])
def summary():
    response1 = request.form['response1']
    response2 = request.form['response2']

    number_chars_response1, number_words_response1, number_sen_response1, number_emoji_response1 = response_summary(
        response1)
    number_chars_response2, number_words_response2, number_sen_response2, number_emoji_response2 = response_summary(
        response2)

    if len(response1.split(' ')) > 20:
        response1_sum = ' '.join(response1.split(' ')[:20])
        response1_sum = f"{response1_sum}..."
    else:
        response1_sum = response1

    if len(response2.split(' ')) > 20:
        response2_sum = ' '.join(response2.split(' ')[:20])
        response2_sum = f"{response2_sum}..."
    else:
        response2_sum = response2

    return render_template('summary.html', response1_sum=response1_sum, response2_sum=response2_sum, response1=response1, response2=response2, response1_char=number_chars_response1, response1_word=number_words_response1, response1_sen=number_sen_response1, response2_char=number_chars_response2, response2_word=number_words_response2, response2_sen=number_sen_response2, response1_emoji=number_emoji_response1, response2_emoji=number_emoji_response2)


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port='8000')
