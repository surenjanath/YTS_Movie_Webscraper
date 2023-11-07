import asyncio
from time import perf_counter
import os
import datetime
from uuid import uuid4
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# External Libraries

# import pandas as pd
import aiohttp
import requests

# SQL DATABASE Libraries
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime, Date, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship, declarative_base


cwd = os.getcwd()
Database_Name = 'YTS_Movies.db'

Location = r'ScrapedData'
WorkingDir = os.path.join(cwd, Location)

if os.path.isdir(WorkingDir) :
    pass
else:
    os.mkdir(WorkingDir)

Database = os.path.join(WorkingDir,  Database_Name)

# # Initialize Method
Base = declarative_base()

# Export Database
db_path        = Database

# Define the many-to-many relationship table between Movie and Genre
movie_genre_association = Table('movie_genre_association', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.movie_id')),
    Column('genre_id', Integer, ForeignKey('genres.genre_id'))
)

class Movie(Base):
    __tablename__ = 'movies'

    movie_id = Column(Integer, primary_key=True)
    url = Column(String)
    imdb_code = Column(String)
    title = Column(String)
    title_english = Column(String)
    title_long = Column(String)
    slug = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    runtime = Column(Integer)
    summary = Column(Text)
    description_full = Column(Text)
    synopsis = Column(Text)
    yt_trailer_code = Column(String)
    language = Column(String)
    mpa_rating = Column(String)
    background_image_original = Column(String)
    state = Column(String)
    date_uploaded = Column(DateTime)

    # Utility Variables
    uniqueId = Column(String)
    date_created = Column(Date)
    last_updated = Column(Date)

    genres = relationship("Genre", secondary=movie_genre_association, back_populates="movies")

    def __init__(self, movie_id,  url, imdb_code, title, title_english, title_long, slug, year, rating, runtime, summary, description_full, synopsis, yt_trailer_code, language, mpa_rating, background_image_original, state, date_uploaded):
        self.movie_id = movie_id
        self.url = url
        self.imdb_code = imdb_code
        self.title = title
        self.title_english = title_english
        self.title_long = title_long
        self.slug = slug
        self.year = year
        self.rating = rating
        self.runtime = runtime
        self.summary = summary
        self.description_full = description_full
        self.synopsis = synopsis
        self.yt_trailer_code = yt_trailer_code
        self.language = language
        self.mpa_rating = mpa_rating
        self.background_image_original = background_image_original
        self.state = state
        self.date_uploaded = date_uploaded

        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
        if self.date_created is None:
            self.date_created = datetime.datetime.now()

        self.last_updated = datetime.datetime.now()

    def __repr__(self):
        return f"<Movie(imdb_code='{self.imdb_code}'>"

class Genre(Base):
    __tablename__ = 'genres'

    genre_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    # Establish the many-to-many relationship with Movie
    movies = relationship("Movie", secondary=movie_genre_association, back_populates="genres")

    def __init__(self, name):
        self.name = name

class ErrorLog(Base):
    __tablename__  = 'errorLog'
    id             = Column(Integer, primary_key=True)
    Status         = Column(String)
    Error          = Column(String)
    RunDate        = Column(DateTime)
    NumItems       = Column(Integer)
    TimeTaken      = Column(Float)

    # Utility Variable
    uniqueId = Column(String)
    date_created = Column(Date)
    last_updated = Column(Date)

    def __init__(self, Status, Error,NumItems, TimeTaken):
        self.Status     = Status
        self.Error      = Error
        self.NumItems   = NumItems
        self.TimeTaken  = TimeTaken

        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
        if self.date_created is None:
            self.date_created = datetime.datetime.now()

        self.last_updated = datetime.datetime.now()
        self.RunDate = datetime.datetime.now()

    def __repr__(self):
        return f"<ErrorLog(RunDate='{self.RunDate}')>"

############################################
#               FUNCTIONS
############################################

