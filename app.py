from flask import Flask, render_template, session, request, jsonify, redirect, url_for
import parser, colors

app = Flask(__name__)

@app.route('/')
def main():
    color_values = colors.randomize_colors()
    data = parser.get_data('https://news.ycombinator.com/')
    return render_template('index.html', zipped=zip(data, color_values))

# View stock button
@app.route('/view/<page>/')
def view_page(page):
    print 2342343243234123234234234
    color_values = colors.randomize_colors()
    print 'https://news.ycombinator.com/' + page
    data = parser.get_data('https://news.ycombinator.com/' + page)
    return render_template('index.html', data=data, colors=color_values)

if __name__ == '__main__':
    app.run(debug=True)