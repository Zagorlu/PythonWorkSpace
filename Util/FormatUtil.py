#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2018 Taha Emre Demirkol

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
from Util.PackageUtil import PackageUtil as packageControl


class FormatUtil:
    """
    THIS IS NOT DESCRIPTION FOR "CommandUtil.py" CLASS.
    This part represent to Static Initiliazer Code on Java, it's check to version for the avaiable version.
    At least current Python version must be 3.6.4+, anything else you should update Python version
    """
    ####################################################################################################################
    if not packageControl.checkVersionForApplicable(3, 6, 4):
        raise EnvironmentError("At least current must be 3.6.4+, anything else you should update Python version !!!")

    if packageControl.getPlatformInfo() != 'Linux' and packageControl.getPlatformInfo() != 'OS X':
        raise SystemError("This class only execute Linux or Posix OS platform !!!")
    ####################################################################################################################

    def __init__(self):
        """
        INFO: Default Constructure cannot be Creatable
        WARNING: If attand to create this object, it will raise NotImplementedError
        """
        assert NotImplementedError("This object useing only library, cannot be creatable!!!")

    def __new__(cls):
        """
        INFO: This method was overrided only avoided to __new__ operator
        :return: NOISE_OBJECT
        """
        return object.__new__(cls)

    @staticmethod
    def humanFormatForNumbers(value):
        """
        INFO: This function will return numbers readble String. Ex. 1000 -> 1K
        :param value: This value for will calculate for readable
        :return: STRING
        """
        magnitude = 0
        while abs(value) >= 1000:
            magnitude += 1
            value /= 1000.0
        return '%.2f%s' % (value, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])