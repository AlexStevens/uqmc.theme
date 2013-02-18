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
                title = 'Home'
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
        about = portal['about']
        about.portal_workflow.doActionFor(about, 'publish')

    if 'membership' not in portal:
        portal.invokeFactory(
                'Folder',
                'membership',
                title = 'Membership'
            )
        membership = portal['membership']
        membership.portal_workflow.doActionFor(membership, 'publish')

    if 'trips-events' not in portal:
        portal.invokeFactory(
                'Folder',
                'trips-events',
                title = 'Trips & Events'
            )
        trips = portal['trips-events']
        trips.portal_workflow.doActionFor(trips, 'publish')

    if 'useful-info' not in portal:
        portal.invokeFactory(
                'Folder',
                'useful-info',
                title = 'Useful Info'
            )
        useful = portal['useful-info']
        useful.portal_workflow.doActionFor(useful, 'publish')

    if 'training' not in portal:
        portal.invokeFactory(
                'Folder',
                'training',
                title = 'Training'
            )
        training = portal['training']
        training.portal_workflow.doActionFor(training, 'publish')

    if 'executives' not in portal:
        portal.invokeFactory(
                'Folder',
                'executives',
                title = 'Executives'
            )
        executives = portal['executives']
        executives.portal_workflow.doActionFor(executives, 'publish')

    if 'contacts' not in portal:
        portal.invokeFactory(
                'Folder',
                'contacts',
                title = 'Contacts'
            )
        contacts = portal['contacts']
        contacts.portal_workflow.doActionFor(contacts, 'publish')

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

    if 'background' not in portal:
        portal.invokeFactory(
                'Folder',
                'background',
                title = 'Background Pictures'
            )
