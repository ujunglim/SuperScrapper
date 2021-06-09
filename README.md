# Super Scrapper
Scrap Stackoverflow by using `Python`, `Flask` to bring up the page to the development server.

![home](image/home.png)
## [Try at here👆](https://superscrapper.yujungjung1.repl.co/)
or here
https://replit.com/@yujungjung1/SuperScrapper#main.py

- [x] Stack Overflow Jobs Scrapping
- [x] Indeed Jobs Scrapping
- [x] Web Server
- [x] Search Feature
- [x] Export to CSV

---
Install Package 
- Flask
- Requests
- beatuifulSoup4

```python
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect, send_file
import csv
```

![report](image/report.png)





