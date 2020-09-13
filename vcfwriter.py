# VCF FILE WRITER 
# VCF VERSION:3
from typing import NamedTuple
from typing import Dict

## GLOBAL VARIABLES ##
VCFBEGIN = "BEGIN:VCARD"
VERSION = "VERSION:3"
VCFEND   = "END:VCARD"
TYPEPREFIX = "#"
SEPARATOR = ";"
KEYWORD = dict(Name="N:",DisplayName="FN:",Address="ADR:",Birthday="BDAY:")
##                  ##

class Name(NamedTuple):
    lastname:str
    firstname:str
    additionalN:str
    namePfx:str

    def _getRes(self) -> str:
        return set_Result("Name",self.lastname,self.firstname,self.additionalN,self.namePfx)

class DisplayName(NamedTuple):
    name:str

    def _getRes(self) -> str:
        return set_Result("DisplayName",self.name)

class Address(NamedTuple):
    type_:str
    street:str
    town:str
    region:str
    zipcode:int
    country:str

    def _getRes(self) -> str:
        self.type_ = TYPEPREFIX + self.type_
        if self.zipcode == 0 and self.type_ != "":
            return set_Result("Address",self.type_, self.street,
                    self.town,self.region,self.country)
        elif self.type_ != "" and self.zipcode != 0:
            return set_Result("Address",self.type_, self.street,
                    self.town,self.region,self.zipcode,self.country)
        return ""

    
class Birthday(NamedTuple):
    bday:str
    def _getRes(self) -> str:
        return set_Result("Birthday",self.bday)

def set_Result(fieldName:str,*args) -> str:
    res = ""
    if fieldName != "" and len(args)>0:
        key = KEYWORD[fieldName]
        res += key
        for i,w in enumerate(args):
            if i != len(args)-1:
                res += w + SEPARATOR
            else:
                res += w + "\n"
        return res
    return res


class VcfV3:
    Name:Name
    Fn:DisplayName
    Adr:Address
    Bday:Birthday

    Rdata = []

    @classmethod
    def Insert_name(cls,lastname:str="",firstname:str="",
            additionalN:str="",namePfx:str=""):
        if lastname != "" or firstname != "" :
            cls.Name = Name(lastname,firstname,additionalN,namePfx) 
            cls.Rdata.append(cls.Name._getRes())
        else :
            raise Exception("need at least lastname value or firstname's")

    @classmethod
    def Insert_FN(cls,name:str):
        if name != "":
            cls.Fn = DisplayName(name)
            cls.Rdata.append(cls.Fn._getRes())
        else:
            raise Exception("name value is required")

    @classmethod
    def Insert_Address(cls,type_:str,street:str="",town:str="",
            region:str="",zipcode:int=0,country:str=""):
        if type_ != "":
            ntype = TYPEPREFIX+type_
            cls.Adr(ntype,street,town,region,zipcode,country)
            cls.Rdata.append(cls.Adr._getRes())
        else:
            raise Exception("type is required")
    
    @classmethod
    def Insert_Bday(cls,bdy:str):
        if bdy != "":
            cls.Bday = Birthday(bdy)
            cls.Rdata.append(cls.Bday._getRes())
        else:
            raise Exception("birthdate is required")

    def Write(self,filename:str):
        with open(filename,"w") as f:
            f.write(VCFBEGIN+"\n")
            f.write(VERSION+"\n")
            f.writelines(self.Rdata)
            f.write(VCFEND)
