#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
Fill out the count_tags function. It should return a dictionary with the 
tag name as the key and number of times this tag can be encountered in 
the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""
import xml.etree.cElementTree as ET
import pprint


def count_tags(filename):
    tags = {}
    for event, element in ET.iterparse(filename):
        if tags.has_key(element.tag):
            tags[element.tag] = tags[element.tag]+1
        else:
            tags[element.tag]=1
    return tags
    #print  tags    
        #print event

    
    # Top-level elements
    

    # All 'neighbor' grand-children of 'country' children of the top-level
    # elements
    #root.findall("./country/neighbor")

# Nodes with name='Singapore' that have a 'year' child
    #root.findall(".//year/..[@name='Singapore']")

# 'year' nodes that are children of nodes with name='Singapore'
    #root.findall(".//*[@name='Singapore']/year")

# All 'neighbor' nodes that are the second child of their parent
    
    #root.findall(".//neighbor[2]")
    
    #if elem.tag == "item":
    #    print elem.findtext("link"), "-", elem.findtext("title")
        # YOUR CODE HERE


def test():

    tags = count_tags('example.osm')
    pprint.pprint(tags)
    assert tags == {'bounds': 1,
                     'member': 3,
                     'nd': 4,
                     'node': 20,
                     'osm': 1,
                     'relation': 1,
                     'tag': 7,
                     'way': 1}

    

if __name__ == "__main__":
    test()