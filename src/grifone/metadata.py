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

	def getChildNodes(self, path):
		lists = []
		nodes = self.mdml.getChildNodes(path)
		for node in nodes:
			lists.append(node.get('name'))
		return lists

	def stat(self, node):
		stat = Stat()
		stat.setStringItems(node)
		return stat

	def make_directory(self, path, name):
		# initialize root directory
		new_node = self.mdml.addNode(path, name)
		if new_node == None:
			return None

		# initialize directory
		stat = Stat().setDefaultContext().setDirectory()
		for key, value in stat.getStringItems():
			new_node.set(key, value)
		return new_node

	def __str__(self):
		return str(self.mdml)

if __name__ == '__main__':
	meta = Metadata()
	node = meta.getNode('/')
	print meta.stat(node)

