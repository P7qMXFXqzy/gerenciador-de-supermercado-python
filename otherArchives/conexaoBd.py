from mysql.connector import connect as connectToDb
class ConnectionClass:

    connection = connectToDb(
      host="localhost",
      user="root",
      password="abcd",
      database="gerenciadormercado"
    )
    cursor = connection.cursor()
    #function that will check if a product with the given id exists, will return false if not.
    def checkIfIdExists(self, insertedId):
      self.cursor.execute("SELECT idProduto FROM produtos WHERE idProduto = \"" + str(insertedId) + "\"")
      foundProduct = self.cursor.fetchone()
      if foundProduct == None: return False
      else:return True
    #if the id has been found, request for all of it's data and return it
    def searchById(self, insertedId):
      if(self.checkIfIdExists(insertedId) == True):
        self.cursor.execute("SELECT * FROM produtos WHERE idProduto = \"" + str(insertedId) + "\"")
        foundProduct = self.cursor.fetchone()
        return foundProduct
      else:return None
