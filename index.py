from flask import Flask, jsonify
import utils

#khoi tao app
app = Flask(__name__)


#moi api tuong ung 3 phan
#(1) route: địa chỉ url của api
#(2) method: phương thức để tương tác với api( get, post,.)
#(3) hàm xử lý dữ liệu : dữ liệu gì được xử lý ntn trả cho client
# những kết quả gì
#api thu 0
@app.route("/categories", methods = ["GET"])
def get_category():
    rows = utils.get_all("SELECT * FROM category")
    data = []
    for r in rows:
        data.append({
            "id": r[0],
            "subject":r[1],
            "url": r[2]
        })
    return jsonify({"categories": data})

#api thu 1
@app.route("/news", methods = ["GET"])
def get_news():
    rows = utils.get_all("SELECT * FROM news")
    data = []
    for r in rows:
        data.append({
            "id": r[0],
            "subject":r[1],
            "description": r[2],
            "image": r[3],
            "original_url": r[5]
        })
    return jsonify({"news": data})
#api thu 2 lay thong tin cua 1 tin tuc
@app.route("/news/<int:news_id>", methods=["GET"])
def get_new_by_id(news_id):
    pass

#api thu 3
@app.route("/news/add", methods=["POST"])
def insert_news():
    pass

# viết api lay các bài báo về để add trong csdl của mình dùng lib newspaper3k
# thuw vieejn nafy trisch xuất thông tin các bài báo trên internet cho mình

#api thu 4
# tu dong them cac bai bao moi


if __name__ == "__main__":
    app.run()