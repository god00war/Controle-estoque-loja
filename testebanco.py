import fdb
import locale
con = fdb.connect(
    host="localhost",
    database="C:/Users/God War/Documents/TCC/Banco de dados/gino14.FDB",
    user='sysdba', password='masterkey'
)
cur = con.cursor()
name ='alisson1'
end ='dlç1'
outR = '24141,41'
locale.setlocale(locale.LC_ALL, '') #Define o local
outRen = locale.atof(outR,float)
print(outRen)
#outRen = locale.format_string(format, outR, grouping=False, monetary=True)
#outRen = locale.currency(outR, symbol=False) #Troca o float para o padrao local

cur.execute("INSERT INTO T001_CLIENTE (T001_CA_NOME, T001_CA_ENDERECO,T001_NR_OUTRAS_RENDAS) "
            "VALUES (?,?,?)",(name, end, outRen))
con.commit()