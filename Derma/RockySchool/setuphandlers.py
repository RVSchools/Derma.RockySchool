from browser.interfaces import IIconbarConfiguration
from config import IconbarConfiguration

def setupVarious(context):
    if context.readDataFile('Derma.RockySchool_various.txt') is None:
        return
    portal = context.getSite()
    sm = portal.getSiteManager()
    if not sm.queryUtility(IIconbarConfiguration, name='iconbar_config'):
        sm.registerUtility(IconbarConfiguration(),
                           IIconbarConfiguration,
                           'iconbar_config')
