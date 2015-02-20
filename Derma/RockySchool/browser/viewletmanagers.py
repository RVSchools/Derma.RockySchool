from Products.Five.viewlet.manager import ViewletManagerBase

class PortalToolBarViewletManager(ViewletManagerBase):
    """A custom viewlet manager to wrap the breadcrumbs & tools plone viewlets.
    """
    def __getitem__(self, name):
        """Overriding getitem to call update() on access
        """
        viewlet = super(PortalToolBarViewletManager, self).__getitem__(name)
        viewlet.update()

        return viewlet
