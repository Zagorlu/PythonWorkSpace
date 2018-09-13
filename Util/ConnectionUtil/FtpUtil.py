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
import os
import paramiko
import functools
import pysftp
from Util.PackageUtil import PackageUtil as packageControl
from ftplib import FTP


class FtpUtil:
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


    class AllowAnythingPolicy(paramiko.MissingHostKeyPolicy):
        """
        This Noise class only check paramiko policy and Marker class for ftp connection
        """
        def missing_host_key(self, client, hostname, key):
            """
            INFO: This Function only created for dummy function. It's not necessary for create to body of function.
            :param client: DUMMY PARAMETER
            :param hostname: DUMMY PARAMETER
            :param key: DUMMY PARAMETER
            :return: NONE
            """
            return

    @staticmethod
    def occureConnectionError(e):
        """
        INFO: This function will raise error
        :param e: Error Message
        :return: NONE
        """
        raise ConnectionError("This upload function has been occured error : " + str(e))

    @staticmethod
    def getFtpConnection(user, password, ip, port):
        """
        INFO: This function will return to Ftp Object
        :param user: Remote FTP user
        :param password: Remote FTP password
        :param ip: Remote FTP ip
        :param port: Remote FTP port
        :return: FTP OBJECT : Opened FTP Class Object
        """
        ftp = FTP()
        ftp.connect(ip, port)
        ftp.login(user, password),
        return ftp

    @staticmethod
    def uploadFile(ftpConnection, fileName, binaryFlag=True):
        """
        INFO: This function will send your declerated file with connection and path
        WARNING: Dont use this function with directly, it was designed for using other functions
        TRICKS: The file name could be contain with path, it can obtain certain result
        :param ftpConnection: This argument must be contain ftplibs FTP class
        :param fileName: File name for upload
        :param binaryFlag: Upload file transfer can be binary : it is defult True
        :return: NONE
        """
        try:
            uploadFileName = open(fileName, 'r')
            pathSplit = fileName.strip('/').split('/')
            finalFileName = pathSplit[len(pathSplit) - 1]
            print('Uploading ' + finalFileName + '...')

            if binaryFlag:
                ftpConnection.storbinary('STOR ' + finalFileName, uploadFileName)
            else:
                ftpConnection.storlines('STOR ' + finalFileName, uploadFileName)

            print('Upload Finished...')

        except Exception as e:
            FtpUtil.occureConnectionError(e)

    @staticmethod
    def transferedByteDisplay(fileName, bytesToFar, totalByte):
        """
        INFO: This function will display number of the how many bytes transfered. This function usefull for ftp, sftp
              Internal modules inner callable functions.
        :param fileName: Filename
        :param bytesToFar: The proceeded byte count
        :param totalByte: Total byte count of the filename
        :return: NONE
        """
        print('Transfer of %r is at %d/%d bytes (%.1f%%)' %
               (fileName, bytesToFar, totalByte, 100. * bytesToFar / totalByte))

    @staticmethod
    def connectHostGetFile(fileName, filePath, userName, password, ip, port=22):
        """
        INFO: This function will connect the remote host and get from file with ftp.
        TRICK: fileName argument search as keyword, so you can insert only contain that string.
        :param fileName: File name in the declerated path
        :param filePath: File in the remote path
        :param userName: Remote username
        :param password: Remote password
        :param ip: Remote ip address
        :param port: Remote port, default value is 22 in argument
        :return: NONE
        """
        try:
            sftp = paramiko.SSHClient()
            sftp.set_missing_host_key_policy(FtpUtil.AllowAnythingPolicy())
            sftp.connect(ip, port, userName, password, allow_agent=False, look_for_keys=False)
        except Exception as ex:
            raise ConnectionError("Connection Error : {0}".format(str(ex)))

        sftp_last = sftp.open_sftp()
        sftp_last.chdir(filePath)
        for filename in sorted(sftp_last.listdir()):
            filename = filename.strip()
            if fileName in filename:
                callback_for_filename = functools.partial(FtpUtil.transferedByteDisplay, filename)
                sftp_last.get(filename, filename, callback=callback_for_filename)

        sftp_last.close()
        sftp.close()

    @staticmethod
    def connectHostSendFileWithFtp(user, password, ip, fileName, filePath = os.path.dirname(os.path.realpath(__file__)), port=21):
        """
        INFO: This funtion will send your file with FTP
        TRICK: portname optional insert, it can change your on demand
        :param user: Remote FTP user
        :param password: Remote FTP password
        :param ip: Remote FTP ip
        :param port: Remote FTP port
        :param fileName: File name
        :param filePath: File path : Default value is current path
        :return: NONE
        """
        dirs = os.listdir(filePath)
        try:
            ftpCon = FtpUtil.getFtpConnection(user,password,ip,port)
            for file in dirs:
                if fileName in file:
                    FtpUtil.uploadFile(ftpCon, file)
        except Exception as e:
            FtpUtil.occureConnectionError(e)

    @staticmethod
    def connectHostSendFileWithSftp(user, password, ip, destinationFilePath, sourceFileWithPath):
        """
        INFO: This function will send your file with SFTP
        WARNING: sourceFileWithPath argument must be path info
        :param user: Remote FTP user
        :param password: Remote FTP password
        :param ip: Remote FTP ip
        :param destinationFilePath: Destination file path in remote path
        :param sourceFileWithPath: Source file name with path
        :return: NONE
        """
        try:
            srv = pysftp.Connection(host=ip, username=user, password=password)
            with srv.cd(destinationFilePath):
                srv.put(sourceFileWithPath)
            srv.close()
        except Exception as e:
            FtpUtil.occureConnectionError(e)

