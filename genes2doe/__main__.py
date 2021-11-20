from argparse import (
    ArgumentParser,
    Namespace
)
from logging import Logger
from colored import fg, bg, attr
from .Args import build_args_parser
from .convert import extract_genes

def init(
    parser: ArgumentParser,
    args: Namespace
) -> Logger:
    from brs_utils import create_logger
    from ._version import __version__

    if args.log.lower() in ['silent', 'quiet'] or args.silent:
        args.log = 'CRITICAL'

    # Create logger
    logger = create_logger(parser.prog, args.log)

    logger.info(
        '{color}{typo}{prog} {version}{rst}{color}{rst}\n'.format(
            prog = logger.name,
            version = __version__,
            color=fg('white'),
            typo=attr('bold'),
            rst=attr('reset')
        )
    )
    logger.debug(args)

    return logger

def entry_point():
    parser = build_args_parser(
        prog = 'genes2doe',
        description='Extract genes for OptDoE'
    )
    args = parser.parse_args()

    logger = init(parser, args)

    genes = extract_genes(
        sbml_file=args.sbml_file,
        maxgenes=args.maxgenes,
        )
    genes.to_csv(args.outfile, index=False)

    logger.info(f'Results written in file \'{args.outfile}\'')


if __name__ == '__main__':
    entry_point()
