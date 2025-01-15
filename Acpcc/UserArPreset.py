# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserArPreset(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserArPreset()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserArPreset(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserArPreset
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserArPreset
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserArPreset
    def PresetGroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserArPreset
    def State(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def UserArPresetStart(builder):
    builder.StartObject(3)

def Start(builder):
    UserArPresetStart(builder)

def UserArPresetAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserArPresetAddId(builder, id)

def UserArPresetAddPresetGroup(builder, presetGroup):
    builder.PrependInt32Slot(1, presetGroup, 0)

def AddPresetGroup(builder, presetGroup):
    UserArPresetAddPresetGroup(builder, presetGroup)

def UserArPresetAddState(builder, state):
    builder.PrependInt32Slot(2, state, 0)

def AddState(builder, state):
    UserArPresetAddState(builder, state)

def UserArPresetEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserArPresetEnd(builder)