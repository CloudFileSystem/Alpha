#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, os.path
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump

class MetadataManager:
	def __init__(self):
		# Meta Data Markup language
		self.mdml = Element('mdml')

		# head: this tag means header
		# tree: this tag means directory tree
		self.head = SubElement(self.mdml, 'head')
		self.tree = SubElement(self.mdml, 'tree')

		# node: this tag measn file or directory node
		self.root = SubElement(self.mdml, 'node', name='/')

	def getNode(self, path):
		# divide path, filename
		path, filename = os.path.split(path)

		# parse path
		pathlist = path.split(os.sep)
		pathlist[0] = '/'
		pathlist.remove('')

		# discovery path resource
		node	= self.root
		nodes	= [node]
		for pathname in pathlist:
			# get element that match pathname
			nodelist = [n for n in nodes if n.attrib['name'] == pathname]
			if len(nodelist) == 0: return False

			node	= nodelist[0]
			nodes	= node.findall('node')

		# return find out node
		return node

	def addNode(self, path, node):
		# get path node
		target_node = self.getNode(path)
		if target_node == False:
			return False
		# add node element
		return SubElement(target_node, 'node', name=node)

	def __str__(self):
		return ElementTree.tostring(self.mdml)

if __name__ == '__main__':
	mm = MetadataManager()
	print mm.addNode('/', 'bin')
	print mm.addNode('/', 'etc')
	print mm

