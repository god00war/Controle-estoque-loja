import sqlite3
from sqlite3 import Error


venid = "5"
prodid = "3"
qtd = "1    "
def conexaoBanco():
    caminho = "C:\\Users\\God War\\Documents\\TCC\\banco de dados\\sqlite\\ginomodas.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
        print(con)
    except Error as er:
         print(er)
    return con

def executarSelect(sql):
    try:
        conexao = conexaoBanco()
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        resultado = c.fetchall()
        c.close()
        return resultado
    except Error as e:
        print(e)

def executarSql():
    try:
        conexao = conexaoBanco()
        c = conexao.cursor()
        c.execute("INSERT INTO itensvenda (ven_id, prod_id, item_qtd) VALUES (?, ?, ?)", (venid, prodid, qtd))
        conexao.commit()
        c.close()
    except Error as e:
        print(e)

#sq = ("INSERT INTO itensvendas (ven_id, prod_id, item_qtd) VALUES (?, ?, ?)", (venid, prodid, qtd))

executarSql()
#print(vcon)

#vsql = " SELECT * FROM produtos"
""""def teste(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        ultimoItem = c.fetchall()
        print(ultimoItem)
    except Error as e:
        print (e)

teste(vcon,vsql)"""
"""
descricao = "asdasdasd"
codBarras = "12123213"
try:
    con = conexaoBanco()
    c = con.cursor()
    c.execute("INSERT INTO produtos (prod_desc, prod_cod) VALUES (?, ?)", (descricao, codBarras))
    con.commit()
    c.close()
except Error as e:
    print(e)

sql = " SELECT * FROM produtos"

a = executarSelect(sql)
print (a)
"""