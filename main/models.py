#!/usr/bin/env python
# encoding: utf-8

"""
Models for plivo.
"""

__author__ = 'confessin@gmail.com (Mohammad Rafi)'


from django.db import models


STATUS_CHOICES = (
    (1, 'Answered'),
    (2, 'Not answered'),
    (3, 'No ring'),
)


# Create your models here.
class CDR(models.Model):
  from_number = models.BigIntegerField(12)
  to_number = models.BigIntegerField(12)
  status = models.CharField(max_length=20, choices=STATUS_CHOICES)
  timestamp = models.DateTimeField()
  duration = models.IntegerField()

  def __unicode__(self):
    return '%s-%s' % (self.from_number, self.to_number)
