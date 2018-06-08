#!/usr/bin/evn python
from sense_hat import SenseHat
import time
sense = SenseHat()

i = 0
blood_red = (113, 12, 4)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
orange = (255, 128, 0)
aa = blood_red
ab = blood_red
ac = blood_red
ad = blood_red
ae = blood_red
af = blood_red
ag = blood_red
ah = blood_red
ba = blood_red
bb = blood_red
bc = blood_red
bd = blood_red
be = blood_red
bf = blood_red
bg = blood_red
bh = blood_red
ca = blood_red
cb = blood_red
cc = blood_red
cd = blood_red
ce = blood_red
cf = blood_red
cg = blood_red
ch = blood_red
da = blood_red
db = blood_red
dc = blood_red
dd = blood_red
de = blood_red
df = blood_red
dg = blood_red
dh = blood_red
ea = blood_red
eb = blood_red
ec = blood_red
ed = blood_red
ee = blood_red
ef = blood_red
eg = blood_red
eh = blood_red
fa = blood_red
fb = blood_red
fc = blood_red
fd = blood_red
fe = blood_red
ff = blood_red
fg = blood_red
fh = blood_red
ga = blood_red
gb = blood_red
gc = blood_red
gd = blood_red
ge = blood_red
gf = blood_red
gg = blood_red
gh = blood_red
ha = blood_red
hb = blood_red
hc = blood_red
hd = blood_red
he = blood_red
hf = blood_red
hg = blood_red
hh = blood_red

while (i == 0):

	pixels = [
		aa, ab, ac, ad, ae, af, ag, ah,
		ba, bb, bc, bd, be, bf, bg, bh,
		ca, cb, cc, cd, ce, cf, cg, ch,
		da, db, dc, dd, de, df, dg, dh,
		ea, eb, ec, ed, ee, ef, eg, eh,
		ga, gb, gc, gd, ge, gf, gg, gh,
		ha, hb, hc, hd, he, hf, hg, hh,
	]
	time.sleep(1)

sense.set_pixels(pixels)


