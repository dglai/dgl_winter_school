import dgl
import pandas as pd
import torch
import torch.nn.functional as F
import os
import tarfile

def load_zachery():
    nodes_data = pd.read_csv('data/nodes.csv')
    edges_data = pd.read_csv('data/edges.csv')
    src = edges_data['Src'].to_numpy()
    dst = edges_data['Dst'].to_numpy()
    g = dgl.graph((src, dst))
    club = nodes_data['Club'].to_list()
    # Convert to categorical integer values with 0 for 'Mr. Hi', 1 for 'Officer'.
    club = torch.tensor([c == 'Officer' for c in club]).long()
    # We can also convert it to one-hot encoding.
    club_onehot = F.one_hot(club)
    g.ndata.update({'club' : club, 'club_onehot' : club_onehot})
    return g
    
def download_and_extract():
    import shutil
    import requests
    
    url = "https://s3.us-west-2.amazonaws.com/dgl-data/dataset/DRKG/drkg.tar.gz"
    path = "../data/"
    filename = "drkg.tar.gz"
    fn = os.path.join(path, filename)
    if os.path.exists("../data/drkg/drkg.tsv"):
        return
    
    opener, mode = tarfile.open, 'r:gz'
    os.makedirs(path, exist_ok=True)
    cwd = os.getcwd()
    os.chdir(path)
    while True:
        try:
            file = opener(filename, mode)
            try: file.extractall()
            finally: file.close()
            break
        except Exception:
            f_remote = requests.get(url, stream=True)
            sz = f_remote.headers.get('content-length')
            assert f_remote.status_code == 200, 'fail to open {}'.format(url)
            with open(filename, 'wb') as writer:
                for chunk in f_remote.iter_content(chunk_size=1024*1024):
                    writer.write(chunk)
            print('Download finished. Unzipping the file...')
    os.chdir(cwd)
    
def create_drkg_edge_lists():
    download_and_extract()
    path = "../data/"
    filename = "drkg.tsv"
    drkg_file = os.path.join(path, filename)
    df = pd.read_csv(drkg_file, sep ="\t", header=None)
    triplets = df.values.tolist()
    entity_dictionary = {}
    def insert_entry(entry, ent_type, dic):
        if ent_type not in dic:
            dic[ent_type] = {}
        ent_n_id = len(dic[ent_type])
        if entry not in dic[ent_type]:
             dic[ent_type][entry] = ent_n_id
        return dic

    for triple in triplets:
        src = triple[0]
        split_src = src.split('::')
        src_type = split_src[0]
        dest = triple[2]
        split_dest = dest.split('::')
        dest_type = split_dest[0]
        insert_entry(src,src_type,entity_dictionary)
        insert_entry(dest,dest_type,entity_dictionary)

    edge_dictionary={}
    for triple in triplets:
        src = triple[0]
        split_src = src.split('::')
        src_type = split_src[0]
        dest = triple[2]
        split_dest = dest.split('::')
        dest_type = split_dest[0]

        src_int_id = entity_dictionary[src_type][src]
        dest_int_id = entity_dictionary[dest_type][dest]

        pair = (src_int_id,dest_int_id)
        etype = (src_type,triple[1],dest_type)
        if etype in edge_dictionary:
            edge_dictionary[etype] += [pair]
        else:
            edge_dictionary[etype] = [pair]
    return edge_dictionary