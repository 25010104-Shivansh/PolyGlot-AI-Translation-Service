from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

# Language mapping
# Note: Haryanvi ('bgc') support is limited in free APIs. 
# We use Hindi ('hi') as a linguistic proxy or 'hi' if 'bgc' fails.
LANG_MAP = {
    'en': 'english',
    'hi': 'hindi',
    'pa': 'punjabi',
    'fr': 'french',
    'ru': 'russian',
    'bgc': 'hindi' # Fallback for Haryanvi in this demo
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.json
    text = data.get('text', '')
    source = data.get('source', 'auto')
    target = data.get('target', 'en')

    # Handle Haryanvi manual mapping if needed
    if source == 'bgc': source = 'hi' 
    if target == 'bgc': target = 'hi'

    try:
        translator = GoogleTranslator(source=source, target=target)
        translated_text = translator.translate(text)
        
        # Simulating Haryanvi nuance if target is Haryanvi (Basic rule-based replacement for demo)
        # In a real specific model, this would be a trained transformer.
        if data.get('target') == 'bgc':
            translated_text = translated_text.replace('है', 'सै').replace('मैं', 'मन्नै')

        return jsonify({'status': 'success', 'translation': translated_text})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)