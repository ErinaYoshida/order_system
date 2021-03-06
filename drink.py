# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 21:54:55 2021

@author: erina
"""

from menu_item import Menu_Item

class Drink(Menu_Item):
    def __init__(self, name, price, alcohol):
        super().__init__(name, price)
        self.alcohol = alcohol
        
    def info(self):
        return self.name + ": " + str(self.price) + "円(" + self.alcohol + ")"
    #引数に追加でname, price, alcoholを指定するとscript.pyでエラー。
    #selfだけならOKだが上記でNGな理由不明
    #⇒(追記)引数としてはinfoに必要ない。
    #__init__で引数として渡して、インスタンスの各引数がインスタンス変数として定義済み。
    #そのインスタンス変数を使えば良いため引数としては不必要。
    