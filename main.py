import pandas as pd

from fastapi import FastAPI
import pandas as pd

app = FastAPI()

url = 'https://raw.githubusercontent.com/juliom86/apix/main/dataset_listo.csv'


@app.get('/get_count')
def get_count(plat: str, keyword: str):
    df = pd.read_csv(url)
    cant = df.loc[(df.title.str.contains(keyword)) & (df.plataforma==plat)]
    conteo = cant.shape[0]
    return f"En la plataforma {plat}, se menciona {conteo} la palabra {keyword}"


@app.get('/get_movies')
def get_movies(plat: str, puntaje: int, anio: int):
    df = pd.read_csv(url)
    cant = df.loc[(df.score > puntaje) & (df.plataforma== plat) & (df.release_year == anio)]
    conteo = cant.shape[0]
    return f"En la plataforma {plat}, tuvo {conteo} en {anio}, con un score mayor a {puntaje}"


@app.get('/second_best_movie')
def second_best_movie(plat: str, rating: int, tipo: str):
    df = pd.read_csv(url)
    seg = df.loc[(df.plataforma==plat) & (df.score == rating) & (df.type == tipo)]
    seg2 = seg.sort_values(['title', 'score'],ascending = [True, False])
    seg3 = seg2[['title', 'score']]
    lista = seg3.iloc[1].to_list()
    return f"En la plataforma {plat}, la segunda mejor pelicula {lista[0]} que tiene un rating de {lista[1]}"


@app.get('/movie_higher_duration')
def movie_higher_duration(plat: str, anio: int, dur: str):
    df = pd.read_csv(url)
    film = df.loc[(df.duration_type == dur) & (df.plataforma==plat) & (df.release_year == anio)]
    film2=film.sort_values(['duration_int'], ascending = [False])
    film3 = film2[['title', 'duration_int', 'duration_type']]
    lista=film3.iloc[0].to_list()
    return f"En la plataforma {plat}, la pelicula {lista[0]}, tuvo una duracion de {lista[1]} {lista[2]}, en {anio}"


@app.get('/contents')
def contents(rat):
    df = pd.read_csv(url)
    cant3 = df.loc[(df.rating == rat)]
    conteo = cant3.shape[0]
    return f"Con el rating {rat} se tiene un total de contenido de {conteo}"
