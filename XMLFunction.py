import config
import xml.etree.ElementTree as ET


# Extract string from XML file
def ExtractString(AData):
    try:

        StartDelimiterPosition = AData.find('{')
        EnddelimiterPosition = AData.find('}')
        if StartDelimiterPosition != -1 and EnddelimiterPosition != -1:
            return AData[EnddelimiterPosition + 1:]
        else:
            raise Exception('Error While Extract String')
    except Exception as e:
        print("Error: ",str(e))


# The module will return list of test cases need to be executed
def ExecuteTestcases():
    try:

        # List all the testcases that need to be executed
        TestDataPath = config.TestDataXML  # Path of testcase file
        TestCaseList = {}
        TestData = {}

        # Read XML file
        tree = ET.parse(TestDataPath)
        root = tree.getroot()
        for child in root:
            Data = child.tag
            if ExtractString(Data) == config.XML_NODE_TEST_DATA:
                for child1 in child:
                    Data = child1.tag
                    ExecuteAllTestCases = child1.attrib["ExecuteAllTestCases"]
                    suite = child1.attrib["suite"]
                    if ExtractString(Data) == config.XML_NODE_TEST_CASES:
                        TestCaseList.update({suite: {}})
                        for child2 in child1:
                            _text = child2.text
                            _tag = ExtractString(child2.tag)
                            if ExecuteAllTestCases.upper() == config.XML_NODE_EXECUTE_YES:
                                TestCaseList[suite].update({_tag: config.XML_NODE_EXECUTE_YES})
                            elif _text.upper() == config.XML_NODE_EXECUTE_YES:
                                TestCaseList[suite].update({_tag: config.XML_NODE_EXECUTE_YES})

        return TestCaseList

    except Exception as err:
        print("Error: %s" % err)


def RecodLogsXML(FilePath, ResultDict):
    try:

        # Create the file structure
        root = ET.Element('Output')

        hList = ['Result', 'Comment']
        rList = []

        print(str(ResultDict))

        for data in ResultDict:
            # Adding nodes to the XML
            tc = ET.SubElement(root, 'TestCase')
            item = ET.SubElement(tc, 'ID')
            item.text = data
            count = 0
            rList = [None, None]

            if ResultDict[data] != None:
                rList = ResultDict[data].split(',')
                print(rList)

                for i in rList:
                    item = ET.SubElement(tc, hList[count])
                    item.text = rList[count]
                    count += 1

                # item1.set('name','item1') # To set attribute of any element

        # Create a new XML file with the results
        mydata = ET.tostring(root, encoding="unicode")
        myfile = open(FilePath, "w+")
        myfile.write(mydata)

    except Exception as e:
        print(str(e))
