
# STL Generator with OpenAI and Flask

This project is a Flask-based web application that generates 3D models (STL files) from user prompts using OpenAI's GPT-4 to generate OpenSCAD code. The STL files are saved in an `outputs` directory.

## Features
- Input prompts to generate OpenSCAD code.
- Convert OpenSCAD code to STL files.
- Save generated files in an `outputs` directory.
- Display success messages and clear the input field for new prompts.

## Requirements
- Python 3.x
- Flask
- OpenAI Python client
- OpenSCAD
- Git Bash (for Windows users)
- MeshLab (optional, not used in this setup)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/stl-generator.git
cd stl-generator`` 
```

### 2. Set Up Virtual Environment

`python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate` 

### 3. Install Dependencies

`pip install -r requirements.txt` 

### 4. Set Up OpenAI API Key

-   Create a file named `credentials.txt` in the parent directory of the project (one level above the cloned directory).
-   Add your OpenAI API key to the `credentials.txt` file.

Example:
`your_openai_api_key` 

### 5. Ensure OpenSCAD is Installed

-   Download and install OpenSCAD from OpenSCAD Downloads.
-   Ensure OpenSCAD is in your system's PATH. You can add it to the PATH in Git Bash by editing your `.bashrc` or `.bash_profile` file:

`export PATH=$PATH:"/c/Program Files/OpenSCAD"
source ~/.bashrc  # Or source ~/.bash_profile` 

## Project Structure

.
├── app.py
├── nlp
│   ├── __init__.py
│   └── processor.py
├── model_generation
│   ├── __init__.py
│   ├── scad_executor.py
├── templates
│   └── index.html
├── static
│   └── style.css
├── utils
│   ├── __init__.py
│   └── logger.py
├── requirements.txt
└── credentials.txt  # This file should be in the parent directory


## Usage

### Running the Application

`python app.py` 

### Accessing the Web Interface

-   Open a web browser and navigate to `http://127.0.0.1:5000/`.

### Submitting a Prompt

-   Enter a prompt such as "Create a cube with a size of 10 units" and submit.
-   A popup will appear indicating success, and the input field will be cleared for new input.
-   The generated OpenSCAD file and STL file will be saved in the `outputs` directory.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
