import os
from subprocess import PIPE, call  # noqa
import tempfile

import aiger
from aiger_analysis.common import extract_aig


def simplify(e):
    # avoids confusion and guarantees deletion on exit
    with tempfile.TemporaryDirectory() as tmpdirname:
        aag_name = os.path.join(tmpdirname, 'input.aag')
        extract_aig(e).write(aag_name)
        aig_name = os.path.join(tmpdirname, 'input.aig')
        call(['aigtoaig', aag_name, aig_name])
        call(['abc',
              '-c',
              f'read {aig_name}; print_stats; dc2; dc2; dc2; print_stats; write {aig_name}']  # noqa
            # , stdout=PIPE  # comment this line to see more output
            )
        call(['aigtoaig', aig_name, aag_name])
        return aiger.parser.load(aag_name)
