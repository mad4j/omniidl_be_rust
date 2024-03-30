

from omniidl import idlast, idlvisitor, idlutil


class ExampleVisitor (idlvisitor.AstVisitor):
    
    def visitAST(self, node):
        
        for n in node.declarations():
            n.accept(self)
            
            
    def visitModule(self, node):
        for n in node.definitions():
            n.accept(self)
            
    def visitInterface(self, node):
        name = idlutil.ccolonName(node.scopedName())
        if node.mainFile():
            for c in node.callables():
                if isinstance(c, idlast.Operation):
                    print(name + "::" + c.identifier() + "()")

def run(tree, args):
    visitor = ExampleVisitor()
    tree.accept(visitor)
