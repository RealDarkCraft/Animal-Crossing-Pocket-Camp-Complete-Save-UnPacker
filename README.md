# Animal-Crossing-Pocket-Camp-Complete-Save-Unpacker
Unpack/deserialize and serialize/repack Animal Crossing Pocket Camp Complete saves

This tool allow you to unpack Animal-Crossing-Pocket-Camp-Complete saves and repack it
Files which his name start with "__" are raw data and can be directly edited
Files that was json are deserialized files and can be edited
If a file was a binary file you should dont edit it if you dont know what you do

This is not a save editor, so the tool will not verify if the data you edited was correct and wont corrupt you file (Even if iirc if you made bad change the tool could throw error when re-serialize)

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
