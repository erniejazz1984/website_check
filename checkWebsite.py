import urllib2
import winsound
import time
import datetime
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
models = []

while (True):
    print "Checking the website current time",datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    response = urllib2.urlopen('http://outlet.us.dell.com/ARBOnlineSales/Online/InventorySearch.aspx?brandId=222806&c=us&cs=22&l=en&MODEL_DESC=ALL&s=dfh&~ck=mn&dgc=CJ&cid=287135&lid=5535540&acd=12309198377458490&ven1=12382062-1225267-07166094f60611e58c3b36b34f139fbd0INT&ven3=274203133803755706')
    html = response.read()
    for line in html.split("</td>"):
        if "fl-topalign fl-inv-img-col" in line:
            model =  line.split("title=")[-1].split("src")[0]
            if model not in models:
                print "!!!! New model", model
                models.append(model)
                winsound.Beep(2500,100)            
    time.sleep(5)           
