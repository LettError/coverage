# -*- coding: utf-8 -*-

"""
    Calculate a value for the density of a font. 
"""

from __future__ import print_function, division

import sys, traceback

import os
from pprint import pprint 
from fontTools.pens.areaPen import AreaPen
import coverage.data

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
    
def calculateGlyphCoverage(glyph, font=None, cache=None):
    """
        Area of the glyph / area of the (font.em * glyph.width)
        This calculates the coverage of any glyph.
    """
    if cache is None:
        cache = {}
    if glyph.width == 0:
        return 0
    if font is None:
        font = glyph.getParent()
        if font is None:
            return 0
    if font.info.unitsPerEm == 0:
        return 0
    if glyph.name in cache:
        new = cache.get(glyph.name)
    else:
        new = decomposeRemoveOverlapFactory(glyph, font)
        cache[glyph.name] = new
    if new.box is None:
        return 0
    p = AreaPen(font)
    try:
        new.draw(p)
    except NotImplementedError:
        print("caught NotImplementedError in areaPen draw", glyph.name)
        return None
    coverage = p.value/(font.info.unitsPerEm * glyph.width)
    return coverage

def getFontCoverage(f, glyphCache=None):
    """
        Calculate a weighted average of all glyph coverages.
        Use frequencies of multiple languages to average out language specific bias.
        So it does not use all the glyphs, just the A-Z, a-z for the languages we have fequencies for.
    """
    total = []
    if glyphCache is None:
        glyphCache = {}
    supportedLanguages = coverage.data.checkLanguages(f)
    # make a prioritised list of glyphnames:
    # - only the glyphs we need for the tables
    # - and the components they need
    # - then do the glyphs without components first
    # - so that remove overlap work will propagate to the compoents, saving work
    availableGlyphs = []
    for name in coverage.data.coverageNames:
        if not name in f: continue
        g = f[name]
        availableGlyphs.append(name)
        
    if not supportedLanguages:
        return None
    for lang in supportedLanguages:
        table = coverage.data.frequencies[lang]
        languageTotal = 0
        for glyphName in availableGlyphs:
            if not glyphName in table:
                continue
            weight = table[glyphName]
            if glyphName in f:
                g = f[glyphName]
            else:
                continue
            try:
                a = calculateGlyphCoverage(g, f, cache=glyphCache)
            except:
                if f.path is not None:
                    fontName = os.path.basename(f.path)
                else:
                    fontName = "object: %s-%s"%(f.info.familyName, f.info.styleName)
                print("failed calculating the coverage for %s in %s"%(g.name, fontName))
                traceback.print_exc(file=sys.stdout)
                a = 0
            if a > 0:
                languageTotal += a * weight
        total.append(languageTotal/len(table))
    return sum(total) / len(supportedLanguages)

def getFontWidth(f):
    """
        Calculate a weighted average of all glyph advance widths.
    """
    total = []
    supportedLanguages = coverage.data.checkLanguages(f)
    if not supportedLanguages:
        return None
    for lang in supportedLanguages:
        table = coverage.data.frequencies[lang]
        languageTotal = 0
        for glyphName, weight in table.items():
            if glyphName in f:
                languageTotal += (f[glyphName].width/f.info.unitsPerEm)
        total.append(languageTotal/len(table))
    return sum(total) / len(supportedLanguages)


def measureAllFonts():
    for font in AllFonts():
        if font is None:
            continue
        if font.path is not None:
            print(os.path.basename(font.path))
        print("weighted font coverage", getFontCoverage(font))
        print("weighted font width", getFontWidth(font))
        print

def test():
    try:
        font = CurrentFont()
        if font is not None:
            print(os.path.dirname(font.path))
            k = font.keys()
            k.sort()
            totes = []
            for name in k:
                value = calculateGlyphCoverage(font[name])
                totes.append(value)
                print(name, value)
            print(font.info.familyName, font.info.styleName)
            print("\nweighted font coverage", getFontCoverage(font))
            print("\naverage font coverage", sum(totes)/len(totes))
            print("\nweighted font width", getFontWidth(font))
    except NameError:
        pass
        
if __name__ == "__main__":
    measureAllFonts()

