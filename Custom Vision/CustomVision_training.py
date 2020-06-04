# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# 説明：CUSTOM VISIONの予測AIに学習データを登録してIterationを作成します
# 参考資料
# https://docs.microsoft.com/ja-jp/azure/cognitive-services/custom-vision-service/quickstarts/image-classification?pivots=programming-language-python
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry
from msrest.authentication import ApiKeyCredentials

# 呼び出し先のAPIアクセスキーを指定して認証用クラスをインスタンス化する
training_credentials = ApiKeyCredentials(
    in_headers={
        "Training-key": "APIキー"
        }
    )

# 認証用クラスと呼び出し先のエンドポイントURLを指定して通信クラスをインスタンス化する
trainer = CustomVisionTrainingClient(
    "エンドポイントURL",
    training_credentials
    )

# プロジェクトIDをコンソールから入力してプロジェクトを呼び出し、プロジェクトに登録されているタグ名とタグIDを取得してコンソールに表示する
# メモ１：タグのIDをCustomVisionのプロジェクトサイトから確認できないため、APIを呼び出して取得する
project_ID = input("プロジェクトIDを入力してください >> ")
print("====プロジェクトに登録されているタグの一覧====")
for target_tag in trainer.get_tags(project_ID):
    print("Tag_ID: " + target_tag.id + ", Tag_Name: " + target_tag.name)
print("=========================================")

# 登録する画像のリストを格納する配列の変数を宣言する
image_list = []

# タグ付けされた登録用の画像データを作成する
# メモ２：複数のファイルを同時に登録したい場合は、Image_listに要素を追加するだけでOK
# メモ３：タグIDも複数設定できる（ソースコードが複雑になるので、今回は一つしか登録できない）
image_list.append(
    ImageFileCreateEntry(
        name=input("CustomVisionに登録する画像のファイル名を入力してください >> "),
        contents=open(input("CustomVisionに登録する画像のファイルパスを入力してください >> "), mode="rb").read(),
        tag_ids=[input("画像に紐付けるタグのIDを入力してください >> ")]
    )
)

# プロジェクトIDを指定して、画像データをCustomVisionに登録する
upload_result = trainer.create_images_from_files(project_ID, images=image_list)

# 登録が成功した場合、新しいIterationを作成する
if upload_result:
    iteration = trainer.train_project(project_ID)