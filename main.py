import sys
from importlib.abc import MetaPathFinder
from importlib.machinery import PathFinder, ModuleSpec
from importlib.metadata import DistributionFinder, PathDistribution
from importlib.util import spec_from_file_location
from pathlib import Path

from typing import Iterable, Optional


class CustomFinder(PathFinder, MetaPathFinder):
    """As example, we load tqdm from a custom location"""

    tqdm_folder = Path(__file__).parent.joinpath("tqdm_folder")

    def find_spec(self, fullname, path=None, target=None) -> Optional[ModuleSpec]:
        if fullname == "tqdm":
            init_py = self.tqdm_folder.joinpath("tqdm").joinpath("__init__.py")
            return spec_from_file_location(fullname, init_py)

    def find_distributions(
        self, context: DistributionFinder.Context = ...
    ) -> Iterable[PathDistribution]:
        dist_info = self.tqdm_folder.joinpath("tqdm_folder").joinpath(
            "tqdm-4.64.0.dist-info"
        )
        # Here, we return a normal python3.8 importlib.metadata.PathDistribution
        return iter([PathDistribution(dist_info)])


sys.meta_path.append(CustomFinder())

# this works - we successfully made tqdm importable
# noinspection PyUnresolvedReferences
import tqdm
print(tqdm.__version__)
# this doesn't
# noinspection PyUnresolvedReferences
import virtualenv
print(virtualenv.__version__)
