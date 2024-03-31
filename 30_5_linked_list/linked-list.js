/** Node: node for a singly linked list. */

class Node {
    constructor(val) {
      this.val = val;
      this.next = null;
    }
  }
  
  /** LinkedList: chained together nodes. */
  
  class LinkedList {
    constructor(vals = []) {
      this.head = null;
      this.tail = null;
      this.length = 0;
  
      for (let val of vals) this.push(val);
    }
  

  /** get_node(idx): retrieve node at idx. */
  get_node(idx) {
    let current = this.head;
    let count = 0;

    while (current !== null && count != idx) {
        count += 1;
        current = current.next;
    }

    return current;
  }


    /** push(val): add new value to end of list. */
    push(val) {
        const newNode = new Node(val);

        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
        this.length += 1;
    }
  
    /** unshift(val): add new value to start of list. */
  
    unshift(val) {
        const newNode = new Node(val);

        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            newNode.next = this.head;
            this.head = newNode;
        }

        this.length += 1;        
    }
  
    /** pop(): return & remove last item. */
    pop() {
        return this.removeAt(this.length - 1);     
  
    }
  
    /** shift(): return & remove first item. */
  
    shift() {
        return this.removeAt(0);
    }
  
    /** getAt(idx): get val at idx. */
    getAt(idx) {
        if (idx >= this.length || idx < 0) {
            throw new Error("Invalid index.");
        }        
        return this.get_node(idx).val;
    }
  
    /** setAt(idx, val): set val at idx to val */
    setAt(idx, val) {
        if (idx >= this.length || idx < 0) {
            throw new Error("Invalid index.");
        }
        const current = this.get_node(idx);
        current.val = val;         
    }
  
    /** insertAt(idx, val): add node w/val before idx. */
    insertAt(idx, val) {
        if (idx >= this.length || idx < 0) {
            throw new Error("Invalid index.");
        }

        if (idx === 0) return this.unshift(val);
        if (idx === this.length) return this.push(val);

        const newNode = new Node(val);
        const before_curr = this.get_node(idx-1);

        newNode.next = before_curr.next;
        before_curr.next = newNode;

        this.length += 1;
    }
  
    /** removeAt(idx): return & remove item at idx, */
    removeAt(idx) {
        if (idx >= this.length || idx < 0) {
            throw new Error("Invalid index.");
        }

        const before_curr = this.get_node(idx-1);

        if(idx === 0) {
            const val = this.head.val;
            this.head = this.head.next;
            this.length -= 1;
            if (this.length < 2) this.tail = this.head;

            return val;
        } 

        if(idx === this.length - 1) {
            const val = current.val;
            before_curr = null;
            this.tail = before_curr;
            this.length -= 1;

            return val;
        }

        const val = before_curr.next.val;
        before_curr.next = before_curr.next.next;
        this.length -= 1;
        return val;
    }

    /** average(): return an average of all values in the list */
    average() {
        if (this.length === 0) return 0;

        let current = this.head;
        let sum = 0;

        while(current) {
            sum += current.val;
            current = current.next;
        }
        return sum/this.length;
    }
  }
  
  module.exports = LinkedList;
  