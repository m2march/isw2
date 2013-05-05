#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Version 1.0 12/01/2010

# ***************************************************************************
# *   Copyright (C) 2010, Paul Lutus                                        *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU General Public License for more details.                          *
# *                                                                         *
# *   You should have received a copy of the GNU General Public License     *
# *   along with this program; if not, write to the                         *
# *   Free Software Foundation, Inc.,                                       *
# *   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             *
# ***************************************************************************

import re, sys, shutil

class PyBeautify:

  def __init__(self):
    self.default_indent = 2

  # split line into indent and content
  def parse_line(self,s):
    indent,content = re.search(r'^(\s*)(.*)$',s).groups()
    return indent,len(indent),content

  def parse_stream(self,stream,path,indv):
    lines = [line.expandtabs().rstrip() for line in stream.readlines()]

    # pass 1: find the minimum indent
    mi = 1000000
    for line in lines:
      if(re.search(r'\S',line)): # only non-blank lines
        indent,li,content = self.parse_line(line)
        if(li > 0 and li < mi): mi = li

    # pass 2: create output string with specified indentation
    output = []
    for n,line in enumerate(lines):
      indent,li,content = self.parse_line(line)
      if(li % mi != 0): # if indentation is not a multiple of mi
        sys.stderr.write("Warning: inconsistent indentation in line %d of file \"%s\".\n" \
        % (n+1,path))
      iv = li * indv / mi # create indent value
      output.append("%s%s" % (' ' * iv,content))
    return '\n'.join(output) + '\n'

  def parse_file(self,path,indv):
    if (path == '-'): # stdin, stdout
      print(self.parse_stream(sys.stdin,path,indv)) # end = ' '
    else: # it's a file
      try: # making a backup copy
        shutil.copyfile(path,path+"~")
      except: # backup failed
        sys.stderr.write("Error: unable to create backup copy of file \"%s\", quitting.\n" \
        % path)
        exit(1)
      with open(path) as fh: # read the file
        output = self.parse_stream(fh,path,indv)
      with open(path,'w') as fh: # write the result
        fh.write(output)

  def process(self):
    sys.argv.pop(0) # drop program name
    if (not sys.argv): # no program arguments
      sys.stderr.write("Usage: [indent default %d] filenames or \"-\" for stream\n" \
      % self.default_indent)
      exit(0)
    else:
      try: # is the first argument a number?
        indent = int(sys.argv[0])
        sys.argv.pop(0) # drop the number
      except: # not a number, probably a file name
        indent = self.default_indent
      if(indent <= 0 or indent > 64): # test of acceptable indentations
        sys.stderr.write("Error: bad indent entry value: \"%d\", quitting.\n" \
        % indent)
        exit(1)
      for path in sys.argv:
        self.parse_file(path,indent)


PyBeautify().process()
