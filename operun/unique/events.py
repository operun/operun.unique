from zope.component import adapter

from zope.component.hooks import getSite

from zope.lifecycleevent.interfaces import IObjectCreatedEvent
from zope.lifecycleevent import ObjectCopiedEvent

from Products.CMFCore.utils import getToolByName

from interfaces import IUnique

@adapter(IUnique, IObjectCreatedEvent)
def UniquenessPolice(unique_obj, event):
    plone_site = getSite()
    if isinstance(event, ObjectCopiedEvent):
        CopyError = 'Copy Error'
        try:
            catalog = getToolByName(plone_site, 'portal_catalog')
        except AttributeError:
            return
        results = catalog(portal_type = unique_obj.portal_type)
        if len(results)>0:
            raise CopyError
    else:
        assert unique_obj == event.object
        catalog = getToolByName(plone_site, 'portal_catalog')
        results = catalog(portal_type = unique_obj.portal_type)
        if len(results)>0:
            instance = results[0].getObject()
            instance.REQUEST.RESPONSE.redirect(instance.absolute_url())