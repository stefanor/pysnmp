# PySNMP SMI module. Autogenerated from smidump -f python SNMP-USER-BASED-SM-MIB
# by libsmi2pysnmp-0.0.3-alpha at Wed Nov 10 13:12:09 2004,
# Python version (2, 2, 1, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pysnmp.asn1 import subtypes

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( SnmpAdminString, SnmpEngineID, snmpAuthProtocols, snmpPrivProtocols, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString", "SnmpEngineID", "snmpAuthProtocols", "snmpPrivProtocols")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, MibVariable, MibTable, MibTableRow, MibTableColumn, TimeTicks, snmpModules, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "snmpModules")
( AutonomousType, RowPointer, RowStatus, StorageType, TextualConvention, TestAndIncr, ) = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "RowPointer", "RowStatus", "StorageType", "TextualConvention", "TestAndIncr")

# Types

class KeyChange(OctetString):
    pass


# Objects

usmNoAuthProtocol = MibIdentifier((1, 3, 6, 1, 6, 3, 10, 1, 1, 1))
usmHMACMD5AuthProtocol = MibIdentifier((1, 3, 6, 1, 6, 3, 10, 1, 1, 2))
usmHMACSHAAuthProtocol = MibIdentifier((1, 3, 6, 1, 6, 3, 10, 1, 1, 3))
usmNoPrivProtocol = MibIdentifier((1, 3, 6, 1, 6, 3, 10, 1, 2, 1))
usmDESPrivProtocol = MibIdentifier((1, 3, 6, 1, 6, 3, 10, 1, 2, 2))
snmpUsmMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 15))
usmMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 1))
usmStats = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 1, 1))
usmStatsUnsupportedSecLevels = MibVariable((1, 3, 6, 1, 6, 3, 15, 1, 1, 1), Counter32()).setMaxAccess("readonly")
usmStatsNotInTimeWindows = MibVariable((1, 3, 6, 1, 6, 3, 15, 1, 1, 2), Counter32()).setMaxAccess("readonly")
usmStatsUnknownUserNames = MibVariable((1, 3, 6, 1, 6, 3, 15, 1, 1, 3), Counter32()).setMaxAccess("readonly")
usmStatsUnknownEngineIDs = MibVariable((1, 3, 6, 1, 6, 3, 15, 1, 1, 4), Counter32()).setMaxAccess("readonly")
usmStatsWrongDigests = MibVariable((1, 3, 6, 1, 6, 3, 15, 1, 1, 5), Counter32()).setMaxAccess("readonly")
usmStatsDecryptionErrors = MibVariable((1, 3, 6, 1, 6, 3, 15, 1, 1, 6), Counter32()).setMaxAccess("readonly")
usmUser = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 1, 2))
usmUserSpinLock = MibVariable((1, 3, 6, 1, 6, 3, 15, 1, 2, 1), TestAndIncr()).setMaxAccess("readcreate")
usmUserTable = MibTable((1, 3, 6, 1, 6, 3, 15, 1, 2, 2))
usmUserEntry = MibTableRow((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1)).setIndexNames((0, "SNMP-USER-BASED-SM-MIB", "usmUserEngineID"), (0, "SNMP-USER-BASED-SM-MIB", "usmUserName"))
usmUserEngineID = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 1)).setColumnInitializer(MibVariable((), SnmpEngineID()).setMaxAccess("noaccess"))
usmUserName = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 2)).setColumnInitializer(MibVariable((), SnmpAdminString().addConstraints(subtypes.ValueRangeConstraint(1, 32))).setMaxAccess("noaccess"))
usmUserSecurityName = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 3)).setColumnInitializer(MibVariable((), SnmpAdminString()).setMaxAccess("readonly"))
usmUserCloneFrom = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 4)).setColumnInitializer(MibVariable((), RowPointer()).setMaxAccess("readcreate"))
usmUserAuthProtocol = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 5)).setColumnInitializer(MibVariable((), AutonomousType()).setMaxAccess("readcreate"))
usmUserAuthKeyChange = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 6)).setColumnInitializer(MibVariable((), KeyChange()).setMaxAccess("readcreate"))
usmUserOwnAuthKeyChange = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 7)).setColumnInitializer(MibVariable((), KeyChange()).setMaxAccess("readcreate"))
usmUserPrivProtocol = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 8)).setColumnInitializer(MibVariable((), AutonomousType()).setMaxAccess("readcreate"))
usmUserPrivKeyChange = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 9)).setColumnInitializer(MibVariable((), KeyChange()).setMaxAccess("readcreate"))
usmUserOwnPrivKeyChange = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 10)).setColumnInitializer(MibVariable((), KeyChange()).setMaxAccess("readcreate"))
usmUserPublic = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 11)).setColumnInitializer(MibVariable((), OctetString().addConstraints(subtypes.ValueRangeConstraint(0, 32)).set('')).setMaxAccess("readcreate"))
usmUserStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 12)).setColumnInitializer(MibVariable((), StorageType()).setMaxAccess("readcreate"))
usmUserStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 13)).setColumnInitializer(MibVariable((), RowStatus()).setMaxAccess("readcreate"))
usmMIBConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 2))
usmMIBCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 2, 1))
usmMIBGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 2, 2))

