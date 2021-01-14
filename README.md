# Learning Graph Neural Networks with Deep Graph Library

Learning from graph and relational data plays a major role in many applications including social network analysis, marketing, e-commerce, information retrieval, knowledge modeling, medical and biological sciences, engineering, and others. In the last few years, Graph Neural Networks (GNNs) have emerged as a promising new supervised learning framework capable of bringing the power of deep representation learning to graph and relational data. This ever-growing body of research has shown that GNNs achieve state-of-the-art performance for problems such as link prediction, fraud detection, target-ligand binding activity prediction, knowledge-graph completion, and product recommendations.

This tutorial introduces graph neural networks with a set of hands-on tutorials written with Deep Graph Library (DGL), a scalable GNN framework that simplifies the development of efficient GNN-based training and inference programs at a large scale. It starts with a very simple example of showing graph neural networks with DGL. It goes through more details on how to use GNNs on three basic tasks (i.e., node classification, link prediction and graph classification) and how these models can be used on heterogeneous graphs (which has multiple node types and edge types). It further introduces the mini-batch training methods on large graphs for both node classification and link prediction.

Instructors: [George Karypis](http://glaros.dtc.umn.edu/), [Da Zheng](https://zheng-da.github.io/), [Vasileios Ioannidis](https://sites.google.com/site/vasioannidispw/), [Soji Adeshina](https://sojiadeshina.com/about/)

Agenda
---

| Session | Material | Presenter |
|:-------:|:--------:|:---------:|
Overview of Deep Graph Library (DGL) | [slides](https://github.com/dglai/dgl_winter_school/blob/main/dgl-jhu-tripods-2021.pptx) | George Karypis |
(Hands-on) DGL & GNN 101 | [notebook](https://github.com/dglai/dgl_winter_school/tree/main/2-dgl101) | Da Zheng
(Hands-on) GNN models for basic graph tasks | [notebook](https://github.com/dglai/dgl_winter_school/tree/main/3-basics) | Vasileios Ioannidis |
(Hands-on) GNN mini-batch training | [notebook](https://github.com/dglai/dgl_winter_school/tree/main/4-large_graph) | Soji Adeshina |

Section Content
---

* **Section 1: Overview of Deep Graph Library (DGL).** This section describes the different
  abstractions and APIs that DGL provides, which are designed to simplify the implementation
  of GNN models, and explains how DGL interfaces with MXNet, Pytorch, and TensorFlow.
  It then proceeds to introduce DGL’s message-passing API that can be used to develop
  arbitrarily complex GNNs and the pre-defined GNN nn modules that it provides.
* **Section 2: DGL and GNN 101.** This section introduces the basic operations in DGL, such as
  loading graph data to DGL and the graph query API. It introduces a simple GNN model called
  [GraphSage](http://snap.stanford.edu/graphsage/) and introduces multiple ways of implementing
  this model in DGL.
* **Section 3: GNN models for basic graph tasks.** This section demonstrates how to use
  GNNs to solve three key graph learning tasks: node classification, link prediction, graph
  classification. It will also introduce heterogeneous graphs and the implementation of
  graph neural network models on heterogeneous graphs for the same tasks.
* **Section 4: GNN mini-batch training.** This section uses some of the models described
  in Section 3 to demonstrate mini-batch training. It starts by describing how the concept
  of mini-batch training applies to
  GNNs and how mini-batch computations can be sped up by using some sampling techniques.
  It then proceeds to illustrate how one such sampling technique, called neighbor sampling,
  can be implemented in DGL using a Jupyter notebook and how to use mini-batch training
  for both node classification and link prediction.

## Community

Join our [Slack channel "jhu-winter-school"](https://join.slack.com/t/deep-graph-library/shared_invite/zt-eb4ict1g-xcg3PhZAFAB8p6dtKuP6xQ) for discussion.
