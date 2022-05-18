import site
import trafilatura
from trafilatura import sitemaps

homepage= 'https://en.wikipedia.org/wiki/Hrithik_Roshan'
links = sitemaps.sitemap_search('sitemap.xml')
links