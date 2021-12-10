# genes2doe - Extract genes for OptDoE

## Install
### From Conda
```sh
[sudo] conda install -c conda-forge genes2doe

```

## Use
### CLI
```
python -m parts2doe tests/data/input/lycopene.xml GeneParts.csv
```
### As a Python module
```python
from parts2doe import extract_genes

genes = extract_genes(
    sbml_file='tests/data/input/lycopene.xml'
)
genes.to_csv('GeneParts.csv', index=False)
```

## Tests
`pytest` is required and installable by:
```
conda install -c conda-forge pytest
```

Please follow instructions below to run tests:
```
python -m pytest
```
For further tests and development tools, a CI toolkit is provided in https://github.com/breakthewall/cicd-toolkit.


## Authors

* **Joan Hérisson**


## Licence
genes2doe is released under the MIT licence. See the LICENCE file for details.
