from django.shortcuts import render
from django.http import HttpResponse
import math
import sqlite3
import mysql.connector

# Create your views here.

def sqlLab(request):
  if request.method == "POST":
    sqlRequest = request.POST.get("sql")
    if(request.POST.get("firstSql")):
      sqlRequest = "SELECT * FROM books"
    if(request.POST.get("secondSql")):
      sqlRequest = "SELECT name,authors,price,date FROM books JOIN bookadmission ON bookadmission.bookid = books.id WHERE MONTH(date) = 02"
    if(request.POST.get("thirdSql")):
      sqlRequest = "SELECT name,authors,soldprice,soldprice*count FROM books JOIN booksells ON booksells.bookid = books.id"
    if(request.POST.get("fourthSql")):
      sqlRequest = "SELECT name,date FROM books JOIN bookadmission ON bookadmission.bookid = books.id WHERE (YEAR(date) = 2020 AND name LIKE 'V%')"
    conn = mysql.connector.connect(user='root', password='123', host='127.0.0.1', database='bookstore')
    cursor = conn.cursor()
    cursor.execute(sqlRequest)

    response = cursor.fetchall()

    conn.close()

    data = {"sqlResponse":str(response),}

    return render(request,"sql.html",context=data)
  else:
    return render(request,"sql.html", context = {"sqlResponse":"" })