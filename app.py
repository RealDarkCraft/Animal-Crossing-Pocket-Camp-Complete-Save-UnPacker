import subprocess
import importlib
import os
import json
import binascii
import hashlib
import time

try:
    import flatbuffers
except:
    print("Please install flatbuffers module")

class Extractor:
    def __init__(self, serialization):
        self.pos = 0
        self.serial = serialization
    def read(self, byte):
        data_byte = data[self.pos:self.pos+byte]
        self.pos += byte
        return data_byte
    def seek(self, length):
        self.pos = length
    def bi(self, byte): # bi = byte -> int
        return int.from_bytes(byte, byteorder = "big")
    def Repack(self, inputfolder):
        data = b""
        filelist = open(fr"{inputfolder}/filelist.txt","r").read().split("\n")
        filelist = filelist[0:len(filelist)-1]
        print("Repacking :")
        percentage = 0
        baseOffset = 80
        filelistlen = len(filelist)
        for i in filelist:
            percentage += 1
            if (percentage % 500 == 0):
                print(fr"{((100/(filelistlen*3)) * percentage):.2f}%", end = "\r")
            baseOffset += len(i)+24
        data = b""
        pos = 0
        fileoffset = []
        for i in filelist:
            percentage += 1
            if (percentage % 60 == 0):
                print(fr"{((100/(filelistlen*3)) * percentage):.2f}%", end = "\r")
            
            tmp = open(fr"{inputfolder}/{i}", "rb").read()
            try:
                if self.serial.table.get(i.split("_")[0]) != None:
                    tmp = self.serial.serialize(json.loads(tmp.decode()), i)
            except Exception as e:
                print(f"Error when serialize {i} :\n{e}")
                exit(84)
            data += tmp
            fileoffset.append([baseOffset+pos, len(tmp)])
            pos += len(tmp)
        
        listheader = b""
        idx = 0
        for i in filelist:
            percentage += 1
            if (percentage % 100 == 0):
                print(fr"{((100/(filelistlen*3)) * percentage):.2f}%", end = "\r")

            listheader += b"C4SI"
            listheader += (len(i)).to_bytes(4, byteorder = "big")
            listheader += i.encode()
            listheader += (fileoffset[idx][1]).to_bytes(8, byteorder = "big")
            listheader += (fileoffset[idx][0]).to_bytes(8, byteorder = "big")
            idx += 1
            
        binary_nohead = listheader+data
        binary = b"C4SH"+(1).to_bytes(4, byteorder ="big")+len(filelist).to_bytes(4, byteorder ="big")+binary_nohead
        data = b"C4FH"+hashlib.sha256(binary).hexdigest().encode()+binary
        print(fr"{100.00:.2f}%\n", end = "\r")
        return data
        
    def Extract(self, data, outputfolder):
        fullsave = {}
        self.data = data
        extractor = []
        hashs = self.read(68)
        if self.read(4).decode() == "C4SH":
            self.read(4)
            entry_num = self.read(4)
        else:
            print("Bad file :")
            return False
        percentage = 0
        print("Extracting files :")
        for i in range(int.from_bytes(entry_num, byteorder = "big")):
            percentage += 1
            if (percentage % 50 == 0):
                print(fr"{((100/(len(extractor)*2)) * percentage):.2f}%", end = "\r")
            origin = self.read(4)
            string_size = self.read(4)
            string = self.read(int.from_bytes(string_size, byteorder = "big"))
            size = self.read(8)
            offset = self.read(8)
            extractor.append({"name":string.decode(), "offset":self.bi(offset), "size":self.bi(size)})
        os.makedirs(outputfolder, exist_ok = True)
        filelist = ""
        
        for i in extractor:
            error = False
            filelist += f"{i['name']}\n"
            percentage += 1
            if (percentage % 50 == 0):
                print(fr"{((100/(len(extractor)*2)) * percentage):.2f}%", end = "\r")
            if self.serial.table.get(i["name"].split("_")[0]) != None:
                with open(fr"{outputfolder}/{i['name']}", "w", encoding = "utf-8") as f:
                    self.seek(i["offset"])
                    try:
                        des_json = self.serial.deserialize(self.read(i["size"]), i["name"])
                        fullsave[i['name']] = des_json
                        json.dump(des_json, f, ensure_ascii = False, indent = 4)
                    except Exception as e:
                        print(f"Error extracting {i['name']}\n{e}\n")
                        exit(84) # Remove this line if your save have table def that wasent in table.txt
                        error = True
            else:
                with open(fr"{outputfolder}/{i['name']}", "wb") as f:
                    self.seek(i["offset"])
                    f.write(self.read(i["size"]))
            if error == True:
                with open(fr"{outputfolder}/{i['name']}", "wb") as f:
                    self.seek(i["offset"])
                    f.write(self.read(i["size"]))
        print(fr"{100.00:.2f}%", end = "\r")
        with open(fr"{outputfolder}/filelist.txt","w", encoding = "utf-8") as flist:
            flist.write(filelist)
        return True
