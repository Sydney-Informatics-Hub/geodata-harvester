Module geodata_harvester.widgets.ipyfilechooser.filechooser
===========================================================

Classes
-------

`FileChooser(path: str = '/Users/seb/CTDS/Projects/AgReFed/Harvester/geodata-harvester', filename: str = '', title: str = '', select_desc: str = 'Select', change_desc: str = 'Change', show_hidden: bool = False, select_default: bool = False, dir_icon: Optional[str] = '📁 ', dir_icon_append: bool = False, show_only_dirs: bool = False, filter_pattern: Optional[Sequence[str]] = None, sandbox_path: Optional[str] = None, layout: ipywidgets.widgets.widget_layout.Layout = Layout(width='500px'), **kwargs)`
:   FileChooser class.
    
    Initialize FileChooser object.

    ### Ancestors (in MRO)

    * ipywidgets.widgets.widget_box.VBox
    * ipywidgets.widgets.widget_box.Box
    * ipywidgets.widgets.domwidget.DOMWidget
    * ipywidgets.widgets.widget_core.CoreWidget
    * ipywidgets.widgets.valuewidget.ValueWidget
    * ipywidgets.widgets.widget.Widget
    * ipywidgets.widgets.widget.LoggingHasTraits
    * traitlets.traitlets.HasTraits
    * traitlets.traitlets.HasDescriptors

    ### Instance variables

    `default: str`
    :   Get the default value.

    `default_filename: str`
    :   Get the default_filename value.

    `default_path: str`
    :   Get the default_path value.

    `dir_icon: Optional[str]`
    :   Get dir icon value.

    `dir_icon_append: bool`
    :   Get dir icon value.

    `filter_pattern: Optional[Sequence[str]]`
    :   Get file name filter pattern.

    `rows: int`
    :   Get current number of rows.

    `sandbox_path: Optional[str]`
    :   Get the sandbox_path.

    `selected: Optional[str]`
    :   Get selected value.

    `selected_filename: Optional[str]`
    :   Get the selected_filename.

    `selected_path: Optional[str]`
    :   Get selected_path value.

    `show_hidden: bool`
    :   Get _show_hidden value.

    `show_only_dirs: bool`
    :   Get show_only_dirs property value.

    `title: str`
    :   Get the title.

    `value: Optional[str]`
    :   Get selected value.

    ### Methods

    `get_interact_value(self) ‑> Optional[str]`
    :   Return the value which should be passed to interactive functions.

    `refresh(self) ‑> None`
    :   Re-render the form.

    `register_callback(self, callback: Callable[[Optional[ForwardRef('FileChooser')]], None]) ‑> None`
    :   Register a callback function.

    `reset(self, path: Optional[str] = None, filename: Optional[str] = None) ‑> None`
    :   Reset the form to the default path and filename.