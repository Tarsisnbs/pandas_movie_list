import pandas as pd 
import requests
import matplotlib.pyplot as plt
import seaborn as sns


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

def save_csv(df, file_name):
    df.to_csv(file_name, index=False)
    print(f'Arquivo {file_name} criado com sucesso')

def plot_movies_to_year(df): 
    df['Ano'] = pd.to_numeric(df['Ano'], errors='coerce')
    df_filtered = df.dropna(subset=['Ano'])
    count = df_filtered['Ano'].value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=count.index, y=count.values, ax=ax, color='skyblue')
    ax.set_title('Quantidade de Filmes por Ano')
    ax.set_xlabel('Ano')
    ax.set_ylabel('Quantidade')
    ax.yaxis.get_major_locator().set_params(integer=True)
    ax.grid(axis='y', linestyle='--', alpha=0.6)
    fig.tight_layout()
    return fig

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
    save_csv(df, "filmes_coletados.csv")
    fig1 = plot_movies_to_year(df)
    fig1.savefig("filmes_por_ano.png")