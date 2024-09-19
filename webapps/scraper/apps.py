from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler

class ScraperConfig(AppConfig):
    name = 'scraper'

    def ready(self):
        from .tasks import scrape_data 
        scheduler = BackgroundScheduler()
        scheduler.add_job(scrape_data, 'interval', minutes=5)
        scheduler.start()
