scrapy crawl liuyifei -o image.json -t json
>>> d = pq(url='http://www.w3.org/', parser='html')
>>> d('a[title="W3C Activities"]').attr('href')
'/Consortium/activities'
>>> d.make_links_absolute()
[<html>]
>>> d('a[title="W3C Activities"]').attr('href')
'http://www.w3.org/Consortium/activities'