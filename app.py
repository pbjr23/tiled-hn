from flask import Flask, render_template
import parser, colors

app = Flask(__name__)

@app.route('/')
@app.route('/<path>/')
def main(path=''):
    """Handles all routes for TiledHN app"""
    color_values = colors.randomize_colors()
    data, has_next = parser.get_data('https://news.ycombinator.com/' + path.replace(':', '?'))

    # Template looks slightly different for 'jobs' urls
    if 'jobs' in path:
        job_value = 1
    else:
        job_value = None

    return render_template('index.html', zipped=zip(data, color_values), jobs=job_value, next=has_next)

if __name__ == '__main__':
    app.run()