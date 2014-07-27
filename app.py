from flask import Flask, render_template
import parser, colors

app = Flask(__name__)

@app.route('/')
def main():
    color_values = colors.randomize_colors()
    data, has_next = parser.get_data('https://news.ycombinator.com/')
    return render_template('index.html', zipped=zip(data, color_values), next=has_next)

@app.route('/jobs/')
def view_jobs():
    color_values = colors.randomize_colors()
    data, has_next = parser.get_data('https://news.ycombinator.com/jobs')
    return render_template('index.html', zipped=zip(data, color_values), jobs=1, next=has_next)

@app.route('/<path>/')
def view_page(path):
    color_values = colors.randomize_colors()
    data, has_next = parser.get_data('https://news.ycombinator.com/' + path.replace(':', '?'))
    return render_template('index.html', zipped=zip(data, color_values), next=has_next)

if __name__ == '__main__':
    app.run()