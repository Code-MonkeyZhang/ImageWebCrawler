import urllib.request
import ssl

#全局解除证书认证
ssl._create_default_https_context = ssl._create_unverified_context
i=10
while i>0:
    response = urllib.request.urlopen("https://placekitten.com/200/286")
    # urlopen返回的response对象 可以读取
    cat_image = response.read()
    with open("cat_200_286.jpg","wb") as f:
        f.write(cat_image)
    # geturl() getinfo() getcode()
