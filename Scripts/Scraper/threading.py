from Scripts.Scraper.scraper import Scraper
from threading import Thread


if __name__ == '__main__':
    obj1 = Scraper()
    obj2 = Scraper()

    t1 = Thread(obj1.main())
    t2 = Thread(obj2.main())

    t1.start()
    t2.start()
