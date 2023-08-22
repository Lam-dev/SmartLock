from locale import currency
import sqlite3
from typing import cast, TypeVar, Generic, Generator
import time
import os
import traceback

class Repository:
    def __del__(self):
        self.repo.close()
 
    def __init__(self, tableClass, databasePath = "../Database/Database"):
        # print(f"Tạo class {tableClass.Table}")
        self.sqlFilePath = databasePath
        self.repo = sqlite3.connect(self.sqlFilePath, 2)
        self.tableName = tableClass.Table
        self.table = tableClass
        self.tableInfo = self.GetTableInfo()
        self.primaryKey = [x[1] for x in self.tableInfo if x[5] == 1][0]

    def __WriteKey(self):
        with open("../Database/key", "w"): pass

    def __IsLock(self):
        lock = os.path.exists('../Database/key')
        if(lock):
            print("dang khoa")
        return lock

    def __ReleaseKey(self):
        try:
            os.remove("../Database/key")
        except:
            pass

    """
    lay danh sach du lieu
    """
    def GetListColumn(self):
        cursor = self.repo.cursor()
        sql = "PRAGMA table_info(%s)"%(self.tableName)
        cursor.execute(sql)
        results = cursor.fetchall()
        yield [x[1] for x in results]

    def GetTableInfo(self):
        cursor = self.repo.cursor()
        sql = "PRAGMA table_info(%s)"%(self.tableName)
        while(self.__IsLock()):
            time.sleep(0.5)
        self.__WriteKey()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
        except Exception as ex:
            self.__ReleaseKey()
            raise(ex)
        self.__ReleaseKey()
        return results

    # def GetPrimaryKey(self):
    #     cursor = self.repo.cursor()
    #     sql = "PRAGMA table_info(%s)"%(self.tableName)
    #     cursor.execute(sql)
    #     results = cursor.fetchall()
    #     return [x[1] for x in results if(x[5] == 1)]
    
    def Vacumn(self):
        while(self.__IsLock()):
            time.sleep(0.5)
        self.__WriteKey()
        try:
            cursor = self.repo.cursor()
            sql = "VACUUM"
            cursor.execute(sql)
        except Exception as ex:
            self.__ReleaseKey()
            raise(ex) 
        cursor.close()
        self.__ReleaseKey()
     
    def SetWALmodeToDatabase(self):
        while(self.__IsLock()):
            time.sleep(0.5)
        self.__WriteKey()
        try:
            cursor = self.repo.cursor()
            sql = "pragma journal_mode = wal"
            cursor.execute(sql)
        except Exception as ex:
            self.__ReleaseKey()
            raise(ex)
        cursor.close()
        self.__ReleaseKey()
        
    def UpdateEntity(self, entity):
        pass

    def Update(self, tupleColumnName, tupleValue, where):
        tupleBlobData = ()
        cursor = self.repo.cursor()
        sql = 'update `' + self.tableName + '` set '
        for i in range(0,tupleColumnName.__len__()):
            data =  tupleValue[i]
            if(i < tupleColumnName.__len__() - 1):
                
                if(type(data) is not list):
                    sql += '`%s` = "%s", ' % (tupleColumnName[i].__str__(), data.__str__())
                else:
                    sql += '`%s` = ?, '%(tupleColumnName[i].__str__())
                    tupleBlobData += (bytes(data),)
            else:
                if(type(data) is not list):
                    sql += '`%s` = "%s" ' % (tupleColumnName[i].__str__(), data.__str__())
                else:
                    sql += '`%s` = ? '%(tupleColumnName[i].__str__())
                    tupleBlobData += (bytes(data),)
        sql += 'where %s' % (where)
        while(self.__IsLock()):
            time.sleep(0.5)
        self.__WriteKey()
        try:
            cursor.execute(sql, tupleBlobData)
            numberRowEffect = cursor.rowcount
            self.repo.commit()
        except Exception as ex:
            cursor.close()
            self.__ReleaseKey()
            raise(ex)
        cursor.close()
        self.__ReleaseKey()
        return numberRowEffect

    def GetListAllColumn(self, where = "1=1", orderBy = None, asc = True, limit = None):
        cursor = self.repo.cursor()
        sql = 'SELECT  * FROM `'+ self.tableName + '` WHERE ' + where
        if(orderBy != None):
            sql += ' ORDER BY ' + orderBy + (' ASC' if asc else ' DESC')
        if(limit != None):
            sql += ' LIMIT %s'%(limit)
        while(self.__IsLock()):
            time.sleep(0.5)
        lstResults = []
        self.__WriteKey()
        try:
            cursor.execute(sql)
            allRow = cursor.fetchall()
            for row in allRow:
                tableIntance = self.table()
                for column in self.tableInfo:
                    setattr(tableIntance, column[1],row[column[0]])
                lstResults.append(tableIntance)
        except Exception as ex:
            self.__ReleaseKey()
            raise(ex)    
        self.__ReleaseKey()
        return lstResults

    def GetList(self, listColumn, where = "1=1", orderBy = None, asc = True,  limit = None):
        cursor = self.repo.cursor()
        sql = 'SELECT %s FROM `'%(",".join(listColumn))+ self.tableName + '` WHERE ' + where
        if(orderBy != None):
            sql += ' ORDER BY ' + orderBy + (' ASC' if asc else ' DESC')
        if(limit != None):
            sql += ' LIMIT %s'%(limit)
        lstResults = []
        while(self.__IsLock()):
            time.sleep(0.5)
        self.__WriteKey()
        try:
            cursor.execute(sql)
            allRow = cursor.fetchall()
            for row in allRow:
                tableIntance = self.table()
                count = 0
                for column in listColumn:
                    setattr(tableIntance, column,row[count])
                    count += 1
                lstResults.append(tableIntance)
        except Exception as ex:
            cursor.close()
            self.__ReleaseKey()
            raise(ex)
        cursor.close()
        self.__ReleaseKey()
        return lstResults      

    def Delete(self, entity):
        cursor = self.repo.cursor()
        sql = 'DELETE FROM `%s` WHERE `%s`= %s'%(self.tableName, self.primaryKey, str(getattr(entity,self.primaryKey, None)))
        while(self.__IsLock()):
            time.sleep(0.5)
        self.__WriteKey()
        try:
            cursor.execute(sql)
            rowDeleted = cursor.rowcount
            self.repo.commit()
        except Exception as ex:
            self.__ReleaseKey()
            raise(ex)
        cursor.close()
        self.__ReleaseKey()
        return rowDeleted

    def DeleteByWhere(self, where):
        cursor = self.repo.cursor()
        sql = 'DELETE FROM `%s` WHERE %s'%(self.tableName, where)
        while(self.__IsLock()):
            time.sleep(0.5)
        self.__WriteKey()
        try:   # try except tranh truong hop loi khi execute se khong releaseKey
            cursor.execute(sql)
            self.repo.commit()
        except Exception as ex:
            cursor.close()
            self.__ReleaseKey()
            raise(ex)
        cursor.close()
        self.__ReleaseKey()
        
    def AddListData(self, listEntity):
        pass
    
    def AddDataIncludePrimaryKey(self):
        pass

    def AddData(self, entity):
        cursor = self.repo.cursor()
        sqlPart1 = "INSERT INTO %s"%(self.tableName)
        sqlPart2 = ""
        sqlPart3 = ""
        count = 0
        tupleBlobData = ()
        for column in self.tableInfo:
            
            if (column[5] == 1):  #cot 5 la cot primary key.
                valueOfColumn = getattr(entity, column[1], None)
                if(valueOfColumn == None):
                    continue
            valueOfColumn = getattr(entity, column[1], None)
            if((valueOfColumn != None)):
                if((type(valueOfColumn) is not list) & (type(valueOfColumn) is not bytes)):
                    if (count == 0):
                        sqlPart2 += "`%s`"%(column[1])
                        sqlPart3 += '"%s"'%(valueOfColumn)
                    
                    else:
                        sqlPart2 += ",`%s`"%(column[1])
                        sqlPart3 += ',"%s"'%(valueOfColumn)
                else:
                    if (count == 0):
                        sqlPart2 += "`%s`"%(column[1])
                        sqlPart3 += '?'
                    
                    else:
                        sqlPart2 += ",`%s`"%(column[1])
                        sqlPart3 += ',?'
                    tupleBlobData += (bytes(valueOfColumn),)

                count += 1

        sql = sqlPart1 + "(%s)"%(sqlPart2) + " VALUES (" + "%s"%(sqlPart3) + ")"
        while(self.__IsLock()):
            time.sleep(0.5)
        self.__WriteKey()
        try:
            cursor.execute(sql, tupleBlobData)
            self.repo.commit()
            lastRowID = cursor.lastrowid
        except Exception as ex:
            cursor.close()
            self.__ReleaseKey()
            raise(ex)
        cursor.close()
        self.__ReleaseKey()
        return lastRowID

    def GetLastRowID(self):
        cursor = self.repo.cursor()
        sql = 'SELECT rowid FROM '+ self.tableName + ' order by ROWID DESC limit 1'
        while(self.__IsLock()):
            time.sleep(0.5)
        self.__WriteKey()
        try:
            cursor.execute(sql)
            row = cursor.fetchall()
        except Exception as ex:
            self.__ReleaseKey()
            raise(ex)
        self.__ReleaseKey()
        if(len(row) == 0):
            return 0
        return row[0][0]
    