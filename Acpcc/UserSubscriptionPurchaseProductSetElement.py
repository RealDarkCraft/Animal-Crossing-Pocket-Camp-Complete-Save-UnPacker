# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserSubscriptionPurchaseProductSetElement(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserSubscriptionPurchaseProductSetElement()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserSubscriptionPurchaseProductSetElement(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserSubscriptionPurchaseProductSetElement
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserSubscriptionPurchaseProductSetElement
    def ProductId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # UserSubscriptionPurchaseProductSetElement
    def StartsAt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserSubscriptionPurchaseProductSetElement
    def EndsAt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserSubscriptionPurchaseProductSetElement
    def EntryLastEndsAt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserSubscriptionPurchaseProductSetElement
    def RewardUnlockBaseDay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # UserSubscriptionPurchaseProductSetElement
    def RewardUnlockDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserSubscriptionPurchaseProductSetElement
    def RewardUnlockCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserSubscriptionPurchaseProductSetElement
    def RewardUnlockedCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserSubscriptionPurchaseProductSetElement
    def ReceiptLastEndsAt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserSubscriptionPurchaseProductSetElement
    def ReceiptUpdateEndsAt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserSubscriptionPurchaseProductSetElement
    def ReceiptUpdateCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserSubscriptionPurchaseProductSetElement
    def ExpenctancyEndsAt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserSubscriptionPurchaseProductSetElement
    def ContractStartAt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # UserSubscriptionPurchaseProductSetElement
    def InvalidEndsAt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def UserSubscriptionPurchaseProductSetElementStart(builder):
    builder.StartObject(14)

def Start(builder):
    UserSubscriptionPurchaseProductSetElementStart(builder)

def UserSubscriptionPurchaseProductSetElementAddProductId(builder, productId):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(productId), 0)

def AddProductId(builder, productId):
    UserSubscriptionPurchaseProductSetElementAddProductId(builder, productId)

def UserSubscriptionPurchaseProductSetElementAddStartsAt(builder, startsAt):
    builder.PrependInt64Slot(1, startsAt, 0)

def AddStartsAt(builder, startsAt):
    UserSubscriptionPurchaseProductSetElementAddStartsAt(builder, startsAt)

def UserSubscriptionPurchaseProductSetElementAddEndsAt(builder, endsAt):
    builder.PrependInt64Slot(2, endsAt, 0)

def AddEndsAt(builder, endsAt):
    UserSubscriptionPurchaseProductSetElementAddEndsAt(builder, endsAt)

def UserSubscriptionPurchaseProductSetElementAddEntryLastEndsAt(builder, entryLastEndsAt):
    builder.PrependInt64Slot(3, entryLastEndsAt, 0)

def AddEntryLastEndsAt(builder, entryLastEndsAt):
    UserSubscriptionPurchaseProductSetElementAddEntryLastEndsAt(builder, entryLastEndsAt)

def UserSubscriptionPurchaseProductSetElementAddRewardUnlockBaseDay(builder, rewardUnlockBaseDay):
    builder.PrependUint8Slot(4, rewardUnlockBaseDay, 0)

def AddRewardUnlockBaseDay(builder, rewardUnlockBaseDay):
    UserSubscriptionPurchaseProductSetElementAddRewardUnlockBaseDay(builder, rewardUnlockBaseDay)

def UserSubscriptionPurchaseProductSetElementAddRewardUnlockDate(builder, rewardUnlockDate):
    builder.PrependInt64Slot(5, rewardUnlockDate, 0)

def AddRewardUnlockDate(builder, rewardUnlockDate):
    UserSubscriptionPurchaseProductSetElementAddRewardUnlockDate(builder, rewardUnlockDate)

def UserSubscriptionPurchaseProductSetElementAddRewardUnlockCount(builder, rewardUnlockCount):
    builder.PrependUint32Slot(6, rewardUnlockCount, 0)

def AddRewardUnlockCount(builder, rewardUnlockCount):
    UserSubscriptionPurchaseProductSetElementAddRewardUnlockCount(builder, rewardUnlockCount)

def UserSubscriptionPurchaseProductSetElementAddRewardUnlockedCount(builder, rewardUnlockedCount):
    builder.PrependUint32Slot(7, rewardUnlockedCount, 0)

def AddRewardUnlockedCount(builder, rewardUnlockedCount):
    UserSubscriptionPurchaseProductSetElementAddRewardUnlockedCount(builder, rewardUnlockedCount)

def UserSubscriptionPurchaseProductSetElementAddReceiptLastEndsAt(builder, receiptLastEndsAt):
    builder.PrependInt64Slot(8, receiptLastEndsAt, 0)

def AddReceiptLastEndsAt(builder, receiptLastEndsAt):
    UserSubscriptionPurchaseProductSetElementAddReceiptLastEndsAt(builder, receiptLastEndsAt)

def UserSubscriptionPurchaseProductSetElementAddReceiptUpdateEndsAt(builder, receiptUpdateEndsAt):
    builder.PrependInt64Slot(9, receiptUpdateEndsAt, 0)

def AddReceiptUpdateEndsAt(builder, receiptUpdateEndsAt):
    UserSubscriptionPurchaseProductSetElementAddReceiptUpdateEndsAt(builder, receiptUpdateEndsAt)

def UserSubscriptionPurchaseProductSetElementAddReceiptUpdateCount(builder, receiptUpdateCount):
    builder.PrependUint32Slot(10, receiptUpdateCount, 0)

def AddReceiptUpdateCount(builder, receiptUpdateCount):
    UserSubscriptionPurchaseProductSetElementAddReceiptUpdateCount(builder, receiptUpdateCount)

def UserSubscriptionPurchaseProductSetElementAddExpenctancyEndsAt(builder, expenctancyEndsAt):
    builder.PrependInt64Slot(11, expenctancyEndsAt, 0)

def AddExpenctancyEndsAt(builder, expenctancyEndsAt):
    UserSubscriptionPurchaseProductSetElementAddExpenctancyEndsAt(builder, expenctancyEndsAt)

def UserSubscriptionPurchaseProductSetElementAddContractStartAt(builder, contractStartAt):
    builder.PrependInt64Slot(12, contractStartAt, 0)

def AddContractStartAt(builder, contractStartAt):
    UserSubscriptionPurchaseProductSetElementAddContractStartAt(builder, contractStartAt)

def UserSubscriptionPurchaseProductSetElementAddInvalidEndsAt(builder, invalidEndsAt):
    builder.PrependInt64Slot(13, invalidEndsAt, 0)

def AddInvalidEndsAt(builder, invalidEndsAt):
    UserSubscriptionPurchaseProductSetElementAddInvalidEndsAt(builder, invalidEndsAt)

def UserSubscriptionPurchaseProductSetElementEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserSubscriptionPurchaseProductSetElementEnd(builder)