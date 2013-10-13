Keep trac of your subversion location
#####################################
:date: 2009-08-09 11:09
:author: Fschulze42
:category: Development

Many people use `trac`_ and `Subversion`_ together. Inside trac you can
browse the contents of the Subversion repository. There is a plugin to
link from that browser to your actual Subversion repository called
`SubversionLocationPlugin`_.

For the other way around you can use the following XSLT. Most of it just
recreates the default Subversion look. The interesting part is the
``<xsl:element name="a">`` in ``<xsl:template match="index">``. There
the link is created and it's the place where you can set your own URL of
your trac instance (the trac\_prefix variable). To use this file, you
add the SVNIndexXSLT option (see "`Customizing the look`_\ " in the
Subversion book) into you Apache configuration and set it to the url
under which the file is accessible.

.. raw:: html

   <p>

::

    <?xml version="1.0"?><xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">  <xsl:output method="html"/>  <xsl:template match="*"/>  <xsl:template match="svn">    <html>      <head>        <title>          Revision <xsl:value-of select="index/@rev"/>:          <xsl:value-of select="index/@path"/>        </title>      </head>      <body>        <xsl:apply-templates/>        <hr noshade="noshade"/>        <em>Powered by </em>        <xsl:element name="a">          <xsl:attribute name="href">            <xsl:value-of select="@href"/>          </xsl:attribute>          <xsl:text>Subversion</xsl:text>        </xsl:element>        <xsl:text> </xsl:text>        <xsl:value-of select="@version"/>.      </body>    </html>  </xsl:template>  <xsl:template match="index">    <xsl:element name="a">      <xsl:variable name="trac_prefix" select="'https://dev.example.com/browser'"/>      <xsl:attribute name="href">        <xsl:value-of select="concat($trac_prefix, @path)"/>      </xsl:attribute>      Jarn-Trac Location    </xsl:element>    <h2>      Revision <xsl:value-of select="@rev"/>:      <xsl:value-of select="@path"/>    </h2>    <ul>      <xsl:apply-templates select="updir"/>      <xsl:apply-templates select="dir"/>      <xsl:apply-templates select="file"/>    </ul>  </xsl:template>  <xsl:template match="updir">    <li><a href="..">..</a></li>  </xsl:template>  <xsl:template match="dir">    <li>      <xsl:element name="a">        <xsl:attribute name="href">          <xsl:value-of select="@href"/>        </xsl:attribute>        <xsl:value-of select="@name"/>        <xsl:text>/</xsl:text>      </xsl:element>    </li>  </xsl:template>  <xsl:template match="file">    <li>      <xsl:element name="a">        <xsl:attribute name="href">          <xsl:value-of select="@href"/>        </xsl:attribute>        <xsl:value-of select="@name"/>      </xsl:element>    </li>  </xsl:template></xsl:stylesheet>

.. raw:: html

   </p>

The following XSLT is slightly more complex. It has an added
``<xsl:choose>`` part which adds links to customer specific trac
instances.

.. raw:: html

   <p>

::

    <?xml version="1.0"?><xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">  <xsl:output method="html"/>  <xsl:template match="*"/>  <xsl:template match="svn">    <html>      <head>        <title>          Revision <xsl:value-of select="index/@rev"/>:          <xsl:value-of select="index/@path"/>        </title>      </head>      <body>        <xsl:apply-templates/>        <hr noshade="noshade"/>        <em>Powered by </em>        <xsl:element name="a">          <xsl:attribute name="href">            <xsl:value-of select="@href"/>          </xsl:attribute>          <xsl:text>Subversion</xsl:text>        </xsl:element>        <xsl:text> </xsl:text>        <xsl:value-of select="@version"/>.      </body>    </html>  </xsl:template>  <xsl:template match="index">    <xsl:element name="a">      <xsl:variable name="trac_prefix" select="'https://dev.example.com/browser'"/>      <xsl:attribute name="href">        <xsl:value-of select="concat($trac_prefix, @path)"/>      </xsl:attribute>      Jarn-Trac Location    </xsl:element>    <xsl:choose>      <xsl:when test="starts-with(@path, '/customers/foo')">        -        <xsl:element name="a">          <xsl:variable name="trac_prefix" select="'https://trac.example.com/foo/browser'"/>          <xsl:attribute name="href">            <xsl:value-of select="concat($trac_prefix, substring-after(@path, '/customers/foo'))"/>          </xsl:attribute>          Foo-Trac Location        </xsl:element>      </xsl:when>      <xsl:when test="starts-with(@path, '/customers/bar')">        -        <xsl:element name="a">          <xsl:variable name="trac_prefix" select="'https://trac.example.com/bar/browser'"/>          <xsl:attribute name="href">            <xsl:value-of select="concat($trac_prefix, substring-after(@path, '/customers/bar'))"/>          </xsl:attribute>          Bar-Trac Location        </xsl:element>      </xsl:when>    </xsl:choose>    <h2>      Revision <xsl:value-of select="@rev"/>:      <xsl:value-of select="@path"/>    </h2>    <ul>      <xsl:apply-templates select="updir"/>      <xsl:apply-templates select="dir"/>      <xsl:apply-templates select="file"/>    </ul>  </xsl:template>  <xsl:template match="updir">    <li><a href="..">..</a></li>  </xsl:template>  <xsl:template match="dir">    <li>      <xsl:element name="a">        <xsl:attribute name="href">          <xsl:value-of select="@href"/>        </xsl:attribute>        <xsl:value-of select="@name"/>        <xsl:text>/</xsl:text>      </xsl:element>    </li>  </xsl:template>  <xsl:template match="file">    <li>      <xsl:element name="a">        <xsl:attribute name="href">          <xsl:value-of select="@href"/>        </xsl:attribute>        <xsl:value-of select="@name"/>      </xsl:element>    </li>  </xsl:template></xsl:stylesheet>

.. raw:: html

   </p>

I hope this is useful for some people. Since I've never used XSLT before
and I struggled quite a bit with building these, I would love some
feedback on my solution and possible improvements or simplifications.

.. _trac: http://trac.edgewall.org/
.. _Subversion: http://subversion.tigris.org/
.. _SubversionLocationPlugin: http://trac-hacks.org/wiki/SubversionLocationPlugin
.. _Customizing the look: http://svnbook.red-bean.com/en/1.5/svn.serverconfig.httpd.html#svn.serverconfig.httpd.extra.browsing
