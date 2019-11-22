# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class appsidebarnav(Component):
    """An appsidebarnav component.
CoreUI sidebar nav component.

This component manages the location in a multi-page much as Dash Core Components `Location` component.
It is also compatible with the Dash Core Components `Link` component.
See https://dash.plot.ly/urls for details.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children, defaults to `navConfig.items`.
- id (string; default 'appsidebarnav'): The ID used to identify this component in Dash callbacks, defaults to `appsidebarnav`.
- className (string; optional): The CSS class name, defaults to `sidebar-nav`.
- pathname (string; optional): The pathname in window.location - e.g., "/my/full/pathname"
- search (string; optional): The search in window.location - e.g., "?myargument=1"
- hash (string; optional): The hash in window.location - e.g., "#myhash"
- href (string; optional): The href in window.location - e.g., "/my/full/pathname?myargument=1#myhash"
- refresh (boolean; default True): Refresh the page when the location is updated? Default to `true`.
- navConfig (boolean | number | string | dict | list; default {
  items: [
    {
      name: 'Dashboard',
      url: '/dashboard',
      icon: 'cui-speedometer icons',
      badge: { variant: 'info', text: 'NEW' }
    }]
})
- navFunc (string; optional): TODO document this.
- isOpen (boolean; default False): The isOpen flag, defaults to `false`.
- staticContext (boolean | number | string | dict | list; optional): TODO document this.
- tag (string; default 'nav'): The HTML tag, defaults to `nav`.
- style (boolean | number | string | dict | list; optional)"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, pathname=Component.UNDEFINED, search=Component.UNDEFINED, hash=Component.UNDEFINED, href=Component.UNDEFINED, refresh=Component.UNDEFINED, navConfig=Component.UNDEFINED, navFunc=Component.UNDEFINED, isOpen=Component.UNDEFINED, staticContext=Component.UNDEFINED, tag=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'pathname', 'search', 'hash', 'href', 'refresh', 'navConfig', 'navFunc', 'isOpen', 'staticContext', 'tag', 'style']
        self._type = 'appsidebarnav'
        self._namespace = 'qcedu'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'pathname', 'search', 'hash', 'href', 'refresh', 'navConfig', 'navFunc', 'isOpen', 'staticContext', 'tag', 'style']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(appsidebarnav, self).__init__(children=children, **args)
