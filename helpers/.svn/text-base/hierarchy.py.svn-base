from apps.intent.pes.knowandguideem.models.peskgmrpb import PesKgmRpb,PesKgmHierarchy,PesKgmTo

class Hierarchy():
    def __init__(self):
        self.cur_rpb = None
        self.pars = {}
        self.list = []
        self.to_ls = []
        self.structure_ls = []
        self.rpb_ls = []
        self.to = None
        self.structure = None
        self.rpb = None
        
    def set(self, to=None, structure=None, rpb=None):
        if to:
            self.to = to
        if structure:
            self.structure = structure
        if rpb:
            self.rpb = rpb
        #print str(self.to)+','+str(self.structure)+','+str(self.rpb)
    
    def get_children(self):
        if self.to:
            self.get_to()
        if self.structure:
            self.get_structure()
        if self.rpb:
            self.get_rpb()
        return self.to_ls,self.structure_ls
    
    def get_children_self(self):
        if self.to:
            self.get_to_self()
        if self.structure:
            self.get_structure_self()
        if self.rpb:
            self.get_rpb()
        #print self.to_ls,self.structure_ls,'---------------'
        return self.to_ls,self.structure_ls
    
    def get_to(self):
        #print 'TO'
        self.to_ls.append(self.to)
        #print self.to
        #print self.to_ls
        self.get_to_children(self.to)
        
    def get_structure(self):
        self.get_structure_children(self.structure)
    
    def get_structure_self(self):
        self.structure_ls.append(self.structure)
        self.get_structure_children(self.structure)
    
    def get_to_self(self):
        self.to_ls.append(self.to)
        self.get_to_children(self.to)
        
    def get_all_rpb(self):
        rpb_to = PesKgmRpb.objects.filter(to_id__in=self.get_children()[0]).values_list('id',flat=True)
        rpb_hierarchy = PesKgmRpb.objects.filter(hierarchy_id__in=self.get_children()[1]).values_list('id',flat=True)
        return list(rpb_to),list(rpb_hierarchy)
        
    def get_to_children(self,uid):
        _to = PesKgmTo.objects.filter(parent_id=uid)
        for i in _to:
            self.to_ls.append(i.id)
            #self.to_ls += i.id
            self.get_to_children(i.id)
    
    def get_structure_children(self,uid):
        _structure = PesKgmHierarchy.objects.filter(parent_id=uid)
        #print _structure,'pppppppppp'
        for i in _structure:
            self.structure_ls.append(i.id)
            #self.structure_ls += i.id
            self.get_structure_children(i.id)
    
    def get_rpb(self):
        rpb = PesKgmRpb.objects.get(pk=self.rpb)
        self.get_to_children(rpb.to_id)
        self.get_structure_children(rpb.hierarchy_id)
        self.to_ls.append(rpb.to_id)
        self.structure_ls.append(rpb.hierarchy_id)
    
    def get_parent(self):
        if self.structure:
            self.get_parent_struc()
        if self.to:
            self.get_parent_to()
        return self.to_ls,self.structure_ls
        
    def get_parent_struc(self):
        self.structure_ls.append(self.structure)
        self.get_structure_parent(self.structure)
    
    def get_parent_to(self):
        self.to_ls.append(self.to)
        self.get_to_parent(self.to)
    
    def get_structure_parent(self,uid):
        _structure = PesKgmHierarchy.objects.filter(pk=uid)
        for i in _structure:
            if i.parent_id:
                self.structure_ls.append(i.parent_id)
                self.get_structure_parent(i.parent_id)
    
    def get_to_parent(self,uid):
        _to = PesKgmTo.objects.filter(pk=uid)
        for i in _to:
            if i.parent_id:
                self.to_ls.append(i.parent_id)
                self.get_structure_parent(i.parent_id)
    
    
    @staticmethod
    def get_hierarchy_top_parent(cid):
      x = PesKgmHierarchy.objects.get(pk=cid)
      if x.parent_id != None:
        return Hierarchy.get_hierarchy_top_parent(x.parent_id)
      else:
        return x.id
    
    @staticmethod
    def get_full_hierarchy_name(cid):
      x = PesKgmHierarchy.objects.get(pk=cid)
      if x.parent_id != None:
        return Hierarchy.get_full_hierarchy_name(x.parent_id)+' -> '+x.description
      else:
        return x.description
    
    @staticmethod
    def get_hierarchy_choices(ls, ls2, acc_id, hid, depth=0):
      x = PesKgmHierarchy.objects.get(pk=hid)
      ls.append((x.id, ('-'*depth)+(x.description + ' (' + x.numcode + ')')))
      if acc_id == None:
        if x.id in ls2:
            pass
        else:
            ls2[x.id] = hid
            acc_id = hid
      else:
        if x.id in ls2:
            pass
        else:
            ls2[x.id] = acc_id
      
      for child_hid in PesKgmHierarchy.objects.filter(parent_id=hid):
        Hierarchy.get_hierarchy_choices(ls, ls2, acc_id, child_hid.id, depth+1)