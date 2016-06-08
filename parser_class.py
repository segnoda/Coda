#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import resources

class Parser(QXmlStreamReader):

    def __init__(self, game_engine_id):
        super().__init__()

        self.id = str(game_engine_id)

        self.bgm = ''
        self.sd = ''
        self.bg = ''
        self.ptid = {}
        self.ptx = {}
        self.pty = {}
        self.ptxf = {}
        self.ptyf = {}
        self.ptw = {}
        self.pth = {}
        self.vc = ''
        self.char = ''
        self.txt = ''

        self.pt_num = -1

        self.file = QFile(':/script.xml')
        self.file.open(QIODevice.ReadOnly)
        self.setDevice(self.file)

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'content':
                    if self.attributes().value('id') == self.id:
                        self.parse()
                        break

    def parse(self):

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'bgm':
                    self.parse_bgm()
                elif self.name() == 'sd':
                    self.parse_sd()
                elif self.name() == 'bg':
                    self.parse_bg()
                elif self.name() == 'pt':
                    self.parse_pt()
                elif self.name() == 'vc':
                    self.parse_vc()
                elif self.name() == 'char':
                    self.parse_char()
                elif self.name() == 'txt':
                    self.parse_txt()
                else:
                    self.readNext()

            if self.isEndElement():
                if self.name() == 'content':
                    #print('break content')
                    break

    def parse_bgm(self):

        self.bgm = self.readElementText()
        #print(self.bgm)

    def parse_sd(self):

        self.sd = self.readElementText()
        #print(self.sd)

    def parse_bg(self):

        self.bg = self.readElementText()
        #print(self.bg)

    def parse_pt(self):

        self.pt_num += 1
        #print(self.pt_num)

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'ptid':
                    self.ptid[self.pt_num] = self.readElementText()
                    #print(self.ptid[self.pt_num])
                elif self.name() == 'ptx':
                    self.ptx[self.pt_num] = self.readElementText()
                    #print(self.ptx[self.pt_num])
                elif self.name() == 'pty':
                    self.pty[self.pt_num] = self.readElementText()
                    #print(self.pty[self.pt_num])
                elif self.name() == 'ptxf':
                    self.ptxf[self.pt_num] = self.readElementText()
                    #print(self.ptxf[self.pt_num])
                elif self.name() == 'ptyf':
                    self.ptyf[self.pt_num] = self.readElementText()
                    #print(self.ptyf[self.pt_num])
                elif self.name() == 'ptw':
                    self.ptw[self.pt_num] = self.readElementText()
                    #print(self.ptw[self.pt_num])
                elif self.name() == 'pth':
                    self.pth[self.pt_num] = self.readElementText()
                    #print(self.pth[self.pt_num])
                else:
                    self.readNext()

            if self.isEndElement():
                if self.name() == 'pt':
                    #print('break pt')
                    break

    def parse_vc(self):

        self.vc = self.readElementText()
        #print(self.vc)

    def parse_char(self):

        self.char = self.readElementText()
        #print(self.char)

    def parse_txt(self):

        self.txt = self.readElementText()
        #print(self.txt)

if __name__ == '__main__':

    game_engine_id = 3
    parser = Parser(game_engine_id)

    print(parser.bgm)
    print(parser.sd)
    print(parser.bg)
    print(parser.ptid)
    print(parser.ptx)
    print(parser.pty)
    print(parser.ptxf)
    print(parser.ptyf)
    print(parser.ptw)
    print(parser.pth)
    print(parser.vc)
    print(parser.char)
    print(parser.txt)
    print(parser.pt_num)