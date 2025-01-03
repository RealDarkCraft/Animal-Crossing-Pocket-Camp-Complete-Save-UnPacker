# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserMySetLayoutOneSlotSetElement(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserMySetLayoutOneSlotSetElement()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserMySetLayoutOneSlotSetElement(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserMySetLayoutOneSlotSetElement
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserMySetLayoutOneSlotSetElement
    def MySetId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserMySetLayoutOneSlotSetElement
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserMySetLayoutOneSlotSetElement
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserMySetLayoutOneSlotSetElement
    def LightFlag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserMySetLayoutOneSlotSetElement
    def WindowFlag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserMySetLayoutOneSlotSetElement
    def LargeObjList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # UserMySetLayoutOneSlotSetElement
    def LargeObjListAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # UserMySetLayoutOneSlotSetElement
    def LargeObjListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserMySetLayoutOneSlotSetElement
    def LargeObjListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # UserMySetLayoutOneSlotSetElement
    def TerrainList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # UserMySetLayoutOneSlotSetElement
    def TerrainListAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # UserMySetLayoutOneSlotSetElement
    def TerrainListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserMySetLayoutOneSlotSetElement
    def TerrainListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

    # UserMySetLayoutOneSlotSetElement
    def LargeObjLevelList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # UserMySetLayoutOneSlotSetElement
    def LargeObjLevelListAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # UserMySetLayoutOneSlotSetElement
    def LargeObjLevelListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserMySetLayoutOneSlotSetElement
    def LargeObjLevelListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        return o == 0

def UserMySetLayoutOneSlotSetElementStart(builder):
    builder.StartObject(8)

def Start(builder):
    UserMySetLayoutOneSlotSetElementStart(builder)

def UserMySetLayoutOneSlotSetElementAddMySetId(builder, mySetId):
    builder.PrependInt32Slot(0, mySetId, 0)

def AddMySetId(builder, mySetId):
    UserMySetLayoutOneSlotSetElementAddMySetId(builder, mySetId)

def UserMySetLayoutOneSlotSetElementAddName(builder, name):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)

def AddName(builder, name):
    UserMySetLayoutOneSlotSetElementAddName(builder, name)

def UserMySetLayoutOneSlotSetElementAddType(builder, type):
    builder.PrependUint32Slot(2, type, 0)

def AddType(builder, type):
    UserMySetLayoutOneSlotSetElementAddType(builder, type)

def UserMySetLayoutOneSlotSetElementAddLightFlag(builder, lightFlag):
    builder.PrependBoolSlot(3, lightFlag, 0)

def AddLightFlag(builder, lightFlag):
    UserMySetLayoutOneSlotSetElementAddLightFlag(builder, lightFlag)

def UserMySetLayoutOneSlotSetElementAddWindowFlag(builder, windowFlag):
    builder.PrependBoolSlot(4, windowFlag, 0)

def AddWindowFlag(builder, windowFlag):
    UserMySetLayoutOneSlotSetElementAddWindowFlag(builder, windowFlag)

def UserMySetLayoutOneSlotSetElementAddLargeObjList(builder, largeObjList):
    builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(largeObjList), 0)

def AddLargeObjList(builder, largeObjList):
    UserMySetLayoutOneSlotSetElementAddLargeObjList(builder, largeObjList)

def UserMySetLayoutOneSlotSetElementStartLargeObjListVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartLargeObjListVector(builder, numElems):
    return UserMySetLayoutOneSlotSetElementStartLargeObjListVector(builder, numElems)

def UserMySetLayoutOneSlotSetElementAddTerrainList(builder, terrainList):
    builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(terrainList), 0)

def AddTerrainList(builder, terrainList):
    UserMySetLayoutOneSlotSetElementAddTerrainList(builder, terrainList)

def UserMySetLayoutOneSlotSetElementStartTerrainListVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartTerrainListVector(builder, numElems):
    return UserMySetLayoutOneSlotSetElementStartTerrainListVector(builder, numElems)

def UserMySetLayoutOneSlotSetElementAddLargeObjLevelList(builder, largeObjLevelList):
    builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(largeObjLevelList), 0)

def AddLargeObjLevelList(builder, largeObjLevelList):
    UserMySetLayoutOneSlotSetElementAddLargeObjLevelList(builder, largeObjLevelList)

def UserMySetLayoutOneSlotSetElementStartLargeObjLevelListVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartLargeObjLevelListVector(builder, numElems):
    return UserMySetLayoutOneSlotSetElementStartLargeObjLevelListVector(builder, numElems)

def UserMySetLayoutOneSlotSetElementEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserMySetLayoutOneSlotSetElementEnd(builder)
