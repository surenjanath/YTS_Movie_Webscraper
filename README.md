# YTS Movie Data Scraper and Database Importer

This Python script is designed to scrape movie data from the YTS website and store it in a SQLite database. The code leverages various libraries and technologies to achieve this, including asyncio, aiohttp for web scraping, SQLAlchemy for database management, and requests for API requests.

# Youtube Video Showcase
Youtube Video Can be Found here : [https://youtu.be/7Wc_3Zv8AOY](https://youtu.be/7Wc_3Zv8AOY)

# Automated Status Update

GITHUB ACTION LAST RAN :
{{last_run_history}}
- 2024-01-14 21:59:21
- 2024-01-13 21:59:14
- 2024-01-12 21:53:13
- 2024-01-11 21:55:47
- 2024-01-10 21:55:25
- 2024-01-09 21:55:16
- 2024-01-08 21:55:11
- 2024-01-07 21:54:58
- 2024-01-06 21:58:49
- 2024-01-05 21:51:17
- 2024-01-04 21:53:17
- 2024-01-03 21:51:57
- 2024-01-02 21:52:22
- 2024-01-02 00:41:30
- 2024-01-02 00:39:29
- 2024-01-01 21:54:20
- 2023-12-31 21:59:38
- 2023-12-30 21:55:49
- 2023-12-29 21:46:12
- 2023-12-28 21:39:23
- 2023-12-27 21:49:07
- 2023-12-26 21:49:47
- 2023-12-25 21:48:52
- 2023-12-24 21:53:10
- 2023-12-23 21:55:34
- 2023-12-22 21:44:19
- 2023-12-21 21:50:56
- 2023-12-20 21:52:03
- 2023-12-19 21:31:41
- 2023-12-18 21:53:25
- 2023-12-17 21:54:06
- 2023-12-16 21:57:29
- 2023-12-15 21:51:35
- 2023-12-14 21:54:40
- 2023-12-13 21:52:43
- 2023-12-12 21:54:42
- 2023-12-11 21:54:57
- 2023-12-10 21:54:41
- 2023-12-09 21:57:14
- 2023-12-08 21:51:39
- 2023-12-07 21:55:02
- 2023-12-06 21:54:16
- 2023-12-05 21:54:14
- 2023-12-04 21:54:32
- 2023-12-03 21:54:11
- 2023-12-02 21:55:49
- 2023-12-01 21:47:06
- 2023-11-30 21:59:53
- 2023-11-29 21:53:34
- 2023-11-28 21:53:51
- 2023-11-27 21:54:17
- 2023-11-26 21:53:13
- 2023-11-25 21:55:37
- 2023-11-24 21:47:19
- 2023-11-23 21:51:07
- 2023-11-22 21:52:56
- 2023-11-21 21:55:46
- 2023-11-20 21:57:24
- 2023-11-19 21:54:21
- 2023-11-18 21:56:53
- 2023-11-17 21:51:55
- 2023-11-16 21:53:25
- 2023-11-15 21:53:39
- 2023-11-14 21:53:29
- 2023-11-13 21:50:21
- 2023-11-12 21:52:14
- 2023-11-11 21:53:59
- 2023-11-10 21:44:28
- 2023-11-09 21:50:08
- 2023-11-08 21:50:06
- 2023-11-07 21:49:06
- 2023-11-07 00:08:44
- 2023-11-06 23:39:22
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


