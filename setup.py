#!/usr/bin/env python
##############################################################################
#
#    XMI2ODOO, XMI convesort to Odoo module
#    Copyright (C) 2012 Coop Trab Moldeo Interactive, Grupo AdHoc S.A.
#    (<http://www.moldeointeractive.com.ar>; <www.grupoadhoc.com.ar>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from setuptools import setup, find_packages

setup(name='xmi2odoo',
      version='1.3.19',
      author='Cristian S. Rocha',
      author_email='cristian.rocha@moldeointeractive.com.ar',
      maintainer='Cristian S. Rocha',
      maintainer_email='cristian.rocha@moldeo.coop',
      url='http://www.moldeointeractive.com.ar/',
      description='XMI Conversor to OpenERP modules.',
      long_description="""
      With this command you can create Odoo modules from a UML description in XMI file or UML file generated by ArgoUML.
      """,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Natural Language :: English',
          'Operating System :: Unix',
          'Programming Language :: Python :: 2.6',
          'Topic :: Software Development :: Build Tools',
      ],
      scripts=['xmi2odoo/scripts/xmi2odoo'],
      packages=find_packages(),
      test_suite='xmi2odoo.test',
      install_requires=['Genshi','sqlalchemy'],
      include_package_data=True,
      dependency_links=[],
   )

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
