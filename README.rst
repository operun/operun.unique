Introduction
============

operun.unique provides an interface to check the uniqueness of a content type.


Compatibility
=============

Version 1.0.0 is tested with Plone 4.3.x.


Installation
============

Add this line in the eggs section of your ``buildout.cfg``

.. code:: ini

    eggs =
        ...
        operun.unique


Add the interface to your content type class

.. code::

from operun.unique.interfaces import IUnique

class ContentType(xxx):
	"""Content Type
	"""
	implements(IContentType, IUnique)


Uninstalling
------------

TBD.


Installation as a dependency from another product
-------------------------------------------------

If you want to add operun.crm as a dependency from another products use the profile ``default`` in your ``metadata.xml``.

.. code:: xml

    <metadata>
      <version>1</version>
        <dependencies>
            <dependency>profile-operun.unique:default</dependency>
        </dependencies>
    </metadata>


Toubleshooting
==============

Please report issues in the bugtracker at https://github.com/operun/operun.unique/issues.


Branches
========

The master-branch supports Plone 4 only.


License
=======

GNU General Public License, version 2


Contributors
============

* Stefan Antonelli <stefan.antonelli@operun.de>
