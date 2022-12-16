import xml.etree.ElementTree as ET

tree= ET.parse('movies.xml')
root= tree.getroot()

#print(tree)
#print(ET.tostring(root, encoding='utf8').decode('utf8'))
#print(root.tag) #giving us the name of the element tag
#print(root.attrib) #giving us the element attributes in a dictionary
####################blank dictionary means no attributes
#print(len(root))##how many children the element has
#print([elem.tag for elem in root.iter()])##gives me a list of all the elements

for rating in root.iter('rating'):
    #print(rating.text)
    pass

for rating_pg in root.findall("./genre/decade/movie/[rating='PG']"):
    #print(rating_pg.attrib)
    pass

kkid= root.find("./genre/decade/movie[@title='THE KARATE KID']")
kkid.attrib['title']= "The Karate Kid"
#print(kkid.attrib)

anime_genre= ET.SubElement(root, 'genre')

anime_genre.attrib['category']= 'Anime'
#print(ET.tostring(anime_genre, encoding='utf8').decode('utf8'))

for format_variable in root.iter('movie'):
    print(format_variable.attrib, format_variable.text)
    
    
#<movie> </movie>= element
print(ET.tostring(root, encoding='utf8').decode('utf8'))