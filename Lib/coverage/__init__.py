# -*- coding: utf-8 -*-

"""
    Calculate a value for the density of a font. 
"""

from __future__ import print_function, division

import os
from pprint import pprint 
from fontTools.pens.areaPen import AreaPen
from data import *
from lib.fontObjects.robofabWrapper import RobofabWrapperGlyph as RGlyph

from ufoLib.pointPen import AbstractPointPen
from defcon.pens.transformPointPen import TransformPointPen
from defcon.objects.component import _defaultTransformation


class DecomposePointPen(object):
    
    def __init__(self, glyphSet, outPointPen):
        self._glyphSet = glyphSet
        self._outPointPen = outPointPen
        self.beginPath = outPointPen.beginPath
        self.endPath = outPointPen.endPath
        self.addPoint = outPointPen.addPoint
        
    def addComponent(self, baseGlyphName, transformation):
        if baseGlyphName in self._glyphSet:
            baseGlyph = self._glyphSet[baseGlyphName]
            if transformation == _defaultTransformation:
                baseGlyph.drawPoints(self)
            else:
                transformPointPen = TransformPointPen(self, transformation)
                baseGlyph.drawPoints(transformPointPen)

def decomposeRemoveOverlapFactory(glyph, font=None):
    # generate a version of this glyph that has
    #     no components
    #     no overlap
    # in other words, a very very very basic shape of this glyph
    if font is None:
        font = glyph.getParent()
    new = RGlyph()
    p = new.getPointPen()
    tp = DecomposePointPen(font, p)
    glyph.drawPoints(tp)
    new.removeOverlap()
    new.correctDirection()
    new.width = glyph.width
    new.name = glyph.name
    new.unicode = glyph.unicode
    return new
    
def calculateGlyphCoverage(glyph, font=None):
    """
        Area of the glyph / area of the (font.em * glyph.width)
        This calculates the coverage of any glyph.
    """
    if glyph.width == 0:
        return 0
    if font is None:
        font = glyph.getParent()
        if font is None:
            return 0
    if font.info.unitsPerEm == 0:
        return 0
    new = decomposeRemoveOverlapFactory(glyph, font)
    if new.box is None:
        return 0
    p = AreaPen(font)
    try:
        new.draw(p)
    except NotImplementedError:
        print("caught NotImplementedError in areaPen draw", glyph.name)
        return None
    area = p.value
    xMin, yMin, xMax, yMax = glyph.box
    coverage = area/(font.info.unitsPerEm * glyph.width)
    return coverage

def getFontCoverage(f):
    """
        Calculate a weighted average of all glyph coverages.
        Use frequencies of multiple languages to average out language specific bias.
        So it does not use all the glyphs, just the A-Z, a-z for the languages we have fequencies for.
    """
    global frequencies
    total = []
    cmap, supportedLanguages = checkLanguages(f)
    if not cmap:
        # a font without unicode values?
        return None
    if not supportedLanguages:
        return None
    for lang in supportedLanguages:
        table = frequencies[lang]
        languageTotal = 0
        for char, weight in table.items():
            key = cmap.get(ord(char))
            if not key: continue
            g = f[key]
            try:
                a = calculateGlyphCoverage(g, f)
            except:
                print("failed calculating the coverage for %s in %s"%(g.name, os.path.basename(f.path)))
            if a > 0:
                languageTotal += a * weight
        total.append(languageTotal/len(table))
    return sum(total) / len(supportedLanguages)

    
if __name__ == "__main__":
    font = CurrentFont()
    if font is not None:
        k = font.keys()
        k.sort()
        totes = []
        for name in k:
            value = calculateGlyphCoverage(font[name])
            totes.append(value)
            print(name, value)
        print("\nweighted font coverage", font.info.familyName, font.info.styleName, getFontCoverage(font))
        print("\naverage font coverage", font.info.familyName, font.info.styleName, sum(totes)/len(totes))
        