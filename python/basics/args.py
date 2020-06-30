def main():
    packedParamKitten("good", "bad", "mid")
    advPackedParamKitten(shu="ss")  # just pass in some named parameters


# *args will take the parameters in as tuple
def packedParamKitten(*args):
    print(f"type of the args is {type(args)}")
    if len(args):
        for x in args:
            print(x)

    else:
        print("nothing passed in")


# keywords args are passed in as dictionary and can be read by keys
def advPackedParamKitten(**args):
    print(f"type of the args is {type(args)}")
    for k, v in args.items():
        print(f"key is {k}, value is {v}")


if __name__ == "__main__":
    main()
