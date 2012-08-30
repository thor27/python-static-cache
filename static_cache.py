#-*- coding: utf-8 -*-
# Simple permanent cache for Methods and Functions
# Copyright (C) 2012  Thomaz de Oliveira dos Reis
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import cPickle

class Cache(object):
    """ Class that allows a permanent cache from any method or function
        returning the same result for an already processed method
    """
    def __init__(self,original_method):
        """ Receiveis the original method/function as argument,
            and starts cache data. Can be used as a decorator,
            but for improved options there is a cache decorator 
            method bellow.
        """
        self.cached_data = {}
        self.original_method = original_method
    
    def key_method(self,*args, **kwargs):
        """ Returns the key for the new data to cache. This key
            must be uniq per method result. It defaults is to 
            serialize arguments as string
        """
        arguments = (args,kwargs)
        return cPickle.dumps(arguments)
    
    def __call__(self,*args, **kwargs):
        """ When decorated, and the function is called, returns the
            cache value if it exists, if not, executes original method
            and cache the results
        """
        key = self.key_method(*args,**kwargs)
        if not self.cached_data.has_key(key):
            self.cached_data[key] = self.original_method(*args,**kwargs)
        return self.cached_data[key]

def cache(*args, **kwargs):
    """ Cache decorator. If key_function argument is supplied,
        creates a new Cache class with key_function as the new
        method for returning keys. Useful when arguments cannot
        be cPickled or arguments can be processed for improved
        cache.
        
        Example usages:
        
        @cache
        def my_function(my_arg1, my_arg2):
            #My code goes here
        
        or, if args can't be cPickled:
        
        @cache(key_function=lambda my_complex_arg: my_complex_arg.unique_key)
        def my_complex_function(my_complex_arg):
            #My code goes her
    """
    
    key_function = kwargs.get('key_function',None)
    
    if not key_function:
        #Standard decorator, already return 
        #object
        return Cache(*args, **kwargs)
    
    class inner_cache(Cache):
        def key_method(self, *args,**kwargs):
            return key_function(*args, **kwargs)
    
    # Double decorator, return class
    # to be the standard decorator
    return inner_cache