from zope.interface import implements
from plone.app.workflow.interfaces import ISharingPageRole
from Products.CMFCore import permissions as core_permissions

class ManagerRole(object):
    implements(ISharingPageRole)
    
    title = "Can manage"
    required_permission = core_permissions.ManagePortal

