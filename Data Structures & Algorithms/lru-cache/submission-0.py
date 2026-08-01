class LRUCache:
    class Node:
        def __init__(self,key,val):
            self.val=val
            self.key=key
            self.prev=None
            self.next=None

        def unplug(self):
            if self.prev:
                self.prev.next=self.next
            if self.next:
                self.next.prev=self.prev
            
            self.prev=None
            self.next=None

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.nodes_by_val={}

        self.head=self.Node(None,None)
        self.tail=self.Node(None,None)

        self.head.next=self.tail
        self.tail.prev=self.head
    
    def removeLruNode(self):
        node_to_delete=self.tail.prev

        if node_to_delete is self.head:
            return
        
        val_to_remove=node_to_delete.val
        del self.nodes_by_val[node_to_delete.key]
        node_to_delete.unplug()

    def plugAsMruNode(self,node):
        node.unplug()
        new_next=self.head.next

        self.head.next=node
        node.prev=self.head

        new_next.prev=node
        node.next=new_next

    def get(self, key: int) -> int:

       
        if key not in self.nodes_by_val:
            return -1
        
        self.plugAsMruNode(self.nodes_by_val[key])
        return self.nodes_by_val[key].val
        
    def put(self, key: int, value: int) -> None:
        print(self.nodes_by_val)
        if key not in self.nodes_by_val:
            self.nodes_by_val[key]=self.Node(key,value)
        
        self.nodes_by_val[key].val=value
        self.plugAsMruNode(self.nodes_by_val[key])
        
        if len(self.nodes_by_val)>self.capacity:
            self.removeLruNode()
        
