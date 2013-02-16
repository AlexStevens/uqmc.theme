from five import grok
from zope.interface import Interface
from Products.CMFCore.utils import getToolByName
from plone.app.layout.viewlets.interfaces import IPortalFooter

from uqmc.theme.interfaces import IThemeSpecific


grok.templatedir('templates')
grok.layer(IThemeSpecific)


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