class Decryptor:
    def __init__(self):
        self.xorkey = (
        b"x\2553\034\026\232\260\226\311\225D\263$\221\020f5\265\362;\366h\352\033\225\273\230\2719\005\270H\243\273\261y\0222\257'[\005\203\210O\326\267X1\230\367\242\266T-!\301:\341\240;\254\342\250\315\177'\230\332U&3\314t\3538\220\221\351\274"
        b"\244\346_\321\327\361\221\300\274\267\215-\243tO\0165\372\224fn\336|\210n\000J\233o\rtj\216\265\204I\023\022\223+\177*W@{\200\322\353Y5\206\036\3369\315\330\363\204\021\010\216\356\222\031{\036\360\254kY\245\032\270\206\365(B\002\306{"
        b"\316\025\305\007h\302\330\252\347bO/\263\007|\246\323Z\252<\255#?uX\315\006\311\320\247\243:\326\252\370Xb\306\255oR\r\024\260\277^\323\270>\267\2243iM\353_S\337\332R\032U\000\202\230\301\031\367\236\320\016\2433pZa\201\223\035\235"
        b"\021\r\242\371\017\266\023m\276\244\343\250\247\302~\024\333\244\032\177d6W\035\375\026A\220I\220\262\370\262\034.WdD\t\266+\021\336o\347\332\256\207\264\347J\275\360\252\354.U\355\266\362gq\204^\351M\230\257N!\3224vC\247$\235\373\216\306"
        b"\030\366\3656X\0064n3\027\302\315r\333\367\327\335+\343\377\264\347\031p9k\244\213\224\243\211>\026\025\264N\232\265\003e\376\236\243Dv\374/\320\315\360R\205\377l\316u\364\343\326_c\366\345\274,\335\367=\265[\213\265_\340\342o\213\3577*"
        b"HH]u!'q\352y\214\034;\213(\"G\201\201e\242\2333\374Y\202GF\300H\267v\325\302\221\246\024\306D[+~\215te\215\177\244\277\302\221\022\002&\350\224x3\323\342\234C\371\342\005\t\262\351zk\233\367`\307\360?\215K\225\004\274"
        b"\325\362\315\215af\000\244',WR\304\177\007\357\207\242$H\326\220w8\223C<\177\257?\021\2079)\340LlUy\346\346\177\020\327\261\233\226\266\307\306+I\000\233\340\036\036|\261rs?\272-\205UK`Z\021\320\304\241\035\r\325/}%\t"
        b"\000\\e\315\324\037\002\362\235%\316\001[\266\345\301\270'\221w\224\003\034\023'\345\235T\313\221\354\204O\271p\250\303\326\036\310\310\3224\333\214c\024\211\010\333\t\235{\210v\020\"\245\341V\266\366~\327f\261\036u^\261\334ES\023)\224V\026\345\347"
        b"\270\272\033\346h9\253@\242\254pZCt\2005+y\306\226\216\277\013\022OP\224?\250\302\300\310Mj\3560;\373\233\024\360\301\0018N\273[hT\272'\341\263~5YKN*\317\337\272X\325Z\272\351\354\030,\313\037\"\016\202\207/\177\n\343"
        b"\242\007si\334\r \005\212A\233\271]\276\260\000\304\273\034\345q\003\001\177\367\031\300\265_\217P\346C\3173\306*\256\3129\023\213\273\2616\246\321F\014\315\205WPny\365\036v\026z\036Z\330\023~\335\001\262]_~M\3634vZ;f\262o"
        b"\255 \364 \013+Z\337[\375{FU\006O\234\377-0\350\256\201pp\036\026\t\255y\013\337\\\3577\n\345J\220\345\203\344e\326\035\303\263\004\362\224\204^CY\365\r\255\223\352\355\260\310%\377\253~\345\326\252\217\214$\276K\317\337\222\254\360\251\347"
        b"\374\360jU\022\267\010\241'\261v*\016'\\\252q\372=\371\333\242\301gw\016\374\037C\370<X\343M\324+.)\230\334.\307w\002\254_\224~!>\341RC\263r\321V\331b\302\006u\360\003\320\227\265\356\010jp\327\2258\314j<d\303&"
        b"Q19\201\n\206\027\270Y\216\321\036C\351T\372\233\314\2207\241\315o!\216\344\\'\207\243\207\205x\021\362n\262o.*")
    def Shift(self, data, output):
        # Encrypt/Decrypt data in a separated file for optimization
        print("Decrypting/Encrypting file :")
        idx = 0
        datalenght = len(data)
        with open(f"{output}/shifted.bin","wb") as f:
            for i in data:
                f.write((i ^ self.xorkey[idx % 999]).to_bytes(1, byteorder = "big"))
                idx += 1
                if ((idx %10000) == 0):
                    print(fr"{((100/datalenght) * idx):.2f}%", end = "\r")
        print("100.00%\n")
        dec = open(f"{output}/shifted.bin","rb").read()
        os.remove(f"{output}/shifted.bin")
        return dec
