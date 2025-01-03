# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserCraftFtrClothMakeNumOneSlot(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserCraftFtrClothMakeNumOneSlot()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserCraftFtrClothMakeNumOneSlot(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserCraftFtrClothMakeNumOneSlot
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserCraftFtrClothMakeNumOneSlot
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserCraftFtrClothMakeNumOneSlot
    def TraySize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def UserCraftFtrClothMakeNumOneSlotStart(builder):
    builder.StartObject(2)

def Start(builder):
    UserCraftFtrClothMakeNumOneSlotStart(builder)

def UserCraftFtrClothMakeNumOneSlotAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserCraftFtrClothMakeNumOneSlotAddId(builder, id)

def UserCraftFtrClothMakeNumOneSlotAddTraySize(builder, traySize):
    builder.PrependInt32Slot(1, traySize, 0)

def AddTraySize(builder, traySize):
    UserCraftFtrClothMakeNumOneSlotAddTraySize(builder, traySize)

def UserCraftFtrClothMakeNumOneSlotEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserCraftFtrClothMakeNumOneSlotEnd(builder)
