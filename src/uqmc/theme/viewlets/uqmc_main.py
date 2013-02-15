from five import grok
from zope.interface import Interface
from plone.app.layout.viewlets.interfaces import IPortalFooter

from uqmc.theme.interfaces import IThemeSpecific


grok.templatedir('templates')
grok.layer(IThemeSpecific)


class FooterViewlet(grok.Viewlet):
    grok.name('uqmc.theme.footer')
    grok.context(Interface)
    grok.viewletmanager(IPortalFooter)
    grok.order(1)
