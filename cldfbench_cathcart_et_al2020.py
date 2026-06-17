import re
import pathlib

import phlorest

def remove_braces(text):
    text = text.replace("<", "_").replace(">", "")
    # Strip inner node labels (BEAST calibration glottocodes like pahl1241, sans1269, oldp1254).
    # These appear as )glottocode: in the posterior trees and are not leaf taxa.
    text = re.sub(r'\)([a-z]{4}[0-9]{4}):', '):', text)
    return text


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "cathcart_et_al2020"

    def cmd_makecldf(self, args):
        self.init(args)
        tree = self.raw_dir.read_tree('IIr.CCD0.trees', detranslate=True, preprocessor=remove_braces)
        args.writer.add_summary(tree, self.metadata, args.log)

        posterior = self.raw_dir.read_trees(
            self.raw_dir / 'clf-iir-evo' / 'IIr.trees',
            burnin=499, sample=1000, detranslate=True, preprocessor=remove_braces)
        args.writer.add_posterior(posterior, self.metadata, args.log)
 