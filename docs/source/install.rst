.. _install:

Installation of SwSpotify
=========================

This part of the documentation covers the installation of SwagLyrics for Spotify.
The first step to using any software package is getting it properly installed.


$ pip install SwSpotify
------------------------

To install SwagLyrics, simply run this simple command in your terminal of choice::

    $ pip install SwSpotify

SwagLyrics requires Python 3.6+. Use pip or pip3 depending on your installation.

Cool kids these days recommend doing :bash:`python -m pip install SwSpotify`, but either work.

Living on the edge
-------------------

SwSpotify is developed on GitHub, where the code is
`always available <https://github.com/SwagLyrics/SwSpotify>`_. It contains the latest code before it is released but should `hopefully` always work.

You can clone the public repository::

    $ git clone git://SwagLyrics/SwSpotify.git

Once you have a copy of the source, you can embed it in your own Python
package, or install it into your site-packages easily::

    $ cd SwSpotify
    $ pip install .