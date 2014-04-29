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
		# make new node
		new_node = self.mdml.addNode(path, name)
		if new_node == None:
			return None

		# initialize directory
		stat = Stat().setDefaultContext().setDirectory()
		for key, value in stat.getStringItems():
			new_node.set(key, value)
		return new_node

	def remove_directory(self, path, name):
		self.mdml.removeNode(path, name)

	def make_file(self, path, name):
		# make new node
		new_node = self.mdml.addNode(path, name)
		if new_node == None:
			return None

		# initialize file
		stat = Stat().setDefaultContext().setFile()
		for key, value in stat.getStringItems():
			new_node.set(key, value)
		return new_node

	def remove_file(self, path, name):
		self.mdml.removeNode(path, name)

	def change_ownership(self, path, uid, gid):
		node = self.mdml.getNode(path)
		if node == None:
			return False
		# update time
		if uid != -1: node.set("st_uid", str(uid))
		if gid != -1: node.set("st_gid", str(gid))
		return True

	def update_times(self, path, times):
		node = self.mdml.getNode(path)
		if node == None:
			return None
		# update time
		node.set("st_atime", str(times[0]))
		node.set("st_mtime", str(times[1]))

	def update_size(self, path, size):
		node = self.mdml.getNode(path)
		if node == None:
			return None
		# update size
		node.set("st_size", str(size))

	def __str__(self):
		return str(self.mdml)

if __name__ == '__main__':
	meta = Metadata()
	node = meta.getNode('/')
	print meta.stat(node)

