class Patient(object):

    def __init__(self,PatientNmae,AO = 0.0, LA = 0.0, RV = 0.0, IVS = 0.0, LVDd = 0.0, LVDs = 0.0,
                 LVPW = 0.0, RA = 0.0, LVEF = 0.0, AV = 0.0,MVE = 0.0, MVA = 0.0):
        self.PatientNmae = PatientNmae
        self.AO = AO
        self.LA = LA
        self.RV = RV
        self.IVS = IVS
        self.LVDd = LVDd
        self.LVDs = LVDs
        self.LVPW = LVPW
        self.RA = RA
        self.LVEF = LVEF
        self.AV = AV
        self.MVE = MVE
        self.MVA = MVA
        self.Left_ventricle_systolic =None
        self.Left_ventricle_diastolic = None
        self.Right_ventricle_systolic = None
        self.Right_ventricle_diastolic = None
    def print(self):
        print("NO.: ", self.PatientNmae)
        dic = {0: "减退", 1: "未见异常"}
        KeyVarible = ['AO根部: ', 'LA: ', 'RV常规: ', 'IVS: ', 'LVDd: ', 'LVDs: ', 'LVPW: ', 'RA横径: ', 'LVEF: ',
                           'AV: ', 'MVE: ', 'MVA: ']
        print(KeyVarible[0],self.AO)
        print(KeyVarible[1],self.LA)
        print(KeyVarible[2],self.RV)
        print(KeyVarible[3], self.IVS)
        print(KeyVarible[4], self.LVDd)
        print(KeyVarible[5], self.LVDs)
        print(KeyVarible[6], self.LVPW)
        print(KeyVarible[7], self.RA)
        print(KeyVarible[8],self.LVEF)
        print(KeyVarible[9], self.AV)
        print(KeyVarible[10], self.MVE)
        print(KeyVarible[11], self.MVA)
        if self.Left_ventricle_systolic != None:
            print("左室收缩功能: ", dic[self.Left_ventricle_systolic])
        else:
            print("未找到相关语句")
        if self.Left_ventricle_diastolic != None:
            print("左室舒张功能: ", dic[self.Left_ventricle_diastolic])
        else:
            print("未找到相关语句")


