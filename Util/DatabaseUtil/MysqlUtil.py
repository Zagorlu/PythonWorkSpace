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
import os
import time
from Util.PackageUtil import PackageUtil as packageControl


class MysqlUtil:
    """
    THIS IS NOT DESCRIPTION FOR "CommandUtil.py" CLASS.
    This part represent to Static Initiliazer Code on Java, it's check to version for the avaiable version.
    At least current must be 3.6.4+, anything else you should update Python version
    """
    ####################################################################################################################
    if not packageControl.checkVersionForApplicable(3, 6, 4):
        raise EnvironmentError("At least current must be 3.6.4+, anything else you should update Python version !!!")

    if packageControl.getPlatformInfo() != 'Linux' and packageControl.getPlatformInfo() != 'OS X':
        raise SystemError("This class only execute Linux or Posix OS platform !!!")

    if not packageControl.isExistCommand("mysqldump"):
        raise ModuleNotFoundError("mysqldump command is not found, it should be implemented !!!")
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
    def getDatabaseBackup(user, password, databaseName, backupPath, host=""):
        """
        INFO: This function will use the msqldump command and it will create file with defined path. If the path is not
              it will create that path. Also which is the contain SQL scripts in the sql extension file.
        WARNING: That function only running existing msqldump and posix systems. Anything else it will raise Error
        :param host: Hostname of database
        :param user: User authentication name
        :param password: Authentication password
        :param databaseName: Database name in operataring system
        :param backupPath: it will declare to path of the that path, if doesnt exist it will create that path name
        :return: NONE
        """
        flag = False
        dateTimeInfo = time.strftime('%d_%m_%Y__%H_%M_%S')
        if backupPath.endswith('/'):
            backupPath += dateTimeInfo
        else:
            backupPath += ('/' + dateTimeInfo)

        if not os.path.exists(backupPath):
            os.makedirs(backupPath)

        if os.path.exists(databaseName):
            fileOpen = open(databaseName)
            fileOpen.close()
            flag = True

        if flag:
            fileOpen = open(databaseName, "r")
            fileLength = len(fileOpen.readlines())
            fileOpen.close()
            filePointer = 1
            dbfile = open(databaseName, "r")

            while filePointer <= fileLength:
                database = dbfile.readline()
                database = database[:-1]
                if host:
                    dumpcmd = "mysqldump -h " + host + " -u " + user + " -p" + password + " " + database + " > " + backupPath + "/" + database + ".sql"
                else:
                    dumpcmd = "mysqldump -u " + user + " -p" + password + " " + database + " > " + backupPath + "/" + database + ".sql"
                os.system(dumpcmd)
                filePointer += 1
            dbfile.close()
        else:
            if host:
                dumpcmd = "mysqldump -h " + host + " -u " + user + " -p" + password + " " + databaseName + " > " + backupPath + "/" + databaseName + ".sql"
            else:
                dumpcmd = "mysqldump -u " + user + " -p" + password + " " + databaseName + " > " + backupPath + "/" + databaseName + ".sql"
            os.system(dumpcmd)