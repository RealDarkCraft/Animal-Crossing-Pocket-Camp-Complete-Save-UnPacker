# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserMyDesignClothOneSlotSetElement(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserMyDesignClothOneSlotSetElement()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserMyDesignClothOneSlotSetElement(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserMyDesignClothOneSlotSetElement
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserMyDesignClothOneSlotSetElement
    def MyDesignId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserMyDesignClothOneSlotSetElement
    def IsChecked(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

def UserMyDesignClothOneSlotSetElementStart(builder):
    builder.StartObject(2)

def Start(builder):
    UserMyDesignClothOneSlotSetElementStart(builder)

def UserMyDesignClothOneSlotSetElementAddMyDesignId(builder, myDesignId):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(myDesignId), 0)

def AddMyDesignId(builder, myDesignId):
    UserMyDesignClothOneSlotSetElementAddMyDesignId(builder, myDesignId)

def UserMyDesignClothOneSlotSetElementAddIsChecked(builder, isChecked):
    builder.PrependUint8Slot(1, isChecked, 0)

def AddIsChecked(builder, isChecked):
    UserMyDesignClothOneSlotSetElementAddIsChecked(builder, isChecked)

def UserMyDesignClothOneSlotSetElementEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserMyDesignClothOneSlotSetElementEnd(builder)