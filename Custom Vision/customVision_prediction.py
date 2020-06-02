# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# 説明：CUSTOM VISIONの学習データを呼び出して端末にある画像の予測値を取得します
# 参考資料
# https://docs.microsoft.com/ja-jp/azure/cognitive-services/custom-vision-service/quickstarts/image-classification?pivots=programming-language-python
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

# 呼び出し先のAPIアクセスキーを指定して認証用クラスをインスタンス化する
prediction_credentials = ApiKeyCredentials(
    in_headers={
        "Prediction-key": "APIキー"
        }
    )

# 認証用クラスと呼び出し先のエンドポイントURLを指定して通信クラスをインスタンス化する
predictor = CustomVisionPredictionClient(
    "エンドポイントURL", 
    prediction_credentials
    )

# 端末の画像を指定して呼び出しを実行する
# メモ１：引数の値に応じて取得できるデータを変更できる
# メモ２：戻り値は配列で返される（一つの写真に複数のタグが設定される可能性があるため）
results = predictor.classify_image(
    "プロジェクトのID（Project Settingsページの「Project Id」）", 
    "Iterationの名前（Performanceページのiteration選択時に表示される「Published as」の値）", 
    open("画像の保存先ファイルパス", "rb").read()
    )

# 取得した結果をコンソールに表示する
for prediction in results.predictions:
    print(prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))