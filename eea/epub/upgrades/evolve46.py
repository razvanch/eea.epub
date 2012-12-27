""" eea.epub 4.6 upgrade steps
"""
from Products.CMFCore.utils import getToolByName
from types import InstanceType
from eea.epub.mimetype import epub_mimetype
import logging

logger = logging.getLogger('eea.epub: setuphandlers')

def registerMimeType(self,  mimetype):
    """ register mimetypes
    """
    if type(mimetype) != InstanceType:
        mimetype = mimetype()
    mimetypes_registry = getToolByName(self, 'mimetypes_registry')
    mimetypes_registry.register(mimetype)
    logger.info("Registered mimetype %s" % mimetype)

def installMimeTypes(self):
    """ Install epub mimetype 
    """
    logger.info("Installing epub_mimetype mimetype")
    registerMimeType(self, epub_mimetype)
    logger.info("Done Installing epub_mimetype mimetype")

def reindexFileEpubs(self):
    """ Reindex epubs which were uploaded through file upload 
    """
    catalog = getToolByName(self, 'portal_catalog')
    results = catalog.searchResults(filetype='application/zip')
    for brain in results:
        name = brain.id
        print name