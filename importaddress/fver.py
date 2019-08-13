#!/usr/bin/env python
#
#fver.py -> find version

import sqlite3
import codecs
from binascii import hexlify
from os.path import exists

path = __file__[:-7]+"data/bip32version.db"
if not exists(path):
	path = "./data/bip32version.db"
	
connection = sqlite3.connect(path)

def query_ver(cointype="bitcoin",testnet=False,private=False,bip=44):
	c = connection.cursor()
	key = "pubkey" if not private else "privkey"
	cointype = cointype if not testnet else cointype + " testnet"
	c.execute("select {} from bip32version where coin='{}' and bip={}".format(key,cointype,bip))
	return [codecs.decode(e[0],"hex") for e in c.fetchall()]


def query_path(cointype="bitcoin",testnet=False,private=False,bip=44):
	c = connection.cursor()
	path = "BIP32_Path"
	cointype = cointype if not testnet else cointype + " testnet"
	c.execute("select {} from bip32version where coin='{}' and bip={}".format(path,cointype,bip))
	result = c.fetchall()
	return result[0][0] if result else None

def query_coin_num(cointype="bitcoin",testnet=False,private=False,bip=44):
	c = connection.cursor()
	path = "coin_num"
	cointype = cointype if not testnet else cointype + " testnet"
	c.execute("select {} from bip32version where coin='{}' and bip={}".format(path,cointype,bip))
	result = c.fetchall()
	return result[0][0] if result else None
