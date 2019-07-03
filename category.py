# dictionary of applications as key and and package name  used when some exception arises due to api
br={}

# Api to find description of application from their package id.
import play-scraper

# create a file
file=open('appname.tsv','w')

# run package_Id.py to get dict Application (having application names and their package name)

for a,b in Applications.items():
    
    s=str(a)+'\t'+str(b)+'\t'
    try:
        
        # finding category using free api 
        li=play-scraper.details(str(b))['category']
        
        # if the application have multiple categories
        for i in range(3):
            try:
                s=s+li[i]+'\t'
            except:
                s=s+''+'\t'
        file.write(s)
        file.write('\n')
    except:
        br[a]=b
file.close()

        
