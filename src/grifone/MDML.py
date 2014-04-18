#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, os.path
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump

class MDML:
	def __init__(self):
		# Meta Data Markup language
		self.mdml = Element('mdml')

		# head: this tag means header
		# tree: this tag means directory tree
		self.head = SubElement(self.mdml, 'head')
		self.tree = SubElement(self.mdml, 'tree')

		# node: this tag measn file or directory node
		self.root = SubElement(self.tree, 'node')
		self.root.set('name', '/')

	def getRoot(self):
		return self.root

	def getNode(self, path):
		# divide path, filename
		path, filename = os.path.split(path)

		# parse path
		pathlist = path.split(os.sep)
		pathlist[0] = '/'
		pathlist.remove('')

		# if file exist
		if len(filename) != 0:
			pathlist.append(filename)

		# discovery path resource
		node	= self.root
		nodes	= [node]
		for pathname in pathlist:
			# get element that match pathname
			nodelist = [n for n in nodes if n.attrib['name'] == pathname]
			if len(nodelist) == 0: return None

			node	= nodelist[0]
			nodes	= node.findall('node')

		# return find out node
		return node

	def getChildNodes(self, path):
		node	= self.getNode(path)
		if node == None:
			return []

		# get element that match pathname
		nodelist = [n for n in node]
		if len(nodelist) == 0: return []

		return nodelist

	def addNode(self, path, name):
		# divide path, filename
		path, filename = os.path.split(path)

		# get path node
		target_node = self.getNode(path)
		if target_node == None:
			return None
		# add node element
		return SubElement(target_node, 'node', name=name)

	def __str__(self):
		return ElementTree.tostring(self.mdml)

if __name__ == '__main__':
	mm = MDML()
	print mm.addNode('/', 'bin')
	print mm.addNode('/', 'etc')
	print mm

