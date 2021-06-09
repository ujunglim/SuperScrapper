import csv

def save_to_file(jobs):
  # open file
  file = open("jobs.csv", mode="w")
  # write to file
  writer = csv.writer(file)
  writer.writerow(["Title", "Company", "Location", "Link"])
  for job in jobs:
    writer.writerow(list(job.values()))
  return