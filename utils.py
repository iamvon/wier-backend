import sqlite3
from newspaper import Article
import newspaper

# Phuong thuc 1 lay cac bai bao

def get_all(query):
    connect = sqlite3.connect("/home/binhnd/Downloads/shopee.db")
    data = connect.execute(query).fetchall()
    connect.close()

    return data
#cursor con chỏ
def get_news_by_id(news_id):
    connect = sqlite3.connect("data/newsdb.db")
    sql = """
    SELECT N.subject, N.decription, N.image, N.original_url, C.name, C.url 
    FROM news N INNER JOIN category C ON N.category_id = C.id WHERE id = ?
    """
    news = connect.execute(sql, (news_id,) ).fetchone()
    connect.close()

    return news
def add_news(connect, url, category_id):
# def add_news(connect):
    sql ="""
    INSERT INTO news(subject, description, image, original_url, category_id)
    VALUES (?, ?, ?, ?, ?)
    """
    article = Article(url)
    article.download()
    article.parse()
    connect.execute(sql, (article.title, article.text, article.top_image, article.url, category_id))
    # connect.excute(sql, ("tieu de","mo ta","link anh","https://url",3))
    connect.commit()

def get_news_url():
    cats = get_all("SELECT * FROM category")
    connect = sqlite3.connect("data/newsdb.db")
    for cat in cats:
        cat_id = cat[0]
        url = cat[2]
        cat_paper = newspaper.build(url)
        for article in cat_paper.articles:
            try:
                print("=== ", article.url)
                add_news(connect, article.url, cat_id)
            except Exception as ex:
                print("ERROR: "+ str(ex))
                pass
    connect.close()

# def test():
#     connect = sqlite3.connect("data/newsdb.db")
#     sql = """
#     INSERT INTO news(subject, description, image, original_url, category_id)
#     VALUES (?, ?, ?, ?, ?)
#     """
#     connect.execute(sql, ("tieu de","mo ta","anh","link",3))
#     connect.commit()
#     connect.close()

if __name__ == "__main__":
    print(get_all("SELECT * FROM categories"""))
    # get_news_url()
    # test_add_news()
    # test()