AIDungeon Import & Export Plugin
######################################################

:date: 2020-08-08 16:31
:category: article
:summary: Greasemonkey Plugin
:tags: AIDungeon,greasemonkey,plugin

.. block-danger:: Warning:

  The script *might* overwrite existing entries (It really shouldn't but I haven't tested it enough,) use with caution.


Link to greasyfork plugin: `AIDungeon - Import and Export World Entries as Json <https://greasyfork.org/en/scripts/408237-aidungeon-import-and-export-world-entries-as-json>`_

Example of Json of World Entries:
=================================

.. code-block:: json

        [
           {"key": "This is a key", "entry": "This is the World Entry"},

           {"key": "This is another key", "entry": "This is another World Entry"},

           {"key": "This is a key", "entry": "This is the World Entry"}
        ]


|
| You can also add optional "show": true/false ( if not assigned, it default to false ) to toggle hidden world info:

.. code-block:: json

        {"key": "key", "entry": "entry", "show": true }

|

.. frame:: Note

  The scripts tries to emulate the user clicking on "Add World Info" button to fill the next entry, this gets slower and slower the more entries you have. This has something to do with AIDungeon itself, not the script.

|
| Feedback or suggestions are welcome.
|