# Augmentions

# Groups

usmMIBBasicGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 15, 2, 2, 1)).setObjects(("SNMP-USER-BASED-SM-MIB", "usmStatsUnknownEngineIDs"), ("SNMP-USER-BASED-SM-MIB", "usmUserOwnAuthKeyChange"), ("SNMP-USER-BASED-SM-MIB", "usmStatsNotInTimeWindows"), ("SNMP-USER-BASED-SM-MIB", "usmStatsUnknownUserNames"), ("SNMP-USER-BASED-SM-MIB", "usmStatsDecryptionErrors"), ("SNMP-USER-BASED-SM-MIB", "usmStatsUnsupportedSecLevels"), ("SNMP-USER-BASED-SM-MIB", "usmUserSecurityName"), ("SNMP-USER-BASED-SM-MIB", "usmUserStatus"), ("SNMP-USER-BASED-SM-MIB", "usmUserPrivKeyChange"), ("SNMP-USER-BASED-SM-MIB", "usmUserOwnPrivKeyChange"), ("SNMP-USER-BASED-SM-MIB", "usmUserStorageType"), ("SNMP-USER-BASED-SM-MIB", "usmUserSpinLock"), ("SNMP-USER-BASED-SM-MIB", "usmUserAuthKeyChange"), ("SNMP-USER-BASED-SM-MIB", "usmUserCloneFrom"), ("SNMP-USER-BASED-SM-MIB", "usmUserPrivProtocol"), ("SNMP-USER-BASED-SM-MIB", "usmUserAuthProtocol"), ("SNMP-USER-BASED-SM-MIB", "usmStatsWrongDigests"), ("SNMP-USER-BASED-SM-MIB", "usmUserPublic"), )

# Exports

# Types
mibBuilder.exportSymbols("SNMP-USER-BASED-SM-MIB", KeyChange=KeyChange)

# Objects
mibBuilder.exportSymbols("SNMP-USER-BASED-SM-MIB", usmNoAuthProtocol=usmNoAuthProtocol, usmHMACMD5AuthProtocol=usmHMACMD5AuthProtocol, usmHMACSHAAuthProtocol=usmHMACSHAAuthProtocol, usmNoPrivProtocol=usmNoPrivProtocol, usmDESPrivProtocol=usmDESPrivProtocol, snmpUsmMIB=snmpUsmMIB, usmMIBObjects=usmMIBObjects, usmStats=usmStats, usmStatsUnsupportedSecLevels=usmStatsUnsupportedSecLevels, usmStatsNotInTimeWindows=usmStatsNotInTimeWindows, usmStatsUnknownUserNames=usmStatsUnknownUserNames, usmStatsUnknownEngineIDs=usmStatsUnknownEngineIDs, usmStatsWrongDigests=usmStatsWrongDigests, usmStatsDecryptionErrors=usmStatsDecryptionErrors, usmUser=usmUser, usmUserSpinLock=usmUserSpinLock, usmUserTable=usmUserTable, usmUserEntry=usmUserEntry, usmUserEngineID=usmUserEngineID, usmUserName=usmUserName, usmUserSecurityName=usmUserSecurityName, usmUserCloneFrom=usmUserCloneFrom, usmUserAuthProtocol=usmUserAuthProtocol, usmUserAuthKeyChange=usmUserAuthKeyChange, usmUserOwnAuthKeyChange=usmUserOwnAuthKeyChange, usmUserPrivProtocol=usmUserPrivProtocol, usmUserPrivKeyChange=usmUserPrivKeyChange, usmUserOwnPrivKeyChange=usmUserOwnPrivKeyChange, usmUserPublic=usmUserPublic, usmUserStorageType=usmUserStorageType, usmUserStatus=usmUserStatus, usmMIBConformance=usmMIBConformance, usmMIBCompliances=usmMIBCompliances, usmMIBGroups=usmMIBGroups)

# Groups
mibBuilder.exportSymbols("SNMP-USER-BASED-SM-MIB", usmMIBBasicGroup=usmMIBBasicGroup)
