# How to use this code?
# python sample_usage.py > sample_usage.log

import stamodule.mdensity.velogen as dg

# Test by generating a harmonic field

fig3 = dg.get_map(100, "harmonic")

# Print sample image

fig3.savefig("test-harmonic.png")
