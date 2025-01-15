# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserCraftFtrClothOneSlotSetElement(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserCraftFtrClothOneSlotSetElement()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserCraftFtrClothOneSlotSetElement(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserCraftFtrClothOneSlotSetElement
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserCraftFtrClothOneSlotSetElement
    def ItemLabel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserCraftFtrClothOneSlotSetElement
    def IsUnlocked(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserCraftFtrClothOneSlotSetElement
    def IsNew(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserCraftFtrClothOneSlotSetElement
    def CreateCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserCraftFtrClothOneSlotSetElement
    def KeyId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def UserCraftFtrClothOneSlotSetElementStart(builder):
    builder.StartObject(5)

def Start(builder):
    UserCraftFtrClothOneSlotSetElementStart(builder)

def UserCraftFtrClothOneSlotSetElementAddItemLabel(builder, itemLabel):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(itemLabel), 0)

def AddItemLabel(builder, itemLabel):
    UserCraftFtrClothOneSlotSetElementAddItemLabel(builder, itemLabel)

def UserCraftFtrClothOneSlotSetElementAddIsUnlocked(builder, isUnlocked):
    builder.PrependBoolSlot(1, isUnlocked, 0)

def AddIsUnlocked(builder, isUnlocked):
    UserCraftFtrClothOneSlotSetElementAddIsUnlocked(builder, isUnlocked)

def UserCraftFtrClothOneSlotSetElementAddIsNew(builder, isNew):
    builder.PrependBoolSlot(2, isNew, 0)

def AddIsNew(builder, isNew):
    UserCraftFtrClothOneSlotSetElementAddIsNew(builder, isNew)

def UserCraftFtrClothOneSlotSetElementAddCreateCount(builder, createCount):
    builder.PrependInt32Slot(3, createCount, 0)

def AddCreateCount(builder, createCount):
    UserCraftFtrClothOneSlotSetElementAddCreateCount(builder, createCount)

def UserCraftFtrClothOneSlotSetElementAddKeyId(builder, keyId):
    builder.PrependUint32Slot(4, keyId, 0)

def AddKeyId(builder, keyId):
    UserCraftFtrClothOneSlotSetElementAddKeyId(builder, keyId)

def UserCraftFtrClothOneSlotSetElementEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserCraftFtrClothOneSlotSetElementEnd(builder)