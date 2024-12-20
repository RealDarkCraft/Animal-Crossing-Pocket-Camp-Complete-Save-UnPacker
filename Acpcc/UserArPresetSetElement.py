# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserArPresetSetElement(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserArPresetSetElement()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserArPresetSetElement(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserArPresetSetElement
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserArPresetSetElement
    def PresetGroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserArPresetSetElement
    def State(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def UserArPresetSetElementStart(builder):
    builder.StartObject(2)

def Start(builder):
    UserArPresetSetElementStart(builder)

def UserArPresetSetElementAddPresetGroup(builder, presetGroup):
    builder.PrependInt32Slot(0, presetGroup, 0)

def AddPresetGroup(builder, presetGroup):
    UserArPresetSetElementAddPresetGroup(builder, presetGroup)

def UserArPresetSetElementAddState(builder, state):
    builder.PrependInt32Slot(1, state, 0)

def AddState(builder, state):
    UserArPresetSetElementAddState(builder, state)

def UserArPresetSetElementEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserArPresetSetElementEnd(builder)