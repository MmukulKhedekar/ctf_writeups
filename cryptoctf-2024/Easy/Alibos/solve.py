from Crypto.Util.number import *

pkey = 8582435512564229286688465405009040056856016872134514945016805951785759509953023638490767572236748566493023965794194297026085882082781147026501124183913218900918532638964014591302221504335115379744625749001902791287122243760312557423006862735120339132655680911213722073949690947638446354528576541717311700749946777
enc  = 6314597738211377086770535291073179315279171595861180001679392971498929017818237394074266448467963648845725270238638741470530326527225591470945568628357663345362977083408459035746665948779559824189070193446347235731566688204757001867451307179564783577100125355658166518394135392082890798973020986161756145194380336

d = len(str(pkey))

print(long_to_bytes(int(str(((enc - pkey) * (pow(d ** 2, -1, 10 ** d))) % (10 ** d)).rstrip('1'))))
