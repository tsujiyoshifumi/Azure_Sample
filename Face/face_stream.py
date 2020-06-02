# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# 説明：端末にある画像を参照してFaceAPIを呼び出します
# 参考資料
# https://docs.microsoft.com/ja-jp/azure/cognitive-services/face/quickstarts/python-sdk
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

# 呼び出し先のエンドポイントURLとAPIアクセスキーを指定して通信クラスをインスタンス化する
face_client = FaceClient(
    "エンドポイントURL",
    CognitiveServicesCredentials("APIキー")
    )

# 端末の画像を指定して呼び出しを実行する
# メモ１：引数の値に応じて取得できるデータを変更できる
# メモ２：戻り値は配列で返される（一つの写真に複数の顔がある可能性があるため）
detect_faces = face_client.face.detect_with_stream(
    open("画像の保存先ファイルパス", mode="rb"),
    return_face_attributes=["emotion"]
    )