class Serialization:
    def __init__(self):
        self.table = json.load(open("table.txt"))
        
    def Build(self, tablename, namescape):
        data = f"namespace {namescape};\n\n"
        json_1 = self.table[tablename]
        for vec in json_1["vector"]:
            data += f"table {vec['vectorName']} "+ "{\n"
            for i in vec["vectorData"]:
                if "-" in i["type"] and i["type"].split("-")[0] == "vector":
                    data += f"  {i['name']}: [{i['type'].split('-')[1]}];\n"
                elif "-" in i["type"] and i["type"].split("-")[0] == "vectorn":
                    data += f"  {i['name']}: {i['type'].split('-')[1]};\n"
                elif "-" in i["type"] and i["type"].split("-")[0] == "list":
                    data += f"  {i['name']}: [{i['type'].split('-')[1]}];\n"
                else:
                    data += f"  {i['name']}: {i['type']};\n"
            data += "}\n\n"
        data += f"table {tablename} "+ "{\n"
        for i in json_1["tableData"]:
            if "-" in i["type"] and i["type"].split("-")[0] == "vector":
                data += f"  {i['name']}: [{i['type'].split('-')[1]}];\n"
            elif "-" in i["type"] and i["type"].split("-")[0] == "vectorn":
                data += f"  {i['name']}: {i['type'].split('-')[1]};\n"
            elif "-" in i["type"] and i["type"].split("-")[0] == "list":
                data += f"  {i['name']}: [{i['type'].split('-')[1]}];\n"
            else:
                data += f"  {i['name']}: {i['type']};\n"
        data += "}\n\n"
        open("temp.fbs","w").write(data)
        subprocess.call(["flatc", "--python", "temp.fbs"])
    
    def deserializeVectorList(self, key, base_module, json_1, namescape):
        for vec in json_1["vector"]:
            if vec["vectorName"] == key["type"].split("-")[1]:
                tmp = []
                count = getattr(base_module, self.UpperString(key["name"])+"Length")()
                for cnt in range(count):
                    js_temp = {}
                    idx = getattr(base_module, self.UpperString(key["name"]))(cnt)
                    for veckey in vec["vectorData"]:
                        if "-" in veckey["type"] and veckey["type"].split("-")[0] == "vector":
                            tmp_val = (self.deserializeVectorList(veckey, idx, json_1, namescape))
                        elif "-" in veckey["type"] and veckey["type"].split("-")[0] == "vectorn":
                            tmp_val = (self.deserializeVector(veckey, idx, json_1, namescape))
                        elif "-" in veckey["type"] and veckey["type"].split("-")[0] == "list":
                            tmp_val = (self.deserializeList(veckey, idx, json_1, namescape))
                        else:
                            tmp_val = getattr(idx, self.UpperString(veckey["name"]))()
                            if (veckey["type"] == "string"):
                                if tmp_val != None:
                                    tmp_val = tmp_val.decode()
                                else:
                                    tmp_val = ""
                        js_temp[veckey["name"]] = tmp_val
                    tmp.append(js_temp)
                return tmp
    def deserializeVector(self, key, base_module, json_1, namescape):
        for vec in json_1["vector"]:
            if vec["vectorName"] == key["type"].split("-")[1]:
                js_temp = {}
                idx = getattr(base_module, self.UpperString(key["name"]))()                
                if idx != None:
                    for veckey in vec["vectorData"]:
                        if "-" in veckey["type"] and veckey["type"].split("-")[0] == "vector":
                            tmp_val = (self.deserializeVectorList(veckey, idx, json_1, namescape))
                        elif "-" in veckey["type"] and veckey["type"].split("-")[0] == "vectorn":
                            tmp_val = (self.deserializeVector(veckey, idx, json_1, namescape))
                        elif "-" in veckey["type"] and veckey["type"].split("-")[0] == "list":
                            tmp_val.append(self.deserializeList(veckey, idx, json_1, namescape))
                        else:
                            tmp_val = getattr(idx, self.UpperString(veckey["name"]))()
                            if (veckey["type"] == "string"):
                                if tmp_val != None:
                                    tmp_val = tmp_val.decode()
                                else:
                                    tmp_val = ""
                        js_temp[veckey["name"]] = tmp_val
                return js_temp
        
    def deserializeList(self, key, base_module, json_1, namescape):
        tmp = []
        count = getattr(base_module, self.UpperString(key["name"])+"Length")()
        for cnt in range(count):
            idx = getattr(base_module, self.UpperString(key["name"]))(cnt)
            if key["type"].split("-")[1] == "string":
                if idx != None:
                    idx = idx.decode()
                else:
                    idx = ""
            tmp.append(idx)
        return tmp
        
                                
        
    def deserialize(self, binary, file):
        self.buf = binary
        filename = file.split("/")[len(file.split("/"))-1]
        tablename = filename.split("_")[0]
        namescape = "Acpcc"
        
        
        if self.table.get(tablename) != None:
            json_1 = self.table[tablename]
            result = {} 
            table_import = importlib.import_module(f"{namescape}.{tablename}")
            table_get = getattr(getattr(table_import, tablename),"GetRootAs")(self.buf, 0)
            for i in json_1["tableData"]:
                if "-" in i["type"] and i["type"].split("-")[0] == "vector":
                    result[i["name"]] = self.deserializeVectorList(i, table_get, json_1, namescape)
                elif "-" in i["type"] and i["type"].split("-")[0] == "vectorn":
                    result[i["name"]] = self.deserializeVector(i, table_get, json_1, namescape)
                    
                    
                elif "-" in i["type"] and i["type"].split("-")[0] == "list":
                    result[i["name"]] = self.deserializeList(i, table_get, json_1, namescape)  
                else:
                    result[i["name"]] = getattr(table_get, self.UpperString(i["name"]))()
                    if i["type"] == "string":
                        if result[i["name"]] != None:
                            result[i["name"]] = result[i["name"]].decode()
                        else:
                            result[i["name"]] = ""
            return result
        return None
    
    def UpperString(self, string):
        new_string = ""
        a = string.split("_")
        for i in a:
            new_string += i[0].upper()+i[1:] 
        return new_string 
    
    def serializeVector(self, json_data, key, base_module, json_1, namescape):
        for vec in json_1["vector"]:
            if "-" in key["type"] and key["type"].split("-")[1] == vec["vectorName"]:
                vec_import = importlib.import_module(f"{namescape}.{vec['vectorName']}")
                vecidx = json_data[key["name"]]
                if vecidx != {}:
                    list_data = []
                    for veckey in vec["vectorData"]:
                        if "-" in veckey["type"] and veckey["type"].split("-")[0] == "vector":
                            new_module = importlib.import_module(f"{namescape}.{vec['vectorName']}")
                            list_data.append(self.serializeVectorList(vecidx, veckey, new_module, json_1, namescape))
                        elif "-" in veckey["type"] and veckey["type"].split("-")[0] == "vectorn":
                            new_module = importlib.import_module(f"{namescape}.{vec['vectorName']}")
                            list_data.append(self.serializeVector(vecidx, veckey, new_module, json_1, namescape))
                        elif "-" in veckey["type"] and veckey["type"].split("-")[0] == "list":
                            new_module = importlib.import_module(f"{namescape}.{vec['vectorName']}")
                            list_data.append(self.serializeList(vecidx, veckey, new_module))
                        else:
                            t = vecidx[veckey["name"]]
                            if type(t) == str:
                                t = self.builder.CreateString(t.encode())
                            list_data.append(t)
                    getattr(vec_import, "Start")(self.builder)
                    idx = 0
                    for veckey in vec["vectorData"]:
                        getattr(vec_import, f"Add{self.UpperString(veckey['name'])}")(self.builder, list_data[idx])
                        idx+=1
                    return getattr(vec_import, "End")(self.builder)
                return None

    def serializeVectorList(self, json_data, key, base_module, json_1, namescape):
        for vec in json_1["vector"]:
            if "-" in key["type"] and key["type"].split("-")[1] == vec["vectorName"]:
                list_data = []
                vec_import = importlib.import_module(f"{namescape}.{vec['vectorName']}")
                
                for vecidx in json_data[key["name"]]:
                    value_tab = []
                    for veckey in vec["vectorData"]:
                        if "-" in veckey["type"] and veckey["type"].split("-")[0] == "vector":
                            new_module = importlib.import_module(f"{namescape}.{vec['vectorName']}")
                            value_tab.append(self.serializeVectorList(vecidx, veckey, new_module, json_1, namescape))
                        elif "-" in veckey["type"] and veckey["type"].split("-")[0] == "vectorn":
                            new_module = importlib.import_module(f"{namescape}.{vec['vectorName']}")
                            value_tab.append(self.serializeVector(vecidx, veckey, new_module, json_1, namescape))
                        elif "-" in veckey["type"] and veckey["type"].split("-")[0] == "list":
                            new_module = importlib.import_module(f"{namescape}.{vec['vectorName']}")
                            value_tab.append(self.serializeList(vecidx, veckey, new_module))
                        else:
                            t = vecidx[veckey["name"]]
                            if type(t) == str:
                                t = self.builder.CreateString(t.encode())
                            value_tab.append(t)
                    getattr(vec_import, "Start")(self.builder)
                    idx = 0
                    for veckey in vec["vectorData"]:
                        getattr(vec_import, f"Add{self.UpperString(veckey['name'])}")(self.builder, value_tab[idx])
                        idx+=1
                    list_data.append(getattr(vec_import, "End")(self.builder))
                getattr(base_module, f"Start{self.UpperString(key['name'])}Vector")(self.builder, len(list_data))
                for weap in reversed(list_data):
                    self.builder.PrependUOffsetTRelative(weap)
                return self.builder.EndVector()          
        
    
    def serializeList(self, json_data, key, base_module):
        list_data = []
        for listidx in json_data[key["name"]]:
            t = listidx
            if (key["type"].split("-")[1] == "string"):
                t = self.builder.CreateString(t.encode())
            list_data.append(t)
        getattr(base_module, f"Start{self.UpperString(key['name'])}Vector")(self.builder, len(list_data))

        for s in reversed(list_data):
            if (key["type"].split("-")[1] == "string"):
                self.builder.PrependUOffsetTRelative(s)
            elif (key["type"].split("-")[1] == "short"):
                self.builder.PrependInt16(s)
            elif (key["type"].split("-")[1] == "ushort"):
                self.builder.PrependUint16(s)
            elif (key["type"].split("-")[1] == "uint"):
                self.builder.PrependUint32(s)
            elif (key["type"].split("-")[1] == "int"):
                self.builder.PrependInt32(s)
            elif (key["type"].split("-")[1] == "long"):
                self.builder.PrependInt64(s)
            elif (key["type"].split("-")[1] == "bool"):
                self.builder.PrependBool(s)
            elif (key["type"].split("-")[1] == "ubyte"):
                self.builder.PrependUint8(s)
        return self.builder.EndVector()
        
    
    def serialize(self, json_data, file):
        filename = file.split("\\")[len(file.split("\\"))-1]
        tablename = filename.split("_")[0]
        namescape = "Acpcc"
        if self.table.get(tablename) != None:
            self.builder = flatbuffers.Builder(2048)
            json_1 = self.table[tablename]
            base_module = importlib.import_module(f"{namescape}.{tablename}")
            
            values = []
            for key in json_1["tableData"]:
                if "-" in key["type"] and key["type"].split("-")[0] == "vector":
                    values.append(self.serializeVectorList(json_data, key, base_module, json_1, namescape))
                elif "-" in key["type"] and key["type"].split("-")[0] == "vectorn":
                    values.append(self.serializeVector(json_data, key, base_module, json_1, namescape))
                elif "-" in key["type"] and key["type"].split("-")[0] == "list":
                    values.append(self.serializeList(json_data, key, base_module))
                else:
                    t = json_data[key["name"]]
                    if (type(t) == str):
                        t = t = self.builder.CreateString(t.encode())
                    values.append(t)
            idx = 0
            getattr(base_module, "Start")(self.builder)
            for key in json_1["tableData"]:
                if values[idx] != None:
                    getattr(base_module, f"Add{self.UpperString(key['name'])}")(self.builder, values[idx])
                idx += 1
            
            
            

            data_offset = getattr(base_module, "End")(self.builder)
            self.builder.Finish(data_offset, b"D4AO")
            
            return self.builder.Output()
        return None

