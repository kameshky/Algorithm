from linked_list import LinkedList

def main():
    ll = LinkedList()
    print("Size:",len(ll),sep='   ')
    ll.push(12)

    print("contents:",ll, sep='   ')

    ll.append(24)
    ll.push(0)

    print("Size:",len(ll),sep='   ')
    print("Contents:",ll, sep='   ')

    ll.delete(12)
    print("Contents:", ll, sep='   ')

if __name__ == "__main__":
    main()
