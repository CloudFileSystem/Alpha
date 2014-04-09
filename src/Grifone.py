#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import os.path
import stat
import errno
from fuse import FUSE, FuseOSError, Operations

from grifone.metadata import Metadata

class Grifone(Operations):
	def __init__(self):
		# initialize metadata
		self.metadata = Metadata()

	# +===============================================
	# | Filesystem method
	# +===============================================
	def access(self, path, mode):
		print "ACCESS: (path=%s, mode=%s)" %(path, mode)
		raise FuseOSError(errno.EACCES)

	def chmod(self, path, mode):
		print "CHMOD: (path=%s, mode=%s)" %(path, mode)
		raise FuseOSError(errno.EACCES)

	def chown(self, path, mode):
		print "CHOWN: (path=%s, mode=%s)" %(path, mode)
		raise FuseOSError(errno.EACCES)

	def getattr(self, path, fh=None):
		print "GETATTR: (path=%s, fh=%s)" %(path, fh)
		node = self.metadata.getNode(path)
		if node == None:
			raise FuseOSError(errno.EACCES)
		return self.metadata.stat(node)

	def readdir(self, path, fh):
		print "READDIR: (path=%s, fh=%s)" %(path, fh)
		raise FuseOSError(errno.EACCES)
		#return ['.', '..'] + os.listdir(path)

	def readlink(self, path):
		print "READLINK: (path=%s)" %(path, fh)
		raise FuseOSError(errno.EACCES)

	def mknod(self, path, mode, dev):
		print "MKNOD: (path=%s, mode=%s, dev=%s)" %(path, mode, dev)
		raise FuseOSError(errno.EACCES)

	def mkdir(self, path, mode):
		print "MKDIR: (path=%s, mode=%s)" %(path, mode)
		raise FuseOSError(errno.EACCES)

	def rmdir(self, path):
		print "RMDIR: (path=%s)" %(path)
		raise FuseOSError(errno.EACCES)

	def statfs(self, path):
		print "STATFS: (path=%s)" %(path)
		raise FuseOSError(errno.EACCES)

	def unlink(self, path):
		print "UNLINK: (path=%s)" %(path)
		raise FuseOSError(errno.EACCES)

	def symlink(self, target, source):
		print "SYMLINK: (target=%s, source=%s)" %(target, source)
		raise FuseOSError(errno.EACCES)

	def rename(self, old, new):
		print "SYMLINK: (old=%s, new=%s)" %(old, new)
		raise FuseOSError(errno.EACCES)

	def link(self, target, source):
		print "LINK: (target=%s, source=%s)" %(target, source)
		raise FuseOSError(errno.EACCES)

	def utimens(self, path, times=None):
		print "UTIMES: (path=%s, times=%s)" %(path, times)
		raise FuseOSError(errno.EACCES)

	# +===============================================
	# | File method
	# +===============================================
	def open(self, path, flags):
		print "OPEN: (path=%s, flags=%s)" %(path, times)
		raise FuseOSError(errno.EACCES)

	def create(self, path, mode):
		print "CREATE: (path=%s, mode=%s)" %(path, mode)
		raise FuseOSError(errno.EACCES)

	def read(self, path, size, offset, fh):
		print "READ: (path=%s, size=%s, offset=%s, fh=%s)" %(path, size, offset, fh)
		raise FuseOSError(errno.EACCES)

	def write(self, path, data, offset, fh):
		print "READ: (path=%s, data=%s, offset=%s, fh=%s)" %(path, data, offset, fh)
		raise FuseOSError(errno.EACCES)

	def truncate(self, path, length, fh=None):
		print "READ: (path=%s, length=%s, fh=%s)" %(path, length, fh)
		raise FuseOSError(errno.EACCES)

	def flush(self, path, fh):
		print "READ: (path=%s, fh=%s)" %(path, fh)
		raise FuseOSError(errno.EACCES)

	def release(self, path, fh):
		print "RELEASE: (path=%s, fh=%s)" %(path, fh)
		raise FuseOSError(errno.EACCES)

	def fsync(self, path, datasync, fh):
		print "FSYNC: (path=%s, datasync, fh=%s)" %(path, datasync, fh)
		raise FuseOSError(errno.EACCES)

if __name__ == '__main__':
	mntpoint = os.path.abspath('%s/../mnt' %(os.path.dirname(os.path.abspath(__file__))))
	print "I will mount %s" %(mntpoint)
	FUSE(Grifone(), mntpoint, foreground=True)

