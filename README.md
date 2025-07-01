# Calculator Flask App

This project is a simple calculator web application built with Flask, a lightweight Python web framework.

## Features

- Perform basic arithmetic operations: addition, subtraction, multiplication, and division
- Clean and user-friendly web interface
- Input validation and error handling

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/tojadamian/calc_flask.git
    cd calc_flask
    ```

2. (Optional) Create and activate a virtual environment:
    - ```PowerShell
        python -m venv venv
        .\venv\Scripts\Activate.ps1
        ```
    - ```Bash
        python -m venv venv
        source venv/bin/activate
        ```

3. Install dependencies (use the same shell as above):

    ```bash
    pip install flask
    ```

## Usage

To start the application, run:
```powershell
python app.py
```
or
```bash
python app.py
```

Then open your browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Project Structure

```
calc_flask/
├── app.py
├── templates/
│   └── calculator.html
├── static/
│   ├── style.css
│   └── script.js
└── README.md
```

## License

This project is licensed for educational purposes only.