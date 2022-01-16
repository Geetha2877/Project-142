from flask import Flask, json,jsonify,request
from storage import liked_articles,unliked_articles,did_not_read_articles
import csv

app = Flask(__name__)

with open('articles.csv',encoding='utf8') as f:
    reader=csv.reader(f)
    data=list(reader)
    all_articles = data[1:]
    headers = data[0]

@app.route("/get-articles")
def get_articles():
    articles_data={
        "url": all_articles[0][11],
        "title": all_articles[0][12],
        "text": all_articles[0][13],
        "lang": all_articles[0][14],
        "total_events": all_articles[0][15]
    }
    return jsonify({
        "data":articles_data,
        "status":"success"
    })

@app.route("/liked-articles",methods=['POST'])
def like_articles():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status":"success"
    }),201

@app.route("/unliked-articles",methods=['POST'])
def unlike_articles():
    article = all_articles[0]
    unliked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status":"success"
    }),201

@app.route("/did-not-read-articles",methods=['POST'])
def yet_to_read_articles():
    article = all_articles[0]
    did_not_read_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status":"success"
    }),201

if __name__ == "__main__":
    app.run()