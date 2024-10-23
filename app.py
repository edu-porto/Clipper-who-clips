from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store news in dictionaries for Companies and World
news_data = {"Companies": [], "World": []}

@app.route('/')
def index():
    return render_template('index.html', companies=news_data["Companies"], world=news_data["World"])

@app.route('/add_news', methods=['POST'])
def add_news():
    category = request.form.get('category')
    title = request.form.get('title')
    link = request.form.get('link')
    news_body = request.form.get('news_body')
    
    # Add the news item to the appropriate category
    if category in news_data:
        news_data[category].append({"title": title, "link": link, "news_body": news_body})
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
