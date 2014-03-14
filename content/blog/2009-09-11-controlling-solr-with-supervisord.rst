Controlling Solr with supervisord
#################################
:date: 2009-09-11 20:10
:author: Fschulze42
:category: Development

A while ago I found a solution to run `Solr`_ with `supervisord`_,
without leaking java processes, which you get when you use the generated
``solr-instance`` script with supervisord.

You need something like this in your supervisord.conf:

.. raw:: html

   <p>

::

    [program:solr]directory = ${solr-instance:jetty-destination}/..command = java -jar start.jarautostart = trueautorestart = true

.. raw:: html

   </p>

The key is the ``directory`` option. With that the ``command`` is
executed in that directory, which starts Solr correctly and doesn't
leave java processes when stopping it with supervisord.

I discovered today that Solr, when used with
`collective.recipe.solrinstance`_, by default logs every query to
stdout.

The solution is to change the ``command`` like the following:

.. raw:: html

   <p>

::

    command = java -Djava.util.logging.config.file=${buildout:directory}/etc/solr-logging.properties -jar start.jar

.. raw:: html

   </p>

Now you just need to add the ``solr-logging.properties`` file with
something like this as content:

.. raw:: html

   <p>

::

    # Default global logging level:.level = WARNING

.. raw:: html

   </p>

.. _Solr: http://lucene.apache.org/solr/
.. _supervisord: http://supervisord.org/
.. _collective.recipe.solrinstance: http://pypi.python.org/pypi/collective.recipe.solrinstance
