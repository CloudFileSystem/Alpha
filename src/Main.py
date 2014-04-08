#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path
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
		pathname, filename = os.path.split(path)
		pass

	def addNode(self, path, node):
		print path, node
		pass

	def __str__(self):
		return ElementTree.tostring(self.mdml)

if __name__ == '__main__':
	mm = MetadataManager()
	mm.addNode('/', 'etc')

