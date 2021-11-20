from sys import (
    path as sys_path,
)
from os import (
    path as os_path,
)
from typing import (
    Dict
)
from logging import (
    Logger,
    getLogger
)
from pandas import DataFrame
from rptools.rplibs import (
    rpPathway
)
from .Args import DEFAULT_MAXGENES


def extract_genes(
    sbml_file: str,
    maxgenes: int = DEFAULT_MAXGENES,
) -> DataFrame:

    pathway = rpPathway.from_rpSBML(infile=sbml_file)
    selenzyme_info = {
        rxn.get_id(): rxn.get_selenzy()
        for rxn in
        pathway.get_list_of_reactions()
    }

    return __selenzinfo2table(selenzyme_info, pathway, maxgenes)

def __selenzinfo2table(si, pathway, maxgenes):
    """Convert the selenzyme_info dictionary into the input table: Name, Type, Part, Step

    It assumes that pathway steps are in reverse direction and are called as RP1, RP2, etc.

    :param si: The selenzyme information of the heterologous pathway
    :param maxgenes: The maximal number of genes

    :type si: dict
    :type maxgenes: int

    :rtype: pandas.DataFrame
    :return: The table of parts
    """
    genes = DataFrame(columns=['Name','Type', 'Part', 'Step'])
    for rxn_id in si:
        for enz_id in si[rxn_id]:
            genes.loc[len(genes)] = [
                enz_id,
                'gene',
                enz_id,
                pathway.get_reaction(rxn_id).get_idx_in_path()
            ]
    return genes
