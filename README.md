# Localizable
Localization of iOS and Android projects


## Configuration
create yaml file 

ex : 
```
datasource : "data/izy.xlsx"
ios : {"root" : "../izy-ios","path" : "izy/Application"}
android : {"root" : "../izy-android"}
```

datasource : path to excel file contains localizable strings
ios : root of project and path for Base.lproj if needed
android : root of project

## Run
```
sudo pip install -r requirements.txt
python localize.py <file.yaml>
```
