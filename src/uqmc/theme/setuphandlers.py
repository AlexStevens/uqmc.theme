def install(context):
    if context.readDataFile('uqmc.theme.marker.txt') is None:
        return

    portal = context.getSite()

    for folder in ['front-page', 'news', 'events', 'Members']:
        if folder in portal:
            portal.manage_delObjects([folder])

    if 'landing' not in portal:
        portal.invokeFactory(
                'Document',
                'landing',
                title = ' '
            )
        landing = portal['landing']
        landing.portal_workflow.doActionFor(landing, 'publish')
        portal.setDefaultPage('landing')

    if 'about' not in portal:
        portal.invokeFactory(
                'Folder',
                'about',
                title = 'About'
            )

    if 'membership' not in portal:
        portal.invokeFactory(
                'Folder',
                'membership',
                title = 'Membership'
            )

    if 'trips-events' not in portal:
        portal.invokeFactory(
                'Folder',
                'trips-events',
                title = 'Trips & Events'
            )

    if 'useful-info' not in portal:
        portal.invokeFactory(
                'Folder',
                'useful-info',
                title = 'Useful Info'
            )

    if 'training' not in portal:
        portal.invokeFactory(
                'Folder',
                'training',
                title = 'Training'
            )

    if 'executives' not in portal:
        portal.invokeFactory(
                'Folder',
                'executives',
                title = 'Executives'
            )

    if 'contacts' not in portal:
        portal.invokeFactory(
                'Folder',
                'contacts',
                title = 'Contacts'
            )

    if 'quartermaster' not in portal:
        portal.invokeFactory(
                'Folder',
                'quartermaster',
                title = 'Quartermaster Area'
            )
        types = ['uqmc.types.kit', 'uqmc.types.gear']
        qm = portal.quartermaster
        qm.setConstrainTypesMode(1)
        qm.setImmediatelyAddableTypes(types)
        qm.setLocallyAllowedTypes(types)
