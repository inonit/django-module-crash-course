# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.test import TestCase


class DeepThoughtTestCase(TestCase):

    def test_deepthought_view(self):
        response = self.client.get(reverse("django_foobar_deepthought"))
        self.assertEqual(response.content, b"42")
