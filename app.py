from flask import Flask, render_template, session, request, jsonify, redirect, url_for
import parser, colors

app = Flask(__name__)

@app.route('/')
def main():
    color_values = colors.randomize_colors()
    print 2
    data = parser.get_data('https://news.ycombinator.com/')
    return render_template('index.html', zipped=zip(data, color_values))

# View stock button
@app.route('/<page>')
def view_page(page):
    color_values = colors.randomize_colors()
    print page
    data = parser.get_data('https://news.ycombinator.com/')
    return render_template('index.html', data=data, colors=color_values)

if __name__ == '__main__':
    app.run(debug=True)