#!/usr/bin/env python
# encoding: utf-8

"""
Management commmand for adding CDR data.
"""

__author__ = 'confessin@gmail.com (Mohammad Rafi)'


import random
from datetime import timedelta, datetime
from django.core.management.base import BaseCommand
from main.models import CDR, STATUS_CHOICES

MIN = 000000000000
MAX = 999999999999
START_DATE = datetime.strptime('09/01/2012 12:01 AM', '%m/%d/%Y %I:%M %p')
END_DATE = datetime.strptime('09/30/2012 11:59 PM', '%m/%d/%Y %I:%M %p')


class Command(BaseCommand):

  def handle(self, *args, **options):
    print 'starting'
    cdr_rows = []
    for i in range(20000000):
      # creating 1000 at a time
      if i % 1000 == 0:
        CDR.objects.bulk_create(cdr_rows)
        cdr_rows = []
        print '%s rows done' % i
      if i <= 2000000:
        status = STATUS_CHOICES[2][0]
      elif 2000000 < i < 5000000:
        status = STATUS_CHOICES[1][0]
      else:
        status = STATUS_CHOICES[0][0]
      from_number = random.randint(MIN, MAX)
      to_number = random.randint(MIN, MAX)
      timestamp = self.random_date()
      if status == STATUS_CHOICES[0][0]:
        duration = random.randint(60, 3600)
      duration = 0
      cdr_rows.append(
          CDR(from_number=from_number, to_number=to_number, status=status,
              timestamp=timestamp, duration=duration))
    print len(CDR.objects.all())
    print 'done'

  def random_date(self, start=START_DATE, end=END_DATE):
    """
    returns a random datetime between two datetime objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return (start + timedelta(seconds=random_second))
