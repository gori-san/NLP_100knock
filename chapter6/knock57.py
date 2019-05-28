import xml.etree.ElementTree as ET
import pydot_ng as pydot

tree = ET.parse('nlp.txt.xml')

for sentence in tree.iterfind('.//sentences/sentence'):
    sentence_id = int(sentence.get('id'))
    edges = []
    for dep in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):
        if dep.get('type') == 'punct':
            continue
        governor = dep.find('governor').text
        dependent = dep.find('dependent').text
        edges.append((governor, dependent))
    graph = pydot.graph_from_edges(edges, directed=True)
    graph.write_png(f'{sentence_id}.png')
