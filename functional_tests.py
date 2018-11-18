from selenium import webdriver

#设置浏览器参数，解决访问Google浏览器不安全访问被阻止的问题
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\RanJi')

#启动Google浏览器，注意要下载Google浏览器的驱动程序，放置在Path环境变量中
brower = webdriver.Chrome(chrome_options=options)
brower.get('http://localhost:8000')
assert 'Django' in brower.title
