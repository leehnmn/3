from flask import Flask, request, Response # flask 에서 Flask, request(요청정보) , Response(반응)
import os #윤영체제 관련기능
from io import BytesIO #메모리에 데이터를 저장하는 기능을 사용
from gtts import gTTS # gtts에서 gTTS 문자를 음성으로 바꿔주는 기능

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko') 
app = Flask(__name__)

@app.route("/")
def home():

    text = "Hello, DevOps"

    lang = request.args.get('lang', DEFAULT_LANG)
    fp = BytesIO()
    gTTS(text, "com", lang).write_to_fp(fp)

    return Response(fp.getvalue(), mimetype='audio/mpeg') # 페이지 전달없이 바로 재생

if __name__ == '__main__':
    app.run('0.0.0.0', 5005)