from pydfs_lineup_optimizer import Site, Sport, get_optimizer


optimizer = get_optimizer(Site.DRAFTSTARS, Sport.NRL)
optimizer.load_players_from_csv("NRLG1.csv")
optimizer.set_max_repeating_players(7)
lineup_generator = optimizer.optimize(3)
for lineup in lineup_generator:
    print(lineup)
optimizer.print_statistic()

optimizer = get_optimizer(Site.DRAFTSTARS, Sport.NRL)
optimizer.load_players_from_csv("NRLG1-RFP.csv")
optimizer.set_max_repeating_players(7)
lineup_generator = optimizer.optimize(3)
for lineup in lineup_generator:
    print(lineup)
optimizer.print_statistic()

optimizer = get_optimizer(Site.DRAFTSTARS, Sport.NRL)
optimizer.load_players_from_csv("NRLG1-avg.csv")
optimizer.set_max_repeating_players(7)
lineup_generator = optimizer.optimize(3)
for lineup in lineup_generator:
    print(lineup)
optimizer.print_statistic()
