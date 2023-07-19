from config.celery import app


from news.management.commands.parse_news import main


@app.task
def parsing():
    main()