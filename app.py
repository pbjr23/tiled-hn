from flask import Flask, render_template
import scraper
import colors


app = Flask(__name__)

@app.route('/')
@app.route('/<path>/')
def main(path=''):
    """Handles all routes for TiledHN app"""
    color_values = colors.randomize_colors()
    data, has_next = scraper.get_data('https://news.ycombinator.com/' + path.replace(':', '?'))

    # Only one attribute to show
    flag = 'jobs' in path

    return render_template('index.html', zipped=list(zip(data, color_values)), flag=flag, next=has_next)

if __name__ == '__main__':
    app.run(debug=True)
