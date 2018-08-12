# reference from Michelle J Levine who has kindly published her work on Github.

import psycopg2
import bleach

DBNAME = "news"


def most_popular_articles():

    query = """SELECT articles.title, count(log.path)
    FROM log, articles
    WHERE log.path LIKE concat('/article/%', articles.slug)
    GROUP BY articles.title
    ORDER by count(log.path) DESC
    LIMIT 3;
    """

    # Run Query
    db = psycopg2.connect('dbname=' + DBNAME)
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()

    # Print Results
    print('\nTOP THREE ARTICLES BY PAGE VIEWS:')
    count = 1
    for i in rows:
        print(str(count) + '. "' + i[0] + '" : ' + str(i[1]) + " views")
        count += 1


def most_popular_authors():
    query = """SELECT authors.name, count(log.path)
    FROM log, articles, authors
    WHERE log.path like concat('/article/%', articles.slug)
    AND authors.id = articles.author
    GROUP BY authors.name
    ORDER BY count(log.path) desc;
    """

    db = psycopg2.connect('dbname=' + DBNAME)
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()

    # Print Results
    print('\nTOP AUTHORS BY PAGE VIEWS:')
    count = 1
    for i in rows:
        print(str(count) + '. "' + i[0] + '" : ' + str(i[1]) + " views")
        count += 1


def most_error_days():
    query = """  SELECT total.day,
          ROUND(((errors.error_dates*1.0) / total.total_dates), 3) AS percent
        FROM (
          SELECT date_trunc('day', time) "day", count(*) AS error_dates
          FROM log
          WHERE status LIKE '404%'
          GROUP BY day
        ) AS errors,
        (
          SELECT date_trunc('day', time) "day", count(*) AS total_dates
          FROM log
          GROUP BY day
          ) AS total
        WHERE total.day = errors.day
        AND (ROUND(((errors.error_dates*1.0) / total.total_dates), 3) > 0.01)
        ORDER BY percent DESC;
    """

    db = psycopg2.connect('dbname=' + DBNAME)
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()

    # Print Results
    print('\nDAYS WITH MORE THAN 1''%'' ERROR:')
    for i in rows:
        date = i[0].strftime('%B %d, %Y')
        errors = str(round(i[1]*100, 1)) + "%" + " errors"
        print(date + " -- " + errors)


most_popular_articles()
most_popular_authors()
most_error_days()
