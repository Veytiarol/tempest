# -*- coding: utf-8 -*-

'''
    Incursion Add-on
    Copyright (C) 2016 Incursion

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import requests
import sys
import re
from bs4 import BeautifulSoup


class source:
    def __init__(self):
        self.priority = 0
        self.language = ['en']
        self.domain = 'soaptv.me'
        self.base_link = 'https://soaptv.me'
        self.search_link = 'https://soaptv.me/index.php?do=search'
        self.headers = {'referer':'https://soaptv.me'}

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = tvshowtitle
            return url
        except:
            return ""

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        with requests.Session() as s:
            try:
                sources = []
                data = {'do':'search','subaction':'search','story':(url + " season " + season),'all_word_search':'1'}
                p = s.post(self.search_link, data=data)
                soup = BeautifulSoup(p.text,'html.parser')
                p = soup.find_all('h2', {'class':'dtitle'})
                for i in p:
                    if re.sub(r'\W+', '', i.text.split('(')[0].lower()) == \
                            re.sub(r'\W+', '',((url + " season " + season).lower())):
                        p = (i.find_all('a')[0]['href'])
                p = s.get(p)
                soup = BeautifulSoup(p.text, 'html.parser')
                soup = soup.find_all('div', {'class':'fff6'})[0].find_all('a')
                if len(episode) == 1:
                    episode = "0"+episode

                for i in soup:
                    if ("e" + episode).lower() in i.text.lower():
                        url = (i['href'])
                p = s.get(url, headers = self.headers)
                sources.append(
                    {'source': 'depfile.us', 'quality': 'HD', 'language': 'en', 'url': p.url, 'direct': False, 'debridonly': True})
                return sources
            except:
                return ""

    def sources(self, url, hostDict, hostprDict):
        return url

    def resolve(self, url):
            return url
