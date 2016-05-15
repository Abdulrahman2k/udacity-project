#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This the first program used for cleaning of Data, we are cleaning following values
a. Names with unexpected Values
b. Phone Number in proper Syntax
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint
##from sets import Set
import json as simplejson



OSMFILE = "dubai_abu-dhabi.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Avenue", "Road","Boulevard", "Drive", "Court", "Place", "Square", "Lane", 
            "Trail", "Parkway", "Commons"]

# update this dictionary with addittional street type and their valid names from Expected list using Audit_street_type Module
mapping = { "St": "Street",
            "St.": "Street"
            }

def add_mapping(street_type):
	fo = open("foo.txt", "ab+")
	fo.write( "\n"+street_type)
	fo.close()

## this maps the Street type with Most Probable match based on the 
## maximum number of charachters from incorrect street type matching
## with Expected Street Types and puts it in the mapping Dictionary
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
                    if lower_names.find(street_type_char)!=-1  :
                        single_name_char_match +=1
                if single_name_char_match > overall_char_match:
                    overall_char_match = single_name_char_match
                    best_match_street_type =names
            mapping[street_type] = best_match_street_type
            add_mapping(best_match_street_type)            
                    

## checking for street types
def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


## this is for generating a file for list of all unique keys available
def add_mapping(street):
    fo = open("debug_file.txt", "ab+")
    street =list(street)
    for key in street:	
        fo.write(bytes("\n",'UTF-8'))
        fo.write(bytes(key,'UTF-8'))
    fo.close()

##cleaning the phone format and checking for unique key values
def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    street = set([])
    street.add("test")
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                audit_street_type(street_types, tag.attrib['v'])
                updated_phone =None
                street.add(tag.attrib['k'])
                if tag.attrib['k']== "phone":
                    updated_phone = phone_format(tag.attrib['v'])
                    street_types[tag.attrib['k']]=updated_phone 
                street_types[tag.attrib['k']]=tag.attrib['v']
    osm_file.close()
    pprint.pprint(street)
    add_mapping(street)
    return street_types
			#for tag in elem.iter("tag"):
			#	audit_street_type(street_types, tag.attrib['v'])
	


## Update Name Mapping with Correct Street type
def update_name(name, mapping):
    for key, value in mapping.iteritems() :
        if name.find(key)!=-1 :
            name = name.replace(key,value)
            break

    return name

## module to update the phone number with the correct type
def phone_format(phone_number):
    clean_phone_number = str(int(re.sub('[^0-9]+', '', phone_number)))
    formatted_phone_number = '+{0} {1} {2}'.format(clean_phone_number[:-8],clean_phone_number[-8:-7],clean_phone_number[-7:] ) 
    return formatted_phone_number

## main program
def test():
    st_types = audit(OSMFILE)
    pprint.pprint(dict(st_types))


    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)

## main program call
if __name__ == '__main__':
    test()