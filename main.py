from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask("SuperScrapper")
db = {} # fake database

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/report")
def report():
  # find word from url query arguments
  word = request.args.get('word')
  # check if searching word exists
  if word:
    word = word.lower() # make word lowercase
    # check if db has data of word
    if db.get(word):
      jobs = db.get(word) # get jobs from db
    else:
      jobs = get_jobs(word) # scrap jobs
      db[word] = jobs # save scrapped jobs to db
  else:
    return redirect("/")
  # render html
  return render_template("report.html", searchingBy=word, resultsNumber=len(jobs), jobs=jobs)
  
@app.route("/export")
def export():
  try: 
    word = request.args.get('word') # try to get word
    if not word: 
      raise Exception() # when word not exist throw error
    word = word.lower() # when word exist change to lowercase
    jobs = db.get(word) # get jobs from db
    if not jobs:
      raise Exception() # if db has no data throw error
    save_to_file(jobs) # if db jas, then save jobs to file
    return send_file("jobs.csv") # send file to user
  except:
    return redirect("/") # when error happens redirect to home
  
app.run(host:="0.0.0.0")