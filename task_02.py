#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

len(inquisition.SPANISH)

inquisition.SPANISH [slice(19,26)]

FLEMISH_1 = inquisition.SPANISH[0:19] + 'Flemish'

FLEMISH = FLEMISH_1 + inquisition.SPANISH[26:]
