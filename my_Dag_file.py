from py2neo import Graph
from py2neo import Node, Relationship
from lxml import etree

from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

import warnings
warnings.filterwarnings("ignore")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 26),
    'retries': 1
}

dag = DAG(
    'load_xml_to_neo4j',
    default_args=default_args,
    schedule_interval=None
)

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

load_xml_task = PythonOperator(
    task_id='load_xml',
    python_callable=Load_into_Neo4j,
    dag=dag
)
try:
    Load_into_Neo4j()
    print("Data Added")

except:
    print("Data Insertion Failed")


