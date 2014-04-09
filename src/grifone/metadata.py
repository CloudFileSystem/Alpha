#!/usr/bin/env python
# -*- coding: utf-8 -*-
from MDML import MDML
from STAT import Stat

class Metadata:
	def __init__(self):
		# initialize meta data markup language
		self.mdml = MDML()

		# initialize root directory
		root = self.mdml.getRoot()
		stat = Stat().setDefaultContext().setDirectory()
		for key, value in stat.getStringItems():
			root.set(key, value)

	def getNode(self, path):
		return self.mdml.getNode(path)

	def stat(self, node):
		stat = Stat()
		stat.setStringItems(node)
		return stat

if __name__ == '__main__':
	meta = Metadata()
	node = meta.getNode('/')
	print meta.stat(node)

