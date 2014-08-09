from flask import Flask, render_template
import parser, colors

app = Flask(__name__)

@app.route('/')
@app.route('/<path>/')
def main(path=''):
    """Handles all routes for TiledHN app"""
    color_values = colors.randomize_colors()
    data, has_next = parser.get_data('https://news.ycombinator.com/' + path.replace(':', '?'))

    # Only one attribute to show
    if 'jobs' in path:
        flag = 1
    else:
        flag = None

    return render_template('index.html', zipped=zip(data, color_values), jobs=flag, next=has_next)

if __name__ == '__main__':
    app.run(debug=True)