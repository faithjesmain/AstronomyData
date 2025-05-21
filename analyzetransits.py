from lightkurve import search_lightcurve
import matplotlib.pyplot as plt
import numpy as np

# search for kepler data for kepler-10
search_result = search_lightcurve("Kepler-10", mission="Kepler")

# download & normalize data (so baseline is 1.0) & remove background noise (flatten)
lc = search_result.download().normalize().flatten(window_length=401)

# plot lightcurve
# lc.plot(title="Kepler-10 Light Curve")

# fold lightcurve at planet's known period
folded_lc = lc.fold(period=0.837)
folded_lc.plot(title="Folded Light Curve")

plt.show()

# how big a planet is compared to its star based on dips in brightness
# how deep transit is - how much planet dims
depth = 1 - np.min(folded_lc.flux)  # deepest part of transit
print(f"Estimated Transit Depth: {depth: .4f}")

# Approximate radius ratio - area of planet blocking star is proportional to its radius squared
# how large planet is compared to star
radius_ratio = np.sqrt(depth)  # Rplanet/Rstar
print(f"Planet-to-Star Radius Ratio: {radius_ratio: .4f}")
