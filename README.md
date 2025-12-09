# Animal-Crossing-Pocket-Camp-Complete-Save-Unpacker
Unpack/deserialize and serialize/repack Animal Crossing Pocket Camp Complete saves

You should always make saves backup (even with vanilla saves though)

This tool allow you to unpack Animal-Crossing-Pocket-Camp-Complete saves and repack it
Files where his filename start with "__" are raw data and can be edited without deserialization

Json files are likely deserialized by the tool, so you can modify them

Binary files are likely file program couldn't deserialize, so you shouldn't edit them if you dont know what's you'r doing.

This is not a save editor, so the tool will not verify if the data you edited is correct. (For example, in some cases, modifying certain values without modifying other specific values could cause crashes.)

If you want an actual save editor you can try this one : https://github.com/MyShiLingStar/PCCE

Credits :

    @Thulinma : Original decryption key/algorithm

Information about the tool :

    1 : Acpcc folder contain flatbuffer generated binary 

    2 : If you have error about he cant find module (not the flatbuffer import error) and/or exit 84 result code, try the restore command

    2 : table.txt contain data type definition. there was some type possible like :

        Normal Types : (int, string, byte, bool...)

        Normal List Types ("list-{type}" in table.txt) : list of types like (int, string, byte, bool...)

        subEntries data ("vectorn-{VectorName}" in table.txt) : sub element (like json)

        list of subEntries data ("vector-{VectorName}" in table.txt) : list of sub element (like list of json)
    
    the structure was : {KeyBaseName : {"tableData"|rootTableDef: [{"name":..., "type":...}, ...], "vector": [{"vectorName":..., "vectorData": [{"name":..., "type":...}, ...]}, ...]}, ...}
