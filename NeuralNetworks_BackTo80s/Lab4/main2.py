import utils
import tsp_boltzmann
import bruteforce
from main import calc_d, set_cities


class BColors:
  HEADER = '\033[95m'
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  NORMAL = '\033[0m'
  BOLD = '\033[1m'


def show(title, paths, dist):
    print("%s%s paths%s (Distance=%f):" % (BColors.HEADER, title.title(), BColors.NORMAL, dist))
    for path in sorted(paths):
        print("   ", path)
    print()


if __name__ == "__main__":
    city = set_cities(3)
    distanceMatrix = calc_d(city)

    print("%sDistance Matrix%s" % (BColors.HEADER, BColors.NORMAL))
    print("  ", str(distanceMatrix).replace("\n","\n   "))
    print()

    comparisons = [
        ("shortest", bruteforce.shortestPaths),
        ("longest", bruteforce.longestPath),
    ]

    distLookup = {}
    for title, func in comparisons:
        paths = func(distanceMatrix)
        dist = utils.pathDistance(distanceMatrix, paths[0])
        distLookup[title] = dist
        show(title, paths, dist)

    print ("Running...")
    for i in range(3):
        print(f"Iteration: {i}")
        tsp = tsp_boltzmann.TSP(distanceMatrix)
        path = tsp.solve()
        dist = utils.pathDistance(distanceMatrix, path)

        show("boltzmann", [path], dist)

        score = (1.0-(float(dist-distLookup['shortest'])/float(distLookup['longest']-distLookup['shortest']) ))

        color = BColors.RED
        if score == 1:
            color = BColors.GREEN
        elif score > 0.6:
            color = BColors.YELLOW

        print ("%sScore (out of 1, higher is better):%s %s%2.2f%s" % (BColors.HEADER, BColors.NORMAL, color, score,
                                                                      BColors.NORMAL))