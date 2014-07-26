from flask import Flask, render_template, session, request, jsonify, redirect, url_for
import parser, colors

app = Flask(__name__)

@app.route('/')
def main():
    color_values = colors.randomize_colors()
    data, next = parser.get_data('https://news.ycombinator.com/')
    return render_template('index.html', zipped=zip(data, color_values), next=next)


@app.route('/jobs/')
def view_jobs():
    color_values = colors.randomize_colors()
    data, next = parser.get_data('https://news.ycombinator.com/jobs')
    return render_template('index.html', zipped=zip(data, color_values), jobs=1, next=next)

@app.route('/<page>/')
def view_page(page):
    color_values = colors.randomize_colors()
    data, next = parser.get_data('https://news.ycombinator.com/' + page)
    return render_template('index.html', zipped=zip(data, color_values), next=next)

if __name__ == '__main__':
    app.run(debug=True)