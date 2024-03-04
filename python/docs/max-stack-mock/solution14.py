class MaxStack:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self,value):
        self.stack1.append(value)
        if self.stack2.isEmpty() or value>=self.stack2[-1]:
            self.stack2.append(value)
    
        
    