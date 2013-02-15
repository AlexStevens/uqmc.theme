from zope.interface import Interface
from zope.viewlet.interfaces import IViewletManager

class IThemeSpecific(Interface):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "NVP Theme" theme, this interface must be its layer
       (in skin/viewlets/configure.zcml).
    """

class IBetweenContent(IViewletManager):
    """ Viewlet manager for in between plone.portaltop and plone.abovecontent
    """
