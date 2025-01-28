# YTS Movie Data Scraper and Database Importer

This Python script is designed to scrape movie data from the YTS website and store it in a SQLite database. The code leverages various libraries and technologies to achieve this, including asyncio, aiohttp for web scraping, SQLAlchemy for database management, and requests for API requests.

# Youtube Video Showcase
Youtube Video Can be Found here : [https://youtu.be/7Wc_3Zv8AOY](https://youtu.be/7Wc_3Zv8AOY)

# Automated Status Update

GITHUB ACTION LAST RAN :
{{last_run_history}}
- 2025-01-27 22:10:43
- 2025-01-26 22:13:11
- 2025-01-25 22:13:31
- 2025-01-24 22:06:48
- 2025-01-23 22:11:31
- 2025-01-22 22:11:46
- 2025-01-21 22:13:25
- 2025-01-20 22:11:34
- 2025-01-19 22:12:59
- 2025-01-18 22:16:28
- 2025-01-17 22:07:29
- 2025-01-16 22:10:09
- 2025-01-15 22:10:23
- 2025-01-14 22:12:07
- 2025-01-13 22:10:07
- 2025-01-12 22:19:26
- 2025-01-11 22:22:02
- 2025-01-10 22:14:15
- 2025-01-09 22:17:22
- 2025-01-08 22:46:04
- 2025-01-07 22:14:26
- 2025-01-06 22:15:45
- 2025-01-05 22:19:20
- 2025-01-04 22:20:19
- 2025-01-03 22:11:47
- 2025-01-02 22:14:46
- 2025-01-01 22:13:32
- 2024-12-31 22:21:27
- 2024-12-30 22:13:56
- 2024-12-29 22:17:08
- 2024-12-28 22:21:04
- 2024-12-27 22:11:18
- 2024-12-26 22:14:14
- 2024-12-25 22:13:15
- 2024-12-24 22:13:14
- 2024-12-23 22:14:08
- 2024-12-22 22:17:02
- 2024-12-21 22:20:07
- 2024-12-20 22:12:52
- 2024-12-19 22:14:57
- 2024-12-18 22:21:01
- 2024-12-17 22:20:15
- 2024-12-16 22:24:54
- 2024-12-15 22:28:23
- 2024-12-14 22:37:41
- 2024-12-13 22:21:02
- 2024-12-12 22:26:24
- 2024-12-11 22:24:50
- 2024-12-10 22:25:00
- 2024-12-09 22:27:07
- 2024-12-08 22:28:06
- 2024-12-07 22:37:13
- 2024-12-06 22:22:53
- 2024-12-05 22:24:41
- 2024-12-04 22:25:36
- 2024-12-03 22:25:16
- 2024-12-02 22:25:05
- 2024-12-01 22:26:30
- 2024-11-30 22:44:40
- 2024-11-29 22:18:54
- 2024-11-28 22:23:00
- 2024-11-27 22:23:12
- 2024-11-26 22:23:34
- 2024-11-25 22:21:42
- 2024-11-24 22:22:47
- 2024-11-23 22:26:19
- 2024-11-22 22:16:36
- 2024-11-21 22:20:59
- 2024-11-20 22:19:47
- 2024-11-19 22:19:58
- 2024-11-18 22:20:37
- 2024-11-17 22:23:13
- 2024-11-16 22:24:03
- 2024-11-15 22:18:20
- 2024-11-14 22:20:58
- 2024-11-13 22:14:52
- 2024-11-12 22:13:55
- 2024-11-11 22:11:50
- 2024-11-10 22:15:19
- 2024-11-09 22:16:56
- 2024-11-08 22:09:22
- 2024-11-07 22:13:38
- 2024-11-06 22:13:32
- 2024-11-05 22:12:40
- 2024-11-04 22:13:06
- 2024-11-03 22:18:47
- 2024-11-02 22:20:31
- 2024-11-01 22:13:13
- 2024-10-31 22:23:10
- 2024-10-30 22:17:25
- 2024-10-29 22:16:26
- 2024-10-28 22:17:15
- 2024-10-27 22:19:44
- 2024-10-26 22:21:09
- 2024-10-25 22:12:02
- 2024-10-24 22:16:32
- 2024-10-23 22:14:59
- 2024-10-22 22:14:59
- 2024-10-21 22:16:11
- 2024-10-20 22:17:59
- 2024-10-19 22:21:38
- 2024-10-18 22:13:26
- 2024-10-17 22:15:58
- 2024-10-16 22:15:14
- 2024-10-15 22:17:14
- 2024-10-14 22:16:37
- 2024-10-13 22:17:49
- 2024-10-12 22:19:31
- 2024-10-11 22:11:42
- 2024-10-10 22:14:04
- 2024-10-09 22:14:42
- 2024-10-08 22:14:12
- 2024-10-07 22:18:02
- 2024-10-06 22:17:56
- 2024-10-05 22:20:21
- 2024-10-04 22:13:00
- 2024-10-03 22:15:07
- 2024-10-02 22:15:13
- 2024-10-01 22:14:24
- 2024-09-30 22:23:18
- 2024-09-29 22:19:51
- 2024-09-28 22:20:44
- 2024-09-27 22:13:16
- 2024-09-26 22:15:04
- 2024-09-25 22:14:11
- 2024-09-24 22:16:08
- 2024-09-23 22:15:22
- 2024-09-22 22:14:44
- 2024-09-21 22:19:10
- 2024-09-20 22:09:31
- 2024-09-19 22:11:59
- 2024-09-18 22:12:01
- 2024-09-17 22:09:56
- 2024-09-16 21:50:34
- 2024-09-15 22:18:04
- 2024-09-14 22:18:19
- 2024-09-13 22:08:32
- 2024-09-12 22:10:20
- 2024-09-11 22:09:22
- 2024-09-10 22:09:25
- 2024-09-09 22:10:05
- 2024-09-08 22:12:10
- 2024-09-07 22:14:08
- 2024-09-06 22:06:32
- 2024-09-05 22:08:54
- 2024-09-04 22:08:40
- 2024-09-03 22:08:19
- 2024-09-02 22:07:18
- 2024-09-01 22:09:31
- 2024-08-31 22:20:13
- 2024-08-30 22:07:05
- 2024-08-29 22:08:14
- 2024-08-28 22:07:30
- 2024-08-27 22:06:30
- 2024-08-26 22:05:34
- 2024-08-25 22:04:55
- 2024-08-24 22:09:08
- 2024-08-23 22:03:07
- 2024-08-22 22:03:41
- 2024-08-21 22:05:06
- 2024-08-20 22:03:02
- 2024-08-19 22:02:46
- 2024-08-18 22:05:12
- 2024-08-17 22:06:26
- 2024-08-16 22:00:23
- 2024-08-15 22:03:08
- 2024-08-14 21:56:24
- 2024-08-13 22:03:42
- 2024-08-12 22:04:56
- 2024-08-11 22:05:46
- 2024-08-10 22:08:31
- 2024-08-09 22:03:35
- 2024-08-08 22:04:10
- 2024-08-07 22:03:11
- 2024-08-06 22:04:14
- 2024-08-05 22:02:07
- 2024-08-04 22:04:11
- 2024-08-03 22:06:26
- 2024-08-02 21:59:52
- 2024-08-01 22:01:57
- 2024-07-31 22:08:12
- 2024-07-30 21:39:12
- 2024-07-29 22:01:52
- 2024-07-28 22:04:10
- 2024-07-27 22:06:03
- 2024-07-26 21:59:04
- 2024-07-25 22:00:56
- 2024-07-24 22:01:26
- 2024-07-23 22:05:31
- 2024-07-22 22:01:40
- 2024-07-21 22:05:24
- 2024-07-20 22:05:16
- 2024-07-19 21:58:18
- 2024-07-18 22:34:12
- 2024-07-17 22:00:21
- 2024-07-16 22:02:17
- 2024-07-15 22:02:14
- 2024-07-14 22:05:03
- 2024-07-13 22:07:57
- 2024-07-12 21:59:24
- 2024-07-11 21:59:32
- 2024-07-10 22:01:46
- 2024-07-09 22:00:31
- 2024-07-08 22:00:54
- 2024-07-07 22:01:44
- 2024-07-06 22:04:59
- 2024-07-05 21:56:10
- 2024-07-04 21:58:19
- 2024-07-03 21:59:24
- 2024-07-02 21:58:25
- 2024-07-01 21:59:44
- 2024-06-30 22:07:06
- 2024-06-29 22:04:29
- 2024-06-28 21:56:34
- 2024-06-27 21:58:53
- 2024-06-26 21:58:19
- 2024-06-25 21:57:58
- 2024-06-24 21:58:29
- 2024-06-23 21:59:57
- 2024-06-22 22:01:52
- 2024-06-21 21:55:25
- 2024-06-20 21:56:51
- 2024-06-19 21:56:09
- 2024-06-18 21:58:47
- 2024-06-17 21:58:20
- 2024-06-16 22:00:54
- 2024-06-15 22:03:15
- 2024-06-14 21:56:59
- 2024-06-13 21:57:43
- 2024-06-12 21:57:43
- 2024-06-11 21:58:26
- 2024-06-10 21:58:20
- 2024-06-09 22:00:24
- 2024-06-08 22:02:53
- 2024-06-07 21:56:03
- 2024-06-06 21:58:26
- 2024-06-05 21:56:33
- 2024-06-04 21:56:19
- 2024-06-03 21:56:35
- 2024-06-02 21:57:53
- 2024-06-01 21:59:51
- 2024-05-31 21:59:11
- 2024-05-30 21:56:09
- 2024-05-29 21:56:22
- 2024-05-28 22:01:23
- 2024-05-27 21:56:06
- 2024-05-26 21:56:02
- 2024-05-25 21:58:43
- 2024-05-24 21:52:25
- 2024-05-23 21:54:40
- 2024-05-22 21:53:39
- 2024-05-21 21:54:10
- 2024-05-20 21:53:24
- 2024-05-19 21:56:18
- 2024-05-18 21:57:24
- 2024-05-17 21:51:40
- 2024-05-16 21:52:59
- 2024-05-15 21:53:46
- 2024-05-14 21:56:28
- 2024-05-13 21:52:48
- 2024-05-12 21:55:37
- 2024-05-11 21:57:11
- 2024-05-10 21:50:24
- 2024-05-09 21:55:38
- 2024-05-08 21:55:06
- 2024-05-07 21:31:30
- 2024-05-06 21:53:48
- 2024-05-05 21:53:56
- 2024-05-04 21:54:52
- 2024-05-03 21:47:02
- 2024-05-02 21:53:24
- 2024-05-01 21:50:15
- 2024-04-30 21:55:48
- 2024-04-29 21:49:35
- 2024-04-28 21:52:16
- 2024-04-27 21:56:17
- 2024-04-26 21:45:55
- 2024-04-25 21:49:30
- 2024-04-24 21:51:27
- 2024-04-23 21:51:19
- 2024-04-22 21:50:53
- 2024-04-21 21:52:00
- 2024-04-20 21:53:36
- 2024-04-19 21:44:28
- 2024-04-18 21:47:55
- 2024-04-17 21:44:32
- 2024-04-16 21:45:48
- 2024-04-15 21:45:42
- 2024-04-14 23:47:24
- 2024-04-13 22:54:05
- 2024-04-12 21:30:19
- 2024-04-11 21:45:28
- 2024-04-10 21:47:54
- 2024-04-09 21:44:26
- 2024-04-08 21:44:40
- 2024-04-07 21:51:41
- 2024-04-06 21:52:16
- 2024-04-05 21:42:14
- 2024-04-04 21:44:27
- 2024-04-03 21:46:49
- 2024-04-02 21:48:09
- 2024-04-01 21:51:14
- 2024-03-31 21:56:20
- 2024-03-30 21:52:17
- 2024-03-29 21:40:09
- 2024-03-28 21:42:46
- 2024-03-27 21:43:30
- 2024-03-26 21:43:27
- 2024-03-25 21:43:07
- 2024-03-24 21:46:36
- 2024-03-23 21:52:52
- 2024-03-22 21:40:16
- 2024-03-21 21:42:12
- 2024-03-20 21:43:53
- 2024-03-19 21:42:12
- 2024-03-18 21:42:49
- 2024-03-17 21:43:15
- 2024-03-16 21:48:27
- 2024-03-15 21:40:34
- 2024-03-14 21:44:02
- 2024-03-13 21:53:42
- 2024-03-12 21:45:52
- 2024-03-11 21:42:08
- 2024-03-10 21:42:50
- 2024-03-09 21:49:41
- 2024-03-08 21:38:18
- 2024-03-07 21:41:58
- 2024-03-06 21:27:39
- 2024-03-05 21:42:17
- 2024-03-04 21:42:16
- 2024-03-03 21:59:38
- 2024-03-02 21:44:33
- 2024-03-01 21:40:14
- 2024-02-29 21:51:47
- 2024-02-28 21:41:17
- 2024-02-27 21:43:09
- 2024-02-26 21:41:15
- 2024-02-25 21:45:07
- 2024-02-24 21:48:25
- 2024-02-23 21:39:02
- 2024-02-22 21:41:42
- 2024-02-21 21:41:50
- 2024-02-20 21:43:01
- 2024-02-19 21:41:32
- 2024-02-18 21:44:20
- 2024-02-17 21:48:47
- 2024-02-16 21:41:08
- 2024-02-15 21:42:23
- 2024-02-14 21:43:01
- 2024-02-13 21:43:23
- 2024-02-12 21:42:48
- 2024-02-11 21:42:48
- 2024-02-10 21:49:33
- 2024-02-09 21:39:56
- 2024-02-08 21:41:27
- 2024-02-07 21:41:37
- 2024-02-06 21:41:20
- 2024-02-05 21:42:23
- 2024-02-04 21:49:30
- 2024-02-03 21:49:58
- 2024-02-02 21:40:05
- 2024-02-01 21:43:03
- 2024-01-31 21:50:20
- 2024-01-30 21:43:38
- 2024-01-29 21:42:58
- 2024-01-28 21:43:34
- 2024-01-27 21:49:52
- 2024-01-26 21:40:59
- 2024-01-25 21:46:06
- 2024-01-24 21:57:28
- 2024-01-23 21:56:25
- 2024-01-22 21:57:20
- 2024-01-21 21:59:17
- 2024-01-20 21:59:37
- 2024-01-19 21:53:08
- 2024-01-18 21:55:52
- 2024-01-17 21:54:24
- 2024-01-16 21:55:20
- 2024-01-15 21:54:55
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


