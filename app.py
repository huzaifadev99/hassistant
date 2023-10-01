from flask import Flask ,  request , jsonify ,render_template
import openai
import os
import pyttsx3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/server' , methods=['POST'])
def server():
    input_value = request.form['input_data']
    print(input_value)
    # open ai playground
    openai.api_key = "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"
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
          "role": "user",
          "content": input_value
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    content = response.choices[0].message['content']
    print(content)

    return jsonify({'response': content , 'quest': input_value})

if __name__ == '__main__':
    app.run(host='192.168.203.193', port=5000, debug=True) 