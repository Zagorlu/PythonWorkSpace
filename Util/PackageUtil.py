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

import re
import pip
import sys
import os
import subprocess


class PackageUtil:
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
    def checkExistingPythonModule(module):
        """
        INFO: This function check file module. If exist return True else it return False
        :param module: module name which is the check
        :return: BOOLEAN
        """
        installedPackages = pip.get_installed_distributions()
        installedPackagesList = sorted(["%s==%s" % (i.key, i.version) for i in installedPackages])
        for line in installedPackagesList:
            if module in line:
                return True
        return False

    @staticmethod
    def getPythonVersionInfo():
        """
        INFO: This function return to exsiting system python info.
        :return: LIST[STRING]
        """
        return sys.version_info

    @staticmethod
    def checkVersionWithCurrentVersion(version):
        """
        INFO: Tnis function will compare current Python version with argument
        :param version: This parameter will be X.X.X, function will seperate and compare with current OS version
        :return: BOOLEAN
        """
        if version is not "str":
            raise TypeError("This Argument must be String !!!")

        if re.split("[.]+", version.strip()).__len__() != 3:
            raise TypeError("This Argument must be seperated with dot !!! : Ex. 3.7.4")

        value = re.split("[.]+", version.strip())
        return int(value[0]) == PackageUtil.getPythonVersionInfo()[0] \
               and int(value[1]) == PackageUtil.getPythonVersionInfo()[1] \
               and int(value[2]) == PackageUtil.getPythonVersionInfo()[2]

    @staticmethod
    def checkVersionForApplicable(major, minor, micro):
        """
        INFO: Tnis function will compare current Python version with arguments(major,minor, micro)
        :param major: Python major version int value
        :param minor: Python minor version int value
        :param micro: Python micro version int value
        :return: BOOLEAN
        """
        return major >= PackageUtil.getPythonVersionInfo()[0] \
               and minor >= PackageUtil.getPythonVersionInfo()[1] \
               and micro >= PackageUtil.getPythonVersionInfo()[2]

    @staticmethod
    def getPlatformInfo():
        """
        INFO: This method will return to OS name on current system
        :return: STRING
        """
        platforms = {
            'linux1': 'Linux',
            'linux2': 'Linux',
            'darwin': 'OS X',
            'win32': 'Windows'
        }
        if sys.platform not in platforms:
            return sys.platform
        return platforms[sys.platform]

    @staticmethod
    def isExistCommand(commandName):
        """
        INFO: This method will check to command in OS
        :param commandName: Command name of the operating system
        :return: BOOLEAN
        """
        try:
            devnull = open(os.devnull)
            subprocess.Popen([commandName], stdout=devnull, stderr=devnull).communicate()
        except OSError as e:
            if e.errno == os.errno.ENOENT:
                return False
        return True