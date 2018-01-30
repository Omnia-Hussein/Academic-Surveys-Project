# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from builtins import object

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from future import standard_library

from Student.models import Student
from Survey.models import Survey

standard_library.install_aliases()


class Response(models.Model):
    """
    A Response object is a collection of questions and answers with a
    unique interview uuid.
    """

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    survey = models.ForeignKey(Survey, related_name="responses", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='responses', on_delete=models.CASCADE)

    class Meta(object):
        verbose_name = _('response')
        verbose_name_plural = _('responses')
        unique_together = (
            'survey',
            'student',
        )

    def __str__(self):
        msg = u"Response to {} by {}".format(self.survey, self.student.user)
        msg += u" on {}".format(self.creation_date)
        return msg
