from historicalTree import historical_tree


def main():
    print("show historical tree")
    # p = {"brother":"a", "brother":"b", "brother":"b"}
    brother = set( ["a", "b", "c"])
    persons = [brother]
    mp = "X"
    ht = historical_tree(mp, persons)
    ht.view()
    
    
if __name__ == '__main__':
    main()