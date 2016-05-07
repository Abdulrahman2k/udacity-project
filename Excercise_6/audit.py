"""
Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "example.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Avenue", "Road","Boulevard", "Drive", "Court", "Place", "Square", "Lane", 
            "Trail", "Parkway", "Commons"]

# UPDATE THIS VARIABLE
mapping = { "St": "Street",
            "St.": "Street"
            }


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected :
            street_types[street_type].add(street_name)
            overall_char_match  = 0
            best_match_street_type = None
            for names in expected:
                single_name_char_match = 0
                lower_names = names.lower()
                lower_street_type = street_type.lower().replace(".","").replace("#","")
                for street_type_char in lower_street_type:
                    #print street_type_char
                    #print lower_names
                    if lower_names.find(street_type_char)!=-1  :
                        #print "Passed  test for Avenue"
                        single_name_char_match +=1

                if single_name_char_match > overall_char_match:
                    #print "Number of Charachters Match for "+lower_street_type+"  in  string "+ lower_names +" is "+ str(single_name_char_match)
                    #print "overall_char_match ", str(overall_char_match)
                    overall_char_match = single_name_char_match
                    best_match_street_type =names
            mapping[street_type] = best_match_street_type
                        
                    


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types


def update_name(name, mapping):
    #ln_count = 0
    for key, value in mapping.iteritems() :
        #print "key  ", key
        #print "value ",value
        if name.find(key)!=-1 :
            print "name " ,name
            print "key  ", key
            print "value ",value
            name = name.replace(key,value)
            #ln_count +=1
            break

    # YOUR CODE HERE

    return name


def test():
    st_types = audit(OSMFILE)
    assert len(st_types) == 3
    pprint.pprint(dict(st_types))
    pprint.pprint(dict(mapping))

    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print name, "=>", better_name
            if name == "West Lexington St.":
                assert better_name == "West Lexington Street"
            if name == "Baldwin Rd.":
                assert better_name == "Baldwin Road"


if __name__ == '__main__':
    test()