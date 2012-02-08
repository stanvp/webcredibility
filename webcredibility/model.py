# -*- coding: utf-8 -*-
'''
Database model

@author: Stanislav Peshterliev
'''

from elixir import *

class Document(Entity):
    using_options(tablename='documents')
    
    url = Field(UnicodeText)
    topic = Field(UnicodeText)
    search_query = Field(UnicodeText)
    content = Field(UnicodeText)
    result_rank = Field(Integer)
    rating = Field(Integer) 
    expert_rating1 = Field(Integer)
    expert_rating2 = Field(Integer)
    features = OneToMany('Feature')
    
    def __repr__(self):
        return '<Document "%s" (%s)>' % (self.url, self.rating)
    
class Feature(Entity):
    using_options(tablename='features')
    
    name = Field(UnicodeText)
    value = Field(Float)
    document = ManyToOne('Document')    
    
    def __repr__(self):
        return '<Feature (%s, %s) - %s>' % (self.name, self.value, self.document.url)    
        
setup_all()
