import scrapy

def date_returner(month):
	if (month==2):
		return 28
	elif (month<=7 and month%2!=0):
		return 31
	elif (month>7 and month%2==0):
		return 31
	else:
		return 30

class HinduSpider(scrapy.Spider):
	name = 'hinduscrapper2010'

	successful = 0;
	article_no = 0;
	def start_requests(self):
		base_url = 'http://www.thehindu.com/archive/'
		parts = ['print/','web/']

		for pub in parts:
			url = base_url+pub			
			for year in xrange(2010,2011):
				for month in xrange(1,13):
					if (pub=='web/' and month<=7):
						continue
					for day in xrange(1,date_returner(month)+1):
						if (pub=='web/' and month==8 and day<15):
							continue
						if (day<10):
							day_s = '0'+str(day)+'/'
						else:
							day_s = str(day)+'/'
						if (month<10):
							month_s = '0'+str(month)+'/'
						else:
							month_s = str(month)+'/'
						final_url = url+str(year)+'/'+month_s+day_s
						print final_url
						try:
							yield scrapy.Request(url=final_url, callback=self.parse_page)
						except Exception as e:
							print "Error found while opening base pages: ",e

	def parse_page(self, response):
		#print response
		self.successful += 1
		#print self.successful
		urls = response.css('ul.archive-list a::attr(href)').extract()
		for url in urls:
			try:
				yield scrapy.Request(url=url, callback=self.parse_article)
			except Exception as e:
				print "Error while parsing article lists: ",e

	def parse_article(self, response):
		print response
		arr = response.css('div.article p::text').extract()
		arr = ' '.join(arr)
		if ('HIV' in arr or 'AIDS' in arr):
			with open('2010/hindu_article'+str(self.article_no)+'.txt','wb') as f:
				f.write(arr.encode('utf8'))
				self.article_no += 1
				f.closed