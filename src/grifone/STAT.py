#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import stat
import time
import fuse

class Stat:
	def __init__(self):
		self.st_mode = 0
		self.st_ino = 0
		self.st_dev = 0
		self.st_nlink = 0
		self.st_uid = 0
		self.st_gid = 0
		self.st_size = 0
		self.st_atime = 0
		self.st_mtime = 0
		self.st_ctime = 0

	def setFile(self):
		self.st_mode	= (stat.S_IFREG | 0644)
		return self

	def setDirectory(self):
		self.st_mode	= (stat.S_IFDIR | 0755)
		self.st_nlink	= 2
		return self

	def setDefaultContext(self, uid = None, gid = None):
		# get fuse context
		fuid, fgid, fpid = fuse.fuse_get_context()
		if uid == None: uid = fuid
		if gid == None: gid = fgid

		# set user, group id
		self.st_uid = uid
		self.st_gid = gid

		# set create time
		self.st_ctime = time.time()

		return self

	def items(self):
		stats = dict(
			st_mode  = self.st_mode,
			st_ino   = self.st_ino,
			st_dev   = self.st_dev,
			st_nlink = self.st_nlink,
			st_uid   = self.st_uid,
			st_gid   = self.st_gid,
			st_size  = self.st_size,
			st_atime = self.st_atime,
			st_mtime = self.st_mtime,
			st_ctime = self.st_ctime,
		)
		return stats.items()

	def getStringItems(self):
		stats = dict(
			st_mode  = str(self.st_mode),
			st_ino   = str(self.st_ino),
			st_dev   = str(self.st_dev),
			st_nlink = str(self.st_nlink),
			st_uid   = str(self.st_uid),
			st_gid   = str(self.st_gid),
			st_size  = str(self.st_size),
			st_atime = str(self.st_atime),
			st_mtime = str(self.st_mtime),
			st_ctime = str(self.st_ctime),
		)
		return stats.items()

	def setStringItems(self, item):
		self.st_mode  = int(item.attrib.get("st_mode"))
		self.st_ino   = int(item.attrib.get("st_ino"))
		self.st_dev   = int(item.attrib.get("st_dev"))
		self.st_nlink = int(item.attrib.get("st_nlink"))
		self.st_uid   = int(item.attrib.get("st_uid"))
		self.st_gid   = int(item.attrib.get("st_gid"))
		self.st_size  = int(item.attrib.get("st_size"))
		self.st_atime = float(item.attrib.get("st_atime"))
		self.st_mtime = float(item.attrib.get("st_mtime"))
		self.st_ctime = float(item.attrib.get("st_ctime"))

	def __str__(self):
		string = """
		####################################################################
		st_mode=%d, st_ino=%d, st_dev=%d, st_nlink=%d, st_uid=%d, st_gid=%d,
		st_size=%d, st_atime=%d, st_mtime=%d, st_ctime=%d
		####################################################################
		""" %(self.st_mode, self.st_ino, self.st_dev, self.st_nlink,
		self.st_uid, self.st_gid, self.st_size, self.st_atime,
		self.st_mtime, self.st_ctime)
		return string

if __name__ == "__main__":
	print "OK"

