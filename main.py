import pandas as pd 
import requests

API_KEY = "f1515222"

def fetch_data_omdb(movies, api_key):
    movies_data = []

    for title in movies: 
        url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
        response = requests.get(url)
        data_js = response.json()

        if data_js['Response'] == 'True':
            movies_data.append({
                'Título' : data_js.get('Title'),
                'Ano' : data_js.get('Year'),
                'Gênero' : data_js.get('Genre'),
                'Duração' : data_js.get('Runtime'),
                'Diretor' : data_js.get('Director'),
                'Nota IMDB' : data_js.get('imdbRating')
            })
        else:
            print(f'Erro: {data_js['Error']} para o filme: {title}')
    
    return pd.DataFrame(movies_data)

def salvar_csv(df, file_name):
    df.to_csv(file_name, index=False)
    print(f'Arquivo {file_name} criado com sucesso')

if __name__ == '__main__':
    filmes = [
        "The Matrix",
        "Inception",
        "The Godfather",
        "Interstellar",
        "Pulp Fiction",
        "The Dark Knight",
        "Forrest Gump"
    ]


    df = fetch_data_omdb(filmes, API_KEY)
    df.to_csv("filmes_coletados.csv", index=False)
    print("Arquivo CSV criado com sucesso!")