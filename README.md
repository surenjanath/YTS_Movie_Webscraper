# YTS Movie Data Scraper and Database Importer

This Python script is designed to scrape movie data from the YTS website and store it in a SQLite database. The code leverages various libraries and technologies to achieve this, including asyncio, aiohttp for web scraping, SQLAlchemy for database management, and requests for API requests.


# Automated Status Update

GITHUB ACTION LAST RAN :
{{last_run_history}}
- 2023-11-06 23:31:48
- 2023-11-06 23:22:43
- 2023-11-07 03:18:34
- 2023-11-07 03:14:39


## Features

- **Web Scraping:** The script uses asynchronous web scraping with aiohttp to fetch movie data from the YTS website. It extracts movie details, including title, year, rating, runtime, and more.

- **Database Storage:** The scraped movie data is stored in a SQLite database. The code defines a database schema using SQLAlchemy and includes tables for movies, genres, and error logs. Movie-genre associations are handled through a many-to-many relationship.

- **Error Logging:** In case of errors during the scraping process, the code logs error information, including status, description, number of items processed, and the time taken.

## How to Use

1. Clone this repository or download the code to your local machine.

2. Install the required Python libraries by running `pip install aiohttp sqlalchemy request`.

3. Run the script by executing `python YTS_Movie Webscraper.py`. Make sure to set up the working directory and database location as needed.

4. The script will fetch movie data from the YTS website, process it, and store it in a SQLite database.

5. You can further customize the code to fit your specific needs, such as adjusting the batch size for database commits or modifying error handling.

## Dependencies

- [aiohttp](https://docs.aiohttp.org/en/stable/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [requests](https://docs.python-requests.org/en/latest/)

## License

This project is open-source and available under the [MIT License](LICENSE).


