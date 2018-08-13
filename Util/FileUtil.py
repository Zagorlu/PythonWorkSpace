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


class FileUtil:
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
    def checkClassName(obj, className):
        """
        INFO: This function will compare object's class name
        WARNING: If not equal will raise exception
        :param obj: Which is the checking object
        :param className: Which is the important class name
        :return: NONE
        """
        if obj.__class__.__name__ != className:
            raise EnvironmentError("Object not equal to class name !!!")

    @staticmethod
    def checkFile(path):
        """
        INFO: This function checks the path state
        WARNING: If Not exist or not avaiable format raise exception
        :param path: File path on which is the target source
        :return:
        """
        if (not FileUtil.isDirectory(path)):
            raise IsADirectoryError("Parameter not Directory!!!")
        if (not FileUtil.isDirectory(path)):
            raise NotADirectoryError("Directory does not exist !!!")

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
    def getFileLinesAsList(fileName):
        """
        INFO: This function will return file's line as list
        :param fileName: File name for which is the result for list
        :return: LIST[STRING]
        """
        try:
            fOpen = open(fileName)
            result = fOpen.readlines()
            return result
        except Exception as exception:
            raise exception

    @staticmethod
    def compareConfigurationFileResult(firstConfList, secondConfList):
        """
        INFO: This function will return to result of list compare
        WARNING: If parameter different class object from list, it will raise error
        :param firstConfList: First conf file list
        :param secondConfList: Second conf file list
        :return: LIST[STRING]
        """
        FileUtil.checkClassName(firstConfList, "list")
        FileUtil.checkClassName(secondConfList, "list")
        resultArray = []
        secondArrayCounter = 0
        for i in range(0, firstConfList.__len__()):
            firstListLine = firstConfList[i].strip()
            addFlag = True
            for j in range(secondArrayCounter, secondConfList):
                secondListLine = secondConfList[j].strip()
                if firstListLine is secondListLine:
                    addFlag = False
                    break
            secondArrayCounter += 1
            if addFlag:
                resultArray.append(firstListLine)
        return resultArray

    @staticmethod
    def compareConfigurationFileResultWithFile(firstConfFile, secondConfFile):
        """
        INFO: This function will return to result of Files list compare
        WARNING: If parameter different class object from list, it will raise error
                or if file error occured on that block it will re-raise excepton
        :param firstConfFile: First conf file name
        :param secondConfFile: Second conf file name
        :return: LIST[STRING]
        """
        try:
            return FileUtil.compareConfigurationFileResult(FileUtil.getFileLinesAsList(firstConfFile),
                                                           FileUtil.getFileLinesAsList(secondConfFile))
        except Exception as exception:
            raise exception

    @staticmethod
    def removeFileInCurrentPath(fileName):
        """
        INFO: This function will remove current path file
        :param fileName: which will removes the file name
        :return: NONE
        """
        path = os.path.dirname(os.path.realpath(__file__))
        dirs = os.listdir(path)
        for file in dirs:
            if fileName in file:
                os.remove(file)

    @staticmethod
    def removeFileInExternalPath(fileName, pathName):
        """
        INFO: This function will remove specific path file
        :param fileName: which will removes the file name
        :param pathName: which will removes the files pathName
        :return: NONE
        """
        path = os.path.dirname(pathName)
        dirs = os.listdir(path)
        for file in dirs:
            if fileName in file:
                os.remove(file)

    @staticmethod
    def dataFileSplit(fileName, maximumChaperSize = 500 * 1024 * 1024, memoryBufferSize = 50 * 1024 * 1024 * 1024):
        """
        INFO: This function will sperate files to datasize. This file applicable for data file
        :param fileName: fileName for which is the source file name
        :param maximumChaperSize: Maximum chapter size default value 500MB
        :param memoryBufferSize: Memory buffer size default vaule 50GB
        :return: NONE
        """
        chapterCount = 0
        bufferText = ''
        with open(fileName, 'rb') as src:
            while True:
                target = open(fileName + '.%03d' % chapterCount, 'wb')
                written = 0
                while written < maximumChaperSize:
                    if len(bufferText) > 0:
                        target.write(bufferText)
                    target.write(src.read(min(memoryBufferSize, maximumChaperSize - written)))
                    written += min(memoryBufferSize, maximumChaperSize - written)
                    bufferText = src.read(1)
                    if len(bufferText) == 0:
                        break
                target.close()
                if len(bufferText) == 0:
                    break
                chapterCount += 1

    @staticmethod
    def textFileSplit(fileName, lineCount = 20, outputFileName = "output.txt"):
        """
        INFO: This function will sperate files to line count, this is applicable for text file
        :param fileName: fileName for which is the source file name
        :param lineCount: Split for each file default value 20
        :param outputFileName: Output file names for each one output.1.txt, output.2.txt, etc.
        :return: NONE
        """
        fOpen = open(fileName, 'r')

        count = 0
        at = 0
        dest = None
        for line in fOpen:
            if count % lineCount == 0:
                if dest: dest.close()
                dest = open(outputFileName + str(at) + '.txt', 'w')
                at += 1
            dest.write(line)
            count += 1




