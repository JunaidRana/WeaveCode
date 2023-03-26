from py2neo import Graph
from py2neo import Node, Relationship
from lxml import etree

import warnings
warnings.filterwarnings("ignore")


def Load_into_Neo4j():
    graph = Graph("bolt://localhost:7687", auth=("neo4j","Inbox@123"))

    tree = etree.parse("Q9Y261.xml")
    root = tree.getroot()

    for element in root.iter():
        node = Node(element.tag, **element.attrib)
        graph.create(node)
        for child in element:
            child_node = Node(child.tag, **child.attrib)
            graph.create(child_node)
            rel = Relationship(node, child.tag, child_node)
            graph.create(rel)
    pass

try:
    Load_into_Neo4j()
    print("Data Added")

except:
    print("Data Insertion Failed")


