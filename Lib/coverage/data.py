 # -*- coding: utf-8 -*-


# Character frequency data for Latin scripts, with permission from @bianca_berning

# map the character values to glyphnames so we don't have to mess with cmaps later on. 
cmap = {65: 'A',
    66: 'B',
    67: 'C',
    68: 'D',
    69: 'E',
    70: 'F',
    71: 'G',
    72: 'H',
    73: 'I',
    74: 'J',
    75: 'K',
    76: 'L',
    77: 'M',
    78: 'N',
    79: 'O',
    80: 'P',
    81: 'Q',
    82: 'R',
    83: 'S',
    84: 'T',
    85: 'U',
    86: 'V',
    87: 'W',
    88: 'X',
    89: 'Y',
    90: 'Z',
    97: 'a',
    98: 'b',
    99: 'c',
    100: 'd',
    101: 'e',
    102: 'f',
    103: 'g',
    104: 'h',
    105: 'i',
    106: 'j',
    107: 'k',
    108: 'l',
    109: 'm',
    110: 'n',
    111: 'o',
    112: 'p',
    113: 'q',
    114: 'r',
    115: 's',
    116: 't',
    117: 'u',
    118: 'v',
    119: 'w',
    120: 'x',
    121: 'y',
    122: 'z',
    193: 'Aacute',
    196: 'Adieresis',
    197: 'Aring',
    199: 'Ccedilla',
    200: 'Egrave',
    201: 'Eacute',
    205: 'Iacute',
    206: 'Icircumflex',
    214: 'Odieresis',
    216: 'Oslash',
    220: 'Udieresis',
    222: 'Thorn',
    224: 'agrave',
    225: 'aacute',
    226: 'acircumflex',
    227: 'atilde',
    228: 'adieresis',
    229: 'aring',
    230: 'ae',
    231: 'ccedilla',
    232: 'egrave',
    233: 'eacute',
    234: 'ecircumflex',
    235: 'edieresis',
    236: 'igrave',
    237: 'iacute',
    238: 'icircumflex',
    240: 'eth',
    241: 'ntilde',
    242: 'ograve',
    243: 'oacute',
    244: 'ocircumflex',
    245: 'otilde',
    246: 'odieresis',
    248: 'oslash',
    249: 'ugrave',
    250: 'uacute',
    251: 'ucircumflex',
    252: 'udieresis',
    253: 'yacute',
    254: 'thorn',
    257: 'amacron',
    259: 'abreve',
    261: 'aogonek',
    263: 'cacute',
    268: 'Ccaron',
    269: 'ccaron',
    270: 'Dcaron',
    271: 'dcaron',
    273: 'dcroat',
    275: 'emacron',
    277: 'ebreve',
    279: 'edotaccent',
    281: 'eogonek',
    283: 'ecaron',
    287: 'gbreve',
    291: 'gcommaaccent',
    302: 'Iogonek',
    303: 'iogonek',
    304: 'Idotaccent',
    305: 'dotlessi',
    311: 'kcommaaccent',
    314: 'lacute',
    316: 'lcommaaccent',
    318: 'lcaron',
    322: 'lslash',
    324: 'nacute',
    326: 'ncommaaccent',
    328: 'ncaron',
    337: 'ohungarumlaut',
    339: 'oe',
    345: 'rcaron',
    347: 'sacute',
    350: 'Scedilla',
    351: 'scedilla',
    352: 'Scaron',
    353: 'scaron',
    355: 'uni0163',
    357: 'tcaron',
    363: 'umacron',
    367: 'uring',
    369: 'uhungarumlaut',
    371: 'uogonek',
    378: 'zacute',
    379: 'Zdotaccent',
    380: 'zdotaccent',
    381: 'Zcaron',
    382: 'zcaron'}

names = ["Albanian", "Basque", "Bosnian", "Catalan", "Croatian", "Czech", "Danish", "Dutch", "English", "Estonian", "Finnish", "French", "German", "Hungarian", "Icelandic", "Italian", "Latvian", "Lithuanian", "Norwegian", "Polish", "Portuguese", "Romanian", "Slovak", "Slovenian", "Spanish", "Swedish", "Turkish"]

import sys
import codecs

# read data.txt
d = []
f = codecs.open('data.txt', 'r', encoding="utf-8")
data = f.read()
f.close()

# parse the text
for l in data.split("\n"):
    if len(l)==0:
        continue
    parts =  l.split("\t")
    assert len(parts) == len(names)*2
    d.append(parts)

frequencies = {}

for i, line in enumerate(d):
    for j, languageName in enumerate(names):
        if not languageName in frequencies:
            frequencies[languageName] = {}
        k, v = line[j*2:j*2+2]
        if k and v:
            glyphName = cmap[ord(k)]
            frequencies[languageName][glyphName] = float(v)

# normalize the values
eps = 0.00001
for k, v in frequencies.items():
    scale = sum(v.values())
    for letter, value in v.items():
        v[letter] = 100 * float(value)/scale
    assert -eps < sum(v.values()) - 100 < eps

def checkLanguages(font):
    # return a list of language names that are supported in this font
    # note: this is not at all a formal or complete evaluation of
    # language support in a font. It only checks if the frequency table
    # might be asking for glyphs that are not in the font, which would skew the result.
    supportedLanguages = []
    for languageName, table in frequencies.items():
        ok = True
        for glyphName in table.keys():
            if not glyphName in font:
                ok = False
                break
        if ok:
            supportedLanguages.append(languageName)
    return cmap, supportedLanguages
            
__all__ = ["checkLanguages", "frequencies", 'data']

if __name__ == "__main__":
    from pprint import pprint
    pprint(frequencies)
