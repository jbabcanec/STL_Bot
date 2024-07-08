from flask import Flask, request, render_template
from nlp.processor import process_prompt
from model_generation.scad_executor import export_to_stl
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    scad_code, token_count = process_prompt(prompt)
    try:
        output_dir = 'outputs'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_file = os.path.join(output_dir, 'output.stl')
        export_to_stl(scad_code, output_file)
        
        return render_template('index.html', message="STL file generated and saved to outputs/output.stl.")
    except FileNotFoundError as e:
        return render_template('index.html', message=f"Error: {str(e)}. Make sure OpenSCAD is installed and added to your system's PATH.")

if __name__ == "__main__":
    app.run(debug=True)
