import os
import pandas as pd
import numpy as np

node_features = pd.read_csv("data/node-feat.csv")
node_features = node_features.rename(columns={"id": "paper"})
node_labels = pd.read_csv("data/node-label.csv")
node_labels = node_labels.rename(columns={"id": "paper"})

author_write_paper = pd.read_csv("data/author_write_paper_edge.csv")
author_affiliated_with_institution = pd.read_csv("data/author_affiliated_with_institution_edge.csv")
paper_cites_paper = pd.read_csv("data/paper_cites_paper_edge.csv")
paper_has_topic_field_of_study = pd.read_csv("data/paper_has_topic_field_of_study_edge.csv")

id_to_node = {}
id_to_node['author'] = {node_id: i for i, node_id in enumerate(np.unique(author_write_paper.index.values))}
id_to_node['field_of_study'] = {node_id: i
                                for i, node_id in enumerate(np.unique(paper_has_topic_field_of_study.field_of_study.values))}
id_to_node['institution'] = {node_id: i
                            for i, node_id in enumerate(np.unique(author_affiliated_with_institution['author.institution'].values))}


author_write_paper["author"] = [id_to_node['author'][node_id] for node_id in author_write_paper.index.values]
author_write_paper["paper"] = author_write_paper["author.paper"]
awp = author_write_paper[["author", "paper"]]

author_affiliated_with_institution["author"] = [id_to_node['author'][node_id] for node_id in author_affiliated_with_institution.index.values]
author_affiliated_with_institution["institution"] = [id_to_node['institution'][node_id] for node_id in author_affiliated_with_institution['author.institution'].values]
aawi = author_affiliated_with_institution[["author", "institution"]]

paper_has_topic_field_of_study["field_of_study"] = [id_to_node['field_of_study'][node_id] for node_id in paper_has_topic_field_of_study.field_of_study.values]
phpfos = paper_has_topic_field_of_study[["paper", "field_of_study"]]

os.system("rm -rf processed")
os.mkdir("processed")
node_features.to_csv("processed/node-feat.csv", index=False, header=True)
node_labels.to_csv("processed/node-label.csv", index=False, header=True)
awp.to_csv("processed/author_write_paper_edge.csv", index=False, header=True)
aawi.to_csv("processed/author_affiliated_with_institution_edge.csv", index=False, header=True)
phpfos.to_csv("processed/paper_has_topic_field_of_study_edge.csv", index=False, header=True)
paper_cites_paper.to_csv("processed/paper_cites_paper_edge.csv", index=False, header=True)
