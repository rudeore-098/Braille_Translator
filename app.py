from flask import Flask, request, render_template, jsonify
from googletrans import Translator
from setup import get_result_list, set_result_list # 추가
import subprocess
import setup
import code_3rd
import serial # 추기
import time #추가


app = Flask(__name__)
#추가====================================================
try:
    ser = serial.Serial(port='COM3', baudrate=4800, timeout=10)
except Exception as e:
    print(f"Error opening serial port: {e}")
#추가====================================================


def braille_translate(text):
    code_3rd.init(text)
    setup.start()
    code_3rd.end()
    setup.end()

#추가======================================================
    #결과 리스트 가져오기
    result_list_from_setup = get_result_list()
    #결과 리스트 출력
    print("Result List from setup.py:", result_list_from_setup)


    # 리스트를 0과 1로 구성된 문자열로 변환//리스트로 전송은 어려움
    result_string = ''.join(map(str, result_list_from_setup)) + "\n"
    if ser.is_open==False:
            try:
                ser.open()
                print("Serial port opend successfully.")
            except Exception as open_error:
                print("Error opening serial port:", open_error)
    # 결과 문자열을 시리얼 통신을 통해 Arduino로 전송
    try:
        #print(1)
        print(result_string)
        ser.write(result_string.encode())
        #print(2)
        ser.flush()
        #print(3)

    except Exception as e:
        print("시리얼 통신 중 에러 발생:", e)
        # Additional debugging information
        print("Serial port status:", ser.is_open)
        print("Result string:", result_string)

        # If the serial port is still open, try closing it
        # if ser.is_open:
        #     try:
        #         ser.close()
        #         print("Serial port closed successfully.")
        #     except Exception as close_error:
        #         print("Error closing serial port:", close_error)

    time.sleep(10)
    # print(ser.readall())
    # if(ser.readable):
    #     LINE = ser.readline()
    #     print(LINE)
    # else:
    #     print("실패")
    ser.close()
#추가========================================================



# Function to translate text between Korean and English using Google Translate API
def translate_text(text, source_language='ko', target_language='en'):
    translator = Translator()
    try:
        translated_text = translator.translate(text, src=source_language, dest=target_language)
        # braille_translate(translated_text.text)
        return translated_text.text
    except Exception as e:
        return f"Translation Error: {e}"


def run_runcode():
    subprocess.run(["python3", "Runcode.py"])


def get_selected_langauges():
    source_language = request.form.get('source_language')
    target_language = request.form.get('target_language')
    return source_language, target_language


def translate_and_store(text, source_langauge, target_langauge):
    translated_text = translate_text(text, source_langauge, target_langauge)
    return translated_text


# Route for the home page
@app.route("/", methods=['GET', 'POST'])
def index():
    input_text = ''
    translated_text = '변역 결과'
    source_language = ''
    target_langauge = ''

    if request.method == 'POST':
        if 'trans_button' in request.form:

            input_text = request.form['input_text']
            source_language, target_langauge = get_selected_langauges()

            # 번역 결과를 가져와서 전역 변수에 저장
            translated_text = translate_and_store(input_text, source_language, target_langauge)
            print("요청 : trans_button")

            # return render_template("index.html", input_text=input_text, translated_txt=translated_text)

        elif 'print_button' in request.form:
            translated_text = request.form['output_text']
            print('번역된 언어 :', translated_text, '번역 시작 ~!')
            braille_translate(translated_text)
            print("Braille_Print 버튼이 클릭되었습니다.")

        # return render_template("index.html", input_text=input_text)

    # HTML에 전달
    print("요청 확인")
    return render_template("index.html",input_text=input_text,translated_txt=translated_text)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
