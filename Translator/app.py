from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES

app = Flask(__name__, static_url_path='/static')

class TranslateClass(object):
    def __init__(self, words, language):
        self.words = words
        self.language = language
        self.translator = Translator(service_urls=["translate.google.com"])
        self.translation = None  

    def translate(self):
        if not self.words:
            self.translation = "Please enter a word or sentence."
        elif not self.language:
            self.translation = "Please select a language."
        else:
            try:
                self.translation = self.translator.translate(self.words, dest=self.language).text
            except ValueError as e:
                self.translation = f"Error translating: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = None  
    if request.method == 'POST':
        translate = request.form['translate']
        language = request.form['language']
        translator = TranslateClass(translate, language)
        translator.translate()
        translation = translator.translation  
        
    if request.method == 'GET':
        translation = None

    return render_template('index.html', translation=translation, languages=LANGUAGES)

if __name__ == '__main__':
    app.run(debug=True)
