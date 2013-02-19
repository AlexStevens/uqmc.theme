from five import grok
from zope.interface import Interface
from Products.CMFCore.utils import getToolByName
from plone.app.layout.viewlets.interfaces import IPortalFooter
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
import random

from uqmc.theme.interfaces import IThemeSpecific, IBackgroundMarker


grok.templatedir('templates')
grok.layer(IThemeSpecific)


def get_background_properties(brain):
    metadata = {}
    Title = brain.Title.split('|')
    
    if len(Title) > 1:
        metadata['Title'] = Title[0].strip()
        metadata['position'] = Title[1].strip().lower()
    else:
        metadata['Title'] = Title
        metadata['position'] = 'center'

    metadata['description'] = brain.Description
    metadata['url'] = brain.getURL()

    return metadata


class FooterViewlet(grok.Viewlet):
    grok.name('uqmc.theme.footer')
    grok.context(Interface)
    grok.viewletmanager(IPortalFooter)
    grok.order(1)

    def get_newest_newsitem(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        news_items = catalog({'portal_type': 'News Item',
                'sort_on': 'effective', 'sort_order': 'descending' })

        if len(news_items):
            return news_items[0]


class BackgroundFooterViewlet(grok.Viewlet):
    grok.name('uqmc.theme.background')
    grok.context(Interface)
    grok.viewletmanager(IPortalFooter)
    grok.order(0)

    def get_backgrounds(self):
        metadata = []

        fpath = '/'.join(self.context.getPhysicalPath()[0:2]) + '/background'
        photos = self.context.portal_catalog(
                portal_type='Image',
                path={'query':fpath}
            )

        for photo in photos:
            meta_photo = get_background_properties(photo)
            metadata.append(meta_photo)
        random.shuffle(metadata)

        return metadata
