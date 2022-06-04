import azure.cognitiveservices.speech as speechsdk
import time
import re


def main():
    speech_config = speechsdk.SpeechConfig(
        subscription="f6389c46-fc08-4043-a77c-8fd23ba6a283", region="japanwest"
    )
    speech_config.speech_recognition_language = "ja-JP"

    # audioconfigの作成
    audio_filename = "filename"
    audio_input = speechsdk.AudioConfig(filename=audio_filename)

    # speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    # にするとマイク入力になります。その時はwhile文を別の手段で抜けられるようにしてください。
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, audio_config=audio_input
    )

    print("Recognizing first result...")

    # 設定の関数
    done = False

    def stop_cb(evt):
        print("CLOSING on {}".format(evt))
        nonlocal done
        done = True

    # 認識部分だけを取り出します。
    def split(evt):
        st = re.search(r"\".+?\"", str(evt))
        print(st.group(0).strip('"'))

    # 認識を行った時の設定
    speech_recognizer.recognized.connect(split)

    # 認識が終わる時の設定
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    # 処理前の時刻
    t1 = time.time()

    # 認識開始
    speech_recognizer.start_continuous_recognition()
    # 音声が終わるまでループを続けます
    while not done:
        time.sleep(0.5)
    # 認識終了
    speech_recognizer.stop_continuous_recognition()

    # 処理後の時刻
    t2 = time.time()
    # 経過時間を表示
    elapsed_time = t2 - t1
    print(f"経過時間：{elapsed_time}")
