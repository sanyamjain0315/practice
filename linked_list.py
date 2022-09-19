class node:
    def __init__(self,val):
        self.data = val
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def print_list(self):
        temp=self.head
        print('')
        if(temp==None):
            print('There is no linked list')
        while (temp):
            print(temp.data)
            temp=temp.next
    def add_beginning(self,newdata):
        if(self.head==None):
            self.head=node(newdata)
            return
        newnode=node(newdata)
        newnode.next=self.head
        self.head=newnode
    def add_end(self,newdata):
        newnode=node(newdata)
        temp=self.head
        if(self.head==None):
            self.head=node(newdata)
            return
        while(temp):
            prev=temp
            temp=temp.next
        prev.next=newnode
    def add_before(self,afternode,newdata):
        if afternode is None:
            print("Specified node does not exist")
            return
        newnode=node(newdata)
        temp=self.head
        while(temp!=afternode):
            prev=temp
            temp=temp.next
        newnode.next=afternode
        prev.next=newnode
    def add_after(self,beforenode,newdata):
        if beforenode is None:
            print("Specified node does not exist")
            return
        newnode=node(newdata)
        newnode.next=beforenode.next
        beforenode.next=newnode
    def remove(self,val):
        temp=self.head
        prev=temp
        if temp is None:
            print('There are no nodes to remove')
            return
        if (temp.data==val):
            self.head=temp.next
            temp=None
            return
        while(temp):
            if(temp.data==val):
                break
            prev=temp
            temp=temp.next
        if(temp==None):
            print("Specified node does not exist")
            return
        prev.next=temp.next
        temp=None


import streamlit as st
llt=Linkedlist()

llt.head=node(3)
node2=node(1)
node3=node(4)

llt.head.next=node2
node2.next=node3

llt.print_list()
llt.remove(3)
llt.remove(1)
llt.remove(4)
llt.print_list()
