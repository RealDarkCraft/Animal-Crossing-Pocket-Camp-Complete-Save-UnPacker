# Animal-Crossing-Pocket-Camp-Complete Save Unpacker

Unpack/deserialize and repack/serialize Animal Crossing Pocket Camp Complete save files.

> ⚠️ **Always back up your saves before using this tool** — even unmodified ones.

---

## Overview

This tool lets you unpack ACPCC save files into editable formats, and repack them afterward.

- Files prefixed with `__` are **raw data** and can be edited directly without deserialization.
- `.json` files are **deserialized** — safe to edit.
- Binary files are **serialized** — do not edit unless you know exactly what you're doing.

> 🛑 **This is not a save editor.** The tool does not validate your changes. For example, modifying certain values without updating related fields can cause crashes.

If you want a proper save editor, check out: [PCCE by MyShiLingStar](https://github.com/MyShiLingStar/PCCE)

---

## Credits

- **@Thulinma** — Original decryption key and algorithm

---

## Technical Notes

### General

- The `acpcc/` folder contains FlatBuffer-generated binaries.
- If you get a "module not found" error (not the FlatBuffer import error) or an exit code `84`, run the **restore** command.

### table.txt — Data Type Definitions

`table.txt` defines the data types used in the save files. The supported types are:

- **Normal types** — `int`, `string`, `byte`, `bool`, etc.
- **Normal list types** (`list-{type}`) — lists of normal types, e.g. `list-int`, `list-string`
- **Sub-entry data** (`vectorn-{VectorName}`) — a single sub-element (similar to a JSON object)
- **List of sub-entries** (`vector-{VectorName}`) — a list of sub-elements (similar to a JSON array)

### Schema Structure

```json
{
  "KeyBaseName": {
    "tableData": [
      { "name": "...", "type": "..." }
    ],
    "vector": [
      {
        "vectorName": "...",
        "vectorData": [
          { "name": "...", "type": "..." }
        ]
      }
    ]
  }
}
```
