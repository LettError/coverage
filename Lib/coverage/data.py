 # -*- coding: utf-8 -*-

# Character frequency data for Latin scripts, with permission from @bianca_berning

names = ["Albanian", "Basque", "Bosnian", "Catalan", "Croatian", "Czech", "Danish", "Dutch", "English", "Estonian", "Finnish", "French", "German", "Hungarian", "Icelandic", "Italian", "Latvian", "Lithuanian", "Norwegian", "Polish", "Portuguese", "Romanian", "Slovak", "Slovenian", "Spanish", "Swedish", "Turkish"]

data = u"""
e	544	e	812	a	724	e	741	a	751	o	579	e	955	e	1202	e	750	a	934	a	1256	e	813	e	1244	a	734	a	661	e	727	a	878	i	1104	e	1038	a	617	a	702	e	735	o	584	a	669	e	769	e	661	a	1080
ë	519	a	802	o	613	a	675	o	628	a	457	r	504	n	645	t	516	e	781	i	1013	s	518	n	778	e	681	r	554	i	667	i	652	a	877	r	512	i	606	e	674	i	652	a	542	e	665	a	722	a	633	n	801
t	469	o	459	i	606	s	490	e	603	e	442	t	461	t	434	a	468	i	763	t	961	a	486	i	520	t	585	i	517	a	650	s	561	s	666	n	507	e	584	o	615	a	630	e	474	o	634	o	477	t	597	e	747
r	452	i	444	e	590	r	429	i	574	n	426	n	440	a	426	n	419	s	693	n	839	n	445	r	508	l	501	n	505	o	541	t	515	t	489	t	506	o	502	s	470	r	493	i	378	i	598	s	461	r	589	i	738
a	447	n	433	n	427	i	402	n	430	t	325	a	394	o	408	o	417	t	573	s	788	i	427	t	423	n	404	e	344	n	418	e	458	e	445	a	377	z	395	r	371	t	400	n	355	n	474	n	419	n	564	l	590
i	415	r	422	r	353	l	387	r	347	r	287	i	371	r	399	i	409	l	448	e	741	r	402	s	410	s	395	s	337	l	411	r	426	o	431	i	358	n	391	i	369	n	388	r	351	r	380	r	387	s	401	r	569
n	355	s	361	j	338	n	338	j	344	i	276	d	338	d	390	s	345	u	438	o	590	t	392	a	388	k	320	u	316	r	403	u	406	r	418	s	329	r	331	d	349	l	329	t	288	s	314	i	363	i	351	ı	423
s	280	t	320	u	319	t	336	u	313	l	270	s	333	i	381	r	344	n	399	l	587	l	341	d	343	á	304	ð	302	t	399	n	383	n	415	l	307	w	323	n	306	u	311	v	278	v	313	d	347	l	291	k	324
h	230	d	306	s	271	d	279	d	289	d	266	l	305	s	243	h	280	d	328	k	524	u	326	h	330	i	302	l	286	d	297	ā	304	k	322	o	279	y	272	m	276	o	271	s	259	j	282	l	302	d	260	m	324
m	212	l	301	d	268	o	242	s	272	v	252	o	267	l	236	l	228	k	322	u	448	o	319	u	273	z	300	t	280	s	248	o	295	u	307	d	245	s	268	t	269	d	260	d	250	l	274	t	266	o	253	d	305
o	205	u	281	t	265	u	222	t	270	s	226	g	252	g	195	d	222	r	273	ä	340	d	300	l	217	g	294	m	279	c	230	k	291	m	284	k	241	d	256	c	194	c	240	k	239	d	263	c	238	k	233	t	285
j	201	c	230	k	220	c	189	k	257	k	216	k	235	v	191	c	168	m	267	m	275	c	228	g	208	o	291	k	252	m	183	p	287	p	237	m	202	t	254	u	190	p	186	l	235	k	252	u	218	m	209	s	261
d	179	p	167	v	211	m	189	v	238	u	201	m	202	h	183	m	160	o	265	v	270	m	193	m	200	r	287	g	203	p	170	l	261	l	216	g	192	k	240	p	149	s	183	p	193	p	236	p	192	g	204	y	243
k	175	m	158	m	203	p	189	m	194	p	199	f	164	m	176	u	137	v	174	r	201	p	189	c	189	m	267	f	191	u	163	m	239	d	207	v	135	c	237	l	139	m	173	m	188	t	235	m	181	f	156	o	203
u	175	b	101	l	176	g	78	l	179	í	185	v	118	u	128	g	125	p	150	h	185	é	184	o	186	é	236	v	147	b	108	d	209	v	150	f	127	p	208	v	74	ă	165	h	148	m	184	b	74	ä	147	u	195
p	147	g	92	p	161	b	73	p	175	m	181	h	99	k	127	f	107	g	129	j	174	v	76	b	113	b	179	d	125	g	101	v	179	g	149	p	108	l	180	g	64	ţ	84	u	144	u	137	g	60	h	128	ü	144
l	127	k	88	g	130	q	69	g	143	h	168	p	91	c	111	b	98	j	114	y	159	b	69	k	98	y	177	í	120	v	73	j	151	j	143	å	95	m	178	b	63	î	77	c	136	z	124	q	57	ö	121	b	139
v	100	z	85	b	125	v	63	b	123	á	154	b	81	b	110	p	98	h	113	d	148	q	59	z	91	v	141	o	119	h	71	b	126	ė	131	u	88	u	174	f	47	ş	70	z	133	b	123	ó	57	v	114	ş	110
b	83	q	50	z	125	h	54	z	102	c	142	æ	78	p	91	w	93	ä	107	p	147	f	52	f	77	d	138	á	95	z	49	z	110	b	120	b	84	j	146	h	47	b	65	á	122	g	118	y	52	å	112	ç	105
g	77	ó	50	c	65	f	52	ć	80	z	142	u	77	j	70	y	81	õ	96	Y	41	g	49	w	70	h	101	þ	91	f	47	g	104	ų	120	h	79	b	118	q	35	v	63	y	118	č	95	h	51	b	105	h	99
f	41	h	44	ć	56	é	47	č	74	y	118	å	63	w	69	v	54	b	90	ö	39	h	47	p	56	ö	83	h	82	C	26	ē	85	y	86	ø	57	ł	117	ã	31	f	62	b	112	h	88	v	44	p	102	c	96
q	34	f	42	č	55	ó	27	c	62	b	110	ø	52	z	56	k	27	ü	69	b	31	à	34	v	49	p	76	b	68	à	19	c	79	š	77	j	39	g	97	ç	29	g	50	j	101	š	76	f	37	u	100	g	85
z	25	v	37	h	42	è	25	š	37	j	96	y	37	f	53	T	24	S	28	K	15	x	24	ä	44	j	70	j	58	S	18	š	67	ž	76	y	39	ó	79	C	24	z	42	ý	76	c	47	á	24	c	77	v	85
y	20	E	26	š	42	E	24	h	36	ž	77	U	21	D	24	W	21	A	21	g	14	C	18	ü	43	ó	65	ó	57	O	11	ì	50	į	66	D	21	ę	78	á	24	C	30	š	74	ž	38	í	22	j	40	z	77
c	17	y	24	ž	38	C	20	ž	32	ě	73	A	20	H	18	S	17	O	20	P	12	è	17	S	42	u	61	æ	53	è	11	S	44	ą	62	S	15	ą	70	O	22	A	29	ž	67	A	16	C	18	y	23	B	69
K	17	í	22	D	24	à	19	S	24	é	63	j	20	R	18	M	16	U	18	O	11	j	13	M	39	ő	44	y	52	q	10	â	44	ū	41	A	11	ż	60	P	20	S	24	í	62	Z	14	E	16	O	17	ö	58
x	17	j	17	S	23	x	18	B	23	ý	60	D	19	A	16	H	14	B	14	E	10	M	10	B	33	f	38	p	50	B	9	V	39	A	34	I	11	h	55	é	18	U	16	č	54	D	10	z	16	D	16	ğ	58
B	14	á	17	A	21	í	17	f	22	š	59	S	19	O	16	O	13	c	14	J	9	L	8	A	31	í	35	ö	49	L	9	ņ	39	č	29	N	11	ś	41	R	17	O	14	é	48	K	10	ú	12	A	13	p	42
O	13	é	15	đ	19	ò	14	A	18	ř	48	c	12	B	8	R	12	I	11	S	8	y	8	D	28	ü	33	ú	29	U	8	è	35	c	28	U	11	ć	40	õ	17	â	14	ť	44	N	8	P	8	S	13	A	40
P	13	U	11	f	13	j	13	đ	17	ů	44	E	12	C	8	D	11	M	11	V	8	O	7	G	28	A	30	B	21	A	7	A	33	B	24	c	10	P	22	í	14	h	12	ú	38	O	8	x	8	U	10	D	39
S	13	A	9	B	12	O	10	D	15	č	39	M	12	E	7	x	11	P	10	B	7	B	6	W	28	c	29	Þ	17	I	6	ø	22	J	24	O	10	A	21	D	13	j	12	ľ	29	B	7	é	8	V	9	f	20
A	10	C	9	K	8	S	9	P	15	g	33	O	12	V	7	U	10	V	8	R	7	E	6	K	20	ú	23	ý	16	ì	5	B	14	V	23	B	9	f	17	j	12	P	10	A	19	f	7	L	7	F	6	M	17
D	10	K	8	O	8	y	9	K	14	f	19	R	11	I	5	C	9	f	7	c	6	ê	6	H	19	O	13	S	13	k	4	P	14	S	21	M	9	ń	15	A	11	B	8	g	16	T	7	B	6	M	6	O	17
H	8	S	8	R	8	A	7	O	14	S	17	N	7	é	5	B	8	K	5	M	6	A	5	P	19	E	12	A	11	N	4	ž	14	z	21	F	8	N	14	S	11	k	7	P	16	V	7	D	5	N	6	S	16
M	7	x	7	M	7	B	7	M	12	A	16	B	5	N	4	A	7	w	5	N	5	S	5	R	19	ű	11	F	10	ù	4	K	13	ę	18	P	7	O	14	ó	10	R	7	O	15	J	6	j	5	B	4	K	15
R	5	O	6	P	7	T	7	C	8	O	15	H	5	F	3	j	7	D	4	A	4	ô	5	F	18	T	10	O	7	E	3	L	12	O	17	R	7	D	13	x	9	x	6	ô	15	S	5	S	5	I	4	T	15
G	4	B	5	N	5	U	7	N	5	P	14	I	3	P	3	J	6	N	4	L	4	ù	4	N	17	G	9	R	6	G	3	ū	11	R	12	J	6	R	11	B	8	N	5	S	12	P	4	T	5	P	4	C	11
N	4	L	5	U	5	ç	7	R	4	K	11	J	3	S	3	P	6	R	4	D	3	R	2	V	17	S	7	H	5	J	3	f	9	f	11	E	5	S	11	M	8	Î	5	ň	11	W	4	N	4	E	3	P	6
V	3	R	5	V	5	D	6	y	4	ú	10	P	3	W	3	E	5	T	4	H	3	U	2	ö	15	Á	7	Ö	5	M	3	O	9	K	11	æ	5	K	10	T	8	D	3	f	10	Č	4	O	4	H	3	J	4
U	2	N	4	T	4	R	6	G	3	D	8	C	2	Z	3	N	5	y	4	T	2	z	2	E	13	D	6	c	4	R	3	ð	8	P	9	H	4	W	10	E	7	H	3	T	10	M	3	R	4	x	3	İ	4
ç	2	P	4	W	4	ú	5	H	3	B	7	G	2	L	2	I	4	G	3	U	2	ç	2	Z	11	P	6	D	4	W	3	I	7	T	8	K	4	B	8	H	7	I	3	ó	9	C	2	U	4	J	2	H	2
I	1	T	4	G	3	M	4	J	2	N	7	K	2	x	2	L	4	J	3	C	1	î	2	O	9	K	5	E	4	y	3	ļ	7	h	6	G	3	T	8	z	7	M	3	C	8	G	2	ñ	4	R	2	j	2
L	1	ú	4	I	3	N	4	U	2	U	7	V	2	X	2	F	3	C	2	Ä	1	H	1	C	7	M	5	K	4	H	2	h	6	M	6	T	3	Z	8	N	6	E	2	K	8	w	2	A	3	W	2	N	2
Q	1	F	3	y	3	P	4	V	1	V	6	W	2	y	2	q	3	E	2	Ö	1	I	1	J	7	N	5	C	3	P	2	J	6	D	5	C	2	C	7	à	6	F	2	B	7	Y	2	G	2	é	2	U	2
T	1	G	3	C	2	k	3	Z	1	M	5	F	1	G	1	z	3	L	2			J	1	y	6	H	4	M	3	Q	2	M	6	Š	5	L	2	M	7	â	6	L	2	D	7	F	1	J	2	G	1	F	1
X	1	H	2	H	2	G	2	Č	1	T	5	T	1	J	1	G	2	H	1			k	1	I	5	V	4	T	3	T	2	N	6	H	4	V	2	J	6	k	5	T	2	N	7	L	1	k	2	L	1	G	1
Z	1	M	2	J	2	L	2	Š	1	Z	5	w	1	M	1	V	2	W	1			N	1	T	5	B	2	z	3	w	2	ú	6	N	4	x	1	G	5	U	5	V	2	V	7	R	1	M	1	T	1	L	1
		ñ	2	L	1	W	2	Ž	1	ň	5	Y	1	T	1			Y	1			P	1	j	3	C	2	Á	3	È	2	D	5	C	3	Ø	1	I	5	ê	5	W	2	ď	7	U	1	Q	1	w	1	W	1
		D	1	w	1	J	1			C	4	é	1	U	1							T	1	L	2	J	2	Í	3	D	1	R	5	I	2			U	5	W	3	G	1	M	6	y	1	V	1			Y	1
		W	1	Y	1	z	1			J	4			ë	1							w	1	U	2	w	2	N	2	F	1	ģ	4	Į	2			ź	3	ú	3	J	1	Z	6	Š	1	W	1			Ç	1
				Z	1	É	1			F	3											û	1	Ü	2	W	2	P	2	x	1	ķ	4	E	1			F	2	G	2	K	1	ä	6							Ö	1
				Č	1					E	2											œ	1	q	1	Í	2	w	2	é	1	C	3	F	1			v	2	J	2	y	1	R	4							Ü	1
										G	2													Q	1	L	1	W	2	ò	1	T	3	G	1			X	2	V	2	Ş	1	E	3								
										R	2															R	1	G	1			î	3	L	1			Y	2	w	2			F	3								
										x	2															U	1	x	1			G	2	x	1			E	1	y	2			I	3								
										Y	2															x	1	Y	1			H	2	Z	1			H	1	F	1			x	3								
										Č	2															Y	1	É	1			F	1	é	1			q	1	K	1			H	2								
										ĕ	2																					U	1	Ž	1			Ż	1	L	1			L	2								
										H	1																					Z	1							Q	1			W	2								
										L	1																					Å	1							Y	1			Ď	2								
										w	1																					å	1											Š	2								
										W	1																					č	1											J	1								
										ď	1																					Š	1											U	1								
																																												ĺ	1								
"""
from pprint import pprint
import sys

