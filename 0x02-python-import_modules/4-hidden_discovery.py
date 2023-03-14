f __name__ == "__main__":
    import hidden_4
    for str in range(len(dir(hidden_4))):
        if dir(hidden_4)[str][:2] != "__":
            print("{:s}".format(dir(hidden_4)[str]))
