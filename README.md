# 🎬 Movie Data Collector with Python

This project collects movie data using the public [OMDb](http://www.omdbapi.com/) API, and saves the results to a CSV file. The goal is to evolve this script into a more robust project with object orientation, automated testing, and graphical visualizations.

---

## 🚀 Features

- Collects movie data via the OMDb API
- Saves to a CSV file
- Basic error handling
- Automated testing framework with `pytest` and `unittest.mock`
- CI/CD-ready with GitHub Actions

---

## 📦 Requirements

- Python 3.10+
- Free OMDb API account (you will receive an `API_KEY`)

---

## 📁 Project Structure
pandas_movie_list/
│
├── main.py # Main script
├── filmes_coltados.csv # Collection result
├── requirements.txt # Project dependencies
├── .gitignore
├── README.md
│
├── tests/ # Automated tests
│ └── test_main.py
│
└── .github/workflows/
└── python-

---

## ⚙️ How to use

1. Clone the repository:
    git clone https://github.com/Tarsisnbs/pandas_movie_list.git
    cd pandas_movie_list

2. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # or `venv\Scripts\activate` in Windows

3. Install the dependencies:
    pip install -r requirements.txt

4. Configure your OMDb API key in the main.py file:
    API_KEY = "SUA_CHAVE_AQUI"

5. Run the script:
    python main.py

6. Executando os testes
    python -m unittest discover -s tests

🎯 Next steps
    -Refactoring with Object-Oriented Programming (OOP)
    -Visualizations with matplotlib and seaborn
    -Export in other formats (.xlsx, JSON)
    -Dashboard with Flask (in the future)
    -Data validation and more advanced testing

📌 License
MIT © Társis Natan Boff da Silva