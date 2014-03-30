#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import stat
import errno

from mystat import Stat
from fuse import FUSE, FuseOSError, Operations

class Passthrough(Operations):
	def __init__(self):
		self.dir = []
		pass

	# Helpers
	# =======

	def _full_path(self, partial):
		if partial.startswith("/"):
			partial = partial[1:]
			path = os.path.join(self.root, partial)
		return path

	# Filesystem methods
	# ==================
	def access(self, path, mode):
		print "access"
		print path, mode
		return 0
		#raise FuseOSError(errno.EACCES)

	def chmod(self, path, mode):
		print "chmod"
		raise FuseOSError(errno.EACCES)

	def chown(self, path, uid, gid):
		print "chown"
		raise FuseOSError(errno.EACCES)

	#
	# return metadata
	#
	def getattr(self, path, fh=None):
		print "getattr"
		print path, fh

		st = Stat().setDefaultContext()

		if fh == None:
			st.isFile()
		elif fh == 1:
			st.isDirectory()
		else:
			raise FuseOSError(errno.EACCES)

		if path == '/':
			st.isDirectory()

		return st

	def readdir(self, path, fh):
		print "readdir"

		paths = ['.', '..']
		dirs = self.dir + paths

		for path in dirs:
			yield path
		#raise FuseOSError(errno.EACCES)

	def readlink(self, path):
		print "readlink"
		raise FuseOSError(errno.EACCES)

	def mknod(self, path, mode, dev):
		print "mknod"
		raise FuseOSError(errno.EACCES)

	def rmdir(self, path):
		print "rmdir"
		raise FuseOSError(errno.EACCES)

	def mkdir(self, path, mode):
		print "mkdir"
		self.dir.append('test')
		print "OK "
		return None
		#raise FuseOSError(errno.EACCES)

	def statfs(self, path):
		print "statfs"
		raise FuseOSError(errno.EACCES)

	def unlink(self, path):
		print "unlink"
		raise FuseOSError(errno.EACCES)

	def symlink(self, target, name):
		print "symlink"
		raise FuseOSError(errno.EACCES)

	def rename(self, old, new):
		print "rename"
		raise FuseOSError(errno.EACCES)

	def link(self, target, name):
		print "link"
		raise FuseOSError(errno.EACCES)

	def utimens(self, path, times=None):
		print "utimes"
		#raise FuseOSError(errno.EACCES)

	# File methods
	# ============

	def open(self, path, flags):
		print "open"
		return 123
		#raise FuseOSError(errno.EACCES)

	def create(self, path, mode, fi=None):
		print "create"
		raise FuseOSError(errno.EACCES)

	def read(self, path, length, offset, fh):
		print "read"
		raise FuseOSError(errno.EACCES)

	def write(self, path, buf, offset, fh):
		print "write"
		raise FuseOSError(errno.EACCES)

	def truncate(self, path, length, fh=None):
		print "truncate"
		raise FuseOSError(errno.EACCES)

	def flush(self, path, fh):
		print "flush"
		print path, fh
		#raise FuseOSError(errno.EACCES)

	def release(self, path, fh):
		print "release"
		#raise FuseOSError(errno.EACCES)

	def fsync(self, path, fdatasync, fh):
		print "fsync"
		raise FuseOSError(errno.EACCES)

if __name__ == '__main__':
	current_dir	= os.path.dirname(os.path.abspath(__file__))
	mount_dir	= os.path.abspath(current_dir + '/../mnt')
	FUSE(Passthrough(), mount_dir, foreground=True)

