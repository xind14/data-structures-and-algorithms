from data_structures.linked_list import LinkedList

def zip_lists(a, b):
    current1=a.head
    current2=b.head

    zipped_list = LinkedList()

    while current1 or current2:
        if current1:
            zipped_list.append(current1.value)
            current1=current1.next
        if current2:
            zipped_list.append(current2.value)
            current2=current2.next
    return zipped_list

