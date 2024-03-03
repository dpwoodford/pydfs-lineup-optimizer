from typing import List, Type, Optional
from pydfs_lineup_optimizer.settings import BaseSettings, LineupPosition
from pydfs_lineup_optimizer.constants import Sport, Site
from pydfs_lineup_optimizer.sites.sites_registry import SitesRegistry
from pydfs_lineup_optimizer.lineup_printer import IndividualSportLineupPrinter
from pydfs_lineup_optimizer.rules import OptimizerRule, FanduelBaseballRosterRule
from pydfs_lineup_optimizer.sites.draftstars.classic.importer import DraftstarsCSVImporter
from pydfs_lineup_optimizer.lineup_exporter import DraftstarsCSVLineupExporter


class DraftstarsSettings(BaseSettings):
    site = Site.DRAFTSTARS
    budget = 100000
    max_from_one_team = 8  # type: Optional[int]
    min_teams = 2  # type: Optional[int]
    csv_importer = DraftstarsCSVImporter
    csv_exporter = DraftstarsCSVLineupExporter


@SitesRegistry.register_settings
class DraftstarsNRLSettings(DraftstarsSettings):
    sport = Sport.NRL
    positions = [
        LineupPosition('OB', ('OB', )),
        LineupPosition('OB', ('OB', )),
        LineupPosition('HH', ('HH', )),
        LineupPosition('FWD', ('FWD', )),
        LineupPosition('FWD', ('FWD', )),
        LineupPosition('FWD', ('FWD', )),
        LineupPosition('FLEX', ('OB','HH','FWD', )),
        LineupPosition('FLEX', ('OB','HH','FWD', )),
    ]

