import requests

headers = \
{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

for date in range(201, 172, -1): 
    url = 'https://www.todayhumor.co.kr/board/view.php?table=bestofbest&no=465{0}&s_no=465{0}&page=1'.format(date)
    site = requests.get(url, headers=headers)
    source_data = site.text

    count = source_data.count('<div class="upfile" id="upfile1"> ')

    for i in range(count):
          pos1 = source_data.find('<div class="upfile" id="upfile1"> ')+ len('<div class="upfile" id="upfile1"> ')
          source_data = source_data[pos1:]

          pos2 = source_data.find('</div>')
          a_data = source_data[: pos2].strip()

          source_data = source_data[pos2+1:]
          print(i+1, a_data)

