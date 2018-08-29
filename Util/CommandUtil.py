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
import os
import subprocess as osCommand
from Util.PackageUtil import PackageUtil as packageControl


class CommandUtil:
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
    def isDirectory(path):
        """
        INFO: This function checking directory applicable
        :param path: File path on which is the target source
        :return: BOOLEAN
        """
        return os.path.isdir(path)

    @staticmethod
    def isDirectoryExist(path):
        """
        INFO: This function checking directory exist state
        :param path: File path on which is the target source
        :return: BOOLEAN
        """
        return os.path.exists(path)

    @staticmethod
    def checkFile(path):
        """
        INFO: This function checks the path state
        WARNING: If Not exist or not avaiable format raise exception
        :param path: File path on which is the target source
        :return:
        """
        if (not CommandUtil.isDirectory(path)):
            raise IsADirectoryError("Parameter not Directory!!!")
        if (not CommandUtil.isDirectory(path)):
            raise NotADirectoryError("Directory does not exist !!!")

    @staticmethod
    def sendCommandGetResult(command):
        """
        INFO: This function running on Subprocess library and OS dependent. It can run on MAC, WIN, LNX
        :param command: This parameter will insert on OS
        :return: STRING
        """
        return osCommand.getoutput(command)

    @staticmethod
    def sendCommandGetResultAsList(command):
        """
        INFO: This function running on Subprocess library and OS dependent. It can run on MAC, WIN, LNX
        :param command: This parameter will insert on OS
        :return: LIST[STRING]
        """
        return re.split('[\n]+', osCommand.getoutput(command))

    @staticmethod
    def getLastUpdatedFileName(nullable = None):
        """
        COMMAND: "ls -Artf | tail -n 1"
        INFO: This function is execute running only current directory
        WARNING: This Function should be use LinuxOS
        :return: STRING
        """
        return osCommand.getoutput("ls -Artf | tail -n 1")

    @staticmethod
    def getLastUpdatedFileNameWithDirectory(path):
        """
        INFO: This function return added directory infos last file name
        WARNING:  If file does not exist or Format not avaiable it will raise Error
        :param path: File path on which is the target source
        :return: STRING
        """
        CommandUtil.checkFile(path)
        return osCommand.getoutput("ls -Artf " + path + " | tail -n 1")

    @staticmethod
    def getLastUpdatedFileNameWithDirectoryAndPath(path):
        """
        INFO: This function return added directory infos last file name with directory
        WARNING:  If file does not exist or Format not avaiable it will raise Error
        :param path: File path on which is the target source
        :return: STRING
        """
        return path.rstrip('/') + '/' + CommandUtil.getLastUpdatedFileNameWithDirectory(path)

    @staticmethod
    def getFilesInfoIfKeyContainInDirectory(path, key):
        """
        COMMAND: "grep -rnw '<PATH>' -e '<KEY>'"
        INFO: This function search on path existing files and return which are the exsiting keyword array
        WARNING: This Function should be use LinuxOS
        :param path: Path of which is the important file tree
        :param key: This parameter will search all files
        :return: LIST[STRING]
        """
        CommandUtil.checkFile(path)
        return re.split('[\n]+', osCommand.getoutput("grep -rnw \'" + path + "\' -e \'" + key + "\'"))

    @staticmethod
    def getFilesInfoIfKeyContainInDirectoryAsString(path, key):
        """
        COMMAND: "grep -rnw '<PATH>' -e '<KEY>'"
        INFO: This function search on path existing files and return which are the exsiting keyword string
        WARNING: This Function should be use LinuxOS
        :return: STRING
        """
        CommandUtil.checkFile(path)
        return osCommand.getoutput("grep -rnw \'" + path + "\' -e \'" + key + "\'")

    @staticmethod
    def getCurrentFilesNameAsList(parameter="-l"):
        """
        COMMAND: "ls"
        INFO: This function return the file names as list on absolute path
        :param parameter: This parameter will insort with ls command default value is "-l"
        :return: LIST[STRING]
        """
        return re.split('[\n]+', osCommand.getoutput("ls " + parameter.strip()))