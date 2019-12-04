# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import uvc.schriften


class UvcSchriftenLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=uvc.schriften)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'uvc.schriften:default')


UVC_SCHRIFTEN_FIXTURE = UvcSchriftenLayer()


UVC_SCHRIFTEN_INTEGRATION_TESTING = IntegrationTesting(
    bases=(UVC_SCHRIFTEN_FIXTURE,),
    name='UvcSchriftenLayer:IntegrationTesting',
)


UVC_SCHRIFTEN_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(UVC_SCHRIFTEN_FIXTURE,),
    name='UvcSchriftenLayer:FunctionalTesting',
)


UVC_SCHRIFTEN_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        UVC_SCHRIFTEN_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='UvcSchriftenLayer:AcceptanceTesting',
)
