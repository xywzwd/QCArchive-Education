# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class eduside(Component):
    """An eduside component.


Keyword arguments:
- id (string; default 'orb')
- style (dict; optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'style']
        self._type = 'eduside'
        self._namespace = 'qcedu'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'style']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(eduside, self).__init__(**args)
