import xml.etree.ElementTree as ET
import re

tree= ET.parse('movies.xml')
root= tree.getroot()

print(tree)
print(root)

print(root.tag)
print(root.attrib)

for child in root:
    #print(child.tag, child.attrib)
    pass

#print([elem.tag for elem in root.iter()])
#print(ET.tostring(root, encoding='utf8').decode('utf8'))

for movie in root.iter('movie'):
    #print(movie.attrib)
    pass
    

for description in root.iter('description'):
    #print(description.text)
    pass

for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
    #print(movie.attrib)
    pass

for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']..."):
    #print(movie.attrib)
    pass

#back= root.find("./genre/decade/movie[@title='Back to the Future']")
#print(back)
#back.attrib["title"]= "Back To the Future"
#print(back.attrib)

#tree.write('movies.xml')

for form in root.findall("./genre/decade/movie/format"):
    
    #search for the commas in the format text
    match= re.search(',',form.text)
    if match:
        form.set('multiple', 'Yes')
    else:
        form.set('multiple', 'No')
    #print(form.attrib, form.text)

for decade in root.findall("./genre/decade"):
    print(decade.attrib)
    for year in decade.findall("./movie/year"):
        print(year.text, '\n')

for movie in root.findall("./genre/decade/movie/[year='2000']"):
    #print(movie.attrib)
    pass

add= root.find("./genre[@category='Action']")
#print(add)
new_dec= ET.SubElement(add, 'decade')
new_dec.attrib['years']= '2000s'


for genre in root.findall("./genre"):
    #print(genre.attrib)
    pass

#print(ET.tostring(add, encoding='utf8').decode('utf8'))

xmen= root.find("./genre/decade/movie[@title='X-Men']")
dec2000= root.find("./genre[@category='Action']/decade[@years='2000s']")
dec2000.append(xmen)

dec1990= root.find("./genre[@category='Action']/decade[@years='1990s']")
dec1990.remove(xmen)
print(ET.tostring(add, encoding='utf8').decode('utf8'))

tree.write('movies.xml')