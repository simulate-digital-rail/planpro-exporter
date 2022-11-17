# PlanPro-Generator

This library can generate [PlanPro](https://fahrweg.dbnetze.com/fahrweg-de/unternehmen/dienstleister/PlanPro) files.
Therefor this library can either be used as a library as part of another program or as a stand-alone program.

Currently, it's generating PlanPro 1.9 files, but 1.10 is upcoming.

## Usage as library

To use the generator as a library, install it via:
```shell
pip3 install git+https://github.com/arneboockmeyer/planpro-generator
```

Afterwards you can import it to your application with:
```python
from planprogenerator import Generator, Node, Edge, Signal
```

To create the objects, use:
```python
node = Node(<identifier>, <x>, <y>, <description>)
edge = Edge(<node_a>, <node_b>)
signal = Signal(<edge>, <distance>, <effective_direction>, <function>, <kind>, [<name>])
```

So far, only nodes, edges and signals are supported. The signal function must be one of `Einfahr_Signal`, `Ausfahr_Signal`, `Blocksignal` or `andere` and the signal kind has to be one of `Hauptsignal`, `Mehrabschnittssignal`, `Vorsignal`, `Sperrsignal`, `Hauptsperrsignal` or `andere`. The effective direction is either `in` or `gegen`.

To add intermediate geo nodes, use the following:
```python
geo_node = GeoNode(x, y)
edge.intermediate_geo_nodes.append(geo_node)
```

To generate the file, run:
```python
generator = Generator()
generator.generate(<list of nodes>, <list of edges>, <list of signals>, <filename>)
```

## Usage as stand-alone program

To use the stand-alone version of this library, just run the `generatorcli.py` with Python3:

```shell
python3 generatorcli.py
```

Afterwards a CLI will guide you through the process of creating PlanPro files.
Start with entering the filename and afterwards create your objects:

```
node <id> <x> <y> <description>
edge <node id a> <node id b> [coords x1,y1 [x2,y2 ...]]
signal <node id from> <node id to> <distance to node from> <function> <kind> [<name>]
```

So far, only nodes, edges and signals are supported. The signal function must be one of `Einfahr_Signal`, `Ausfahr_Signal`, `Blocksignal` or `andere` and the signal kind has to be one of `Hauptsignal`, `Mehrabschnittssignal`, `Vorsignal`, `Sperrsignal`, `Hauptsperrsignal` or `andere`.

To add intermediate geo nodes, add a list of space separated coordinates after the keyword `coords`.

To generate the file, run the command `generate`. To exit before, just use `exit`.

## Users

This library was used by the [Digital Rail Summer School](https://hpi.de/drss) in the project [ORM-PlanPro-Converter](https://github.com/DRSS-EULYNX-2022/ORM-PlanPro-Converter).

## Contributors

- [Arne Boockmeyer](https://osm.hpi.de/people/boockmeyer)
- [The DRSS 2022 Project](https://osm.hpi.de/drss/2022)

Feel free to create pull requests to this repository :)
