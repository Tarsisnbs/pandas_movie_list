import unittest
from unittest.mock import patch
import pandas as pd
from main import fetch_data_omdb, plot_movies_to_year
import matplotlib.figure

class TestFetchDataOMDB(unittest.TestCase):
    @patch('main.requests.get')
    def test_fetch_data_omdb(self, mock_get):
       #Simulates OMDb API response for any title
       mock_get.return_value.json.return_value = {
            'Response': 'True',
            'Title': 'Inception',
            'Year': '2010',
            'Genre': 'Action, Sci-Fi',
            'Runtime': '148 min',
            'Director': 'Christopher Nolan',
            'imdbRating': '8.8'
       }

       movies = ['Inception']
       df = fetch_data_omdb(movies, api_key = 'fake_key')
       print(df)
       self.assertIsInstance(df, pd.DataFrame)
       self.assertEqual(len(df), 1)
       self.assertEqual(df.iloc[0]['Título'], 'Inception')
       self.assertEqual(df.iloc[0]['Diretor'], 'Christopher Nolan')

class TestPlot(unittest.TestCase):
    def test_plot_filmes_por_ano(self):
        dados = {
            "Ano": ["1999", "2000", "2000", "2001"],
            "Nota IMDb": ["8.7", "7.5", "8.0", "6.9"]
        }
        df = pd.DataFrame(dados)
        fig = plot_movies_to_year(df)
        assert isinstance(fig, matplotlib.figure.Figure)

if __name__ == '__main__':
    unittest.main()