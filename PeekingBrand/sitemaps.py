from django.contrib.sitemaps import Sitemap
from blogapp.models import Blog
from django.urls import reverse

class BlogSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Blog.objects.all().order_by('pub_date')

    def location(self, obj):
        return """/blogList/blogDetail/%s""" % obj.pk

    def lastmod(self, obj):
        return obj.pub_date


class StaticViewSitemap(Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return [
            'blogList',
        ]
    def location(self, item):
        return reverse(item)