# genes2doe - Extract genes for OptDoE

## Install
### From Conda
```sh
[sudo] conda install -c conda-forge parts2doe

```

## Use
### CLI
```
python -m parts2doe tests/data/pathway.xml selenzy.xml
```
### As a Python module
```python
from selenzy_wrapper import selenzy_pathway

pathway = rpPathway.from_rpSBML(infile='tests/data/pathway.xml')

selenzy_pathway(pathway=pathway)

pathway.to_rpSBML().write_to_file('selenzy.xml')
```

## Tests
Please follow instructions below ti run tests:
```
cd tests
pytest -v
```
For further tests and development tools, a CI toolkit is provided in https://github.com/breakthewall/cicd-toolkit.


## Authors

* **Joan Hérisson**


## Licence
parts2doe is released under the MIT licence. See the LICENCE file for details.
