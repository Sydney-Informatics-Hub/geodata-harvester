Module geodata_harvester.widgets.ipyfilechooser.utils
=====================================================
Helper functions for ipyfilechooser.

Functions
---------

    
`get_dir_contents(path: str, show_hidden: bool = False, show_only_dirs: bool = False, dir_icon: Optional[str] = None, dir_icon_append: bool = False, filter_pattern: Optional[Sequence[str]] = None, top_path: Optional[str] = None) ‑> List[str]`
:   Get directory contents.

    
`get_drive_letters() ‑> List[str]`
:   Get all drive letters minus the drive used in path.

    
`get_subpaths(path: str) ‑> List[str]`
:   Walk a path and return a list of subpaths.

    
`has_parent(path: str) ‑> bool`
:   Check if a path has a parent folder.

    
`has_parent_path(path: str, parent_path: Optional[str]) ‑> bool`
:   Verifies if path falls under parent_path.

    
`is_valid_filename(filename: str) ‑> bool`
:   Verifies if a filename does not contain illegal character sequences

    
`match_item(item: str, filter_pattern: Sequence[str]) ‑> bool`
:   Check if a string matches one or more fnmatch patterns.

    
`normalize_path(path: str) ‑> str`
:   Normalize a path string.

    
`prepend_dir_icons(dir_list: Iterable[str], dir_icon: str, dir_icon_append: bool = False) ‑> List[str]`
:   Prepend unicode folder icon to directory names.

    
`strip_parent_path(path: str, parent_path: Optional[str]) ‑> str`
:   Remove a parent path from a path.