def add_movies_to_db(session, movie_data, batch):
    for counter, data in enumerate(movie_data):
        movie_id = data['id']

        # Check if a movie with the same imdb_code already exists in the database
        existing_movie = session.query(Movie).filter_by(movie_id=movie_id).first()
        if existing_movie:
        #     # Movie with the same imdb_code already exists, so skip adding it
        #     print(f'Movie with imdb_code {movie_id} already exists. Skipping.')
            pass
        else:
            try:
                movie_id = data['id']
                url = data['url']
                imdb_code = data['imdb_code']
                title = data['title']
                title_english = data['title_english']
                title_long = data['title_long']
                slug = data['slug']
                year = data['year']
                rating = data['rating']
                runtime = data['runtime']
                summary = data['summary']
                description_full = data['description_full']
                synopsis = data['synopsis']
                yt_trailer_code = data['yt_trailer_code']
                language = data['language']
                mpa_rating = data['mpa_rating']
                background_image_original = data['background_image_original']
                state = data['state']

                try:
                    date_uploaded_str = data['date_uploaded']  # Date in string format
                    date_uploaded = datetime.datetime.strptime(date_uploaded_str, '%Y-%m-%d %H:%M:%S')  # Convert to datetime
                except KeyError:
                    date_uploaded = datetime.date(1990,1,1)



                movie = Movie(
                    movie_id=movie_id,
                    url=url,
                    imdb_code=imdb_code,
                    title=title,
                    title_english=title_english,
                    title_long=title_long,
                    slug=slug,
                    year=year,
                    rating=rating,
                    runtime=runtime,
                    summary=summary,
                    description_full=description_full,
                    synopsis=synopsis,
                    yt_trailer_code=yt_trailer_code,
                    language=language,
                    mpa_rating=mpa_rating,
                    background_image_original=background_image_original,
                    state=state,
                    date_uploaded=date_uploaded,
                )
                try:
                    genres = data['genres']
                except :
                    genres = ['None']

                session.add(movie)

                for genre_name in genres:
                    # Check if the genre already exists in the database
                    genre = session.query(Genre).filter_by(name=genre_name).first()
                    if not genre:
                        genre = Genre(name=genre_name)

                    movie.genres.append(genre)



                if (counter + 1) % batch == 0:
                    print('*' * 50)
                    print(f'[*] Batch Committing : {counter}/{len(movie_data)}')
                    session.commit()

            except Exception as e:
                print('[*] Error:', e)


    session.commit()
    print('*' * 50)
    print(f'[*] Batch Completed : {counter}/{len(movie_data)}')

def add_to_ErrorLog(session, ERROR):
    ErrorLogging = [ErrorLog(**record) for record in ERROR]
    session.add_all(ErrorLogging)
    session.commit()
    return

class WebScraper(object):
    def __init__(self, urls):
        self.urls = urls
        # Global Place To Store The Data:
        self.all_data  = []
        self.ParsedData = []
        self.master_dict = {}
        # Run The Scraper:
        asyncio.run(self.main())

    async def fetch(self, session, url):

        try:
            async with session.get(url) as response:
                # 1. Extracting the Text:
                text = await response.json()
                # 2. Extracting the  Tag:
                movies = text['data']['movies']
                return text, url, movies
        except IndentationError as e:
            print(str(e))

    async def main(self):
        tasks = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            }
        async with aiohttp.ClientSession() as session:
            for url in self.urls:

                tasks.append(self.fetch(session, url))

            movie_data = await asyncio.gather(*tasks)
            self.all_data.extend(movie_data)

            # Storing the raw HTML data.
            for data in movie_data:

                if data is not None:
                    url = data[1]
                    self.master_dict['data'] = {'Raw Html': data[0], 'Results': data[2]}
                    self.ParsedData.extend(data[2])
                else:
                    continue

############################################
#               MAIN
############################################
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
try :
    start = perf_counter()
    r = requests.get('https://yts.mx/api/v2/list_movies.json?limit=50&page=1')
    if r.status_code == 200:
        totalNumber = r.json()["data"]["movie_count"]
        pages = range(1,int(totalNumber/50))
        amt = 50


        engine = create_engine(f'sqlite:///{Database}',  echo=False) # Echo = True means that it shows the logs
        Base.metadata.create_all(engine)

        # # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()

        try:

            datenow = datetime.datetime.now().ctime().replace(" ",'').replace(':','')
            urls = [f'https://yts.mx/api/v2/list_movies.json?limit={amt}&page={page}' for page in pages]
            scraper = WebScraper(urls = urls)
            stop = perf_counter()
            print("[*] Time taken : ", stop - start)

            print('[*] Length of Data Gathered : ', len(scraper.ParsedData))
            ExportPath = os.path.join(os.getcwd(),'Results')
            # if os.path.isdir(ExportPath) == False :
            #     os.mkdir(ExportPath)
            # EXPORTPATH = os.path.join(ExportPath, f'{datenow}_Data.xlsx')

            if len(scraper.ParsedData) > 0:
                print("*"*50)
                print("Adding Data to Database")
                print("*"*50)
                add_movies_to_db(session = session, movie_data = scraper.ParsedData, batch = 15000)

                print('[*] PROGRAM ENDED')
                print('*'*50)
                # pd.DataFrame(scraper.ParsedData).to_excel(EXPORTPATH)
            add_to_ErrorLog(session, [{
                'Status' : 'Scraped Successfully',
                'Error' : 'No Errors',
                'NumItems' : len(scraper.ParsedData),
                'TimeTaken' : stop - start,
            }])
            session.close()

        except Exception as e:
            try:stop = perf_counter()
            except:stop = 0
            session.rollback()
            add_to_ErrorLog(session, [{
                'Status' : 'Scraped Failed',
                'Error' : f'Error : {e}',
                'NumItems' : 0,
                'TimeTaken' : stop - start,
            }])

except Exception as e:
    print('*'*100)
    print(f'Error Occured : {e}')
    print('*'*100)