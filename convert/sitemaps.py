from django import http
from django.contrib import sitemaps
from django.urls import reverse


class StaticViewsSitemap(sitemaps.Sitemap):

    property = 0.5 
    changefreg = "daily"
    protocol = 'https'

    def items(self):
        return [
            'home',
            ]

    def location(self, items):
        return reverse(items)