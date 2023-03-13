from parsing_and_adding import *
import xml.etree.ElementTree as Et


class ParserXml(ParcerFile):  # class for parsing XML
    def __init__(self, p_file, p_record):
        ParcerFile.__init__(self, p_file, p_record)
        self.data = ''
        self.error_in_date = 0
        self.rec = {}

    def verify_record(self, rec):  # verify each particular record
        try:
            if rec.attrib['name'] == "New":
                self.number_of_records["new"] += 1
            elif rec.attrib['name'] == "Add":
                self.number_of_records["add"] += 1
            elif rec.attrib['name'] == "Recipe":
                self.number_of_records["recipe"] += 1
            current_date = datetime.now()
            if rec.attrib['name'] == "Add" and datetime.strptime(rec.find('expiration_date').text, '%m/%d/%y') \
                    > current_date:
                self.error_in_date = 0
            else:
                self.error_in_date = 1

        except AttributeError:
            print('Check attributes')

    def verify_file(self):  # verify file
        xml_file = Et.parse(self.path)
        root = xml_file.getroot()
        for record in root:
            self.verify_record(record)
        self.check_verify()  # check verification of file

    def parse_record(self, p_rec):  # parse record and create record in file
        if self.record == "New":
            new_from_xml = News("News", p_rec.find('text').text, p_rec.find('city').text)
            new_from_xml.add_to_feed()
        elif self.record == "Add":
            add_from_xml = Ads("Privat ad", p_rec.find('text').text, p_rec.find('expiration_date').text)
            add_from_xml.add_to_feed()
        else:
            rec_from_xml = Rec("Recipe", p_rec.find('text').text)
            rec_from_xml.add_to_feed()

    def parc(self):  # parse json file
        self.verify_file()
        if self.type_verify == 1:
            xml_file = Et.parse(self.path)
            root = xml_file.getroot()
            for record in root:
                self.parse_record(record)
            os.remove(self.path)  # if success - delete file