if __name__ == "__main__":
    while True:
        try:
            a = Serialization()
                
            q = input("0 : Extract | 1 : Repack | q : quit | restore : (generate flatbuffer bin files)\n")
            if (q == "q"):
                exit(0)
            elif (q == "restore"):
                temp = open("restore_data.txt").read().split("\n")
                templenght = len(temp)
                percentage = 0
                for i in temp:
                    percentage += 1
                    if (percentage%20 == 0):
                        print(fr"{((100/templenght) * percentage):.2f}%", end = "\r")
                    if (i != ""):
                        a.Build(i, "Acpcc")
                print("100.00%")
            else:
                q = int(q)
                if (q == 0):
                    while True:
                        filename = input("Input file : ")
                        try:
                            filename = filename.replace("\\","/")
                            open(filename, "rb")
                            break
                        except:
                            print("Bad path")
                    while True:
                        outputfolder = input("Output folder : ")
                        try:
                            outputfolder = outputfolder.replace("\\","/")
                            os.makedirs(outputfolder, exist_ok = True)
                            empty_verify = os.listdir(outputfolder)
                            if empty_verify == []:
                                break
                            else:
                                print("The output folder need to be empty")
                        except:
                            print("Bad path")
                    print("\n")
                    data = open(filename,"rb").read()
                    data = Decryptor().Shift(data, outputfolder)
                    target_hash = data[4:68]
                    hashs = hashlib.sha256(data[68:]).hexdigest().encode()
                    if target_hash == hashs:
                        Extractor(a).Extract(data, outputfolder)
                    else:
                        print("Invalide decrypted hashs. Aborting\n")
                        time.sleep(0.1)
                        exit(84)
                    print("\n")
                
                elif (q == 1):
                    while True:
                        inputfolder = input("Input folder : ")
                        try:
                            inputfolder = inputfolder.replace("\\","/")
                            if os.path.exists(inputfolder):
                                break
                        except:
                            print("Bad path")
                    while True:
                        outputfile = input("Output File : ")
                        try:
                            outputfile = outputfile.replace("\\","/")
                            open(outputfile, "wb")
                            break
                        except:
                            print("Bad path\n")
                    print("\n")
                    data = Extractor(a).Repack(inputfolder)
                    data = Decryptor().Shift(data, inputfolder)
                    open(outputfile, "wb").write(data)
                    print("\n")
                else:
                    print("Unknown mode\n")
        except ValueError:
            print("Unknown mode\n")
        except Exception as e:
            raise e
            print(e)
