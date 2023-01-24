# planpro-exporter

This library can generate [PlanPro](https://fahrweg.dbnetze.com/fahrweg-de/unternehmen/dienstleister/PlanPro) files from a [yaramo](https://github.com/simulate-digital-rail/yaramo) topology.

Currently, it's generating PlanPro 1.9 files, but 1.10 is upcoming.

## Usage as library

To use the generator as a library, install it via:
```shell
pip3 install git+https://github.com/simulate-digital-rail/planpro-exporter
```

Afterwards you can import it to your application with:
```python
from planproexporter.generator import Generator
# topology is a yaramo.models.Topology object
Generator().generate(topology, author_name="Name", organisation="Organisation", filename="out.ppxml")
```

Further examples can be found in the [demo repository](https://github.com/simulate-digital-rail/yaramo).

## Contributors

- [Arne Boockmeyer](https://osm.hpi.de/people/boockmeyer)
- [The DRSS 2022 Project](https://osm.hpi.de/drss/2022)

Feel free to create pull requests to this repository :)
