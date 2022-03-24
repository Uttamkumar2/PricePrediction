import sys
import pandas as pd
from sqlalchemy.dialects.mssql import pymssql
from sqlalchemy import create_engine, MetaData, Table, select
import sqlalchemy

import pymongo
import csv
import json
from config import cloudM,cloudMpassword
from pymongo import MongoClient
from flask import Flask, jsonify, render_template


#local mongo install



#cloud mongo connect
cloudMClnt=MongoClient()
##cloudMClnt=MongoClient('mongodb+srv://"+cloudM + ":" + cloudMpassword + "@cluster0.cep5x.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE')
cloudMClnt=MongoClient("mongodb+srv://"+cloudM + ":" + cloudMpassword + "@cluster0.cep5x.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#print(cloudM)
#print(cloudMpassword)
#print(cloudMClnt)
##mongodb+srv://KUMAR:<password>@cluster0.cep5x.mongodb.net/myFirstDatabase?retryWrites=true&w=majority


from sqlalchemy import create_engine, MetaData, Table, select



# read cloud Mongo Data and return dataframes
def cloudM_R():
  db=cloudMClnt['CRYPTO']
  coldata=db['CRYPTO_DATA_FEED']
    
  Adatadf = pd.DataFrame(list(coldata.find().sort([('Timestamp', 1)])))
  del Adatadf['_id']
  return Adatadf


#insert data into local mongo


