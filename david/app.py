from flask import Flask, request, Response # flask 에서 Flask, request(요청정보) , Response(반응)
import os #윤영체제 관련기능
from io import BytesIO #메모리에 데이터를 저장하는 기능을 사용
from gtts import gTTS # gtts에서 gTTS 문자를 음성으로 바꿔주는 기능

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko') #운영체제에게 물어봐서 기본 언어설정을 가져오고 없다면 ko 한국어로 가져오라는 문장
app = Flask(__name__)

@app.route("/")
def home():      #home 변수설정

    text = "Hello, DevOps"

    lang = request.args.get('lang', DEFAULT_LANG) #args 딕셔너리에서 lang 이란 키가 있다면 가져오고 있다면 그 값을 리턴 아니면 DEFAULT_LANG 가져오기
    fp = BytesIO() #음성 데이터 저장 메모리 만들기.  그럴대 쓰는 것이 BytesIO() 즉 음성데이터 저장 메모리
    gTTS(text, "com", lang).write_to_fp(fp) #gtts 구글 텍스트 두 스피치 text로 com에서 lang 언어코드 를 이용 /fp 안에 있는 음성데이터를 fp에써주는 작업.

    return Response(fp.getvalue(), mimetype='audio/mpeg') # 페이지 전달없이 바로 재생 fp.getvalue()는 아까만든 가짜 메모리 파일 mimetype='audio/mpeg'는 음성 파일이라고 브라우저에 알려주는 부분.

if __name__ == '__main__':
    app.run('0.0.0.0', 5005)