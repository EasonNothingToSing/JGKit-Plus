import LSExcelParser


class ExlParser:
    def __init__(self):
        self.handler = LSExcelParser.PeripheralRegisterParser("Venus_SoC_Memory_Mapping.xls",
                                                              ["AP Peripheral AddrMapping",
                                                               "CP Peripheral AddrMapping"],
                                                              exclude=["SysAddrMapping"])

    def get_handler(self):
        return self.handler
