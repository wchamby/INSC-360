# William Chase Hamby
# 2/2/20
# homework-5.py
# -*- coding: utf-8 -*-
# This is the description for homework 5

import csv
import datetime
import logging
logging.basicConfig(
    filename='log' + datetime.datetime.utcnow().strftime("%d%b%Y_%Hh%Mm") + '.log',
    format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO)


counter = 0
with open ('input-data.csv', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=",")
  next(reader)  # Python next() skips to the next line. So skipping the header row

  for row in reader:
    try:
      counter += 1  # keep track of how many records we have processed.
      sales_total = int(row[1]) + int(row[2]) + int(row[3])
      print("{} - Total first quarter sales for store {}: ${:,}".format(counter, row[0], sales_total))
      logging.info("Success in line {}".format(counter))
    except:
      print ("Surprise")
      logging.error("Unknown Error in line {}".format(counter))
