from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/download/oop-guide')
def download_pdf():
    return send_file("static/oop_guide.pdf", as_attachment=False)

if __name__ == "__main__":

	app.run(debug=True)
