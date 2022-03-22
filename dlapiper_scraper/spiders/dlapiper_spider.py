from scrapy.spiders import SitemapSpider
import scrapy
import os
class DlapiperSpider(SitemapSpider):
    name = 'dlapiper'
    sitemap_urls = ['https://www.dlapiper.com/sitemap.xml']
    sitemap_rules = [('/en/us/people', 'parse_people')]
    

    def parse_people(self, response):
        # vCard text in a href
        vcard_url = response.xpath('//a[contains(text(), "vCard")]/@href').extract()[0]
        url = response.urljoin(vcard_url)
        yield scrapy.Request(url, callback=self.save_vcard)

    def save_vcard(self, response):
        # save the vCard text
        # save the vCard text to a file
      
        path = response.url.split('/')[-2]
        self.logger.info('Saving vcard %s', path)
        filename = 'output/vcards/dlapiper/%s.vcf' % path
        
        with open(filename, 'wb') as f:
            f.write(response.body)