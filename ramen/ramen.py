from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def Gourmet_Search(prefecture):
    #グルメサーチAPIのリクエストURL
    URL = 'https://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

    # グルメサーチAPIキーを設定
    API_KEY = '9ea3a92bc7fd9068'

    # グルメサーチAPIのパラメータ
    params = {
        'key': API_KEY,
        'keyword': 'ラーメン',
        'count': 5,
        'format': 'json',
        'address': prefecture
    }

    res = requests.get(URL, params)

    result = res.json()

    items = result['results']['shop']

    return items

@app.route("/", methods=['POST', 'GET'])
def index():
    prefectures = ['北海道', '青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県', '茨城県', '栃木県', '群馬県', '埼玉県', '千葉県', '東京都', '神奈川県', '新潟県', '富山県', '石川県', '福井県', '山梨県', '長野県', '奈良県', '和歌山県', '鳥取県', '島根県', '岡山県', '広島県', '山口県', '徳島県', '香川県', '愛媛県', '高知県', '福岡県', '佐賀県', '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県', '沖縄県']

    if request.method == "POST":
        prefecture = request.form.get("prefecture")
        searchs = Gourmet_Search(prefecture)
        return render_template("result.html", searchs=searchs, prefectures=prefectures)
    else:
        return render_template("base.html", prefectures=prefectures)

if __name__ == '__main__':
    app.run(debug=True)






