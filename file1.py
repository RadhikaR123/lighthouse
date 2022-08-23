from encodings import utf_8
import json
import os
import pandas as pd
from datetime import datetime

df = pd.DataFrame([], columns=['URL','SEO','Accessibility','Performance','Best Practices'])
name = "BestViewsReviews"
getdate = datetime.now().strftime("%m-%d-%y")

urls = ["https://bestviewsreviews.com/"]

for url in urls:    
    stream = os.popen(r'lighthouse --quiet --no-update-notifier --no-enable-error-reporting --output=json --output-path=C:\Users\radhi\Desktop\lighthouseLink2' +name+'_'+getdate+'.report.json --chrome-flags="--headless " ' + url)

# time.sleep(120)
print("Report complete for: " + url)

json_filename = r'C:\Users\radhi\Desktop\lighthouseLink2' + name + '_' + getdate + '.report.json'
with open(json_filename, encoding= "utf_8") as json_data:
    loaded_json = json.load(json_data)
# print(loaded_json)

seo = str(round(loaded_json["categories"]["seo"]["score"] * 100))
accessibility = str(round(loaded_json["categories"]["accessibility"]["score"] * 100))
performance = str(round(loaded_json["categories"]["performance"]["score"] * 100))
best_practices = str(round(loaded_json["categories"]["best-practices"]["score"] * 100))


dict = {"URL":url,"SEO":seo,"Accessibility":accessibility,"Performance":performance,"Best Practices":best_practices}
df = df = df.append(dict, ignore_index=True).sort_values(by='SEO', ascending=False)

df.to_csv(r'C:\Users\radhi\Desktop\lighthouse_' + name + '_' + getdate + '.csv')
print(df)

# print(stream)
