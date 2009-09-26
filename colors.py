# -*- encoding: utf-8 -*-
#
#       colors.py
#       
#       Copyright 2009 Rafael G. Martins <rafael@rafaelmartins.eng.br>
#       
#       Redistribution and use in source and binary forms, with or without
#       modification, are permitted provided that the following conditions are
#       met:
#       
#       * Redistributions of source code must retain the above copyright
#         notice, this list of conditions and the following disclaimer.
#       * Redistributions in binary form must reproduce the above
#         copyright notice, this list of conditions and the following disclaimer
#         in the documentation and/or other materials provided with the
#         distribution.
#       * Neither the name of the  nor the names of its
#         contributors may be used to endorse or promote products derived from
#         this software without specific prior written permission.
#       
#       THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#       "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#       LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#       A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#       OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#       SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#       LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#       DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#       THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#       (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#       OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""PyColors

Python module to ease the use of colors on programs that run on CLI.
Works fine on Linux or on any Operating System running BaSH or compatibles.
If the shell's not color compatible, he'll get the raw string.
The module have predefined some basic colors, but you can use any color,
if you know the color code.

Example:
    
    >>> from colors import Color
    >>> yellow = Color('1;33')
    >>> print yellow('Hello World')
    Hello World
    
    >>> from colors import red
    >>> print red('Ola Mundo')

"""

__all__ = [
    'Colors', 'disable_colors', # Main object and function
    
    # color objects
    'black', 'blue', 'green', 'cyan', 'red', 'purple', 'brown',
    'light_gray', 'dark_gray','light_blue', 'light_green','light_cyan',
    'light_red', 'light_purple', 'yellow', 'white',
]

__author__ = 'Rafael Goncalves Martins'
__email__ = 'rafael@rafaelmartins.eng.br'

__description__ = 'Python module to ease the use of colors on programs that run on CLI'
__url__ = 'http://projects.rafaelmartins.eng.br/pycolors/'
__copyright__ = '(c) 2009 %s' % __author__
__license__ = 'BSD'

__version__ = '0.1'


from os import linesep, environ, devnull
from subprocess import Popen, PIPE

def __has_colors():
    """_has_colors(): Checks if the current shell supports colors
    
    """
    
    p = Popen(
        'tput colors',
        stdout = PIPE,
        stderr = open(devnull, 'w'),
        shell = True
    )

    try:
        num_colors = int(p.stdout.read())
    except:
        num_colors = 1
    
    if num_colors > 1:
        environ['HASCOLORS'] = '1'

def disable_colors():
    """This function forces the non-usage of colors. You can also disable
    colors setting the environment variable DISABLE_COLORS with any value.
    
    """
    
    environ['DISABLE_COLORS'] = '1'


class Color(object):
    """Color: The main object from this module
    
    """
    
    def __init__(self, color_code):
        """Initialize the color object
        
        """
        
        self.color_code = color_code
    
    def __call__(self, string):
        """Callable object, used to return the string with color markup
        or the raw string if colors aren't available on the current
        shell or are disabled by user.
        
        """
        
        string = str(string)
        
        if 'HASCOLORS' in environ and 'DISABLE_COLORS' not in environ:
            return '\033[%sm%s\033[1;0m' % (self.color_code, string)
        else:
            return string


__has_colors()


black = Color('0;30')
blue = Color('0;34')
green = Color('0;32')
cyan = Color('0;36')
red = Color('0;31')
purple = Color('0;35')
brown = Color('0;33')
light_gray = Color('0;37')     
dark_gray = Color('1;30')
light_blue = Color('1;34')
light_green = Color('1;32')
light_cyan = Color('1;36')
light_red = Color('1;31')
light_purple = Color('1;35')
yellow = Color('1;33')
white = Color('1;37')
