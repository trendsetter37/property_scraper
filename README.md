# Tax Sale Property Scraper
---

This repository serves as a tool to scrape tax sale property details.


## Getting started

1. Create a python environvment
1. install requirements
1. Configure awscli with dynamodb creds
1. Run tax sale spider

```
virtualenv -p python3 env
pip install -r requirements.txt
awscli configure
scrapy runspider property_scraper/spiders/tax_sale.py
```

Note: if you have not created the db table, use `utils/db.py` to do so.


