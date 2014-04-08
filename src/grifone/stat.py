#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import stat

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

	def isFile(self):
		self.st_mode	= (stat.S_IFREG | 0444)
		return self

	def isDirectory(self):
		self.st_mode	= (stat.S_IFDIR | 0755)
		self.st_nlink	= 2
		return self

	def setDefaultContext(self, uid = None, gid = None):
		if uid == None: uid = os.geteuid()
		if gid == None: gid = os.getgid()

		self.st_uid = uid
		self.st_gid = gid

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

