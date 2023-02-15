Module geodata_harvester.widgets.ipywidgets_file_selector
=========================================================

Classes
-------

`IPFileSelector(*args, **kwargs)`
:   Widget that can be inserted into the DOM
    
    Parameters
    ----------
    tooltip: str
       tooltip caption
    layout: InstanceDict(Layout)
       widget layout
    
    Public constructor

    ### Ancestors (in MRO)

    * ipywidgets.widgets.domwidget.DOMWidget
    * ipywidgets.widgets.widget.Widget
    * ipywidgets.widgets.widget.LoggingHasTraits
    * traitlets.traitlets.HasTraits
    * traitlets.traitlets.HasDescriptors

    ### Instance variables

    `current_path`
    :   A trait for unicode strings.

    `home_path`
    :   A trait for unicode strings.

    `selected`
    :   An instance of a Python dict.
        
        One or more traits can be passed to the constructor
        to validate the keys and/or values of the dict.
        If you need more detailed validation,
        you may use a custom validator method.
        
        .. versionchanged:: 5.0
            Added key_trait for validating dict keys.
        
        .. versionchanged:: 5.0
            Deprecated ambiguous ``trait``, ``traits`` args in favor of ``value_trait``, ``per_key_traits``.

    `subdirs`
    :   An instance of a Python list.

    `subfiles`
    :   An instance of a Python list.