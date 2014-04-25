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
		# file descriptor dictionary
		self.fd_init = 10
		self.fd_dict = dict()
		self.fd_buff = dict()

	# +===============================================
	# | Filesystem method
	# +===============================================
	def access(self, path, mode):
		node = self.metadata.getNode(path)
		if node == None:
			raise FuseOSError(errno.EACCES)
		return 0

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
			# No such file or directory
			raise FuseOSError(errno.ENOENT)
		return self.metadata.stat(node)

	def readdir(self, path, fh):
		print "READDIR: (path=%s, fh=%s)" %(path, fh)

		lists = self.metadata.getChildNodes(path)
		lists.append('.')
		lists.append('..')

		return lists

	def readlink(self, path):
		print "READLINK: (path=%s)" %(path, fh)
		raise FuseOSError(errno.EACCES)

	def mknod(self, path, mode, dev):
		print "MKNOD: (path=%s, mode=%s, dev=%s)" %(path, mode, dev)
		raise FuseOSError(errno.EACCES)

	def mkdir(self, path, mode):
		print "MKDIR: (path=%s, mode=%s)" %(path, mode)
		basepath, name = os.path.split(path)
		node = self.metadata.getNode(path)
		if node != None:
			raise FuseOSError(errno.EACCES)
		self.metadata.make_directory(basepath, name)

	def rmdir(self, path):
		print "RMDIR: (path=%s)" %(path)
		basepath, name = os.path.split(path)
		self.metadata.remove_directory(basepath, name)

	def statfs(self, path):
		print "STATFS: (path=%s)" %(path)
		raise FuseOSError(errno.EACCES)

	def unlink(self, path):
		print "UNLINK: (path=%s)" %(path)
		basepath, name = os.path.split(path)
		self.metadata.remove_file(basepath, name)

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
		self.metadata.update_times(path, times)
		return 0

	# +===============================================
	# | File method
	# +===============================================
	def open(self, path, flags, mode=None):
		print "OPEN: (path=%s, flags=%s)" %(path, flags)
		basepath, name = os.path.split(path)
		if flags & os.O_CREAT:
			self.metadata.make_file(basepath, name)

		# file descriptor process
		for i in range(self.fd_init, 4096):
			new_fd = self.fd_dict.get(i)
			if new_fd == None:
				self.fd_dict[i] = path
				return i
		raise FuseOSError(errno.EACCES)

	def create(self, path, mode):
		print "CREATE: (path=%s, mode=%s)" %(path, mode)
		return self.open(path, os.O_WRONLY | os.O_CREAT, mode)

	def read(self, path, size, offset, fh):
		print "READ: (path=%s, size=%s, offset=%s, fh=%s)" %(path, size, offset, fh)
		return self.fd_buff.get(path)
		#raise FuseOSError(errno.EACCES)

	def write(self, path, data, offset, fh):
		print "WRITE: (path=%s, offset=%s, fh=%s)" %(path, offset, fh)
		self.fd_buff[path] = data
		print self.fd_buff

		size = len(data)
		self.metadata.update_size(path, size)
		return size

	def truncate(self, path, length, fh=None):
		print "TRUNCATE: (path=%s, length=%s, fh=%s)" %(path, length, fh)
		#raise FuseOSError(errno.EACCES)

	def flush(self, path, fh):
		print "FLUSH: (path=%s, fh=%s)" %(path, fh)

	def release(self, path, fh):
		print "RELEASE: (path=%s, fh=%s)" %(path, fh)

	def fsync(self, path, datasync, fh):
		print "FSYNC: (path=%s, datasync=%s, fh=%s)" %(path, datasync, fh)

if __name__ == '__main__':
	mntpoint = os.path.abspath('%s/../mnt' %(os.path.dirname(os.path.abspath(__file__))))
	print "I will mount %s" %(mntpoint)
	FUSE(Grifone(), mntpoint, foreground=True, nonempty=True)