# parse the text
d = []
for l in data.split("\n"):
	if len(l)==0:
		continue
	parts =  l.split("\t")
	assert len(parts) == len(names)*2
	d.append(parts)

s = {}

for i, line in enumerate(d):
	for j, name in enumerate(names):
		#print j, name
		if not name in s:
			s[name] = {}
		k, v = line[j*2:j*2+2]
		if k and v:
			s[name][k] = float(v)

# normalize

eps = 0.00001
for k, v in s.items():
	scale = sum(v.values())
	for letter, value in v.items():
		v[letter] = 100 * float(value)/scale
	assert -eps < sum(v.values()) - 100 < eps

frequencies = s

def checkLanguages(font):
    # return a list of language names that are supported in this font
    # note: this is not at all a formal or complete evaluation of
    # language support in a font. It only checks if the frequency table
    # might be asking for glyphs that are not in the font, which would skew the result.
    cmap = {}
    for g in font:
        if g.unicode is not None:
            cmap[g.unicode] = g.name
    supportedLanguages = []
    for name, table in frequencies.items():
        ok = True
        for char in table.keys():
            if not ord(char) in cmap:
                ok = False
                break
        if ok:
            supportedLanguages.append(name)
    return cmap, supportedLanguages
            
__all__ = ["checkLanguages", "frequencies"]

if __name__ == "__main__":
	pprint(s)

